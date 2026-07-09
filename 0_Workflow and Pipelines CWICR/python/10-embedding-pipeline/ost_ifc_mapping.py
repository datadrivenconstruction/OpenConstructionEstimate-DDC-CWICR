"""
Heuristic mapping of CWICR rates → Revit OST_Category + IfcClass.

Each rule:
    (regex_on_lowered_rate_name,  OST_Category,  IfcClass,  cross_lang_aliases)

Order matters: more specific rules first (because we return on first match).

`OST_Category` follows Revit built-in category names. `IfcClass` follows IFC4.3
canonical names. `cross_lang_aliases` is a space-separated string of EN/DE
stems we'll inject into dense_text so Revit family-name queries match.

Coverage of CWICR rates:
- Building elements (walls/slabs/columns/beams/doors/windows/roofs/foundations,
  pipes/ducts/cable trays/light fixtures): expected ~80-90%
- Earthworks, transport, demolition, scaffolding, lab/special equipment: lower,
  but mapped to closest OST/IFC where reasonable (e.g. earthworks → OST_Topography
  / IfcGeographicElement) or returned as None to be honest about it.
"""

from __future__ import annotations

import re

# (pattern, OST_Category, IfcClass, EN/DE aliases)
RULES: list[tuple[str, str, str, str]] = [
    # ===== Structural =====
    (r"\bкровл|крыш|стропил|сэндвич.*(?:кровл|крыш)",
        "OST_Roofs", "IfcRoof",
        "roof dach IfcRoof"),
    (r"\bперекрыт(?:ий|ия|ие)?|плит.*перекрыт",
        "OST_Floors", "IfcSlab",
        "slab floor decke platte IfcSlab composite-slab"),
    (r"\bлестничн.*марш|лестниц.*железобет|лестниц(?:а|ы|ой|ам)?\b|марш.*лестниц",
        "OST_Stairs", "IfcStair",
        "stair treppe IfcStair flight"),
    (r"\bленточн.*фундам|фундамент.*ленточн",
        "OST_StructuralFoundation", "IfcFooting",
        "strip-foundation streifenfundament IfcFooting"),
    (r"\bростверк",
        "OST_StructuralFoundation", "IfcPileCap",
        "pile-cap pfahlkopf IfcPileCap"),
    (r"\bфундамент.*стакан|стакан.*фундамент|фундамент.*столбч|столбч.*фундам",
        "OST_StructuralFoundation", "IfcFooting",
        "pad-foundation einzelfundament IfcFooting"),
    (r"\bфундамент",
        "OST_StructuralFoundation", "IfcFooting",
        "foundation fundament IfcFooting"),
    (r"\bсва(?:я|и|й|и-оболочк)|свайн|буронабивн|шпунт",
        "OST_StructuralFoundation", "IfcPile",
        "pile bohrpfahl IfcPile bored-pile sheet-pile"),
    (r"\bколонн.*стальн|стальн.*колонн|колонн.*металл",
        "OST_StructuralColumns", "IfcColumn",
        "steel-column stahlstütze IfcColumn"),
    (r"\bколонн.*железобет|железобет.*колонн|колонн.*монолит|монолит.*колонн|колонн",
        "OST_StructuralColumns", "IfcColumn",
        "concrete-column stütze IfcColumn"),
    (r"\bбалк.*стальн|стальн.*балк|металл.*балк|балк.*металл",
        "OST_StructuralFraming", "IfcBeam",
        "steel-beam stahlträger IfcBeam"),
    (r"\bбалк.*железобет|железобет.*балк|ригель|прогон|балк",
        "OST_StructuralFraming", "IfcBeam",
        "beam balken träger IfcBeam girder"),
    (r"\bопалубк",
        "OST_StructuralFraming", "IfcFormwork",
        "formwork schalung IfcFormwork"),
    (r"\bарматур|стержн.*арм|каркас.*арм|сетк.*арм",
        "OST_Rebar", "IfcReinforcingBar",
        "rebar bewehrung IfcReinforcingBar reinforcement"),
    (r"\bферм(?:а|ы|ой|ам)?\b|стропильн.*ферм",
        "OST_StructuralFraming", "IfcMember",
        "truss fachwerk IfcMember IfcBeam roof-truss"),

    # ===== Architecture - walls / partitions =====
    (r"\bкладк.*кирпич|кирпич.*кладк|кирпичн.*стен",
        "OST_Walls", "IfcWall",
        "brick-wall masonry mauerwerk IfcWall basic-wall"),
    (r"\bперегород",
        "OST_Walls", "IfcWall",
        "partition trennwand IfcWall basic-wall partition-wall"),
    (r"\bстен.*бетон|бетон.*стен|стен.*монолит|монолит.*стен",
        "OST_Walls", "IfcWall",
        "concrete-wall betonwand IfcWall basic-wall"),
    (r"\bвитраж|стоечно-ригельн|фасадн.*систем",
        "OST_CurtainWalls", "IfcCurtainWall",
        "curtain-wall fassade vorhangfassade IfcCurtainWall"),
    (r"\bстен(?:а|ы|ой|ам|ах)?\b",
        "OST_Walls", "IfcWall",
        "wall mauer wand IfcWall basic-wall"),

    # ===== Architecture - openings =====
    (r"\bдвер.*противопожар|противопожар.*двер",
        "OST_Doors", "IfcDoor",
        "fire-door brandschutztür IfcDoor"),
    (r"\bдвер|дверн",
        "OST_Doors", "IfcDoor",
        "door tür IfcDoor"),
    (r"\bворот",
        "OST_Doors", "IfcDoor",
        "gate tor sectional-door IfcDoor"),
    (r"\bокно|оконн",
        "OST_Windows", "IfcWindow",
        "window fenster glazing casement IfcWindow"),

    # ===== Architecture - finishes =====
    (r"\bпотолок.*подвесн|подвесн.*потолок",
        "OST_Ceilings", "IfcCovering",
        "suspended-ceiling abgehängte-decke IfcCovering"),
    (r"\bпотолок|оштукат.*потол",
        "OST_Ceilings", "IfcCovering",
        "ceiling decke IfcCovering"),
    (r"\bштукатур|оштукат",
        "OST_Walls", "IfcCovering",
        "plaster putz IfcCovering wall-finish"),
    (r"\bокраск|покрас|побелк",
        "OST_Walls", "IfcCovering",
        "paint farbe coating IfcCovering"),
    (r"\bоблиц.*плит|плитк.*облиц|керам.*плитк",
        "OST_Walls", "IfcCovering",
        "tile tiling fliese cladding IfcCovering"),
    (r"\bтеплоизоляц|утепл",
        "OST_Walls", "IfcCovering",
        "insulation thermal mineral-wool dämmung IfcCovering"),
    (r"\bгидроизоляц|пароизоляц",
        "OST_Walls", "IfcCovering",
        "waterproofing abdichtung membrane IfcCovering"),
    (r"\bпол.*линолеум|линолеум|пол.*ламинат|ламинат|паркет|пол.*покрыт|покрыт.*пол",
        "OST_Floors", "IfcCovering",
        "floor-finish bodenbelag laminate parquet linoleum vinyl carpet IfcCovering"),
    (r"\bстяжк.*пол|пол.*стяжк|устройство стяжк",
        "OST_Floors", "IfcCovering",
        "screed estrich floor-screed IfcCovering"),

    # ===== MEP - plumbing =====
    (r"\bунитаз|умывальн|раковин|ванн|душ|санитарн.*приб",
        "OST_PlumbingFixtures", "IfcSanitaryTerminal",
        "sink toilet wc washbasin shower bathtub IfcSanitaryTerminal"),
    (r"\bканализац",
        "OST_PipeCurves", "IfcPipeSegment",
        "sewage drain abwasser IfcPipeSegment"),
    (r"\bтрубопровод.*стальн|сталь.*трубопровод|стальн.*труб",
        "OST_PipeCurves", "IfcPipeSegment",
        "steel-pipe stahlrohr IfcPipeSegment"),
    (r"\bтрубопровод.*чугун|чугун.*труб",
        "OST_PipeCurves", "IfcPipeSegment",
        "cast-iron-pipe gusseisen IfcPipeSegment"),
    (r"\bтрубопровод.*медн|медн.*труб",
        "OST_PipeCurves", "IfcPipeSegment",
        "copper-pipe kupferrohr IfcPipeSegment"),
    (r"\bтрубопровод.*пвх|пвх.*труб|трубопровод.*пнд|пнд.*труб|трубопровод.*полипропилен",
        "OST_PipeCurves", "IfcPipeSegment",
        "pvc-pipe pe-pipe pp-pipe kunststoffrohr IfcPipeSegment"),
    (r"\bтрубопровод|труб[ыа]|трубн.*",
        "OST_PipeCurves", "IfcPipeSegment",
        "pipe rohr piping IfcPipeSegment"),
    (r"\bзапорн.*арматур|арматур.*запорн|задвижк|вентил.*шаров|кран.*шаров",
        "OST_PipeAccessory", "IfcValve",
        "valve gate-valve ball-valve absperrarmatur IfcValve"),

    # ===== MEP - HVAC =====
    (r"\bвоздуховод",
        "OST_DuctCurves", "IfcDuctSegment",
        "duct lüftungskanal IfcDuctSegment ventilation HVAC"),
    (r"\bприточн.*установ|вентиляц.*установ|кондиционир.*установ|чиллер",
        "OST_MechanicalEquipment", "IfcAirToAirHeatRecovery",
        "AHU air-handling-unit lüftungsgerät chiller IfcAirToAirHeatRecovery"),
    (r"\bкондиционер|сплит-систем|фанкойл",
        "OST_MechanicalEquipment", "IfcUnitaryEquipment",
        "air-conditioner split-system fan-coil klimaanlage IfcUnitaryEquipment"),
    (r"\bвентилятор",
        "OST_MechanicalEquipment", "IfcFan",
        "fan ventilator IfcFan"),
    (r"\bрадиатор|конвектор|отопит.*приб",
        "OST_MechanicalEquipment", "IfcSpaceHeater",
        "radiator heizkörper konvektor IfcSpaceHeater"),
    (r"\bотопл",
        "OST_MechanicalEquipment", "IfcSpaceHeater",
        "heating heizung IfcSpaceHeater"),

    # ===== MEP - electrical =====
    (r"\bкабельн.*лоток|лоток.*кабельн",
        "OST_CableTray", "IfcCableCarrierSegment",
        "cable-tray kabelpritsche IfcCableCarrierSegment"),
    (r"\bкабел[ьяе]|провод[ао]в?\b",
        "OST_Wire", "IfcCableSegment",
        "cable wire kabel IfcCableSegment electrical"),
    (r"\bсветильник|светодиод.*светил|освещ",
        "OST_LightingFixtures", "IfcLightFixture",
        "lighting luminaire leuchte IfcLightFixture LED"),
    (r"\bэлектрощит|щит.*электр|вру|пунк.*распред",
        "OST_ElectricalEquipment", "IfcElectricDistributionBoard",
        "switchboard panelboard schaltschrank IfcElectricDistributionBoard"),
    (r"\bтрансформатор",
        "OST_ElectricalEquipment", "IfcTransformer",
        "transformer trafo IfcTransformer"),
    (r"\bгенератор",
        "OST_ElectricalEquipment", "IfcGenerator",
        "generator notstrom IfcGenerator"),

    # ===== Fire =====
    (r"\bспринклер|оросител.*спринклер",
        "OST_SprinklerPipes", "IfcFireSuppressionTerminal",
        "sprinkler IfcFireSuppressionTerminal"),
    (r"\bпожарн.*извещател|пожарн.*датчик|дымов.*извещател",
        "OST_FireAlarmDevices", "IfcAlarm",
        "smoke-detector fire-detector IfcAlarm"),

    # ===== Transport equipment =====
    (r"\bлифт|подъемник|эскалатор",
        "OST_MechanicalEquipment", "IfcTransportElement",
        "elevator lift escalator IfcTransportElement"),

    # ===== Earthworks / site =====
    (r"\bразработ.*грунт|выемк.*грунт|разрабатк|рытье|рытьё|котлован",
        "OST_Topography", "IfcGeographicElement",
        "excavation aushub earthworks digging soil IfcGeographicElement"),
    (r"\bнасыпь|уплотн.*грунт|обратн.*засыпк|засыпк.*грунт",
        "OST_Topography", "IfcGeographicElement",
        "embankment fill compaction böschung IfcGeographicElement"),
    (r"\bасфальт.*бет|асфальт",
        "OST_Roads", "IfcPavement",
        "asphalt pavement asphaltbeton wearing-course IfcPavement"),
    (r"\bщеб|щебён|щебен|основан.*щеб",
        "OST_Roads", "IfcCourse",
        "crushed-stone aggregate schotter base-course IfcCourse"),

    # ===== Roads furniture =====
    (r"\bбордюр|бортов.*камен",
        "OST_Roads", "IfcKerb",
        "kerb curb bordstein IfcKerb"),
    (r"\bдорожн.*разметк|разметк.*дорог|термопласт.*разметк",
        "OST_Roads", "IfcSign",
        "road-marking strassenmarkierung IfcSign"),
    (r"\bбарьерн.*огражд|огражд.*барьерн|металл.*барьер",
        "OST_Roads", "IfcRailing",
        "guardrail leitplanke IfcRailing"),

    # ===== Demolition =====
    (r"\bдемонтаж|разборк",
        "_Demolition", "IfcOpeningElement",
        "demolition removal abbruch IfcOpeningElement"),

    # ===== Scaffolding / temp works =====
    (r"\bлеса.*металл|металл.*леса|подмост",
        "OST_TemporaryStructure", "IfcBuildingElementProxy",
        "scaffolding gerüst IfcBuildingElementProxy temporary"),
]
RULES_COMPILED = [(re.compile(p, re.I), ost, ifc, ali) for p, ost, ifc, ali in RULES]


def classify(rate_name: str, section_name: str | None = None,
             collection_name: str | None = None) -> tuple[str | None, str | None, str]:
    """Return (OST_Category, IfcClass, aliases). All None if no match."""
    if not rate_name:
        return None, None, ""
    text = rate_name
    if section_name:
        text = f"{text} | {section_name}"
    if collection_name:
        text = f"{text} | {collection_name}"
    for pat, ost, ifc, ali in RULES_COMPILED:
        if pat.search(text):
            return ost, ifc, ali
    return None, None, ""


# ===========================================================================
# Additional filters for DWG/geometry-based search
# ===========================================================================

# ---- Material class ----
MATERIAL_RULES = [
    (r"\bжелезобетон|ж/б|жб[^а-я]|монолит.*бетон|сборн.*железобет", "ReinforcedConcrete"),
    (r"\bбетон.*легк|керамзитобет|пенобетон|газобетон|ячеист.*бетон", "LightweightConcrete"),
    (r"\bбетон|цемент.*раствор", "Concrete"),
    (r"\bкирпич",                                     "Brick"),
    (r"\bблок.*газобет|блок.*пенобет|блок.*ячеист|блок.*керамзит", "Block"),
    (r"\bблок.*бетон|блок.*фундамент",                "ConcreteBlock"),
    (r"\bстальн|сталь[^а-я]|металлокон|металл.*кон",  "Steel"),
    (r"\bалюмин",                                     "Aluminum"),
    (r"\bмедн|мед[ьи]\b",                            "Copper"),
    (r"\bчугун",                                      "CastIron"),
    (r"\bдерев|древесн|сосн[аы]|листвен.*пород|пиломатериал", "Wood"),
    (r"\bстекл|стеклопакет",                          "Glass"),
    (r"\bпвх|поливинилхлорид|полипропилен|полиэтилен|пнд|пэ\b|пластик", "Plastic"),
    (r"\bминерал.*ват|каменн.*ват|стекловолокн|пенополистирол|пенопласт|пир\b", "Insulation"),
    (r"\bкерам.*плит|керамогранит|керамическ",        "Ceramic"),
    (r"\bбитум|рубероид|унифлекс|мастик|гидростеклоиз", "Bitumen"),
    (r"\bгипсокартон|гкл\b|гвл\b|гипс[^а-я]",         "Gypsum"),
    (r"\bасфальтобетон|асфальт",                      "Asphalt"),
    (r"\bщеб|щебень|щебён|гравий|песчано-гравий",     "Aggregate"),
    (r"\bпесок|песчан",                               "Sand"),
    (r"\bгрунт|земля|почв",                           "Soil"),
]
MATERIAL_COMPILED = [(re.compile(p, re.I), c) for p, c in MATERIAL_RULES]


def classify_material(text: str) -> str | None:
    if not text:
        return None
    for pat, m in MATERIAL_COMPILED:
        if pat.search(text):
            return m
    return None


# ---- Unit type (linear / area / volume / count / mass) ----
def classify_unit_type(rate_unit: str | None) -> str | None:
    """Derive geometric unit type from rate_unit string."""
    if not rate_unit:
        return None
    u = str(rate_unit).lower().strip()
    # Volume
    if re.search(r"м\s*[3³]|м3|m3|m³|куб", u):
        return "Volume"
    # Area
    if re.search(r"м\s*[2²]|м2|m2|m²|кв", u):
        return "Area"
    # Mass
    if re.search(r"\bт\b|тонн|кг", u):
        return "Mass"
    # Count
    if re.search(r"\bшт\b|компл|штук", u):
        return "Count"
    # Linear (м alone, but not м2/м3)
    if re.search(r"\bм\b|метр|пог", u):
        return "Linear"
    # 1000-prefixed (1000 шт, 1000 м, etc)
    if re.search(r"100\s*м[2²]|100м2", u):
        return "Area"
    if re.search(r"100\s*м[3³]|100м3", u):
        return "Volume"
    if re.search(r"100\s*м\b", u):
        return "Linear"
    return None


# ---- Discipline (A=Arch, S=Struct, MEP-*, C=Civil, GE=GenEarthwork) ----
DISCIPLINE_RULES = [
    # MEP first (specific)
    (r"\bвентиляц|воздуховод|кондиц|фанкойл|чиллер|приточн|вытяжн.*возд",   "MEP-HVAC"),
    (r"\bкабел|провод|щит.*электр|трансформат|светильник|освещ|щит.*расп",  "MEP-Electrical"),
    (r"\bтрубопровод|канализац|унитаз|раковин|санитар|водопровод|водоснабж|отопл|радиатор", "MEP-Plumbing"),
    (r"\bспринклер|пожарн.*извещател|пожарн.*датчик|пожаротуш",             "MEP-Fire"),
    # Civil / Roads
    (r"\bдорог|асфальт|бордюр|разметк.*дорог|барьерн.*огражд|мост|путепров|тоннел", "Civil"),
    (r"\bжелезн.*дорог|рельс|шпал",                                          "Civil"),
    # Earthwork
    (r"\bразработ.*грунт|насыпь|котлован|траншея|выемк.*грунт|уплотн.*грунт", "Earthwork"),
    # Structural
    (r"\bколонн|балк|ригель|перекрыт|фундамент|свая|сва[ия]\b|ростверк|опалубк|арматур|каркас.*мет|стропил|ферм", "Structural"),
    # Demolition
    (r"\bдемонтаж|разборк",                                                  "Demolition"),
    # Architecture (everything else with stem hits)
    (r"\bстен|перегород|двер|окно|потолок|кровл|штукатур|окраск|плитк|облиц|пол|линолеум|ламинат|паркет|теплоизоляц|гидроизоляц|кладк|витраж", "Architecture"),
]
DISCIPLINE_COMPILED = [(re.compile(p, re.I), c) for p, c in DISCIPLINE_RULES]


def classify_discipline(text: str) -> str | None:
    if not text:
        return None
    for pat, d in DISCIPLINE_COMPILED:
        if pat.search(text):
            return d
    return None


# ---- Work type (install / demolition / repair / finish / preparation) ----
WORK_TYPE_RULES = [
    (r"\bдемонтаж|разборк|снос",                          "Demolition"),
    (r"\bремонт|восстанов|замен[аы]|реставрац|инъек.*трещин|трещин.*инъек", "Repair"),
    (r"\bокраск|покрас|побелк|лакир|облиц|штукатур|оштукат|шпаклев|обои", "Finish"),
    (r"\bочист|промыв|подготовк.*поверхн",               "Preparation"),
    (r"\bпуско.*наладк|наладк|испытани",                 "Commissioning"),
    (r"\bустройств|монтаж|установк|укладк|прокладк|сборк|кладк|устан|бетонировани|армирован|сварк", "Installation"),
]
WORK_TYPE_COMPILED = [(re.compile(p, re.I), c) for p, c in WORK_TYPE_RULES]


def classify_work_type(text: str) -> str | None:
    if not text:
        return None
    for pat, w in WORK_TYPE_COMPILED:
        if pat.search(text):
            return w
    return None


# ---------------------------------------------------------------------------
# applies_to_classes - detect what BIM element this RATE OPERATES ON when the
# rate itself is a sub-task / secondary work (insulation, painting, fire-proofing,
# coating, marking on a parent element). Returns a list of IfcClass values.
#
# Example: "Теплоизоляция трубопроводов" → primary IfcCovering, applies_to=[IfcPipeSegment]
# This lets a search "find rates for IfcPipeSegment" return both pipes themselves
# AND insulation/painting that applies to pipes.
# ---------------------------------------------------------------------------
APPLIES_TO_RULES = [
    # Sub-task on PIPES
    (r"(?:на|по|вокруг)\s*\w*\s*трубопровод|изоляц.*трубопровод|"
     r"окраск.*трубопровод|маркир.*трубопровод|"
     r"теплоизоляц.*труб|гидроизоляц.*труб|покрыт.*труб|"
     r"обогрев.*труб|обмотк.*труб|подвеск.*труб|опор.*труб",
        "IfcPipeSegment"),
    # Sub-task on DUCTS
    (r"(?:на|по)\s*\w*\s*воздуховод|изоляц.*воздуховод|теплоизоляц.*воздуховод|"
     r"огнезащит.*воздуховод|покрыт.*воздуховод",
        "IfcDuctSegment"),
    # Sub-task on WALLS
    (r"(?:на|по)\s*\w*\s*стен(?:а|ы|ам|ах|у)|штукатур.*стен|оштукатур.*стен|"
     r"окраск.*стен|облиц.*стен|плитк.*стен|обои.*стен|"
     r"гидроизоляц.*стен|теплоизоляц.*стен|шпаклев.*стен",
        "IfcWall"),
    # Sub-task on FLOORS / SLABS
    (r"(?:на|по|поверх)\s*пол(?:ы|у|ам|ах)?|стяжк.*пол|устройств.*стяжк|"
     r"покрыт.*пол|линолеум.*пол|ламинат.*пол|паркет.*пол|"
     r"наливн.*пол|самовыравн.*пол",
        "IfcSlab"),
    # Sub-task on COLUMNS
    (r"(?:на|по|вокруг)\s*колонн|облиц.*колонн|окраск.*колонн|"
     r"огнезащит.*колонн|защит.*колонн",
        "IfcColumn"),
    # Sub-task on BEAMS
    (r"(?:на|по)\s*балк|облиц.*балк|окраск.*балк|огнезащит.*балк",
        "IfcBeam"),
    # Sub-task on ROOFS
    (r"(?:на|по)\s*кровл|кровл.*покрыт|гидроизоляц.*кровл|"
     r"парапет.*кровл|вентиляц.*кровл",
        "IfcRoof"),
    # Sub-task on FOUNDATIONS
    (r"(?:на|по)\s*фундамент|гидроизоляц.*фундамент|"
     r"теплоизоляц.*фундамент",
        "IfcFooting"),
    # Sub-task on DOORS
    (r"(?:на|по)\s*двер|окраск.*двер|облицов.*двер|герметиз.*двер|"
     r"монтаж.*коробк.*двер",
        "IfcDoor"),
    # Sub-task on WINDOWS
    (r"(?:на|по)\s*окно|окраск.*окно|герметиз.*окно|откос.*окно|"
     r"монтаж.*коробк.*окно|подоконник",
        "IfcWindow"),
    # Sub-task on CABLES
    (r"(?:на|по)\s*кабел|маркир.*кабел|опор.*кабел|"
     r"огнезащит.*кабел|изоляц.*кабел",
        "IfcCableSegment"),
    # Sub-task on REINFORCEMENT
    (r"антикорроз.*арматур|защит.*арматур",
        "IfcReinforcingBar"),
]
APPLIES_TO_COMPILED = [(re.compile(p, re.I), c) for p, c in APPLIES_TO_RULES]


def detect_applies_to(rate_name: str) -> list[str]:
    """Return list of IfcClass values this RATE OPERATES ON (sub-task target).
    Empty if this rate is itself a primary element (matches no applies-to pattern).
    """
    if not rate_name:
        return []
    found = []
    for pat, ifc in APPLIES_TO_COMPILED:
        if pat.search(rate_name):
            if ifc not in found:
                found.append(ifc)
    return found


# ---------------------------------------------------------------------------
# base_code stripping for cross-language rate alignment
# ---------------------------------------------------------------------------
LANG_SUFFIXES = (
    "СТР",   # RU
    "CON",   # EN (construction)
    "BAU",   # DE (Bauarbeiten)
    "TRA",   # FR (travaux)
    "TRABAJO",  # ES
    "RAB",   #
    "OBR",   # ES (obra) ?
    "VOI",   # IT (lavori)?
    "LAU",
    "OPE",
    "LAB",
    "OBE",
    "PRA",
    "PIE",
    "LUC",
)
UNIT_SUFFIXES = ("м3", "m3", "м2", "m2", "м", "m", "т", "t", "кг", "kg", "шт", "pc", "pcs")

# Inline language tags appended INSIDE the last token after a 4-char position code.
# Example: RU "KAMEКАП" = "KAME" + "КАП" (капремонт), EN "KAMEMAJ" = "KAME" + "MAJ" (major repair).
# Stripping these aligns rates across languages that don't match via plain LANG_SUFFIXES.
INLINE_LANG_TAGS = (
    # RU + EN (original)
    "КАП", "ПУС", "MAJ", "COM", "MIN", "REM", "REP", "MOD", "EKS", "EXP",
    # 10 European-script languages share INB (commissioning) + GRU (major repair):
    # BG/CS/DE/HR/IT/NL/PL/RO/SV/TR - 894 codes each
    "INB", "GRU",
    # FR - RÉN (rénovation = major repair) - 231 codes
    "RÉN",
    # PT - REF (refurbishment) - 231 codes
    "REF",
    # HI (Hindi/Devanagari) - 1602 codes total: निर(708) + प्र(663) + उपक(231)
    "निर", "प्र", "उपक",
    # ZH (Chinese) - 1602 codes total: 建筑工(708) + 调试工(663) + 设备大(231)
    "建筑工", "调试工", "设备大",
    # AR (Arabic) - 1004 codes total: أعم(773 commissioning) + إصل(231 repair)
    "أعم", "إصل",
)


def base_code(rate_code: str) -> str:
    """Strip language + unit + inline tag suffix from rate_code so it aligns across languages.
    With INLINE_LANG_TAGS extension: 100% set-equal across RU↔EN.
    """
    s = str(rate_code or "")
    # strip language suffix from end
    for suf in sorted(LANG_SUFFIXES, key=len, reverse=True):
        if s.endswith(suf):
            s = s[:-len(suf)]
            break
    # strip unit suffix from end
    for suf in sorted(UNIT_SUFFIXES, key=len, reverse=True):
        if s.endswith(suf):
            s = s[:-len(suf)]
            break
    # strip inline lang tag from end of last token (only if last token > 4 chars)
    parts = s.rsplit("_", 1)
    if len(parts) == 2 and len(parts[1]) > 4:
        last = parts[1]
        for tag in sorted(INLINE_LANG_TAGS, key=len, reverse=True):
            if last.endswith(tag) and len(last) - len(tag) >= 4:
                s = parts[0] + "_" + last[:-len(tag)]
                break
    return s


# ---- One-call enrichment ----
def enrich(rate_name: str, rate_unit: str | None = None,
           section_name: str | None = None,
           collection_name: str | None = None) -> dict:
    """All filters in one call. Returns dict ready to merge into payload."""
    text = rate_name or ""
    if section_name:
        text += f" | {section_name}"
    if collection_name:
        text += f" | {collection_name}"
    ost, ifc, ali = classify(rate_name, section_name, collection_name)
    return {
        "ost_category":       ost,
        "ifc_class":          ifc,
        "applies_to_classes": detect_applies_to(rate_name or ""),
        "material_class":     classify_material(text),
        "unit_type":          classify_unit_type(rate_unit),
        "discipline":         classify_discipline(text),
        "work_type":          classify_work_type(text),
        "_aliases":           ali,
    }


if __name__ == "__main__":
    samples = [
        "Устройство кирпичной кладки стен наружных",
        "Бетонирование монолитного перекрытия толщиной 200 мм",
        "Установка стальных колонн W12x50",
        "Прокладка трубопроводов полипропиленовых диаметром 50 мм",
        "Окраска фасада водно-дисперсионной краской",
        "Демонтаж кирпичных стен",
        "Разработка грунта экскаватором драглайн",
        "Установка дверей деревянных",
        "Устройство ленточного фундамента из бетона",
        "Монтаж кабельных лотков шириной 200 мм",
        "Установка унитазов керамических",
        "Спринклерная сеть пожаротушения",
    ]
    for s in samples:
        ost, ifc, ali = classify(s.lower())
        print(f"  [{ost or '-':28s} {ifc or '-':22s}] {s[:60]}")
        if ali:
            print(f"  → aliases: {ali[:90]}")
        print()
