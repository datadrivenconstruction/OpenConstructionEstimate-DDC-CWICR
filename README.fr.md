<h3 align="center">DDC CWICR - Construction Work Items, Components & Resources </br>
  + Pipelines n8n pour le calcul d'estimations basées sur des descriptions, photos et CAD (BIM)</h3>

<p align="center">
  <a href="README.md">🇬🇧 English</a> •
  <a href="README.zh-CN.md">🇨🇳 中文</a> •
  <a href="README.es.md">🇪🇸 Español</a> •
  <a href="README.pt-BR.md">🇧🇷 Português</a> •
  <a href="README.ru.md">🇷🇺 Русский</a> •
  <a href="README.ja.md">🇯🇵 日本語</a> •
  <a href="README.de.md">🇩🇪 Deutsch</a> •
  <a href="README.fr.md"><b>🇫🇷 Français</b></a>
</p>

<p align="center">
  <img src="https://github.com/datadrivenconstruction/cad2data-Revit-IFC-DWG-DGN-pipeline-with-conversion-validation-qto/blob/main/DDC_in_additon/DDC_readme_content/OpenConstructionEstimate.jpg" alt="OpenConstructionEstimate" width="1000">
</p>

<div align="center">
  <img src="https://img.shields.io/badge/Postes_de_Travail-55,719-2563eb?style=for-the-badge" alt="Postes de Travail">
  <img src="https://img.shields.io/badge/Ressources-27,672-059669?style=for-the-badge" alt="Ressources">
  <img src="https://img.shields.io/badge/Langues-11-d97706?style=for-the-badge" alt="Langues">
  <img src="https://img.shields.io/badge/Pays-12+-dc2626?style=for-the-badge" alt="Pays">
</div>

<div align="center">
  <img src="https://img.shields.io/badge/Licence-CC_BY--NC_4.0-green?style=flat-square" alt="Licence">
  <img src="https://img.shields.io/badge/Version-v0.1.1-blue?style=flat-square" alt="Version">
  <img src="https://img.shields.io/badge/Embeddings-OpenAI_3072d-412991?style=flat-square" alt="Embeddings">
  <img src="https://img.shields.io/badge/Vector_DB-Qdrant-dc382d?style=flat-square" alt="Qdrant">
  <img src="https://img.shields.io/badge/Automatisation-n8n-ea4b71?style=flat-square" alt="n8n">
</div>

<p align="center">
  <img src="https://github.com/datadrivenconstruction/cad2data-Revit-IFC-DWG-DGN-pipeline-with-conversion-validation-qto/blob/main/DDC_in_additon/DDC_readme_content/OpenConstructionEstimate_bottom.jpg" alt="OpenConstructionEstimate" width="1000">
</p>

<h3 align="center">⚡ Workflows n8n</h3>
<p align="center"><code>Choisissez votre entrée → Obtenez l'estimation des coûts</code></p>

<br>

<table width="100%">
<tr>

<td align="center" valign="top" width="33%">
<br>
<h3>📝 Texte</h3>
<p>Conversion rapide du périmètre<br>en devis à partir d'une description</p>
<p><b>Entrée:</b> Message Telegram / chat<br>
<b>Sortie:</b> Postes correspondants + estimation</p>
<br>
<a href="#1️⃣-bot-estimateur-de-texte">📖 Documentation</a>
<br><br>
<a href="./n8n_1_Telegram_Bot_Cost_Estimates_and_Rate_Finder_TEXT_DDC_CWICR.json">
<img src="https://img.shields.io/badge/Télécharger_Workflow-0A84FF?style=for-the-badge&logo=download&logoColor=white" alt="Télécharger"/>
</a>
<br><br>
</td>

<td align="center" valign="top" width="33%">
<br>
<h3>📷 Photo / PDF</h3>
<p>Photos de chantier, devis scannés,<br>photo-PDF du terrain</p>
<p><b>Entrée:</b> Image ou pages PDF<br>
<b>Sortie:</b> Périmètre extrait → estimation</p>
<br>
<a href="#2️⃣-estimateur-de-coûts-par-photo">📖 Docs Photo</a> · <a href="#3️⃣-bot-universel-texte--photo--pdf">📖 Bot Universel</a>
<br><br>
<a href="./n8n_2_Photo_Cost_Estimate_DDC_CWICR.json">
<img src="https://img.shields.io/badge/Workflow_Photo-0A84FF?style=for-the-badge&logo=download&logoColor=white" alt="Photo"/>
</a>
&nbsp;
<a href="./n8n_3_Telegram_Bot_Cost_Estimates_and_Rate_Finder_TEXT_PHOTO_PDF_DDC_CWICR.json">
<img src="https://img.shields.io/badge/Bot_Telegram-0A84FF?style=for-the-badge&logo=telegram&logoColor=white" alt="Bot"/>
</a>
<br><br>
</td>

<td align="center" valign="top" width="33%">
<br>
<h3>🧊 CAD / BIM</h3>
<p>Quantification et estimation<br>basées sur Revit / IFC / DWG</p>
<p><b>Entrée:</b> Export de modèle <br>
<b>Sortie:</b> Estimation 4D/5D + ventilation</p>
<br>
<a href="#4️⃣-pipeline-destimation-cad-bim">📖 Documentation</a>
<br><br>
<a href="./n8n_4_CAD_(BIM)_Cost_Estimation_Pipeline_4D_5D_with_DDC_CWICR.json">
<img src="https://img.shields.io/badge/Télécharger_Workflow-0A84FF?style=for-the-badge&logo=download&logoColor=white" alt="Télécharger"/>
</a>
<br><br>
</td>

</tr>
</table>

<br>
<p align="center">
  <a href="https://openconstructionestimate.com">
    <img src="https://img.shields.io/badge/🌐_DÉMO_EN_DIRECT_(base_de_données_uniquement)-openconstructionestimate.com-2563eb?style=for-the-badge" alt="Démo en Direct">
  </a>
</p>
<br>
<p align="center">
 Clients et utilisateurs de DataDrivenConstruction
  <br>
  <a href="https://datadrivenconstruction.io/">
  <img src="https://github.com/datadrivenconstruction/cad2data-Revit-IFC-DWG-DGN-pipeline-with-conversion-validation-qto/blob/main/DDC_in_additon/DDC_readme_content/Clients_DataDrivenConstruction_logos.png" width="95%"/>
  </a>
  <br></br>
</p>


---

## 📑 Table des Matières

### 🤖 Intégration IA
- [Carburant Parfait pour l'IA](#-carburant-parfait-pour-vos-produits-ia) - Pourquoi cette base de données est idéale pour l'IA
- [Claude Code & Google Antigravity](#-claude-code--google-antigravity--assistants-de-programmation-ia) - Assistants de programmation IA
- [n8n](#-n8n--automatisation-visuelle-des-workflows) - Automatisation des workflows
- [Cas d'Utilisation Universels](#-cas-dutilisation-universels) - Ce que vous pouvez construire
- [Exemples pour Développeurs](#-exemples-pour-développeurs) - Code prêt à exécuter

### 📊 Base de Données & Données
- [À Propos](#à-propos) - Qu'est-ce que DDC CWICR
- [Formats Disponibles](#formats-disponibles) - Excel, Parquet, CSV, Qdrant
- [Schéma de Données](#schéma-de-données) - Structure de 85 champs
- [Groupes de Champs](#groupes-de-champs) - Classification, Ressources, Main d'œuvre, Machines
- [Méthodologie](#méthodologie) - Principes de calcul basé sur les ressources
- [Contexte Historique](#contexte-historique) - 100+ ans de normes

### ⚡ Workflows n8n
- [Aperçu des Workflows n8n](#-workflows-n8n) - Choisissez votre type d'entrée
- [Essayez Maintenant - Bots de Démo en Direct](#-essayez-maintenant--bots-de-démo-en-direct) - Testez instantanément sur Telegram
- [Workflow 1: Bot Estimateur de Texte](#1️⃣-bot-estimateur-de-texte) - Bot Telegram pour entrée texte
- [Workflow 2: Estimateur de Coûts par Photo](#2️⃣-estimateur-de-coûts-par-photo) - Formulaire web avec IA Vision
- [Workflow 3: Bot Universel](#3️⃣-bot-universel-texte--photo--pdf) - Texte + Photo + PDF
- [Workflow 4: Pipeline CAD/BIM](#4️⃣-pipeline-destimation-cad-bim) - Revit/IFC/DWG vers estimation
- [Démarrage Rapide des Workflows](#démarrage-rapide-des-workflows) - Configuration en 4 étapes
- [Configuration n8n 2.0+](#️-configuration-n8n-20-requise) - Activer le nœud Execute Command

### 🏗️ Pipeline CAD/BIM
- [Prérequis](#-prérequis) - Composants requis
- [Étapes du Pipeline](#-étapes-du-pipeline) - Traitement en 10 étapes
- [Sélection du Modèle LLM](#️-sélection-du-modèle-llm) - OpenAI, Claude, Gemini, Grok
- [Fichiers de Sortie](#-fichiers-de-sortie) - Rapports HTML & Excel
- [Dépannage](#️-dépannage) - Problèmes courants

### 🔍 Base de Données Vectorielle
- [Base de Données Vectorielle](#base-de-données-vectorielle) - Recherche sémantique avec Qdrant
- [Snapshots de la Base de Données Vectorielle Qdrant](#snapshots-de-la-base-de-données-vectorielle-qdrant) - Télécharger les snapshots
- [Collections](#collections) - 11 collections linguistiques
- [Déploiement Docker](#déploiement-docker) - Configuration auto-hébergée

### 🌐 API
- [Pricing Search API](#-pricing-search-api--buildcalculatorio) - API REST gratuite pour les prix de construction
- [Points de terminaison API](#points-de-terminaison-api) - Recherche, Langues, Statistiques
- [Exemples de code](#exemples-de-code-api) - cURL, Python, JavaScript

### 🚀 Démarrage
- [Démarrage Rapide - Python](#démarrage-rapide) - Données tabulaires & recherche sémantique
- [Cas d'Utilisation d'Intégration](#intégration) - Niveau débutant à avancé

### 👥 Communauté
- [Ressources & Communauté](#ressources--communauté) - Liens & canaux
- [Conseil & Formation](#conseil--formation) - Services professionnels
- [Contribuer](#contribuer) - Soumettez vos workflows
- [Licence](#licence) - CC BY-NC 4.0
- [Soutenir le Projet](#soutenir-le-projet) - Sponsoriser & donner
- [🤖 Instructions IA](#instructions-ia) - Documentation pour les assistants IA


---

## 🚀 Carburant Parfait pour Vos Produits IA

<p align="center">
  <b>Clonez simplement le repo et décrivez ce que vous voulez - l'IA fait le reste</b>
</p>

DDC CWICR n'est pas qu'une base de données - c'est un **carburant prêt à l'emploi pour les applications alimentées par l'IA**. Que vous construisiez des bots d'estimation des coûts, automatisiez des workflows de construction, ou créiez des assistants intelligents - ces données fonctionnent immédiatement avec les outils IA modernes.

### Pourquoi Cette Base de Données est Idéale pour l'IA

| Caractéristique | Avantage |
|-----------------|----------|
| **Embeddings pré-calculés** | Pas besoin de générer des vecteurs - la recherche sémantique fonctionne instantanément |
| **Schéma structuré de 85 champs** | L'IA peut raisonner sur les relations de données et fournir des réponses précises |
| **11 langues incluses** | Construisez des applications multilingues sans surcharge de traduction |
| **55 000+ postes de travail** | Couverture complète pour toute tâche d'estimation de construction |
| **Méthodologie basée sur les ressources** | Données transparentes que l'IA peut expliquer et décomposer |

### 📋 Descriptions de Travaux Prêtes à l'Emploi pour Tout Système

<p align="center">
  <img src="https://github.com/datadrivenconstruction/cad2data-Revit-IFC-DWG-DGN-pipeline-with-conversion-validation-qto/blob/main/DDC_in_additon/DDC_readme_content/A%20ready-made%20job%20description%20generator.jpg" alt="Générateur de descriptions de travaux prêtes à l'emploi" width="1000">
</p>

DDC CWICR fournit des **descriptions de travaux complètes et structurées** qui peuvent être affichées dans n'importe quel système ou format. Chaque poste de travail contient toutes les informations nécessaires aux différents intervenants du projet :

| Intervenant | Ce qu'il obtient |
|-------------|------------------|
| 🏢 **Maître d'ouvrage / Investisseur** | Transparence totale des coûts, décomposition des ressources, justification des prix pour les décisions d'investissement |
| 📊 **Métreur / Économiste** | Prix détaillés, heures de travail, quantités de matériaux, coûts d'équipement - prêt pour la génération de devis |
| 👷 **Chef de chantier / Conducteur de travaux** | Composition des travaux, besoins en ressources, normes de travail pour la planification et l'exécution quotidienne |
| 🔧 **Entrepreneur / Exécutant** | Spécifications complètes, prix unitaires, références de productivité pour des offres et une planification précises |

Export vers **Excel, PDF, HTML, systèmes ERP, plateformes BIM** - le schéma structuré de 85 champs garantit l'intégrité des données dans tous les formats de sortie.

### 🛠️ Fonctionne Parfaitement Avec

<table>
<tr>
<td align="center" width="20%">
<img src="https://img.shields.io/badge/Claude_Code-000000?style=for-the-badge&logo=anthropic&logoColor=white" alt="Claude Code"/><br/>
<b>Claude Code</b><br/>
<sub>Assistant de programmation IA CLI</sub>
</td>
<td align="center" width="20%">
<img src="https://img.shields.io/badge/Google_Antigravity-4285F4?style=for-the-badge&logo=google&logoColor=white" alt="Google Antigravity"/><br/>
<b>Google Antigravity</b><br/>
<sub>Google Antigravity</sub>
</td>
<td align="center" width="20%">
<img src="https://img.shields.io/badge/n8n-EA4B71?style=for-the-badge&logo=n8n&logoColor=white" alt="n8n"/><br/>
<b>n8n</b><br/>
<sub>Automatisation des workflows</sub>
</td>
<td align="center" width="20%">
<img src="https://img.shields.io/badge/Dify-1677FF?style=for-the-badge&logo=openai&logoColor=white" alt="Dify"/><br/>
<b>Dify</b><br/>
<sub>Développement d'apps LLM</sub>
</td>
<td align="center" width="20%">
<img src="https://img.shields.io/badge/Sim_AI-6366F1?style=for-the-badge&logo=simpleicons&logoColor=white" alt="Sim AI"/><br/>
<b>Sim AI & Autres</b><br/>
<sub>Plateformes IA</sub>
</td>
</tr>
</table>

---

## 🎯 DDC Skills

**[DDC Skills pour Agents IA dans la Construction](https://github.com/datadrivenconstruction/DDC_Skills_for_AI_Agents_in_Construction)** - 196 compétences d'automatisation avec intégration directe dans cette base de données CWICR. Clonez, ouvrez avec un assistant de codage IA, décrivez ce dont vous avez besoin.

<p align="center">
  <a href="https://github.com/datadrivenconstruction/DDC_Skills_for_AI_Agents_in_Construction">
    <img src="https://img.shields.io/badge/DDC_Skills-196_AI_Automations-blue?style=for-the-badge&logo=robot" alt="DDC Skills">
  </a>
</p>

---

### 💻 Claude Code & Google Antigravity - Assistants de Programmation IA

Le moyen le plus rapide de travailler avec DDC CWICR. Ouvrez simplement le repository dans Claude Code ou Google Antigravity et posez des questions en langage naturel.

**Démarrage:**
```bash
# Cloner le repository
git clone https://github.com/datadrivenconstruction/OpenConstructionEstimate-DDC-CWICR.git

# Ouvrir avec Claude Code
cd OpenConstructionEstimate-DDC-CWICR
claude
```

**Exemples de Prompts:**

| Tâche | Prompt |
|-------|--------|
| **Explorer les données** | "Montre-moi la structure de cette base de données de construction et explique quelles données sont disponibles" |
| **Trouver des postes** | "Trouve tous les postes de travail liés aux fondations en béton et montre leurs coûts" |
| **Construire des requêtes** | "Écris un script Python pour rechercher les postes de plomberie avec heures de main d'œuvre > 100" |
| **Créer des rapports** | "Génère un rapport de ventilation des coûts pour les travaux de rénovation résidentielle" |
| **Analyser les coûts** | "Compare les coûts des matériaux entre différentes méthodes de construction de murs" |
| **Construire des intégrations** | "Crée un script qui se connecte à la base Qdrant et effectue une recherche sémantique" |

**Conseils Pro:**
- Pointez Claude vers des fichiers spécifiques: *"Analyse le fichier Parquet et résume la distribution des coûts"*
- Demandez des explications: *"Explique comment la méthodologie de calcul basée sur les ressources fonctionne dans cette base de données"*
- Demandez des modifications: *"Modifie le workflow n8n pour ajouter des notifications par email"*

---

### ⚡ n8n - Automatisation Visuelle des Workflows

Construisez des pipelines d'automatisation puissants sans code. Connectez DDC CWICR à plus de 400 apps et services.

**Cas d'Utilisation:**

| Workflow | Description |
|----------|-------------|
| **Bot Telegram** | Les utilisateurs envoient texte/photo → L'IA extrait les postes → Retourne l'estimation des coûts |
| **Automatisation Email** | Recevoir un devis par email → Traiter avec l'IA → Envoyer une estimation formatée |
| **Intégration CRM** | Nouveau projet dans le CRM → Générer automatiquement une estimation préliminaire → Mettre à jour la valeur du deal |
| **Pipeline BIM** | Export depuis Revit → Extraire les quantités → Correspondre avec les tarifs DDC → Générer un rapport 5D |
| **Bot Slack** | L'équipe pose des questions → L'IA recherche dans la base de données → Retourne les postes pertinents |

**Démarrage Rapide:**
1. Télécharger le JSON du workflow depuis ce repo
2. Importer dans n8n: `Workflows → Importer → Depuis un fichier`
3. Configurer les credentials (OpenAI, Qdrant, Telegram)
4. Activer et tester

Voir la section [Workflows n8n](#workflows-n8n--description-détaillée) pour la configuration détaillée.

---

### 📋 Cas d'Utilisation Universels

Quel que soit l'outil IA que vous choisissez, DDC CWICR permet:

| Cas d'Utilisation | Description |
|-------------------|-------------|
| **Estimation Instantanée des Coûts** | Obtenez les coûts de construction à partir de descriptions textuelles ou de photos |
| **Génération de DQE** | Générez automatiquement des devis quantitatifs à partir de descriptions de projet |
| **Benchmarking des Prix** | Comparez les coûts entre régions et langues |
| **Planification des Ressources** | Calculez les heures de main d'œuvre, matériaux et besoins en équipement |
| **Analyse d'Investissement** | Audits de coûts approfondis avec transparence totale des ressources |
| **Support Multilingue** | Servez les utilisateurs dans 11 langues avec tarification localisée |
| **Intégration BIM** | Connectez à Revit/IFC pour l'estimation automatisée 4D/5D |
| **Entraînement de Modèles IA** | Utilisez des données structurées pour affiner l'IA de construction |

---

## À Propos

**DDC CWICR** (Construction Work Items, Components & Resources) est une base de données ouverte pour l'estimation des coûts de construction, couvrant tout le spectre des activités de construction - des terrassements et du coulage de béton aux travaux d'installation spécialisés.

La base de données s'appuie sur des sources décrivant les pratiques de construction modernes en Eurasie et dans la région Asie-Pacifique, où un écosystème de normalisation technique unifié sert de langage d'ingénierie commun pour plus de dix économies en développement dynamique. DDC CWICR représente un effort d'harmonisation des normes ouvertes en établissant un cadre réglementaire unique pour la gestion des projets d'investissement dans plusieurs langues.

<p align="center">
  <br>
  <img src="https://github.com/datadrivenconstruction/cad2data-Revit-IFC-DWG-DGN-pipeline-with-conversion-validation-qto/blob/main/DDC_in_additon/DDC_readme_content/DDC%20CWICR%20GEOGRAPHIC%20COVERAGE.jpg" width="100%"/>
  <br></br>
</p>

Les données structurées peuvent être accessibles via des formats tabulaires (XLSX, CSV, Parquet) ou interrogées de manière conversationnelle via LLM, permettant aux spécialistes d'intégrer les descriptions de travaux de construction (base de données vectorielle QDRANT) dans des pipelines automatisés et des workflows utilisant un langage simple ou des requêtes concises.

### Formats Disponibles

| Format      | Extension   | Taille       | Idéal Pour                            | Caractéristiques                     |
|-------------|-------------|--------------|---------------------------------------|--------------------------------------|
| **Excel**   | `.xlsx`     | ~150–400 Mo  | Analyse manuelle, filtrage, tableaux croisés | Lisible par l'homme, formatage complet |
| **Parquet** | `.parquet`  | ~55 Mo       | Pipelines ETL, entraînement ML, Big Data | Colonnes, excellente compression     |
| **CSV**     | `.csv`      | ~1,3 Go      | Import base de données, systèmes legacy | Compatibilité universelle            |
| **Qdrant**  | `.snapshot` | ~1 Go        | Recherche sémantique, RAG, assistants IA | Embeddings OpenAI pré-calculés       |


Une démo en direct est disponible sur [openconstructionestimate.com](https://openconstructionestimate.com/), où vous pouvez explorer les données et voir la base de données vectorielle en action pour la recherche sémantique.

<p align="center">
  <img src="https://github.com/datadrivenconstruction/cad2data-Revit-IFC-DWG-DGN-pipeline-with-conversion-validation-qto/blob/main/DDC_in_additon/DDC_readme_content/DDC%20CWICR%20Resource-based%20Work%20Cost%20Norms.jpg" alt="OpenConstructionEstimate" width="1000">
</p>

---

## Schéma de Données

La base de données contient **85 champs** organisés en groupes logiques. Chaque enregistrement représente soit un poste de travail (tarif) soit une ressource avec une ventilation complète des coûts.

```mermaid
erDiagram
    RATE ||--o{ RESOURCE : contient
    RATE ||--o{ LABOR : nécessite
    RATE ||--o{ MACHINERY : utilise
    RATE ||--o{ PRICE_VARIANT : possède

    RATE {
        string rate_code PK "MEKA_KASA_KAKATO_KAME"
        string rate_original_name "Installation de cloisons..."
        string rate_unit "100 m2"
        string category_type "TRAVAUX DE CONSTRUCTION"
        string collection_name "Constructions en bois"
        string department_name "CLOISONS..."
        string section_name "Installation de cloisons..."
        text work_composition_text
    }

    RESOURCE {
        string resource_code PK "KAME-NE-KAME-KARI"
        string resource_name "Plaques de plâtre"
        string resource_unit "m2"
        float resource_quantity "632.0"
        float resource_price_per_unit_eur "5.02"
        float resource_cost_eur "3170.73"
        boolean is_material
        boolean is_abstract
    }

    LABOR {
        string resource_code FK
        float labor_hours_workers "172"
        float labor_hours_operators "1.67"
        int count_workers_per_unit "172"
        int count_operators_per_unit "2"
        float cost_of_working_hours "3088.11"
    }

    MACHINERY {
        string machine_class2_name "Grues"
        string machine_class3_name "Grues sur châssis"
        float electricity_consumption_kwh "0.23"
        float price_operator_wages "13.56"
        float total_value_machinery "64.18"
    }

    PRICE_VARIANT {
        float price_est_median "5.02"
        float price_est_min "3.03"
        float price_est_max "7.99"
        int position_count "24"
        string variable_parts "renforcé de fibres de verre..."
    }
```

### Groupes de Champs
Les 85 champs de la base de données sont organisés en groupes logiques qui reflètent la méthodologie d'estimation des coûts basée sur les ressources. Chaque groupe sert une fonction spécifique dans la structure de ventilation des coûts: de la classification hiérarchique et l'identification des postes de travail à la consommation détaillée des ressources, aux besoins en main d'œuvre, aux coûts de machines et aux totaux agrégés. Cette structure modulaire permet aux utilisateurs de n'interroger que les champs pertinents pour leur tâche - qu'il s'agisse de générer une nomenclature de matériaux, d'analyser la productivité de la main d'œuvre ou de construire une estimation complète des coûts.

<p align="center">
  <br>
  <img src="https://github.com/datadrivenconstruction/cad2data-Revit-IFC-DWG-DGN-pipeline-with-conversion-validation-qto/blob/main/DDC_in_additon/DDC_readme_content/Resource-based%20Work%20Cost%20Norms%20table2.jpg" width="100%"/>
  <br></br>
</p>

**Classification** - `category_type`, `collection_code`, `collection_name`, `department_code`, `department_name`, `department_type`, `section_name`, `section_type`, `subsection_code`, `subsection_name`

**Poste de Travail (Tarif)** - `rate_code`, `rate_original_name`, `rate_final_name`, `rate_unit`, `row_type`, `is_scope`, `is_abstract`, `is_machine`, `is_labor`, `is_material`, `work_composition_text`

**Ressources** - `resource_code`, `resource_name`, `resource_unit`, `resource_quantity`, `parameter_resource_quantity`, `resource_price_per_unit_eur_current`, `resource_cost_eur`

**Main d'Œuvre** - `count_workers_per_unit`, `count_engineers_per_unit`, `count_operators_per_unit`, `count_total_people_per_unit`, `labor_hours_construction_workers`, `labor_hours_operators`, `labor_hours_engineers`, `total_labor_hours_workers_operators`, `total_labor_hours_all_personnel`, `cost_of_working_hours`, `count_people_per_day`

**Machines** - `machine_class2_name`, `machine_class3_name`, `personnel_operator_code`, `personnel_operator_grade`, `price_operator_wages`, `price_relocation_included`, `price_cost_without_wages`, `electricity_consumption_kwh_per_machine_hour`, `electricity_cost_per_unit`, `electricity_cost_total_sum`, `cost_operator_sum`, `total_value_machinery_equipment`

**Variantes de Prix** - `price_code_prefix`, `price_abstract_resource_common_start`, `price_abstract_resource_variable_parts`, `price_abstract_resource_position_count`, `price_abstract_resource_est_price_min`, `price_abstract_resource_est_price_max`, `price_abstract_resource_est_price_mean`, `price_abstract_resource_est_price_median`, `price_abstract_resource_unit`, `abstract_resource_tech_group`

**Agrégats** - `total_cost_per_position`, `total_material_cost_per_position`, `total_resource_cost_per_position`, `total_value_abstract_resources`, `materials_resource_cost_eur`

**Masse & Services** - `mass_name`, `mass_value`, `mass_unit`, `service_category`, `service_type`, `parameter_service_code`, `parameter_service_unit`, `parameter_service_name`, `parameter_service_quantity`, `service_cost_sum`

### Formule de Calcul des Coûts

| Composant         | Norme Technologique | ×   | Prix Régional   | =   | Coût                    |
|-------------------|---------------------|-----|-----------------|-----|-------------------------|
| 👷 **Main d'Œuvre** | 172 h/100m²        | ×   | €17,95/h        | =   | €3 088,11               |
| 🧱 **Matériaux**   | 632 m²/100m²        | ×   | €5,02/m²        | =   | €3 170,73               |
| 🚜 **Équipement**  | 1,67 h/100m²        | ×   | €38,42/h        | =   | €64,18                  |
|                   |                     |     | **Total**       | =   | **€7 725,91 pour 100m²** |

---

## Méthodologie

La valeur clé du **Calcul Basé sur les Ressources** est la séparation de la technologie de production invariable de la composante financière volatile. Elle est basée sur les "principes premiers" physiques de la construction:
- Heures de main d'œuvre requises pour un travail spécifique
- Quantités de matériaux par unité de travail
- Temps d'équipement nécessaire

**Pourquoi c'est important:**

- **Transparence** - Tarification sans marges cachées, ventilation complète des ressources
- **Auditabilité** - Capacité d'analyse approfondie pour l'analyse d'investissement et la vérification
- **Portabilité** - Normes indépendantes de la région applicables sur différents marchés
- **Éprouvé** - Méthodologie standard de l'industrie établie depuis plus de 100 ans

```mermaid
flowchart TB
    subgraph Source["📦 Source de Données"]
        CWICR[(DDC CWICR<br/>────────────<br/>55 719 Postes de Travail<br/>27 672 Ressources<br/>85 Champs par Enregistrement)]
    end

    subgraph Processing["⚙️ Pipeline de Traitement"]
        direction LR
        ETL[["🔄 ETL<br/>Extraction &<br/>Transformation"]]
        TRANS[["🌐 Traduction<br/>11 Langues"]]
        EMBED[["🧠 Vectorisation<br/>OpenAI 3072d"]]
        ETL --> TRANS --> EMBED
    end

    subgraph Outputs["📤 Formats de Sortie"]
        XLSX[("📊 Excel<br/>.xlsx")]
        PARQUET[("⚡ Parquet<br/>.parquet")]
        CSV[("📄 CSV<br/>.csv")]
        QDRANT[("🔍 Qdrant<br/>.snapshot")]
    end

    subgraph Apps["🎯 Applications"]
        SEARCH["🔎 Recherche<br/>Sémantique"]
        BIM["🏗️ BIM 5D<br/>Intégration"]
        RAG["🤖 Systèmes<br/>RAG"]
        BI["📈 Analyse<br/>BI"]
    end

    Source --> Processing
    Processing --> XLSX & PARQUET & CSV & QDRANT
    XLSX & PARQUET & CSV --> BI & BIM
    QDRANT --> SEARCH & RAG & BIM

    style Source fill:#dbeafe,stroke:#2563eb,stroke-width:2px
    style Processing fill:#fef3c7,stroke:#d97706,stroke-width:2px
    style Outputs fill:#d1fae5,stroke:#059669,stroke-width:2px
    style Apps fill:#fce7f3,stroke:#db2777,stroke-width:2px
```


### Contexte Historique

Les descriptions de travaux de construction dans cette base de données sont fondées sur une méthodologie de normalisation basée sur les ressources dont les racines remontent des normes de production du début du XXe siècle aux systèmes de référence numériques d'aujourd'hui. Développée et affinée en continu depuis les années 1920, cette approche a connu une évolution particulièrement robuste dans la région eurasienne.

Au cours de cent ans de développement, le système est passé des calculs manuels aux formats lisibles par machine - mais son principe fondamental reste intact: la mesure précise des ressources physiques nécessaires par unité de production de construction. Les implémentations modernes font le lien entre les données normatives historiques et les prix du marché en temps réel.

Les adaptations régionales de cette méthodologie fonctionnent sous diverses désignations nationales: ENIR, GESN, FER, NRR, ESN, AzDTN, ShNQK, MKS ChT, SNT, BNbD, Dinh Muc, Ding'e.

<p align="center">
  <img src="https://github.com/datadrivenconstruction/cad2data-Revit-IFC-DWG-DGN-pipeline-with-conversion-validation-qto/blob/main/DDC_in_additon/DDC_readme_content/DDC%20CWICR%20SPREAD%20OF%20METHODOLOGY%20FROM%20THE%201920s.jpg" alt="OpenConstructionEstimate" width="1000">
</p>

⭐ <b>Si vous voulez voir de nouvelles mises à jour et versions de la base de données et si vous trouvez nos outils utiles, merci de donner une étoile à nos repositories pour voir plus d'applications similaires pour l'industrie de la construction.</b>
Mettez une étoile au workflow DDC sur GitHub et soyez instantanément notifié des nouvelles releases.
<p align="center">
  <br>
  <img src="https://github.com/datadrivenconstruction/cad2data-Revit-IFC-DWG-DGN-pipeline-with-conversion-validation-qto/blob/main/DDC_in_additon/DDC_readme_content/OCE%20star%20GitHub.gif" width="100%"/>
  <br></br>
</p>


---


## Intégration

### Cas d'Utilisation

- **Niveau Débutant** - Benchmarking des Coûts, Indexation des Prix, Estimation des Appels d'Offres

- **Intermédiaire** - Localisation, Pipelines ETL/BI, Calcul CO₂

- **Avancé** - Entraînement IA/ML, CAD (BIM) 5D, Audit d'Investissement Approfondi

---

## Workflows n8n - Description Détaillée

Quatre workflows prêts pour la production pour l'estimation automatisée des coûts de construction. Chaque workflow se connecte à la base de données vectorielle DDC CWICR via Qdrant et utilise des modèles IA pour le parsing intelligent et la correspondance.

| #   | Workflow                                                        | Entrée      | Idéal Pour                      | Télécharger                                                                                         |
|-----|-----------------------------------------------------------------|-------------|---------------------------------|-----------------------------------------------------------------------------------------------------|
| 1   | [Bot Estimateur de Texte](#1️⃣-bot-estimateur-de-texte)         | 💬 Texte    | Estimations rapides depuis texte | [JSON](./n8n_1_Telegram_Bot_Cost_Estimates_and_Rate_Finder_TEXT_DDC_CWICR.json)                     |
| 2   | [Estimateur Photo](#2️⃣-estimateur-de-coûts-par-photo)          | 📷 Photo    | Visites de chantier, inspections | [JSON](./n8n_2_Photo_Cost_Estimate_DDC_CWICR.json)                                                  |
| 3   | [Bot Universel](#3️⃣-bot-universel-texte--photo--pdf)           | 💬📷📄 Tout | Usage production complet        | [JSON](./n8n_3_Telegram_Bot_Cost_Estimates_and_Rate_Finder_TEXT_PHOTO_PDF_DDC_CWICR.json)           |
| 4   | [Pipeline CAD/BIM](#4️⃣-pipeline-destimation-cad-bim)           | 🏗️ Revit   | Estimation 4D/5D basée sur BIM  | [JSON](./n8n_4_CAD_(BIM)_Cost_Estimation_Pipeline_4D_5D_with_DDC_CWICR.json)                        |

---

### 1️⃣ Bot Estimateur de Texte

**Fichier:** `n8n_1_Telegram_Bot_Cost_Estimates_and_Rate_Finder_TEXT_DDC_CWICR.json`

Bot Telegram pour l'estimation des coûts basée sur le texte. Décrivez les travaux de construction en langage naturel - le bot analyse l'entrée, recherche dans la base de données vectorielle et retourne des ventilations de coûts détaillées.

<p align="center">
  <br>
  <img src="https://github.com/datadrivenconstruction/cad2data-Revit-IFC-DWG-DGN-pipeline-with-conversion-validation-qto/blob/main/DDC_in_additon/DDC_readme_content/Text_Estimator_Bot.jpg" width="100%"/>
  <br></br>
</p>

<h3 align="left">🤖 Essayez Maintenant - Bots de Démo en Direct</h3>
<p align="left"><i>Testez les workflows d'estimation instantanément sur Telegram</i></p>
<p><b>@TextOpenConstructionEstimate_bot</b></p>
<p>Créez des estimations de coûts complètes<br>à partir de descriptions textuelles</p>
<a href="https://t.me/TextOpenConstructionEstimate_bot">
<img src="https://img.shields.io/badge/Ouvrir_Bot-26A5E4?style=for-the-badge&logo=telegram&logoColor=white" alt="Bot Texte"/>
</a>

```mermaid
flowchart LR
    subgraph Input["💬 ENTRÉE"]
        A[Message Telegram]
    end

    subgraph AI["🤖 TRAITEMENT IA"]
        B[Analyser Texte]
        C[Extraire Postes]
    end

    subgraph Search["🔍 RECHERCHE VECTORIELLE"]
        D[Générer Embeddings]
        E[Recherche Qdrant]
        F[Reranking IA]
    end

    subgraph Output["📊 SORTIE"]
        G[Calculer Coûts]
        H[Rapport HTML]
        I[Export Excel]
    end

    A --> B --> C --> D --> E --> F --> G --> H
    G --> I

    style Input fill:#e0f2fe,stroke:#0284c7
    style AI fill:#fef3c7,stroke:#d97706
    style Search fill:#dcfce7,stroke:#16a34a
    style Output fill:#f3e8ff,stroke:#9333ea
```



**Comment ça marche:**

| Étape | Action                                 | Technologie                            |
|-------|----------------------------------------|----------------------------------------|
| 1     | L'utilisateur envoie une description texte | API Bot Telegram                    |
| 2     | L'IA analyse et extrait les postes de travail | OpenAI / Claude / Gemini          |
| 3     | Génère des embeddings pour chaque poste | OpenAI `text-embedding-3-large`       |
| 4     | Recherche les tarifs correspondants dans la base | Recherche vectorielle Qdrant     |
| 5     | L'IA reranke les résultats pour la précision | Scoring LLM                        |
| 6     | Calcule les coûts et génère le rapport | HTML / Excel / PDF                    |

**Fonctionnalités:**

| Fonctionnalité               | Description                                                          |
|------------------------------|----------------------------------------------------------------------|
| 💬 Entrée en langage naturel | Accepte tout format texte - listes, phrases, descriptions structurées |
| 🤖 Support multi-LLM         | Fonctionne avec OpenAI, Claude ou Gemini (commutable)                |
| 🔍 Recherche sémantique      | Trouve les meilleures correspondances même avec une formulation différente |
| 🌍 11 langues                | DE, EN, RU, ES, FR, PT, ZH, AR, HI, US, UK                           |
| 📊 Exports multiples         | Rapport HTML, feuille de calcul Excel, document PDF                  |
| ✏️ Édition interactive       | Modifiez les quantités avant le calcul final                         |

**Credentials requis:**
- Token Bot Telegram (depuis @BotFather)
- Clé API OpenAI (pour embeddings + LLM optionnel)
- URL Qdrant + Clé API

---

### 2️⃣ Estimateur de Coûts par Photo

**Fichier:** `n8n_2_Photo_Cost_Estimate_DDC_CWICR.json`

Interface formulaire web pour l'estimation basée sur les photos. Téléchargez une photo de construction - l'IA Vision identifie les éléments, estime les dimensions et calcule automatiquement les coûts.

<p align="center">
  <br>
  <img src="https://github.com/datadrivenconstruction/cad2data-Revit-IFC-DWG-DGN-pipeline-with-conversion-validation-qto/blob/main/DDC_in_additon/DDC_readme_content/n8n%20pipeline%20photo%20estimator.jpg" width="100%"/>
  <br></br>
</p>

```mermaid
flowchart TB
    subgraph Upload["📷 TÉLÉCHARGEMENT PHOTO"]
        A[Formulaire Web]
        B[Sélectionner Région]
        C[Choisir Type de Travaux]
    end

    subgraph Vision["👁️ IA VISION"]
        D[Analyse GPT-4 Vision]
        E[Identifier Éléments]
        F[Estimer Dimensions]
        G[Détecter Type de Pièce]
    end

    subgraph Decompose["🔧 DÉCOMPOSITION"]
        H[Éléments → Postes de Travail]
        I[Calculer Quantités]
    end

    subgraph Price["💰 TARIFICATION"]
        J[Recherche Vectorielle]
        K[Correspondance Tarifs DDC]
        L[Appliquer Prix Régionaux]
    end

    subgraph Report["📄 RAPPORT"]
        M[Générer HTML]
        N[Ventilation des Coûts]
    end

    A --> B --> C --> D
    D --> E --> F --> G
    G --> H --> I
    I --> J --> K --> L
    L --> M --> N

    style Upload fill:#dbeafe,stroke:#2563eb
    style Vision fill:#fef3c7,stroke:#d97706
    style Decompose fill:#dcfce7,stroke:#16a34a
    style Price fill:#fee2e2,stroke:#dc2626
    style Report fill:#f3e8ff,stroke:#9333ea
```



**Comment ça marche:**

| Étape | Action                                        | Technologie                          |
|-------|-----------------------------------------------|--------------------------------------|
| 1     | L'utilisateur télécharge une photo via formulaire web | n8n Form Trigger                 |
| 2     | L'IA Vision analyse l'image                   | GPT-4 Vision                         |
| 3     | Identifie le type de pièce, éléments, matériaux | Extraction JSON structurée          |
| 4     | Estime les dimensions depuis objets de référence | Raisonnement IA (portes, carreaux, etc.) |
| 5     | Décompose les éléments en postes de travail   | Traitement LLM                       |
| 6     | Tarife chaque travail via recherche vectorielle | Qdrant + embeddings OpenAI          |
| 7     | Génère un rapport HTML professionnel          | Sortie stylisée                      |

**Fonctionnalités:**

| Fonctionnalité         | Description                                             |
|------------------------|---------------------------------------------------------|
| 📷 Analyse photo       | GPT-4 Vision identifie les éléments de construction     |
| 📐 Dimensionnement auto | Estime les tailles en utilisant des objets de référence (portes, carreaux) |
| 🏠 Détection de pièce  | Salle de bain, cuisine, chambre, extérieur, etc.        |
| 🔨 Support type travaux | Construction neuve / Rénovation / Réparation           |
| 🌍 9 bases régionales  | Prix localisés pour Berlin, Toronto, Paris, etc.        |
| 📄 Rapports professionnels | Sortie HTML propre prête pour les clients            |

**Credentials requis:**
- Clé API OpenAI (GPT-4 Vision + embeddings)
- URL Qdrant + Clé API

---

### 3️⃣ Bot Universel (Texte + Photo + PDF)

**Fichier:** `n8n_3_Telegram_Bot_Cost_Estimates_and_Rate_Finder_TEXT_PHOTO_PDF_DDC_CWICR.json`

Bot Telegram complet supportant tous les types d'entrée: descriptions textuelles, photos de construction et plans PDF. Le workflow le plus complet pour une utilisation en production.


<p align="center">
  <br>
  <img src="https://github.com/datadrivenconstruction/cad2data-Revit-IFC-DWG-DGN-pipeline-with-conversion-validation-qto/blob/main/DDC_in_additon/DDC_readme_content/Universal%20Estimator%20Bot%20Text%20%20Photo%20PDF.jpg" width="100%"/>
  <br></br>
</p>

```mermaid
flowchart TB
    subgraph Input["📥 MULTI-ENTRÉE"]
        A[💬 Message Texte]
        B[📷 Photo]
        C[📄 Document PDF]
    end

    subgraph Router["🔀 ROUTEUR INTELLIGENT"]
        D{Détecter Type}
    end

    subgraph TextPath["💬 CHEMIN TEXTE"]
        E[Analyse IA Texte]
        F[Extraire Travaux]
    end

    subgraph PhotoPath["📷 CHEMIN PHOTO"]
        G[IA Vision]
        H[Identifier Éléments]
        I[Décomposer]
    end

    subgraph PDFPath["📄 CHEMIN PDF"]
        J[Extraire Pages]
        K[Analyse Vision]
        L[Analyser Contenu]
    end

    subgraph Common["🔍 PIPELINE COMMUN"]
        M[Générer Embeddings]
        N[Recherche Qdrant]
        O[Reranking IA]
        P[Calculer Coûts]
    end

    subgraph Export["📤 EXPORT"]
        Q[Rapport HTML]
        R[Excel CSV]
        S[Document PDF]
    end

    A --> D
    B --> D
    C --> D
    D -->|Texte| E --> F --> M
    D -->|Photo| G --> H --> I --> M
    D -->|PDF| J --> K --> L --> M
    M --> N --> O --> P
    P --> Q
    P --> R
    P --> S

    style Input fill:#e0f2fe,stroke:#0284c7
    style Router fill:#fef3c7,stroke:#d97706
    style TextPath fill:#dcfce7,stroke:#16a34a
    style PhotoPath fill:#fce7f3,stroke:#db2777
    style PDFPath fill:#f3e8ff,stroke:#9333ea
    style Common fill:#fee2e2,stroke:#dc2626
    style Export fill:#d1fae5,stroke:#059669
```



**Comment ça marche:**

| Étape | Action                                    | Technologie                    |
|-------|-------------------------------------------|--------------------------------|
| 1     | L'utilisateur envoie texte, photo ou PDF  | API Bot Telegram               |
| 2     | Le routeur détecte le type d'entrée       | Analyse content-type           |
| 3a    | **Texte:** L'IA analyse les postes de travail | OpenAI / Gemini             |
| 3b    | **Photo:** L'IA Vision extrait les éléments | GPT-4 Vision / Gemini 2.0   |
| 3c    | **PDF:** Extrait et analyse les pages     | Traitement PDF + Vision        |
| 4     | Recherche sémantique dans DDC CWICR       | Base de données vectorielle Qdrant |
| 5     | Reranking IA pour meilleures correspondances | Scoring LLM                  |
| 6     | Édition interactive via menu du bot       | Claviers inline Telegram       |
| 7     | Exporter les résultats                    | HTML / Excel / PDF             |

**17 Actions du Bot:**

| Action           | Description                         |
|------------------|-------------------------------------|
| `/start`         | Menu de sélection de langue         |
| Téléchargement photo | Déclenche l'analyse IA vision    |
| Message texte    | Analyse et extrait les postes       |
| Téléchargement PDF | Traite les plans                  |
| Éditer quantités | Modifier avant calcul               |
| Ajouter travail  | Entrée manuelle de poste            |
| Calculer         | Exécuter l'estimation complète      |
| Voir détails     | Afficher ressources pour chaque poste |
| Export Excel     | Télécharger feuille de calcul CSV   |
| Export PDF       | Générer rapport PDF                 |
| Aide             | Afficher instructions d'utilisation |
| Affiner          | Ré-analyser avec corrections        |

**Fonctionnalités:**

| Fonctionnalité        | Description                                        |
|-----------------------|----------------------------------------------------|
| 📷 Double IA Vision   | Gemini 2.0 Flash ou GPT-4 Vision (configurable)    |
| 📄 Traitement PDF     | Plans, DQE scannés, documents                      |
| 💬 Analyse texte intelligente | Gère listes, tableaux, texte libre          |
| 🔍 Reranking IA       | Améliore la précision des correspondances          |
| ✏️ Édition complète   | Ajouter, supprimer, modifier les postes de travail |
| 📊 Export multi-format | HTML, Excel, PDF                                  |
| 🌍 11 langues         | Localisation complète                              |

**Credentials requis:**
- Token Bot Telegram
- Clé API OpenAI (embeddings)
- Clé API Gemini (Vision) ou OpenAI GPT-4 Vision
- URL Qdrant + Clé API

---

### 4️⃣ Pipeline d'Estimation CAD (BIM)

**Fichier:** `n8n_4_CAD_(BIM)_Cost_Estimation_Pipeline_4D_5D_with_DDC_CWICR.json`

Estimation automatisée des coûts à partir de modèles Revit/IFC/DWG. Extrait les données BIM, classifie les éléments, décompose en postes de travail et génère des estimations 4D/5D avec ventilation complète des ressources.

<p align="left">
  <a href="https://datadrivenconstruction.io">
    <img src="https://github.com/datadrivenconstruction/cad2data-Revit-IFC-DWG-DGN-pipeline-with-conversion-validation-qto/blob/main/DDC_in_additon/DDC_readme_content/CAD%20(Revit)%20to%205D-4D%20Cost%20and%20Time%20Estimate.jpg" alt="DataDrivenConstruction">
  </a>
</p>

```mermaid
flowchart TB
    subgraph INPUT["📁 ENTRÉE<br/><i>CAD • photos • description textuelle</i>"]
        CAD["📐 Entrée Projet<br/>(texte • photos • RVT / IFC / DWG)"]
    end

    subgraph EXTRACT["⚙️ EXTRACTION"]
        CONV["RvtExporter.exe / CAD Export / ETL"]
        XLSX["📊 .XLSX<br/>(Éléments Bruts)"]
    end

    subgraph PREP["🔧 PRÉPARATION DES DONNÉES"]
        PREP_AI["🤖 IA: Nettoyer & Classifier<br/><i>en-têtes • types • catégories</i>"]
    end

    subgraph STAGE_PLAN["📋 ÉTAPES 1–3: Planification"]
        PLAN["🤖 Détecter Projet & Phases<br/><i>neuf / rénovation / démolition</i><br/><i>petit / moyen / grand</i><br/><i>éléments → phases de construction</i>"]
    end

    subgraph STAGE4["🔨 ÉTAPE 4: Décomposition"]
        S4["🤖 Décomposer Types en Travaux<br/><i>'Mur Briques 240mm' → maçonnerie, mortier, enduit</i>"]
    end

    subgraph STAGE5["💰 ÉTAPE 5: Tarification"]
        S5["🤖 Tarifer via Base Vectorielle<br/><i>Embeddings OpenAI + Qdrant</i><br/><i>rate_code, unit_cost, ressources</i>"]
    end

    subgraph STAGE75["✅ ÉTAPE 7.5: Validation"]
        S75["🤖 Revue CTO<br/><i>complétude • doublons • travaux manquants</i>"]
    end

    subgraph OUTPUT["📤 SORTIE"]
        HTML["📄 Rapport HTML"]
        XLS["📊 Rapport XLS"]
    end

    CAD --> CONV --> XLSX
    XLSX --> PREP_AI --> PLAN --> S4 --> S5 --> S75
    S75 --> HTML & XLS

    style INPUT fill:#f4f4f5,stroke:#d4d4d8,color:#18181b
    style EXTRACT fill:#e0f2fe,stroke:#bae6fd,color:#0f172a
    style PREP fill:#ede9fe,stroke:#ddd6fe,color:#1e1b4b
    style STAGE_PLAN fill:#ecfdf5,stroke:#bbf7d0,color:#064e3b
    style STAGE4 fill:#fef9c3,stroke:#fef3c7,color:#78350f
    style STAGE5 fill:#fee2e2,stroke:#fecaca,color:#7f1d1d
    style STAGE75 fill:#e0f2f1,stroke:#bae5e1,color:#134e4a
    style OUTPUT fill:#eef2ff,stroke:#e0e7ff,color:#111827
```


**n8n fournit plus de 400 intégrations natives** avec des plateformes comme Google Sheets, Notion, Slack, Airtable, bases de données (PostgreSQL, MongoDB), stockage cloud, et plus. Chaque nœud dans ce workflow est modulaire - vous pouvez:

- 🔄 **Changer de fournisseur LLM** (OpenAI ↔ Claude ↔ Gemini ↔ Grok)
- 📊 **Connecter à votre ERP ou système de gestion de projet**
- 📁 **Exporter les résultats vers n'importe quelle destination** (stockage cloud, email, tableaux de bord)
- 🔧 **Modifier n'importe quelle étape** pour correspondre à votre méthodologie d'estimation

Le workflow vous appartient pour l'adapter. Pas de restrictions. Pas de frais de licence. Contrôle total.

---

## 📋 Prérequis

| Composant                                          | Requis                                 | Description                                                           |
|----------------------------------------------------|----------------------------------------|-----------------------------------------------------------------------|
| **[n8n](https://n8n.io/)**                         | v1.0+ (v2.0+ nécessite [configuration](#️-configuration-n8n-20-requise)) | Plateforme d'automatisation de workflow pour orchestrer le pipeline d'estimation |
| **[Qdrant](https://qdrant.tech/)**                 | Instance Cloud ou auto-hébergée        | Base de données vectorielle pour recherche sémantique parmi les postes de travail |
| **[API OpenAI](https://platform.openai.com/)**     | Pour embeddings (`text-embedding-3-large`) | Génère des embeddings vectoriels pour les éléments BIM et la correspondance avec la base de coûts |
| **API LLM**                                        | OpenAI / Claude / Gemini / xAI Grok    | Modèles IA pour la classification des postes et la génération d'estimations |
| **[Convertisseur DDC](https://github.com/datadrivenconstruction/cad2data-Revit-IFC-DWG-DGN-pipeline-with-conversion-validation-qto)** | `RvtExporter.exe` | Extrait les données BIM des modèles Revit vers Excel/JSON pour traitement |

---

## Démarrage Rapide des Workflows

### Étape 1: Importer le Workflow

```
n8n → Nouveau workflow → Importer depuis fichier → Sélectionner JSON
```

### Étape 2: Configurer les Credentials

Dans le nœud **🔑 TOKEN**, définissez vos clés API:

```json
{
  "bot_token": "VOTRE_TOKEN_BOT_TELEGRAM",
  "OPENAI_API_KEY": "VOTRE_CLE_OPENAI",
  "GEMINI_API_KEY": "VOTRE_CLE_GEMINI",
  "QDRANT_URL": "http://localhost:6333",
  "QDRANT_API_KEY": ""
}
```

### Étape 3: Charger DDC CWICR dans Qdrant

Téléchargez le snapshot depuis le dossier de langue correspondant (stocké via Git LFS) et importez:

```bash
curl -X POST "http://localhost:6333/collections/ddc_fr_paris/snapshots/upload" \
  -H "Content-Type: multipart/form-data" \
  -F "snapshot=@EN___DDC_CWICR/EN_TORONTO_workitems_costs_resources_EMBEDDINGS_3072_DDC_CWICR.snapshot"
```

### Étape 4: Activer & Tester

- Activez le workflow dans n8n
- Pour les bots Telegram: envoyez `/start` à votre bot
- Pour les formulaires web: ouvrez l'URL du formulaire fournie par n8n

---

## ⚠️ Configuration n8n 2.0+ Requise

> **À partir de la version 2.0 de n8n, le nœud Execute Command est désactivé par défaut pour des raisons de sécurité.**
>
> Sans la configuration ci-dessous, les workflows utilisant Execute Command (notamment le Pipeline CAD/BIM) **ne fonctionneront pas** - les nœuds s'afficheront avec un point d'interrogation ou ne seront pas reconnus.

### Solution Rapide

**Windows (CMD) - exécuter à chaque fois:**
```cmd
set NODES_EXCLUDE=[] && npx n8n
```

**Solution permanente - créer une fois:**

Créez le fichier `C:\Users\VOTRE_UTILISATEUR\.n8n\.env` avec:
```
NODES_EXCLUDE=[]
```
Puis lancez simplement `npx n8n` comme d'habitude.

**Docker:**
```yaml
environment:
  - NODES_EXCLUDE=[]
```

### Vérifier la Configuration

1. Démarrez n8n
2. Cliquez sur **+** → recherchez **"Execute Command"**
3. Si le nœud apparaît → ✅ vous êtes prêt!

> 📚 Plus de détails: [n8n 2.0 Breaking Changes](https://docs.n8n.io/2-0-breaking-changes/)

---

## 🌍 Langues & Niveaux de Prix Supportés

| Code  | Langue      | Niveau de Prix    | Devise | Collection Qdrant         |
|-------|-------------|-------------------|--------|---------------------------|
| `AR`  | Arabe       | Dubaï             | AED    | `ddc_ar_dubai`            |
| `DE`  | Allemand    | Berlin            | EUR    | `ddc_de_berlin`           |
| `EN`  | Anglais     | Toronto           | CAD    | `ddc_en_toronto`          |
| `ES`  | Espagnol    | Barcelone         | EUR    | `ddc_sp_barcelona`        |
| `FR`  | Français    | Paris             | EUR    | `ddc_fr_paris`            |
| `HI`  | Hindi       | Mumbai            | INR    | `ddc_hi_mumbai`           |
| `PT`  | Portugais   | São Paulo         | BRL    | `ddc_pt_saopaulo`         |
| `RU`  | Russe       | Saint-Pétersbourg | RUB    | `ddc_ru_stpetersburg`     |
| `ZH`  | Chinois     | Shanghai          | CNY    | `ddc_zh_shanghai`         |
| `US`  | Anglais     | USA               | USD    | `ddc_usa_usd`             |
| `UK`  | Anglais     | UK                | GBP    | `ddc_uk_gbp`              |

---

## 📊 Étapes du Pipeline

Le workflow CAD/BIM traite les données à travers 10 étapes:

| Étape   | Nom                  | Description                                                       |
|---------|----------------------|-------------------------------------------------------------------|
| **0**   | Collecter Données BIM | Extraire les éléments de Revit via Convertisseur DDC             |
| **1**   | Détection Projet     | L'IA identifie le type de projet (Résidentiel, Commercial, etc.) |
| **2**   | Génération Phases    | L'IA crée les phases de construction                              |
| **3**   | Affectation Éléments | L'IA mappe les types BIM aux phases                              |
| **4**   | Décomposition Travaux | L'IA décompose les types en postes de travail ("Mur Briques" → maçonnerie, mortier) |
| **5**   | Recherche Vectorielle | Trouver les tarifs correspondants dans DDC CWICR via Qdrant      |
| **6**   | Mapping Unités       | Convertir les unités BIM en unités de tarif                      |
| **7**   | Calcul Coûts         | Qté × Prix Unitaire pour chaque poste                            |
| **7.5** | Validation           | Revue CTO pour complétude et doublons                            |
| **8**   | Agrégation           | Somme par phases et catégories                                   |
| **9**   | Génération Rapport   | Créer les sorties HTML et Excel                                  |

---

## ⚙️ Sélection du Modèle LLM

Le workflow supporte plusieurs fournisseurs IA. Activez votre modèle préféré dans la section **Modèles LLM**:

| Modèle           | Nom du Nœud                  | Statut       |
|------------------|------------------------------|--------------|
| OpenAI GPT-4o    | `OpenAI LLM`                 | ✅ Par défaut |
| Claude Opus 4    | `Anthropic Chat Model2`      | Désactivé    |
| Gemini 2.5 Pro   | `Google Gemini Chat Model`   | Désactivé    |
| xAI Grok         | `xAI Grok Chat Model1`       | Désactivé    |
| DeepSeek         | `DeepSeek Chat Model`        | Désactivé    |

Pour changer de modèle: **Activez** le nœud du modèle souhaité et **Désactivez** les autres.

---

## 📁 Fichiers de Sortie

Les rapports sont sauvegardés dans le dossier du projet:
```
projet_YYYY-MM-DD.html   ← Rapport interactif (s'ouvre dans le navigateur)
projet_YYYY-MM-DD.xls    ← Feuille de calcul compatible Excel
```
<p align="center">
  <br>
  <img src="https://github.com/datadrivenconstruction/cad2data-Revit-IFC-DWG-DGN-pipeline-with-conversion-validation-qto/blob/main/DDC_in_additon/DDC_readme_content/The%20generated%20report%20includes.jpg" width="100%"/>
  <br></br>
</p>

---

## 🔗 Collections Qdrant

Le workflow sélectionne automatiquement la collection correcte basée sur `language_code`:

```
{LANG}_{CITY}_workitems_costs_resources_EMBEDDINGS_3072_DDC_CWICR
```

Exemple: `FR_PARIS_workitems_costs_resources_EMBEDDINGS_3072_DDC_CWICR`

---

## ⚠️ Dépannage

| Problème                     | Solution                                                    |
|------------------------------|-------------------------------------------------------------|
| "Execute Command manquant" (n8n 2.0+) | Définissez la variable d'environnement `NODES_EXCLUDE=[]`. Voir [Configuration n8n 2.0+](#️-configuration-n8n-20-requise) |
| "Fichier Excel non trouvé"   | Vérifiez les chemins `path_to_converter` et `project_file`  |
| "Connexion Qdrant échouée"   | Vérifiez l'URL Qdrant et la clé API dans les credentials    |
| "Limite de taux dépassée"    | Réduisez la taille des lots ou ajoutez des délais entre appels API |
| "Prix non trouvé"            | Vérifiez si la collection de langue correcte existe dans Qdrant |
| "Erreur webhook Telegram"    | Assurez-vous que le workflow est actif et l'URL webhook accessible |
| "API Vision échouée"         | Vérifiez que la clé API Gemini ou OpenAI Vision est valide  |

---

## Base de Données Vectorielle

Collections Qdrant prêtes à l'emploi avec embeddings OpenAI `text-embedding-3-large` pour la recherche sémantique parmi les postes de travail de construction.

Les bases de données vectorielles vous permettent de "parler" à vos données en langage naturel – en utilisant des phrases simples ou de courtes expressions au lieu de code ou de filtres complexes. Cela accélère considérablement la recherche du bon poste de travail ou ligne de coût, même dans de très grands ensembles de données.

Ces collections Qdrant peuvent être connectées à des applications via des workflows d'automatisation et d'intégration modernes (par exemple, des outils Workflow et Pipeline low-code/no-code). Vous pouvez construire des assistants qui recherchent, filtrent et expliquent les postes de travail de construction, ou intégrer la recherche sémantique directement dans vos outils existants d'estimation et de contrôle de projet.

---

### Snapshots de la Base de Données Vectorielle Qdrant

Les snapshots se trouvent désormais directement dans les dossiers de langue correspondants de ce dépôt (stockés via Git LFS), et non plus dans les GitHub Releases.

| Langue          | Région            | Fichier de Snapshot (dans le dossier de langue)                                           |
|-----------------|-------------------|-------------------------------------------------------------------------------------------|
| 🇸🇦 Arabe       | Dubaï             | `AR___DDC_CWICR/AR_DUBAI_workitems_costs_resources_EMBEDDINGS_3072_DDC_CWICR.snapshot`    |
| 🇨🇳 Chinois     | Shanghai          | `ZH___DDC_CWICR/ZH_SHANGHAI_workitems_costs_resources_EMBEDDINGS_3072_DDC_CWICR.snapshot` |
| 🇩🇪 Allemand    | Berlin            | `DE___DDC_CWICR/DE_BERLIN_workitems_costs_resources_EMBEDDINGS_3072_DDC_CWICR.snapshot`   |
| 🇬🇧 Anglais     | Toronto           | `EN___DDC_CWICR/EN_TORONTO_workitems_costs_resources_EMBEDDINGS_3072_DDC_CWICR.snapshot`  |
| 🇪🇸 Espagnol    | Barcelone         | `ES___DDC_CWICR/SP_BARCELONA_workitems_costs_resources_EMBEDDINGS_3072_DDC_CWICR.snapshot`|
| 🇫🇷 Français    | Paris             | `FR___DDC_CWICR/FR_PARIS_workitems_costs_resources_EMBEDDINGS_3072_DDC_CWICR.snapshot`    |
| 🇮🇳 Hindi       | Mumbai            | `HI___DDC_CWICR/HI_MUMBAI_workitems_costs_resources_EMBEDDINGS_3072_DDC_CWICR.snapshot`   |
| 🇧🇷 Portugais   | São Paulo         | `PT___DDC_CWICR/PT_SAOPAULO_workitems_costs_resources_EMBEDDINGS_3072_DDC_CWICR.snapshot` |
| 🇷🇺 Russe       | Saint-Pétersbourg | `RU___DDC_CWICR/RU_STPETERSBURG_workitems_costs_resources_EMBEDDINGS_3072_DDC_CWICR.snapshot` |
| 🇬🇧 UK          | GBP               | `UK___DDC_CWICR/UK_GBP_workitems_costs_resources_EMBEDDINGS_3072_DDC_CWICR.snapshot`      |
| 🇺🇸 USA         | USD               | `US___DDC_CWICR/USA_USD_workitems_costs_resources_EMBEDDINGS_3072_DDC_CWICR.snapshot`     |

### Collections

🇸🇦 `ddc_ar_dubai` (Arabe) · 🇨🇳 `ddc_zh_shanghai` (Chinois) · 🇩🇪 `ddc_de_berlin` (Allemand) · 🇬🇧 `ddc_en_toronto` (Anglais) · 🇪🇸 `ddc_sp_barcelona` (Espagnol) · 🇫🇷 `ddc_fr_paris` (Français) · 🇮🇳 `ddc_hi_mumbai` (Hindi) · 🇧🇷 `ddc_pt_saopaulo` (Portugais) · 🇷🇺 `ddc_ru_stpetersburg` (Russe) · 🇺🇸 `ddc_usa_usd` (USA) · 🇬🇧 `ddc_uk_gbp` (UK)

Chaque collection contient **55 719 vecteurs** avec métadonnées payload complètes.

### Déploiement Docker

```yaml
# docker-compose.yml
services:
  qdrant:
    image: qdrant/qdrant:latest
    container_name: ddc-cwicr-qdrant
    ports:
      - "6333:6333"
      - "6334:6334"
    volumes:
      - qdrant_storage:/qdrant/storage
      - ./snapshots:/qdrant/snapshots
    environment:
      - QDRANT__LOG_LEVEL=INFO
    restart: unless-stopped

volumes:
  qdrant_storage:
```

```bash
# Démarrer
docker-compose up -d

# Importer snapshot
curl -X POST "http://localhost:6333/collections/ddc_fr_paris/snapshots/upload" \
  -H "Content-Type: multipart/form-data" \
  -F "snapshot=@FR___DDC_CWICR/FR_PARIS_workitems_costs_resources_EMBEDDINGS_3072_DDC_CWICR.snapshot"

# Tableau de bord: http://localhost:6333/dashboard
```
---

## 🌐 Pricing Search API - BuildCalculator.io

<p align="center">
  <a href="https://buildcalculator.io/api-docs/">
    <img src="https://img.shields.io/badge/Documentation_API-buildcalculator.io-2563eb?style=for-the-badge" alt="API Docs">
  </a>
  &nbsp;
  <img src="https://img.shields.io/badge/Authentification-Non_requise-059669?style=for-the-badge" alt="No Auth">
  &nbsp;
  <img src="https://img.shields.io/badge/Coût-Gratuit-059669?style=for-the-badge" alt="Free">
  &nbsp;
  <img src="https://img.shields.io/badge/Limite-60_req/min-d97706?style=for-the-badge" alt="Rate Limit">
</p>

API REST gratuite pour rechercher des postes de construction avec ventilation complète des coûts, main-d'œuvre, matériaux et équipements. **55 719 postes** dans **11 langues** avec **84 champs** par poste.

**URL de base :** `https://buildcalculator.io/api/v1`

### Points de terminaison API

#### `GET/POST /api/v1/search` - Rechercher des postes de construction

| Paramètre | Type | Défaut | Requis | Description |
|-----------|------|--------|--------|-------------|
| `q` | string | - | Oui | Requête de recherche (min. 2 caractères). Fonctionne dans toutes les langues |
| `lang` | string | `en` | Non | Langue de la base : `en`, `ru`, `de`, `fr`, `es`, `pt`, `zh`, `ar`, `hi` |
| `top` | integer | 5 | Non | Nombre de résultats (1–20) |

#### `GET /api/v1/languages` - Langues supportées

Retourne toutes les langues disponibles avec le nombre de postes.

#### `GET /api/v1/stats` - Statistiques de la base de données

Retourne le nombre de postes, catégories, langues et métadonnées.

### Exemples de code API

**cURL :**
```bash
curl "https://buildcalculator.io/api/v1/search?q=fondation+béton&lang=fr&top=5"
```

**Python :**
```python
import requests

response = requests.get("https://buildcalculator.io/api/v1/search",
    params={"q": "maçonnerie murs extérieurs", "lang": "fr", "top": 5})
data = response.json()

for item in data["results"]:
    print(f"{item['name']} - {item['pricing']['total_per_unit']} EUR/{item['unit']}")
```

**JavaScript :**
```javascript
const res = await fetch(
  "https://buildcalculator.io/api/v1/search?q=couverture+toiture&lang=fr&top=3"
);
const data = await res.json();
```

**Exemple de réponse :**
```json
{
  "query": "concrete foundation",
  "language": "en",
  "results_count": 5,
  "results": [
    {
      "rate_code": "KANE_KAME_KAKAME_KAMECON",
      "name": "Concrete preparation device",
      "unit": "m3",
      "currency": "EUR",
      "pricing": {
        "total_per_unit": 167.51,
        "labor_per_unit": 18.80,
        "material_per_unit": 142.92,
        "equipment_per_unit": 4.80
      },
      "cost_breakdown": {
        "labor_pct": 11.3,
        "material_pct": 85.8,
        "equipment_pct": 2.9
      }
    }
  ]
}
```

**Codes d'erreur :**

| Code | Signification | Action |
|------|--------------|--------|
| 400 | Requête manquante ou invalide | Vérifier le paramètre `q` (min. 2 caractères) |
| 429 | Limite de requêtes dépassée | Attendre et réessayer (60 req/min) |
| 500 | Erreur serveur | Réessayer ou contacter le support |

> 📖 Documentation complète : [buildcalculator.io/api-docs](https://buildcalculator.io/api-docs/)

---

## Démarrage Rapide

### Python - Données Tabulaires

```python
import pandas as pd

# Parquet (recommandé)
df = pd.read_parquet("DDC_CWICR_FR.parquet")

# Excel
df = pd.read_excel("DDC_CWICR_FR.xlsx")

print(f"Enregistrements: {len(df):,} | Champs: {len(df.columns)}")
print(df[['rate_code', 'rate_original_name', 'rate_unit', 'total_cost_per_position']].head())
```

### Python - Recherche Sémantique

```python
from qdrant_client import QdrantClient
from openai import OpenAI

client = QdrantClient("localhost", port=6333)
openai = OpenAI()

# Recherche en langage naturel
query = "coulage de fondation en béton armé"
embedding = openai.embeddings.create(
    input=query,
    model="text-embedding-3-large"
).data[0].embedding

results = client.search(
    collection_name="ddc_fr_paris",
    query_vector=embedding,
    limit=5
)

for r in results:
    print(f"[{r.score:.3f}] {r.payload['rate_code']}: {r.payload['rate_original_name']}")
```

### Recherche Filtrée

```python
from qdrant_client.models import Filter, FieldCondition, MatchValue, Range

# Par département
results = client.search(
    collection_name="ddc_fr_paris",
    query_vector=embedding,
    query_filter=Filter(must=[
        FieldCondition(key="department_name", match=MatchValue(value="Béton et Béton Armé"))
    ]),
    limit=10
)

# Par fourchette de prix
results = client.search(
    collection_name="ddc_fr_paris",
    query_vector=embedding,
    query_filter=Filter(must=[
        FieldCondition(key="price_est_median", range=Range(gte=1000, lte=50000))
    ]),
    limit=10
)
```


---

## 💻 Exemples pour Développeurs

Le répertoire [`examples/`](./examples/) contient du **code prêt à exécuter** en plusieurs langages.

| # | Example | Language | Level |
|---|---------|----------|-------|
| 01 | Load and explore data | Python, JS, Rust, R | Beginner |
| 02 | Semantic search with Qdrant | Python, JS, Rust | Beginner |
| 03 | Cost estimation from text | Python, JS | Intermediate |
| 04 | Cost estimation from photos | Python | Intermediate |
| 05 | BOQ generation & Excel export | Python, JS | Intermediate |
| 06 | RAG pipeline (Claude + Qdrant) | Python | Advanced |
| 07 | Multi-language cost comparison | Python | Intermediate |
| 08 | Data analysis & visualization | Python, R | Intermediate |
| 09 | Filtered & faceted search | Python | Intermediate |
| 10 | Embedding generation pipeline | Python | Advanced |

**→ [Parcourir tous les exemples](./examples/)**

---

## Ressources & Communauté

[![Site Web](https://img.shields.io/badge/🌐_Site_Web-datadrivenconstruction.io-2563eb?style=for-the-badge)](https://datadrivenconstruction.io)
[![Démo](https://img.shields.io/badge/🎯_Démo-openconstructionestimate.com-059669?style=for-the-badge)](https://openconstructionestimate.com)
[![GitHub](https://img.shields.io/badge/💻_GitHub-datadrivenconstruction-181717?style=for-the-badge&logo=github)](https://github.com/datadrivenconstruction)
[![YouTube](https://img.shields.io/badge/📺_YouTube-@datadrivenconstruction-FF0000?style=for-the-badge&logo=youtube)](https://youtube.com/@datadrivenconstruction)
[![LinkedIn](https://img.shields.io/badge/💼_LinkedIn-datadrivenconstruction-0A66C2?style=for-the-badge&logo=linkedin)](https://linkedin.com/company/datadrivenconstruction)
[![Telegram](https://img.shields.io/badge/💬_Telegram-datadrivenconstruction-26A5E4?style=for-the-badge&logo=telegram)](https://t.me/datadrivenconstruction)

### Conseil & Formation

Nous travaillons avec des entreprises leaders de construction, d'ingénierie, des agences de conseil et des entreprises technologiques du monde entier pour les aider à implémenter les principes de données ouvertes, automatiser le traitement CAD/BIM et construire des pipelines ETL robustes. Nous soutenons activement les organisations recherchant des solutions pratiques pour la transformation digitale et l'interopérabilité, en nous concentrant sur les défis de qualité des données et de classification tout en favorisant l'adoption de workflows ouverts et automatisés.

Si vous souhaitez tester cette solution avec vos propres données ou si vous êtes intéressé par l'adaptation du workflow à des tâches de projet réelles, n'hésitez pas à nous contacter. Notre équipe organise des ateliers pratiques, fournit du conseil stratégique et développe des prototypes adaptés aux processus de projet réels.

<a href="mailto:info@datadrivenconstruction.io">
  <img src="https://img.shields.io/badge/📧_Contactez_Nous-info@datadrivenconstruction.io-2563eb?style=for-the-badge" alt="Contact">
</a>

### Contribuer

DDC CWICR est un projet gratuit et open source dédié à rendre l'industrie de la construction plus efficace, transparente et technologiquement avancée. Nous recherchons activement des enthousiastes partageant cette mission. Si vous créez des solutions utiles et êtes prêt à les partager avec la communauté, nous sommes là pour vous aider à être entendu.

Nous vous invitons à soumettre vos workflows open source, pipelines et intégrations basés sur DDC CWICR - des outils que tout le monde peut utiliser librement dans son travail. Les meilleures solutions seront publiées avec attribution complète de l'auteur sur GitHub et annoncées via notre newsletter et nos réseaux sociaux, atteignant des dizaines de milliers d'abonnés professionnels. Cela place votre nom directement devant une communauté internationale de métreurs, spécialistes BIM et chefs de projet.

Ensemble, nous changeons l'industrie. Vous pouvez envoyer votre solution à info@datadrivenconstruction.io avec le sujet "DDC Open Workflow" ou soumettre une Pull Request directement sur nos repositories GitHub.

Automatisez le traitement des données de construction avec des workflows n8n CAD-BIM prêts à l'emploi:

<a href="https://github.com/datadrivenconstruction/cad2data-Revit-IFC-DWG-DGN-pipeline-with-conversion-validation-qto">
  <img src="https://img.shields.io/badge/Pipeline_cad2data-GitHub-181717?style=for-the-badge&logo=github" alt="Pipeline cad2data">
</a>

---

## 🤖 Instructions IA

Le dossier `AI_INSTRUCTIONS/` contient une documentation complète pour les assistants de programmation IA afin de travailler efficacement avec cette base de données de coûts de construction.

### Qu'est-ce que DDC CWICR?

**DDC CWICR** (Construction Work Items, Components & Resources) est une base de données open-source de coûts de construction contenant:
- **55 719 postes de travaux** - opérations de construction détaillées avec ventilation complète des coûts
- **27 672 ressources** - matériaux, main d'œuvre et équipements avec prix régionaux
- **85 champs de données** - schéma structuré pour des calculs précis
- **11 langues** - avec prix régionaux (EUR, USD, CAD, RUB, CNY, etc.)
- **Embeddings pré-calculés** - vecteurs OpenAI 3072 dimensions pour recherche sémantique

### Méthodologie Basée sur les Ressources

La base de données utilise une **approche de calcul basée sur les ressources** qui sépare:
- **Normes technologiques** (invariables) - heures de travail, quantités de matériaux, temps d'équipement
- **Prix régionaux** (variables) - taux horaires, coûts des matériaux, prix du carburant

```
Coût Réel = Norme Technologique × Prix Régional
```

Cela permet une estimation précise pour différentes régions et périodes.

### Fichiers d'Instructions IA

| Fichier | Objectif |
|---------|----------|
| `INSTRUCTIONS.md` | Aperçu principal, démarrage rapide, formats |
| `CLAUDE.md` | Patterns et exemples pour Claude Code |
| `OPENCODE.md` | Instructions concises pour Opencode |
| `ANTIGRAVITY.md` | Intégration GCP (BigQuery, Vertex AI, Qdrant) |
| `DATABASE_SCHEMA.md` | Schéma complet de 85 champs |

### Workflows n8n - Exemples & Templates

Les workflows n8n inclus sont des **exemples et templates** démontrant la logique d'estimation des coûts. Ils peuvent être:
- ✅ Utilisés tels quels pour un déploiement rapide
- ✅ Partiellement adaptés aux exigences métier spécifiques
- ✅ Étudiés pour comprendre la méthodologie de calcul
- ✅ Utilisés comme référence pour créer des intégrations sur n'importe quelle plateforme

Les workflows démontrent: requêtes de base de données, correspondance des postes, logique de tarification régionale et génération de rapports. L'IA peut les analyser pour comprendre le processus complet d'estimation.

### Pourquoi C'est Important

Les assistants IA peuvent vous aider à:
- Interroger la base de données en langage naturel
- Trouver des travaux par recherche sémantique
- Calculer les coûts avec les prix régionaux
- Générer des rapports et exporter des données
- Créer des intégrations avec les services cloud
- Comprendre la méthodologie de calcul à partir des exemples de workflows

### Démarrage Rapide avec l'IA

1. Ouvrez le projet dans votre IDE compatible IA
2. Demandez: *"Montre-moi tous les travaux de béton avec leurs coûts"*
3. L'IA utilisera les instructions pour interroger correctement les données

**Livre**: Pour les détails méthodologiques, voir [Livre Data-Driven Construction](https://datadrivenconstruction.io/book)

---

## Licence - CC BY-NC 4.0

L'ensemble du dépôt est sous licence [**Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)**](https://creativecommons.org/licenses/by-nc/4.0/).

### Ce que vous POUVEZ faire

| | |
|---|---|
| **Utilisation commerciale** | Créez des produits, SaaS, applications, APIs - gratuitement, sans demander la permission |
| **Copier et distribuer** | Partagez les données dans n'importe quel format |
| **Modifier et adapter** | Transformez, complétez, créez des œuvres dérivées |
| **Utiliser pour l'IA/ML** | Entraînement de modèles, pipelines RAG, embeddings |
| **Utiliser pour la recherche** | Articles scientifiques, rapports, analyses |

### Ce que vous DEVEZ faire

| | |
|---|---|
| **Mentionner l'attribution** | Vous **devez** indiquer la source à chaque utilisation - voir les exemples ci-dessous |
| **Indiquer les modifications** | Si vous avez modifié les données, vous **devez** indiquer ce qui a été changé |
| **Conserver la licence** | Incluez un lien vers CC BY-NC 4.0 lors de la distribution |

### Attribution - format obligatoire

Chaque projet, produit, publication ou application utilisant les données DDC CWICR **doit** inclure :

```
DDC CWICR by Artem Boiko / DataDrivenConstruction
https://github.com/datadrivenconstruction/OpenConstructionEstimate-DDC-CWICR
Licensed under CC BY-NC 4.0
```

**Exemples d'attribution :**

| Où | Comment |
|-----|-----|
| **README / documentation** | `Source des données : DDC CWICR by Artem Boiko / DataDrivenConstruction (CC BY-NC 4.0)` |
| **Application web (pied de page ou "À propos")** | `Données de coûts de construction © Artem Boiko / DataDrivenConstruction - CC BY-NC 4.0` |
| **Article scientifique** | `Boiko, A. (2025). DDC CWICR - Construction Work Items, Costs & Resources. DataDrivenConstruction.` |
| **Application mobile / bureau** | Écran "À propos" : `Données : DDC CWICR by DataDrivenConstruction (CC BY-NC 4.0)` |
| **API / SaaS** | Documentation API : `Fourni par DDC CWICR (CC BY-NC 4.0) - datadrivenconstruction.io` |

## Soutenir le Projet

Si vous trouvez cela utile, merci de considérer nous soutenir:

[![GitHub Sponsors](https://img.shields.io/badge/Sponsoriser_sur-GitHub-ea4aaa?style=for-the-badge&logo=github)](https://github.com/sponsors/datadrivenconstruction)
[![Buy Me A Coffee](https://img.shields.io/badge/Buy_Me_A_Coffee-ffdd00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black)](https://buymeacoffee.com/boikoartem)


<p align="left">
  <br/>
  <b>Libérez la Puissance des Données dans la Construction</b><br/>
  <sub>Passez à une gestion complète des données où seules les données et processus structurés unifiés demeurent</sub>
</p>

<p align="left">
  <a href="https://datadrivenconstruction.io">
    <img src="https://datadrivenconstruction.io/wp-content/uploads/2023/07/DataDrivenConstruction-1-1.png.webp" alt="DataDrivenConstruction" width="180">
  </a>
</p>

<p align="left">
  <sub>© 2025 Artem Boiko · <a href="https://datadrivenconstruction.io">datadrivenconstruction.io</a></sub>
</p>

---

## Marques Déposées

Autodesk®, Revit®, AutoCAD® et DWG™ sont des marques déposées ou des marques commerciales d'Autodesk, Inc. OpenAI™ est une marque commerciale d'OpenAI, Inc. Qdrant est une marque commerciale de Qdrant Solutions GmbH. Tous les autres noms de marques, noms de produits ou marques commerciales appartiennent à leurs propriétaires respectifs.

Ce projet n'est pas affilié, approuvé ou sponsorisé par Autodesk, OpenAI, Qdrant ou tout autre détenteur de marques commerciales mentionné ci-dessus.
