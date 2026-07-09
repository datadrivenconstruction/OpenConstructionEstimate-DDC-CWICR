<div dir="rtl">

<h3 align="center">DDC CWICR - بنود العمل والمكونات والموارد الإنشائية </br>
  + خطوط أنابيب n8n لحساب التقديرات بناءً على الأوصاف والصور وCAD (BIM)</h3>

<p align="center">
  <a href="README.md">🇬🇧 English</a> •
  <a href="README.zh-CN.md">🇨🇳 中文</a> •
  <a href="README.es.md">🇪🇸 Español</a> •
  <a href="README.pt-BR.md">🇧🇷 Português</a> •
  <a href="README.ru.md">🇷🇺 Русский</a> •
  <a href="README.ja.md">🇯🇵 日本語</a> •
  <a href="README.de.md">🇩🇪 Deutsch</a> •
  <a href="README.fr.md">🇫🇷 Français</a> •
  <a href="README.ar.md"><b>🇸🇦 العربية</b></a>
</p>

<p align="center">
  <img src="https://github.com/datadrivenconstruction/cad2data-Revit-IFC-DWG-DGN-pipeline-with-conversion-validation-qto/blob/main/DDC_in_additon/DDC_readme_content/OpenConstructionEstimate.jpg" alt="OpenConstructionEstimate" width="1000">
</p>

<div align="center">
  <img src="https://img.shields.io/badge/بنود_العمل-55,719-2563eb?style=for-the-badge" alt="بنود العمل">
  <img src="https://img.shields.io/badge/الموارد-27,672-059669?style=for-the-badge" alt="الموارد">
  <img src="https://img.shields.io/badge/اللغات-11-d97706?style=for-the-badge" alt="اللغات">
  <img src="https://img.shields.io/badge/الدول-12+-dc2626?style=for-the-badge" alt="الدول">
</div>

<div align="center">
  <img src="https://img.shields.io/badge/الترخيص-CC_BY--NC_4.0-green?style=flat-square" alt="الترخيص">
  <img src="https://img.shields.io/badge/الإصدار-v0.1.1-blue?style=flat-square" alt="الإصدار">
  <img src="https://img.shields.io/badge/التضمينات-OpenAI_3072d-412991?style=flat-square" alt="التضمينات">
  <img src="https://img.shields.io/badge/قاعدة_البيانات_المتجهة-Qdrant-dc382d?style=flat-square" alt="Qdrant">
  <img src="https://img.shields.io/badge/الأتمتة-n8n-ea4b71?style=flat-square" alt="n8n">
</div>

<p align="center">
  <img src="https://github.com/datadrivenconstruction/cad2data-Revit-IFC-DWG-DGN-pipeline-with-conversion-validation-qto/blob/main/DDC_in_additon/DDC_readme_content/OpenConstructionEstimate_bottom.jpg" alt="OpenConstructionEstimate" width="1000">
</p>

<h3 align="center">⚡ سير عمل n8n</h3>
<p align="center"><code>اختر مدخلاتك → احصل على تقدير التكلفة</code></p>

<br>

<table width="100%">
<tr>

<td align="center" valign="top" width="33%">
<br>
<h3>📝 نص</h3>
<p>تحويل سريع من النطاق<br>إلى تقدير من وصف قصير</p>
<p><b>المدخل:</b> رسالة Telegram / دردشة<br>
<b>المخرج:</b> بنود عمل مطابقة + تقدير</p>
<br>
<a href="#1️⃣-روبوت-تقدير-النص">📖 التوثيق</a>
<br><br>
<a href="./n8n_1_Telegram_Bot_Cost_Estimates_and_Rate_Finder_TEXT_DDC_CWICR.json">
<img src="https://img.shields.io/badge/تحميل_سير_العمل-0A84FF?style=for-the-badge&logo=download&logoColor=white" alt="تحميل"/>
</a>
<br><br>
</td>

<td align="center" valign="top" width="33%">
<br>
<h3>📷 صورة / PDF</h3>
<p>صور الموقع، جداول الكميات الممسوحة،<br>صور-PDF من الميدان</p>
<p><b>المدخل:</b> صورة أو صفحات PDF<br>
<b>المخرج:</b> نطاق مستخرج → تقدير</p>
<br>
<a href="#2️⃣-مقدر-التكلفة-بالصور">📖 توثيق الصور</a> · <a href="#3️⃣-الروبوت-العالمي-نص--صورة--pdf">📖 الروبوت العالمي</a>
<br><br>
<a href="./n8n_2_Photo_Cost_Estimate_DDC_CWICR.json">
<img src="https://img.shields.io/badge/سير_عمل_الصور-0A84FF?style=for-the-badge&logo=download&logoColor=white" alt="صورة"/>
</a>
&nbsp;
<a href="./n8n_3_Telegram_Bot_Cost_Estimates_and_Rate_Finder_TEXT_PHOTO_PDF_DDC_CWICR.json">
<img src="https://img.shields.io/badge/روبوت_Telegram-0A84FF?style=for-the-badge&logo=telegram&logoColor=white" alt="روبوت"/>
</a>
<br><br>
</td>

<td align="center" valign="top" width="33%">
<br>
<h3>🧊 CAD / BIM</h3>
<p>الكميات والتقدير<br>بناءً على Revit / IFC / DWG</p>
<p><b>المدخل:</b> تصدير النموذج <br>
<b>المخرج:</b> تقدير 4D/5D + تفصيل</p>
<br>
<a href="#4️⃣-خط-أنابيب-تقدير-cad-bim">📖 التوثيق</a>
<br><br>
<a href="./n8n_4_CAD_(BIM)_Cost_Estimation_Pipeline_4D_5D_with_DDC_CWICR.json">
<img src="https://img.shields.io/badge/تحميل_سير_العمل-0A84FF?style=for-the-badge&logo=download&logoColor=white" alt="تحميل"/>
</a>
<br><br>
</td>

</tr>
</table>

<br>
<p align="center">
  <a href="https://openconstructionestimate.com">
    <img src="https://img.shields.io/badge/🌐_عرض_مباشر_(قاعدة_البيانات_فقط)-openconstructionestimate.com-2563eb?style=for-the-badge" alt="عرض مباشر">
  </a>
</p>
<br>
<p align="center">
 عملاء ومستخدمو DataDrivenConstruction
  <br>
  <a href="https://datadrivenconstruction.io/">
  <img src="https://github.com/datadrivenconstruction/cad2data-Revit-IFC-DWG-DGN-pipeline-with-conversion-validation-qto/blob/main/DDC_in_additon/DDC_readme_content/Clients_DataDrivenConstruction_logos.png" width="95%"/>
  </a>
  <br></br>
</p>


---

## 📑 جدول المحتويات

### 🤖 تكامل الذكاء الاصطناعي
- [الوقود المثالي للذكاء الاصطناعي](#-الوقود-المثالي-لمنتجاتك-الذكية) - لماذا هذه القاعدة مثالية للذكاء الاصطناعي
- [Claude Code و Google Antigravity](#-claude-code--google-antigravity--مساعدو-البرمجة-بالذكاء-الاصطناعي) - مساعدو البرمجة
- [n8n](#-n8n--أتمتة-سير-العمل-المرئي) - أتمتة سير العمل
- [حالات الاستخدام العالمية](#-حالات-الاستخدام-العالمية) - ما يمكنك بناؤه
- [أمثلة للمطورين](#-أمثلة-للمطورين) - كود جاهز للتشغيل

### 📊 قاعدة البيانات والبيانات
- [حول](#حول) - ما هو DDC CWICR
- [الصيغ المتاحة](#الصيغ-المتاحة) - Excel، Parquet، CSV، Qdrant
- [مخطط البيانات](#مخطط-البيانات) - هيكل 85 حقلاً
- [مجموعات الحقول](#مجموعات-الحقول) - التصنيف، الموارد، العمالة، الآلات
- [المنهجية](#المنهجية) - مبادئ حساب التكلفة القائم على الموارد
- [السياق التاريخي](#السياق-التاريخي) - 100+ سنة من المعايير

### ⚡ سير عمل n8n
- [نظرة عامة على سير عمل n8n](#-سير-عمل-n8n) - اختر نوع المدخل
- [جرب الآن - روبوتات العرض المباشر](#-جرب-الآن--روبوتات-العرض-المباشر) - اختبر فوراً على Telegram
- [سير العمل 1: روبوت تقدير النص](#1️⃣-روبوت-تقدير-النص) - روبوت Telegram للإدخال النصي
- [سير العمل 2: مقدر التكلفة بالصور](#2️⃣-مقدر-التكلفة-بالصور) - نموذج ويب مع AI Vision
- [سير العمل 3: الروبوت العالمي](#3️⃣-الروبوت-العالمي-نص--صورة--pdf) - نص + صورة + PDF
- [سير العمل 4: خط أنابيب CAD/BIM](#4️⃣-خط-أنابيب-تقدير-cad-bim) - Revit/IFC/DWG إلى تقدير
- [البداية السريعة لسير العمل](#البداية-السريعة-لسير-العمل) - الإعداد في 4 خطوات
- [إعداد n8n 2.0+](#️-إعداد-n8n-20-المطلوب) - تفعيل عقدة Execute Command

### 🏗️ خط أنابيب CAD/BIM
- [المتطلبات الأساسية](#-المتطلبات-الأساسية) - المكونات المطلوبة
- [مراحل خط الأنابيب](#-مراحل-خط-الأنابيب) - معالجة من 10 مراحل
- [اختيار نموذج LLM](#️-اختيار-نموذج-llm) - OpenAI، Claude، Gemini، Grok
- [ملفات الإخراج](#-ملفات-الإخراج) - تقارير HTML و Excel
- [استكشاف الأخطاء وإصلاحها](#️-استكشاف-الأخطاء-وإصلاحها) - المشاكل الشائعة

### 🔍 قاعدة البيانات المتجهة
- [قاعدة البيانات المتجهة](#قاعدة-البيانات-المتجهة) - البحث الدلالي مع Qdrant
- [لقطات Qdrant](#لقطات-قاعدة-بيانات-qdrant-المتجهة) - تحميل اللقطات
- [المجموعات](#المجموعات) - 11 مجموعة لغوية
- [نشر Docker](#نشر-docker) - إعداد مستضاف ذاتياً

### 🌐 API
- [Pricing Search API](#-pricing-search-api--buildcalculatorio) - واجهة REST API مجانية لأسعار البناء
- [نقاط نهاية API](#نقاط-نهاية-api) - البحث، اللغات، الإحصائيات
- [أمثلة الكود](#أمثلة-الكود-api) - cURL، Python، JavaScript

### 🚀 البدء
- [البداية السريعة - Python](#البداية-السريعة) - البيانات الجدولية والبحث الدلالي
- [حالات استخدام التكامل](#التكامل) - من المستوى المبتدئ إلى المتقدم

### 👥 المجتمع
- [الموارد والمجتمع](#الموارد-والمجتمع) - الروابط والقنوات
- [الاستشارات والتدريب](#الاستشارات-والتدريب) - الخدمات المهنية
- [المساهمة](#المساهمة) - قدم سير عملك
- [الترخيص](#الترخيص) - CC BY-NC 4.0
- [دعم المشروع](#دعم-المشروع) - الرعاية والتبرع
- [🤖 تعليمات الذكاء الاصطناعي](#تعليمات-الذكاء-الاصطناعي) - توثيق لمساعدي الذكاء الاصطناعي


---

## 🚀 الوقود المثالي لمنتجاتك الذكية

<p align="center">
  <b>فقط استنسخ المستودع وصف ما تريد - الذكاء الاصطناعي يقوم بالباقي</b>
</p>

DDC CWICR ليست مجرد قاعدة بيانات - إنها **وقود جاهز للاستخدام للتطبيقات المدعومة بالذكاء الاصطناعي**. سواء كنت تبني روبوتات تقدير التكلفة، أو تؤتمت سير عمل البناء، أو تنشئ مساعدين أذكياء - هذه البيانات تعمل فوراً مع أدوات الذكاء الاصطناعي الحديثة.

### لماذا هذه القاعدة مثالية للذكاء الاصطناعي

| الميزة | الفائدة |
|--------|---------|
| **تضمينات محسوبة مسبقاً** | لا حاجة لتوليد المتجهات - البحث الدلالي يعمل فوراً |
| **مخطط منظم من 85 حقلاً** | الذكاء الاصطناعي يمكنه التفكير في علاقات البيانات وتقديم إجابات دقيقة |
| **11 لغة مضمنة** | بناء تطبيقات متعددة اللغات بدون عبء الترجمة |
| **55,000+ بند عمل** | تغطية شاملة لأي مهمة تقدير بناء |
| **منهجية قائمة على الموارد** | بيانات شفافة يمكن للذكاء الاصطناعي شرحها وتفصيلها |

### 📋 أوصاف عمل جاهزة لأي نظام

<p align="center">
  <img src="https://github.com/datadrivenconstruction/cad2data-Revit-IFC-DWG-DGN-pipeline-with-conversion-validation-qto/blob/main/DDC_in_additon/DDC_readme_content/A%20ready-made%20job%20description%20generator.jpg" alt="مولد أوصاف العمل الجاهزة" width="1000">
</p>

<div dir="rtl">

توفر DDC CWICR **أوصاف عمل كاملة ومنظمة** يمكن عرضها في أي نظام أو تنسيق. كل بند عمل يحتوي على جميع المعلومات التي يحتاجها مختلف أصحاب المصلحة:

| صاحب المصلحة | ما يحصل عليه |
|--------------|--------------|
| 🏢 **العميل / المستثمر** | شفافية كاملة للتكاليف، تفصيل الموارد، تبرير الأسعار لقرارات الاستثمار |
| 📊 **مهندس التسعير** | أسعار تفصيلية، ساعات العمل، كميات المواد، تكاليف المعدات - جاهز لإنشاء جداول الكميات |
| 👷 **مدير الموقع / المشرف** | تكوين العمل، متطلبات الموارد، معايير العمل للتخطيط والتنفيذ اليومي |
| 🔧 **المقاول / المنفذ** | مواصفات كاملة، أسعار الوحدات، معايير الإنتاجية للعطاءات والجدولة الدقيقة |

التصدير إلى **Excel، PDF، HTML، أنظمة ERP، منصات BIM** - المخطط المنظم من 85 حقلاً يضمن سلامة البيانات في جميع تنسيقات الإخراج.

</div>

### 🛠️ يعمل بشكل مثالي مع

<table>
<tr>
<td align="center" width="20%">
<img src="https://img.shields.io/badge/Claude_Code-000000?style=for-the-badge&logo=anthropic&logoColor=white" alt="Claude Code"/><br/>
<b>Claude Code</b><br/>
<sub>مساعد برمجة AI CLI</sub>
</td>
<td align="center" width="20%">
<img src="https://img.shields.io/badge/Google_Antigravity-4285F4?style=for-the-badge&logo=google&logoColor=white" alt="Google Antigravity"/><br/>
<b>Google Antigravity</b><br/>
<sub>Google Antigravity</sub>
</td>
<td align="center" width="20%">
<img src="https://img.shields.io/badge/n8n-EA4B71?style=for-the-badge&logo=n8n&logoColor=white" alt="n8n"/><br/>
<b>n8n</b><br/>
<sub>أتمتة سير العمل</sub>
</td>
<td align="center" width="20%">
<img src="https://img.shields.io/badge/Dify-1677FF?style=for-the-badge&logo=openai&logoColor=white" alt="Dify"/><br/>
<b>Dify</b><br/>
<sub>تطوير تطبيقات LLM</sub>
</td>
<td align="center" width="20%">
<img src="https://img.shields.io/badge/Sim_AI-6366F1?style=for-the-badge&logo=simpleicons&logoColor=white" alt="Sim AI"/><br/>
<b>Sim AI وغيرها</b><br/>
<sub>منصات الذكاء الاصطناعي</sub>
</td>
</tr>
</table>

---

## 🎯 DDC Skills

<div dir="rtl">

**[مهارات DDC لوكلاء الذكاء الاصطناعي في البناء](https://github.com/datadrivenconstruction/DDC_Skills_for_AI_Agents_in_Construction)** - 196 مهارة أتمتة مع تكامل مباشر في قاعدة بيانات CWICR. استنسخ، افتح بمساعد الترميز بالذكاء الاصطناعي، صف ما تحتاجه.

</div>

<p align="center">
  <a href="https://github.com/datadrivenconstruction/DDC_Skills_for_AI_Agents_in_Construction">
    <img src="https://img.shields.io/badge/DDC_Skills-196_AI_Automations-blue?style=for-the-badge&logo=robot" alt="DDC Skills">
  </a>
</p>

---

### 💻 Claude Code و Google Antigravity - مساعدو البرمجة بالذكاء الاصطناعي

أسرع طريقة للعمل مع DDC CWICR. فقط افتح المستودع في Claude Code أو Google Antigravity واطرح أسئلة بلغة طبيعية.

**البدء:**

</div>

```bash
# استنساخ المستودع
git clone https://github.com/datadrivenconstruction/OpenConstructionEstimate-DDC-CWICR.git

# فتح مع Claude Code
cd OpenConstructionEstimate-DDC-CWICR
claude
```

<div dir="rtl">

**أمثلة على الأوامر:**

| المهمة | الأمر |
|--------|-------|
| **استكشاف البيانات** | "أظهر لي هيكل قاعدة بيانات البناء هذه واشرح البيانات المتاحة" |
| **البحث عن بنود العمل** | "ابحث عن جميع بنود العمل المتعلقة بأساسات الخرسانة وأظهر تكاليفها" |
| **بناء الاستعلامات** | "اكتب سكريبت Python للبحث عن أعمال السباكة مع ساعات عمل > 100" |
| **إنشاء التقارير** | "أنشئ تقرير تفصيل التكاليف لأعمال تجديد المساكن" |
| **تحليل التكاليف** | "قارن تكاليف المواد بين طرق بناء الجدران المختلفة" |
| **بناء التكاملات** | "أنشئ سكريبت يتصل بقاعدة بيانات Qdrant ويجري بحثاً دلالياً" |

**نصائح احترافية:**
- وجه Claude إلى ملفات محددة: *"حلل ملف Parquet ولخص توزيع التكاليف"*
- اطلب توضيحات: *"اشرح كيف تعمل منهجية حساب التكلفة القائمة على الموارد في هذه القاعدة"*
- اطلب تعديلات: *"عدل سير عمل n8n لإضافة إشعارات البريد الإلكتروني"*

---

### ⚡ n8n - أتمتة سير العمل المرئي

بناء خطوط أتمتة قوية بدون كتابة كود. ربط DDC CWICR بأكثر من 400 تطبيق وخدمة.

**حالات الاستخدام:**

| سير العمل | الوصف |
|-----------|-------|
| **روبوت Telegram** | المستخدمون يرسلون نص/صورة → الذكاء الاصطناعي يستخرج بنود العمل → يعيد تقدير التكلفة |
| **أتمتة البريد الإلكتروني** | استلام جدول كميات عبر البريد → معالجة بالذكاء الاصطناعي → إرسال تقدير منسق |
| **تكامل CRM** | مشروع جديد في CRM → توليد تقدير أولي تلقائياً → تحديث قيمة الصفقة |
| **خط أنابيب BIM** | تصدير من Revit → استخراج الكميات → مطابقة مع أسعار DDC → توليد تقرير 5D |
| **روبوت Slack** | الفريق يطرح أسئلة → الذكاء الاصطناعي يبحث في القاعدة → يعيد بنود العمل ذات الصلة |

**البداية السريعة:**
1. تحميل JSON لسير العمل من هذا المستودع
2. الاستيراد في n8n: `Workflows → Import → From File`
3. تكوين بيانات الاعتماد (OpenAI، Qdrant، Telegram)
4. التفعيل والاختبار

راجع قسم [سير عمل n8n](#سير-عمل-n8n--الوصف-التفصيلي) للإعداد التفصيلي.

---

### 📋 حالات الاستخدام العالمية

بغض النظر عن أداة الذكاء الاصطناعي التي تختارها، DDC CWICR يمكّن:

| حالة الاستخدام | الوصف |
|----------------|-------|
| **تقدير التكلفة الفوري** | احصل على تكاليف البناء من أوصاف نصية أو صور |
| **توليد جداول الكميات** | توليد جداول الكميات تلقائياً من أوصاف المشروع |
| **معايرة الأسعار** | مقارنة التكاليف عبر المناطق واللغات |
| **تخطيط الموارد** | حساب ساعات العمل والمواد واحتياجات المعدات |
| **تحليل الاستثمار** | تدقيق تكاليف عميق مع شفافية كاملة للموارد |
| **دعم متعدد اللغات** | خدمة المستخدمين بـ 11 لغة مع تسعير محلي |
| **تكامل BIM** | الاتصال بـ Revit/IFC للتقدير الآلي 4D/5D |
| **تدريب نماذج الذكاء الاصطناعي** | استخدام بيانات منظمة لضبط ذكاء البناء |

---

## حول

**DDC CWICR** (Construction Work Items, Components & Resources) هي قاعدة بيانات مفتوحة لتقدير تكاليف البناء، تغطي الطيف الكامل لأنشطة البناء - من أعمال الحفر وصب الخرسانة إلى أعمال التركيب المتخصصة.

تستند القاعدة إلى مصادر تصف ممارسات البناء الحديثة في أوراسيا ومنطقة آسيا والمحيط الهادئ، حيث يعمل نظام توحيد تقني موحد كلغة هندسية مشتركة لأكثر من عشر اقتصادات نامية ديناميكية. يمثل DDC CWICR جهداً لتنسيق المعايير المفتوحة من خلال إنشاء إطار تنظيمي واحد لإدارة المشاريع الرأسمالية بعدة لغات.

<p align="center">
  <br>
  <img src="https://github.com/datadrivenconstruction/cad2data-Revit-IFC-DWG-DGN-pipeline-with-conversion-validation-qto/blob/main/DDC_in_additon/DDC_readme_content/DDC%20CWICR%20GEOGRAPHIC%20COVERAGE.jpg" width="100%"/>
  <br></br>
</p>

يمكن الوصول إلى البيانات المنظمة عبر صيغ جدولية (XLSX، CSV، Parquet) أو الاستعلام عنها محادثياً عبر LLM، مما يتيح للمتخصصين دمج أوصاف أعمال البناء (قاعدة بيانات QDRANT المتجهة) في خطوط الأنابيب الآلية وسير العمل باستخدام لغة بسيطة أو استعلامات موجزة.

### الصيغ المتاحة

| الصيغة | الامتداد | الحجم | الأفضل لـ | الميزات |
|-------|----------|-------|-----------|---------|
| **Excel** | `.xlsx` | ~150-400 ميجابايت | التحليل اليدوي، التصفية، الجداول المحورية | قابل للقراءة البشرية، تنسيق كامل |
| **Parquet** | `.parquet` | ~55 ميجابايت | خطوط أنابيب ETL، تدريب ML، البيانات الضخمة | عمودي، ضغط ممتاز |
| **CSV** | `.csv` | ~1.3 جيجابايت | استيراد قاعدة البيانات، الأنظمة القديمة | توافق عالمي |
| **Qdrant** | `.snapshot` | ~1 جيجابايت | البحث الدلالي، RAG، مساعدي الذكاء الاصطناعي | تضمينات OpenAI محسوبة مسبقاً |


عرض مباشر متاح على [openconstructionestimate.com](https://openconstructionestimate.com/)، حيث يمكنك استكشاف البيانات ورؤية قاعدة البيانات المتجهة في العمل للبحث الدلالي.

<p align="center">
  <img src="https://github.com/datadrivenconstruction/cad2data-Revit-IFC-DWG-DGN-pipeline-with-conversion-validation-qto/blob/main/DDC_in_additon/DDC_readme_content/DDC%20CWICR%20Resource-based%20Work%20Cost%20Norms.jpg" alt="OpenConstructionEstimate" width="1000">
</p>

---

## مخطط البيانات

تحتوي القاعدة على **85 حقلاً** منظمة في مجموعات منطقية. كل سجل يمثل إما بند عمل (سعر) أو مورد مع تفصيل كامل للتكلفة.

### مجموعات الحقول

حقول الـ 85 في القاعدة منظمة في مجموعات منطقية تعكس منهجية تقدير التكلفة القائمة على الموارد. كل مجموعة تخدم وظيفة محددة في هيكل تفصيل التكلفة: من التصنيف الهرمي وتحديد بنود العمل إلى استهلاك الموارد التفصيلي، ومتطلبات العمالة، وتكاليف الآلات، والمجاميع الكلية.

<p align="center">
  <br>
  <img src="https://github.com/datadrivenconstruction/cad2data-Revit-IFC-DWG-DGN-pipeline-with-conversion-validation-qto/blob/main/DDC_in_additon/DDC_readme_content/Resource-based%20Work%20Cost%20Norms%20table2.jpg" width="100%"/>
  <br></br>
</p>

**التصنيف** - `category_type`، `collection_code`، `collection_name`، `department_code`، `department_name`، `department_type`، `section_name`، `section_type`، `subsection_code`، `subsection_name`

**بند العمل (السعر)** - `rate_code`، `rate_original_name`، `rate_final_name`، `rate_unit`، `row_type`، `is_scope`، `is_abstract`، `is_machine`، `is_labor`، `is_material`، `work_composition_text`

**الموارد** - `resource_code`، `resource_name`، `resource_unit`، `resource_quantity`، `parameter_resource_quantity`، `resource_price_per_unit_eur_current`، `resource_cost_eur`

**العمالة** - `count_workers_per_unit`، `count_engineers_per_unit`، `count_operators_per_unit`، `count_total_people_per_unit`، `labor_hours_construction_workers`، `labor_hours_operators`، `labor_hours_engineers`، `total_labor_hours_workers_operators`، `total_labor_hours_all_personnel`، `cost_of_working_hours`، `count_people_per_day`

**الآلات** - `machine_class2_name`، `machine_class3_name`، `personnel_operator_code`، `personnel_operator_grade`، `price_operator_wages`، `price_relocation_included`، `price_cost_without_wages`، `electricity_consumption_kwh_per_machine_hour`، `electricity_cost_per_unit`، `electricity_cost_total_sum`، `cost_operator_sum`، `total_value_machinery_equipment`

**متغيرات السعر** - `price_code_prefix`، `price_abstract_resource_common_start`، `price_abstract_resource_variable_parts`، `price_abstract_resource_position_count`، `price_abstract_resource_est_price_min`، `price_abstract_resource_est_price_max`، `price_abstract_resource_est_price_mean`، `price_abstract_resource_est_price_median`، `price_abstract_resource_unit`، `abstract_resource_tech_group`

**المجاميع** - `total_cost_per_position`، `total_material_cost_per_position`، `total_resource_cost_per_position`، `total_value_abstract_resources`، `materials_resource_cost_eur`

**الكتلة والخدمات** - `mass_name`، `mass_value`، `mass_unit`، `service_category`، `service_type`، `parameter_service_code`، `parameter_service_unit`، `parameter_service_name`، `parameter_service_quantity`، `service_cost_sum`

### صيغة حساب التكلفة

| المكون | المعيار التقني | × | السعر الإقليمي | = | التكلفة |
|--------|-----------------|---|----------------|---|---------|
| 👷 **العمالة** | 172 ساعة/100م² | × | 17.95€/ساعة | = | 3,088.11€ |
| 🧱 **المواد** | 632 م²/100م² | × | 5.02€/م² | = | 3,170.73€ |
| 🚜 **المعدات** | 1.67 ساعة/100م² | × | 38.42€/ساعة | = | 64.18€ |
| | | | **الإجمالي** | = | **7,725.91€ لكل 100م²** |

---

## المنهجية

القيمة الرئيسية لـ **حساب التكلفة القائم على الموارد** هي فصل تكنولوجيا الإنتاج الثابتة عن المكون المالي المتقلب. يعتمد على "المبادئ الأولى" الفيزيائية للبناء:
- ساعات العمل المطلوبة لعمل محدد
- كميات المواد لكل وحدة عمل
- وقت المعدات المطلوب

**لماذا هذا مهم:**

- **الشفافية** - تسعير بدون هوامش مخفية، تفصيل كامل للموارد
- **قابلية التدقيق** - قدرة تحليل عميق لتحليل الاستثمار والتحقق
- **قابلية النقل** - معايير مستقلة عن المنطقة قابلة للتطبيق عبر الأسواق
- **مثبتة** - منهجية معيارية للصناعة أُسست منذ أكثر من 100 عام


### السياق التاريخي

أوصاف أعمال البناء في هذه القاعدة ترتكز على منهجية توحيد قائمة على الموارد بجذور تمتد من معايير الإنتاج في أوائل القرن العشرين إلى أنظمة المراجع الرقمية اليوم. طُورت وصُقلت باستمرار منذ عشرينيات القرن الماضي، وشهد هذا النهج تطوراً قوياً بشكل خاص عبر المنطقة الأوراسية.

على مدى مائة عام من التطوير، انتقل النظام من الحسابات اليدوية إلى الصيغ القابلة للقراءة الآلية - لكن مبدأه الأساسي يبقى سليماً: القياس الدقيق للموارد الفيزيائية المطلوبة لكل وحدة إنتاج بناء. التطبيقات الحديثة تربط البيانات المعيارية التاريخية بأسعار السوق الفورية.

التعديلات الإقليمية لهذه المنهجية تعمل تحت تسميات وطنية مختلفة: ENIR، GESN، FER، NRR، ESN، AzDTN، ShNQK، MKS ChT، SNT، BNbD، Dinh Muc، Ding'e.

<p align="center">
  <img src="https://github.com/datadrivenconstruction/cad2data-Revit-IFC-DWG-DGN-pipeline-with-conversion-validation-qto/blob/main/DDC_in_additon/DDC_readme_content/DDC%20CWICR%20SPREAD%20OF%20METHODOLOGY%20FROM%20THE%201920s.jpg" alt="OpenConstructionEstimate" width="1000">
</p>

⭐ <b>إذا كنت تريد رؤية تحديثات وإصدارات جديدة للقاعدة وإذا وجدت أدواتنا مفيدة، يرجى إعطاء نجمة لمستودعاتنا لرؤية المزيد من التطبيقات المماثلة لصناعة البناء.</b>
ضع نجمة على سير عمل DDC على GitHub وكن على علم فوري بالإصدارات الجديدة.
<p align="center">
  <br>
  <img src="https://github.com/datadrivenconstruction/cad2data-Revit-IFC-DWG-DGN-pipeline-with-conversion-validation-qto/blob/main/DDC_in_additon/DDC_readme_content/OCE%20star%20GitHub.gif" width="100%"/>
  <br></br>
</p>


---


## التكامل

### حالات الاستخدام

- **مستوى مبتدئ** - معايرة التكاليف، فهرسة الأسعار، تقدير المناقصات

- **متوسط** - التوطين، خطوط أنابيب ETL/BI، حساب CO₂

- **متقدم** - تدريب AI/ML، CAD (BIM) 5D، تدقيق استثمار عميق

---

## سير عمل n8n - الوصف التفصيلي

أربعة سير عمل جاهزة للإنتاج لتقدير تكاليف البناء الآلي. كل سير عمل يتصل بقاعدة بيانات DDC CWICR المتجهة عبر Qdrant ويستخدم نماذج الذكاء الاصطناعي للتحليل الذكي والمطابقة.

| # | سير العمل | المدخل | الأفضل لـ | تحميل |
|---|-----------|--------|-----------|-------|
| 1 | [روبوت تقدير النص](#1️⃣-روبوت-تقدير-النص) | 💬 نص | تقديرات سريعة من النص | [JSON](./n8n_1_Telegram_Bot_Cost_Estimates_and_Rate_Finder_TEXT_DDC_CWICR.json) |
| 2 | [مقدر الصور](#2️⃣-مقدر-التكلفة-بالصور) | 📷 صورة | زيارات الموقع، الفحص البصري | [JSON](./n8n_2_Photo_Cost_Estimate_DDC_CWICR.json) |
| 3 | [الروبوت العالمي](#3️⃣-الروبوت-العالمي-نص--صورة--pdf) | 💬📷📄 الكل | استخدام إنتاج كامل | [JSON](./n8n_3_Telegram_Bot_Cost_Estimates_and_Rate_Finder_TEXT_PHOTO_PDF_DDC_CWICR.json) |
| 4 | [خط أنابيب CAD/BIM](#4️⃣-خط-أنابيب-تقدير-cad-bim) | 🏗️ Revit | تقدير 4D/5D قائم على BIM | [JSON](./n8n_4_CAD_(BIM)_Cost_Estimation_Pipeline_4D_5D_with_DDC_CWICR.json) |

---

### 1️⃣ روبوت تقدير النص

**الملف:** `n8n_1_Telegram_Bot_Cost_Estimates_and_Rate_Finder_TEXT_DDC_CWICR.json`

روبوت Telegram لتقدير التكلفة القائم على النص. صف أعمال البناء بلغة طبيعية - الروبوت يحلل المدخل، يبحث في قاعدة البيانات المتجهة، ويعيد تفصيلات التكلفة.

<p align="center">
  <br>
  <img src="https://github.com/datadrivenconstruction/cad2data-Revit-IFC-DWG-DGN-pipeline-with-conversion-validation-qto/blob/main/DDC_in_additon/DDC_readme_content/Text_Estimator_Bot.jpg" width="100%"/>
  <br></br>
</p>

<h3 align="right">🤖 جرب الآن - روبوتات العرض المباشر</h3>
<p align="right"><i>اختبر سير عمل التقدير فوراً على Telegram</i></p>
<p><b>@TextOpenConstructionEstimate_bot</b></p>
<p>أنشئ تقديرات تكلفة كاملة<br>من أوصاف نصية</p>
<a href="https://t.me/TextOpenConstructionEstimate_bot">
<img src="https://img.shields.io/badge/فتح_الروبوت-26A5E4?style=for-the-badge&logo=telegram&logoColor=white" alt="روبوت النص"/>
</a>


**كيف يعمل:**

| الخطوة | الإجراء | التقنية |
|--------|---------|---------|
| 1 | المستخدم يرسل وصفاً نصياً | Telegram Bot API |
| 2 | الذكاء الاصطناعي يحلل ويستخرج بنود العمل | OpenAI / Claude / Gemini |
| 3 | توليد تضمينات لكل بند | OpenAI `text-embedding-3-large` |
| 4 | البحث عن الأسعار المطابقة في القاعدة | بحث Qdrant المتجه |
| 5 | الذكاء الاصطناعي يعيد ترتيب النتائج للدقة | تقييم LLM |
| 6 | حساب التكاليف وتوليد التقرير | HTML / Excel / PDF |

**الميزات:**

| الميزة | الوصف |
|--------|-------|
| 💬 إدخال بلغة طبيعية | يقبل أي صيغة نص - قوائم، جمل، أوصاف منظمة |
| 🤖 دعم LLM متعدد | يعمل مع OpenAI، Claude، أو Gemini (قابل للتبديل) |
| 🔍 بحث دلالي | يجد أفضل المطابقات حتى مع صياغة مختلفة |
| 🌍 11 لغة | DE، EN، RU، ES، FR، PT، ZH، AR، HI، US، UK |
| 📊 تصدير متعدد | تقرير HTML، جدول بيانات Excel، مستند PDF |
| ✏️ تحرير تفاعلي | عدل الكميات قبل الحساب النهائي |

**بيانات الاعتماد المطلوبة:**
- رمز روبوت Telegram (من @BotFather)
- مفتاح OpenAI API (للتضمينات + LLM اختياري)
- URL Qdrant + مفتاح API

---

### 2️⃣ مقدر التكلفة بالصور

**الملف:** `n8n_2_Photo_Cost_Estimate_DDC_CWICR.json`

واجهة نموذج ويب للتقدير القائم على الصور. ارفع صورة بناء - AI Vision يحدد العناصر، يقدر الأبعاد، ويحسب التكاليف تلقائياً.

<p align="center">
  <br>
  <img src="https://github.com/datadrivenconstruction/cad2data-Revit-IFC-DWG-DGN-pipeline-with-conversion-validation-qto/blob/main/DDC_in_additon/DDC_readme_content/n8n%20pipeline%20photo%20estimator.jpg" width="100%"/>
  <br></br>
</p>


**كيف يعمل:**

| الخطوة | الإجراء | التقنية |
|--------|---------|---------|
| 1 | المستخدم يرفع صورة عبر نموذج الويب | n8n Form Trigger |
| 2 | AI Vision يحلل الصورة | GPT-4 Vision |
| 3 | يحدد نوع الغرفة والعناصر والمواد | استخراج JSON منظم |
| 4 | يقدر الأبعاد من كائنات مرجعية | تفكير AI (أبواب، بلاط، إلخ) |
| 5 | يفكك العناصر إلى بنود عمل | معالجة LLM |
| 6 | يسعر كل عمل عبر البحث المتجه | Qdrant + تضمينات OpenAI |
| 7 | يولد تقرير HTML احترافي | مخرج منسق |

**الميزات:**

| الميزة | الوصف |
|--------|-------|
| 📷 تحليل الصور | GPT-4 Vision يحدد عناصر البناء |
| 📐 تحديد أبعاد تلقائي | يقدر الأحجام باستخدام كائنات مرجعية (أبواب، بلاط) |
| 🏠 كشف الغرفة | حمام، مطبخ، غرفة نوم، خارجي، إلخ |
| 🔨 دعم نوع العمل | بناء جديد / تجديد / إصلاح |
| 🌍 9 قواعد إقليمية | أسعار محلية لبرلين، تورونتو، باريس، إلخ |
| 📄 تقارير احترافية | مخرج HTML نظيف جاهز للعملاء |

**بيانات الاعتماد المطلوبة:**
- مفتاح OpenAI API (GPT-4 Vision + التضمينات)
- URL Qdrant + مفتاح API

---

### 3️⃣ الروبوت العالمي (نص + صورة + PDF)

**الملف:** `n8n_3_Telegram_Bot_Cost_Estimates_and_Rate_Finder_TEXT_PHOTO_PDF_DDC_CWICR.json`

روبوت Telegram كامل يدعم جميع أنواع المدخلات: أوصاف نصية، صور البناء، ومخططات PDF. أشمل سير عمل للاستخدام الإنتاجي.


<p align="center">
  <br>
  <img src="https://github.com/datadrivenconstruction/cad2data-Revit-IFC-DWG-DGN-pipeline-with-conversion-validation-qto/blob/main/DDC_in_additon/DDC_readme_content/Universal%20Estimator%20Bot%20Text%20%20Photo%20PDF.jpg" width="100%"/>
  <br></br>
</p>

**كيف يعمل:**

| الخطوة | الإجراء | التقنية |
|--------|---------|---------|
| 1 | المستخدم يرسل نص أو صورة أو PDF | Telegram Bot API |
| 2 | الموجه يكتشف نوع المدخل | تحليل نوع المحتوى |
| 3a | **نص:** الذكاء الاصطناعي يحلل بنود العمل | OpenAI / Gemini |
| 3b | **صورة:** AI Vision يستخرج العناصر | GPT-4 Vision / Gemini 2.0 |
| 3c | **PDF:** يستخرج ويحلل الصفحات | معالجة PDF + Vision |
| 4 | بحث دلالي في DDC CWICR | قاعدة بيانات Qdrant المتجهة |
| 5 | إعادة ترتيب AI لأفضل المطابقات | تقييم LLM |
| 6 | تحرير تفاعلي عبر قائمة الروبوت | لوحات مفاتيح Telegram المضمنة |
| 7 | تصدير النتائج | HTML / Excel / PDF |

**17 إجراء للروبوت:**

| الإجراء | الوصف |
|---------|-------|
| `/start` | قائمة اختيار اللغة |
| رفع صورة | تفعيل تحليل AI vision |
| رسالة نص | تحليل واستخراج بنود العمل |
| رفع PDF | معالجة المخططات |
| تعديل الكميات | تعديل قبل الحساب |
| إضافة عمل | إدخال بند عمل يدوي |
| حساب | تشغيل التقدير الكامل |
| عرض التفاصيل | إظهار الموارد لكل بند |
| تصدير Excel | تحميل جدول بيانات CSV |
| تصدير PDF | توليد تقرير PDF |
| مساعدة | عرض تعليمات الاستخدام |
| تحسين | إعادة التحليل مع تصحيحات |

**الميزات:**

| الميزة | الوصف |
|--------|-------|
| 📷 AI Vision مزدوج | Gemini 2.0 Flash أو GPT-4 Vision (قابل للتكوين) |
| 📄 معالجة PDF | مخططات، جداول كميات ممسوحة، مستندات |
| 💬 تحليل نص ذكي | يتعامل مع القوائم والجداول والنص الحر |
| 🔍 إعادة ترتيب AI | يحسن دقة المطابقة |
| ✏️ تحرير كامل | إضافة، حذف، تعديل بنود العمل |
| 📊 تصدير متعدد الصيغ | HTML، Excel، PDF |
| 🌍 11 لغة | توطين كامل |

**بيانات الاعتماد المطلوبة:**
- رمز روبوت Telegram
- مفتاح OpenAI API (التضمينات)
- مفتاح Gemini API (Vision) أو OpenAI GPT-4 Vision
- URL Qdrant + مفتاح API

---

### 4️⃣ خط أنابيب تقدير CAD (BIM)

**الملف:** `n8n_4_CAD_(BIM)_Cost_Estimation_Pipeline_4D_5D_with_DDC_CWICR.json`

تقدير تكلفة آلي من نماذج Revit/IFC/DWG. يستخرج بيانات BIM، يصنف العناصر، يفكك إلى بنود عمل، ويولد تقديرات 4D/5D مع تفصيل كامل للموارد.

<p align="right">
  <a href="https://datadrivenconstruction.io">
    <img src="https://github.com/datadrivenconstruction/cad2data-Revit-IFC-DWG-DGN-pipeline-with-conversion-validation-qto/blob/main/DDC_in_additon/DDC_readme_content/CAD%20(Revit)%20to%205D-4D%20Cost%20and%20Time%20Estimate.jpg" alt="DataDrivenConstruction">
  </a>
</p>


**n8n يوفر أكثر من 400 تكامل أصلي** مع منصات مثل Google Sheets، Notion، Slack، Airtable، قواعد البيانات (PostgreSQL، MongoDB)، التخزين السحابي، والمزيد. كل عقدة في سير العمل هذا معيارية - يمكنك:

- 🔄 **تبديل مزودي LLM** (OpenAI ↔ Claude ↔ Gemini ↔ Grok)
- 📊 **الاتصال بنظام ERP أو إدارة المشاريع الخاص بك**
- 📁 **تصدير النتائج إلى أي وجهة** (تخزين سحابي، بريد إلكتروني، لوحات معلومات)
- 🔧 **تعديل أي مرحلة** لتتناسب مع منهجية التقدير الخاصة بك

سير العمل ملكك للتكييف. بدون قيود. بدون رسوم ترخيص. تحكم كامل.

---

## 📋 المتطلبات الأساسية

| المكون | المتطلب | الوصف |
|--------|---------|-------|
| **[n8n](https://n8n.io/)** | v1.0+ (v2.0+ يتطلب [إعداد](#️-إعداد-n8n-20-المطلوب)) | منصة أتمتة سير العمل لتنسيق خط أنابيب التقدير |
| **[Qdrant](https://qdrant.tech/)** | سحابي أو مستضاف ذاتياً | قاعدة بيانات متجهة للبحث الدلالي عبر بنود العمل |
| **[OpenAI API](https://platform.openai.com/)** | للتضمينات (`text-embedding-3-large`) | يولد تضمينات متجهة لعناصر BIM ومطابقة قاعدة التكاليف |
| **LLM API** | OpenAI / Claude / Gemini / xAI Grok | نماذج AI لتصنيف بنود العمل وتوليد التقديرات |
| **[محول DDC](https://github.com/datadrivenconstruction/cad2data-Revit-IFC-DWG-DGN-pipeline-with-conversion-validation-qto)** | `RvtExporter.exe` | يستخرج بيانات BIM من نماذج Revit إلى Excel/JSON للمعالجة |

---

## البداية السريعة لسير العمل

### الخطوة 1: استيراد سير العمل

</div>

```
n8n → سير عمل جديد → استيراد من ملف → اختر JSON
```

<div dir="rtl">

### الخطوة 2: تكوين بيانات الاعتماد

في عقدة **🔑 TOKEN**، عيّن مفاتيح API الخاصة بك:

</div>

```json
{
  "bot_token": "YOUR_TELEGRAM_BOT_TOKEN",
  "OPENAI_API_KEY": "YOUR_OPENAI_KEY",
  "GEMINI_API_KEY": "YOUR_GEMINI_KEY",
  "QDRANT_URL": "http://localhost:6333",
  "QDRANT_API_KEY": ""
}
```

<div dir="rtl">

### الخطوة 3: تحميل DDC CWICR إلى Qdrant

حمّل اللقطة من مجلد اللغة المقابل واستوردها:

</div>

```bash
curl -X POST "http://localhost:6333/collections/ddc_ar_dubai/snapshots/upload" \
  -H "Content-Type: multipart/form-data" \
  -F "snapshot=@EN___DDC_CWICR/EN_TORONTO_workitems_costs_resources_EMBEDDINGS_3072_DDC_CWICR.snapshot"
```

<div dir="rtl">

### الخطوة 4: التفعيل والاختبار

- فعّل سير العمل في n8n
- لروبوتات Telegram: أرسل `/start` إلى روبوتك
- لنماذج الويب: افتح URL النموذج المقدم من n8n

---

## ⚠️ إعداد n8n 2.0+ المطلوب

> **بدءاً من إصدار n8n 2.0، عقدة Execute Command معطلة افتراضياً لأسباب أمنية.**
>
> بدون التكوين أدناه، سير العمل الذي يستخدم Execute Command (خاصة خط أنابيب CAD/BIM) **لن يعمل** - العقد ستظهر بعلامة استفهام أو لن يتم التعرف عليها.

### حل سريع

**Windows (CMD) - تشغيل كل مرة:**

</div>

```cmd
set NODES_EXCLUDE=[] && npx n8n
```

<div dir="rtl">

**حل دائم - إنشاء مرة واحدة:**

أنشئ ملف `C:\Users\YOUR_USER\.n8n\.env` مع:

</div>

```
NODES_EXCLUDE=[]
```

<div dir="rtl">

ثم شغل `npx n8n` كالمعتاد.

**Docker:**

</div>

```yaml
environment:
  - NODES_EXCLUDE=[]
```

<div dir="rtl">

### التحقق من الإعداد

1. ابدأ n8n
2. انقر **+** → ابحث عن **"Execute Command"**
3. إذا ظهرت العقدة → ✅ أنت جاهز!

> 📚 المزيد من التفاصيل: [n8n 2.0 Breaking Changes](https://docs.n8n.io/2-0-breaking-changes/)

---

## 🌍 اللغات ومستويات الأسعار المدعومة

| الرمز | اللغة | مستوى السعر | العملة | مجموعة Qdrant |
|-------|-------|-------------|--------|---------------|
| `AR` | العربية | دبي | AED | `ddc_ar_dubai` |
| `DE` | الألمانية | برلين | EUR | `ddc_de_berlin` |
| `EN` | الإنجليزية | تورونتو | CAD | `ddc_en_toronto` |
| `ES` | الإسبانية | برشلونة | EUR | `ddc_sp_barcelona` |
| `FR` | الفرنسية | باريس | EUR | `ddc_fr_paris` |
| `HI` | الهندية | مومباي | INR | `ddc_hi_mumbai` |
| `PT` | البرتغالية | ساو باولو | BRL | `ddc_pt_saopaulo` |
| `RU` | الروسية | سانت بطرسبرغ | RUB | `ddc_ru_stpetersburg` |
| `ZH` | الصينية | شنغهاي | CNY | `ddc_zh_shanghai` |
| `US` | الإنجليزية | USA | USD | `ddc_usa_usd` |
| `UK` | الإنجليزية | UK | GBP | `ddc_uk_gbp` |

---

## 📊 مراحل خط الأنابيب

سير عمل CAD/BIM يعالج البيانات عبر 10 مراحل:

| المرحلة | الاسم | الوصف |
|---------|-------|-------|
| **0** | جمع بيانات BIM | استخراج العناصر من Revit عبر محول DDC |
| **1** | كشف المشروع | الذكاء الاصطناعي يحدد نوع المشروع (سكني، تجاري، إلخ) |
| **2** | توليد المراحل | الذكاء الاصطناعي ينشئ مراحل البناء |
| **3** | تعيين العناصر | الذكاء الاصطناعي يربط أنواع BIM بالمراحل |
| **4** | تفكيك الأعمال | الذكاء الاصطناعي يفكك الأنواع إلى بنود عمل ("جدار طوب" → بناء، ملاط) |
| **5** | البحث المتجه | إيجاد الأسعار المطابقة في DDC CWICR عبر Qdrant |
| **6** | ربط الوحدات | تحويل وحدات BIM إلى وحدات السعر |
| **7** | حساب التكلفة | الكمية × السعر الوحدوي لكل بند |
| **7.5** | التحقق | مراجعة CTO للاكتمال والتكرارات |
| **8** | التجميع | الجمع حسب المراحل والفئات |
| **9** | توليد التقرير | إنشاء مخرجات HTML وExcel |

---

## ⚙️ اختيار نموذج LLM

سير العمل يدعم عدة مزودي AI. فعّل النموذج المفضل في قسم **نماذج LLM**:

| النموذج | اسم العقدة | الحالة |
|---------|-----------|--------|
| OpenAI GPT-4o | `OpenAI LLM` | ✅ افتراضي |
| Claude Opus 4 | `Anthropic Chat Model2` | معطل |
| Gemini 2.5 Pro | `Google Gemini Chat Model` | معطل |
| xAI Grok | `xAI Grok Chat Model1` | معطل |
| DeepSeek | `DeepSeek Chat Model` | معطل |

لتبديل النماذج: **فعّل** عقدة النموذج المطلوب و**عطّل** الأخرى.

---

## 📁 ملفات الإخراج

التقارير تُحفظ في مجلد المشروع:

</div>

```
project_YYYY-MM-DD.html   ← تقرير تفاعلي (يفتح في المتصفح)
project_YYYY-MM-DD.xls    ← جدول بيانات متوافق مع Excel
```

<div dir="rtl">

<p align="center">
  <br>
  <img src="https://github.com/datadrivenconstruction/cad2data-Revit-IFC-DWG-DGN-pipeline-with-conversion-validation-qto/blob/main/DDC_in_additon/DDC_readme_content/The%20generated%20report%20includes.jpg" width="100%"/>
  <br></br>
</p>

---

## 🔗 مجموعات Qdrant

سير العمل يختار المجموعة الصحيحة تلقائياً بناءً على `language_code`:

</div>

```
{LANG}_{CITY}_workitems_costs_resources_EMBEDDINGS_3072_DDC_CWICR
```

<div dir="rtl">

مثال: `AR_DUBAI_workitems_costs_resources_EMBEDDINGS_3072_DDC_CWICR`

---

## ⚠️ استكشاف الأخطاء وإصلاحها

| المشكلة | الحل |
|---------|-----|
| "Execute Command مفقود" (n8n 2.0+) | عيّن متغير البيئة `NODES_EXCLUDE=[]`. راجع [إعداد n8n 2.0+](#️-إعداد-n8n-20-المطلوب) |
| "ملف Excel غير موجود" | تحقق من مسارات `path_to_converter` و`project_file` |
| "فشل اتصال Qdrant" | تحقق من URL Qdrant ومفتاح API في بيانات الاعتماد |
| "تجاوز حد المعدل" | قلل حجم الدفعات أو أضف تأخيرات بين استدعاءات API |
| "السعر غير موجود" | تحقق من وجود مجموعة اللغة الصحيحة في Qdrant |
| "خطأ webhook Telegram" | تأكد أن سير العمل نشط وURL webhook متاح |
| "فشل Vision API" | تحقق أن مفتاح Gemini أو OpenAI Vision API صالح |

---

## قاعدة البيانات المتجهة

مجموعات Qdrant جاهزة للاستخدام مع تضمينات OpenAI `text-embedding-3-large` للبحث الدلالي عبر بنود أعمال البناء.

قواعد البيانات المتجهة تسمح لك بـ "التحدث" إلى بياناتك بلغة طبيعية – باستخدام جمل بسيطة أو عبارات قصيرة بدلاً من الكود أو الفلاتر المعقدة. هذا يسرع بشكل كبير إيجاد بند العمل أو سطر التكلفة الصحيح، حتى في مجموعات البيانات الكبيرة جداً.

يمكن ربط مجموعات Qdrant هذه بالتطبيقات عبر سير عمل الأتمتة والتكامل الحديثة (مثل أدوات Workflow وPipeline منخفضة/بدون كود). يمكنك بناء مساعدين يبحثون ويفلترون ويشرحون بنود أعمال البناء، أو دمج البحث الدلالي مباشرة في أدوات التقدير والتحكم في المشاريع الحالية.

---

### لقطات قاعدة بيانات Qdrant المتجهة

اللقطات موجودة في مجلدات اللغة المقابلة في هذا المستودع (مخزنة عبر Git LFS).

| اللغة | المنطقة | لقطة Qdrant |
|-------|---------|-------------|
| 🇸🇦 العربية | دبي | `AR___DDC_CWICR/AR_DUBAI_workitems_costs_resources_EMBEDDINGS_3072_DDC_CWICR.snapshot` |
| 🇨🇳 الصينية | شنغهاي | `ZH___DDC_CWICR/ZH_SHANGHAI_workitems_costs_resources_EMBEDDINGS_3072_DDC_CWICR.snapshot` |
| 🇩🇪 الألمانية | برلين | `DE___DDC_CWICR/DE_BERLIN_workitems_costs_resources_EMBEDDINGS_3072_DDC_CWICR.snapshot` |
| 🇬🇧 الإنجليزية | تورونتو | `EN___DDC_CWICR/EN_TORONTO_workitems_costs_resources_EMBEDDINGS_3072_DDC_CWICR.snapshot` |
| 🇪🇸 الإسبانية | برشلونة | `ES___DDC_CWICR/SP_BARCELONA_workitems_costs_resources_EMBEDDINGS_3072_DDC_CWICR.snapshot` |
| 🇫🇷 الفرنسية | باريس | `FR___DDC_CWICR/FR_PARIS_workitems_costs_resources_EMBEDDINGS_3072_DDC_CWICR.snapshot` |
| 🇮🇳 الهندية | مومباي | `HI___DDC_CWICR/HI_MUMBAI_workitems_costs_resources_EMBEDDINGS_3072_DDC_CWICR.snapshot` |
| 🇧🇷 البرتغالية | ساو باولو | `PT___DDC_CWICR/PT_SAOPAULO_workitems_costs_resources_EMBEDDINGS_3072_DDC_CWICR.snapshot` |
| 🇷🇺 الروسية | سانت بطرسبرغ | `RU___DDC_CWICR/RU_STPETERSBURG_workitems_costs_resources_EMBEDDINGS_3072_DDC_CWICR.snapshot` |
| 🇬🇧 الإنجليزية (UK) | المملكة المتحدة (GBP) | `UK___DDC_CWICR/UK_GBP_workitems_costs_resources_EMBEDDINGS_3072_DDC_CWICR.snapshot` |
| 🇺🇸 الإنجليزية (US) | الولايات المتحدة (USD) | `US___DDC_CWICR/USA_USD_workitems_costs_resources_EMBEDDINGS_3072_DDC_CWICR.snapshot` |

### المجموعات

🇸🇦 `ddc_ar_dubai` (العربية) · 🇨🇳 `ddc_zh_shanghai` (الصينية) · 🇩🇪 `ddc_de_berlin` (الألمانية) · 🇬🇧 `ddc_en_toronto` (الإنجليزية) · 🇪🇸 `ddc_sp_barcelona` (الإسبانية) · 🇫🇷 `ddc_fr_paris` (الفرنسية) · 🇮🇳 `ddc_hi_mumbai` (الهندية) · 🇧🇷 `ddc_pt_saopaulo` (البرتغالية) · 🇷🇺 `ddc_ru_stpetersburg` (الروسية) · 🇺🇸 `ddc_usa_usd` (USA) · 🇬🇧 `ddc_uk_gbp` (UK)

كل مجموعة تحتوي **55,719 متجه** مع بيانات وصفية كاملة.

### نشر Docker

</div>

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
# البدء
docker-compose up -d

# استيراد اللقطة
curl -X POST "http://localhost:6333/collections/ddc_ar_dubai/snapshots/upload" \
  -H "Content-Type: multipart/form-data" \
  -F "snapshot=@AR___DDC_CWICR/AR_DUBAI_workitems_costs_resources_EMBEDDINGS_3072_DDC_CWICR.snapshot"

# لوحة المعلومات: http://localhost:6333/dashboard
```

<div dir="rtl">

---

## 🌐 Pricing Search API - BuildCalculator.io

</div>

<p align="center">
  <a href="https://buildcalculator.io/api-docs/">
    <img src="https://img.shields.io/badge/توثيق_API-buildcalculator.io-2563eb?style=for-the-badge" alt="API Docs">
  </a>
  &nbsp;
  <img src="https://img.shields.io/badge/المصادقة-غير_مطلوبة-059669?style=for-the-badge" alt="No Auth">
  &nbsp;
  <img src="https://img.shields.io/badge/التكلفة-مجاني-059669?style=for-the-badge" alt="Free">
  &nbsp;
  <img src="https://img.shields.io/badge/حد_الطلبات-60_طلب/دقيقة-d97706?style=for-the-badge" alt="Rate Limit">
</p>

<div dir="rtl">

واجهة REST API مجانية للبحث عن بنود أعمال البناء مع تفصيل كامل للتكاليف والعمالة والمواد والمعدات. **55,719 بند** بـ **11 لغة** مع **84 حقلاً** لكل بند.

**عنوان URL الأساسي:** `https://buildcalculator.io/api/v1`

### نقاط نهاية API

#### `GET/POST /api/v1/search` - البحث عن بنود البناء

| المعامل | النوع | الافتراضي | مطلوب | الوصف |
|---------|-------|-----------|-------|-------|
| `q` | string | - | نعم | استعلام البحث (حد أدنى حرفان). يعمل بأي لغة |
| `lang` | string | `en` | لا | لغة قاعدة البيانات: `en`، `ru`، `de`، `fr`، `es`، `pt`، `zh`، `ar`، `hi` |
| `top` | integer | 5 | لا | عدد النتائج (1–20) |

#### `GET /api/v1/languages` - اللغات المدعومة

يعرض جميع اللغات المتاحة مع عدد البنود.

#### `GET /api/v1/stats` - إحصائيات قاعدة البيانات

يعرض عدد البنود والفئات واللغات والبيانات الوصفية.

### أمثلة الكود API

</div>

**cURL:**
```bash
curl "https://buildcalculator.io/api/v1/search?q=أساسات+خرسانية&lang=ar&top=5"
```

**Python:**
```python
import requests

response = requests.get("https://buildcalculator.io/api/v1/search",
    params={"q": "بناء جدران طوب", "lang": "ar", "top": 5})
data = response.json()

for item in data["results"]:
    print(f"{item['name']} - {item['pricing']['total_per_unit']} EUR/{item['unit']}")
```

**JavaScript:**
```javascript
const res = await fetch(
  "https://buildcalculator.io/api/v1/search?q=تسقيف&lang=ar&top=3"
);
const data = await res.json();
```

<div dir="rtl">

**مثال الاستجابة:**

</div>

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

<div dir="rtl">

**رموز الخطأ:**

| الرمز | المعنى | الإجراء |
|-------|--------|---------|
| 400 | استعلام مفقود أو غير صالح | تحقق من معامل `q` (حد أدنى حرفان) |
| 429 | تم تجاوز حد الطلبات | انتظر وأعد المحاولة (60 طلب/دقيقة) |
| 500 | خطأ في الخادم | أعد المحاولة أو تواصل مع الدعم |

> 📖 التوثيق الكامل: [buildcalculator.io/api-docs](https://buildcalculator.io/api-docs/)

---

## البداية السريعة

### Python - البيانات الجدولية

</div>

```python
import pandas as pd

# Parquet (موصى به)
df = pd.read_parquet("DDC_CWICR_AR.parquet")

# Excel
df = pd.read_excel("DDC_CWICR_AR.xlsx")

print(f"السجلات: {len(df):,} | الحقول: {len(df.columns)}")
print(df[['rate_code', 'rate_original_name', 'rate_unit', 'total_cost_per_position']].head())
```

### Python - البحث الدلالي

```python
from qdrant_client import QdrantClient
from openai import OpenAI

client = QdrantClient("localhost", port=6333)
openai = OpenAI()

# البحث بلغة طبيعية
query = "صب أساس خرساني مسلح"
embedding = openai.embeddings.create(
    input=query,
    model="text-embedding-3-large"
).data[0].embedding

results = client.search(
    collection_name="ddc_ar_dubai",
    query_vector=embedding,
    limit=5
)

for r in results:
    print(f"[{r.score:.3f}] {r.payload['rate_code']}: {r.payload['rate_original_name']}")
```

### البحث المفلتر

```python
from qdrant_client.models import Filter, FieldCondition, MatchValue, Range

# حسب القسم
results = client.search(
    collection_name="ddc_ar_dubai",
    query_vector=embedding,
    query_filter=Filter(must=[
        FieldCondition(key="department_name", match=MatchValue(value="الخرسانة والخرسانة المسلحة"))
    ]),
    limit=10
)

# حسب نطاق السعر
results = client.search(
    collection_name="ddc_ar_dubai",
    query_vector=embedding,
    query_filter=Filter(must=[
        FieldCondition(key="price_est_median", range=Range(gte=1000, lte=50000))
    ]),
    limit=10
)
```

<div dir="rtl">


---

## 💻 أمثلة للمطورين

يحتوي دليل [`examples/`](./examples/) على **كود جاهز للتشغيل** بعدة لغات برمجة.

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

**→ [تصفح جميع الأمثلة](./examples/)**

---

## الموارد والمجتمع

[![الموقع](https://img.shields.io/badge/🌐_الموقع-datadrivenconstruction.io-2563eb?style=for-the-badge)](https://datadrivenconstruction.io)
[![العرض](https://img.shields.io/badge/🎯_العرض-openconstructionestimate.com-059669?style=for-the-badge)](https://openconstructionestimate.com)
[![GitHub](https://img.shields.io/badge/💻_GitHub-datadrivenconstruction-181717?style=for-the-badge&logo=github)](https://github.com/datadrivenconstruction)
[![YouTube](https://img.shields.io/badge/📺_YouTube-@datadrivenconstruction-FF0000?style=for-the-badge&logo=youtube)](https://youtube.com/@datadrivenconstruction)
[![LinkedIn](https://img.shields.io/badge/💼_LinkedIn-datadrivenconstruction-0A66C2?style=for-the-badge&logo=linkedin)](https://linkedin.com/company/datadrivenconstruction)
[![Telegram](https://img.shields.io/badge/💬_Telegram-datadrivenconstruction-26A5E4?style=for-the-badge&logo=telegram)](https://t.me/datadrivenconstruction)

### الاستشارات والتدريب

نعمل مع شركات البناء والهندسة الرائدة ووكالات الاستشارات وشركات التكنولوجيا حول العالم لمساعدتهم في تنفيذ مبادئ البيانات المفتوحة، وأتمتة معالجة CAD/BIM، وبناء خطوط أنابيب ETL قوية. ندعم بنشاط المنظمات التي تبحث عن حلول عملية للتحول الرقمي والتوافقية، مع التركيز على تحديات جودة البيانات والتصنيف مع دفع اعتماد سير العمل المفتوح والآلي.

إذا كنت ترغب في اختبار هذا الحل مع بياناتك الخاصة أو مهتم بتكييف سير العمل لمهام المشروع الحقيقية، لا تتردد في الاتصال بنا. فريقنا يقدم ورش عمل عملية، واستشارات استراتيجية، ويطور نماذج أولية مصممة لعمليات المشروع الحقيقية.

<a href="mailto:info@datadrivenconstruction.io">
  <img src="https://img.shields.io/badge/📧_اتصل_بنا-info@datadrivenconstruction.io-2563eb?style=for-the-badge" alt="الاتصال">
</a>

### المساهمة

DDC CWICR مشروع مجاني ومفتوح المصدر مكرس لجعل صناعة البناء أكثر كفاءة وشفافية وتقدماً تقنياً. نبحث بنشاط عن متحمسين يشاركون هذه المهمة. إذا أنشأت حلولاً مفيدة ومستعد لمشاركتها مع المجتمع، نحن هنا لمساعدتك على أن تُسمع.

ندعوك لتقديم سير العمل المفتوح المصدر الخاص بك وخطوط الأنابيب والتكاملات المبنية على DDC CWICR - أدوات يمكن لأي شخص استخدامها بحرية في عمله. أفضل الحلول ستُنشر مع إسناد كامل للمؤلف على GitHub وتُعلن عبر نشرتنا الإخبارية وقنوات التواصل الاجتماعي، لتصل إلى عشرات الآلاف من المشتركين المحترفين. هذا يضع اسمك مباشرة أمام مجتمع دولي من مقدري التكاليف ومتخصصي BIM ومديري المشاريع.

معاً نغير الصناعة. يمكنك إرسال حلك إلى info@datadrivenconstruction.io بموضوع "DDC Open Workflow" أو تقديم Pull Request مباشرة إلى مستودعات GitHub الخاصة بنا.

أتمت معالجة بيانات البناء مع سير عمل n8n CAD-BIM الجاهزة:

<a href="https://github.com/datadrivenconstruction/cad2data-Revit-IFC-DWG-DGN-pipeline-with-conversion-validation-qto">
  <img src="https://img.shields.io/badge/خط_أنابيب_cad2data-GitHub-181717?style=for-the-badge&logo=github" alt="خط أنابيب cad2data">
</a>

---

## 🤖 تعليمات الذكاء الاصطناعي

مجلد `AI_INSTRUCTIONS/` يحتوي على توثيق شامل لمساعدي البرمجة بالذكاء الاصطناعي للعمل بفعالية مع قاعدة بيانات تكاليف البناء هذه.

### ما هو DDC CWICR؟

**DDC CWICR** (Construction Work Items, Components & Resources) هي قاعدة بيانات مفتوحة المصدر لتكاليف البناء تحتوي على:
- **55,719 بند عمل** - عمليات بناء مفصلة مع تفصيل كامل للتكاليف
- **27,672 مورد** - مواد وعمالة ومعدات مع تسعير إقليمي
- **85 حقل بيانات** - مخطط منظم لحسابات دقيقة
- **11 لغة** - مع تسعير خاص بالمنطقة (EUR، USD، CAD، RUB، CNY، إلخ)
- **تضمينات محسوبة مسبقاً** - متجهات OpenAI بـ 3072 بُعد للبحث الدلالي

### منهجية قائمة على الموارد

القاعدة تستخدم **نهج حساب قائم على الموارد** يفصل:
- **المعايير التقنية** (ثابتة) - ساعات العمل، كميات المواد، وقت المعدات
- **الأسعار الإقليمية** (متغيرة) - أسعار الساعة، تكاليف المواد، أسعار الوقود

</div>

```
التكلفة الفعلية = المعيار التقني × السعر الإقليمي
```

<div dir="rtl">

هذا يسمح بتقدير دقيق عبر مناطق وفترات زمنية مختلفة.

### ملفات تعليمات الذكاء الاصطناعي

| الملف | الغرض |
|-------|-------|
| `INSTRUCTIONS.md` | نظرة عامة رئيسية، بداية سريعة، الصيغ |
| `CLAUDE.md` | أنماط وأمثلة خاصة بـ Claude Code |
| `OPENCODE.md` | تعليمات موجزة لـ Opencode |
| `ANTIGRAVITY.md` | تكامل GCP (BigQuery، Vertex AI، Qdrant) |
| `DATABASE_SCHEMA.md` | مرجع مخطط 85 حقل الكامل |

### سير عمل n8n - أمثلة وقوالب

سير عمل n8n المضمنة هي **أمثلة وقوالب** توضح منطق تقدير التكلفة. يمكن أن تكون:
- ✅ مستخدمة كما هي للنشر السريع
- ✅ معدلة جزئياً لمتطلبات عمل محددة
- ✅ مدروسة لفهم منهجية حساب التكلفة
- ✅ مرجع عند بناء تكاملات مخصصة على أي منصة

سير العمل توضح: استعلامات القاعدة، مطابقة بنود العمل، منطق التسعير الإقليمي، وتوليد التقارير. يمكن للذكاء الاصطناعي تحليلها لفهم عملية التقدير الكاملة.

### لماذا هذا مهم

مساعدو الذكاء الاصطناعي يمكنهم مساعدتك في:
- الاستعلام عن القاعدة باستخدام لغة طبيعية
- البحث عن أعمال بالبحث الدلالي
- حساب التكاليف مع التسعير الإقليمي
- توليد التقارير وتصدير البيانات
- بناء تكاملات مع الخدمات السحابية
- فهم منهجية حساب التكلفة من أمثلة سير العمل

### البدء السريع مع الذكاء الاصطناعي

1. افتح المشروع في IDE المدعوم بالذكاء الاصطناعي
2. اسأل: *"أظهر لي جميع أعمال الخرسانة مع تكاليفها"*
3. الذكاء الاصطناعي سيستخدم التعليمات للاستعلام عن البيانات بشكل صحيح

**الكتاب**: لتفاصيل المنهجية، راجع [كتاب Data-Driven Construction](https://datadrivenconstruction.io/book)

---

## الترخيص - CC BY-NC 4.0

المستودع بالكامل مرخص بموجب [**Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)**](https://creativecommons.org/licenses/by-nc/4.0/).

### ما يُمكنك فعله

| | |
|---|---|
| **الاستخدام التجاري** | أنشئ منتجات، SaaS، تطبيقات، API - مجاناً، بدون طلب إذن |
| **النسخ والتوزيع** | شارك البيانات بأي صيغة |
| **التعديل والتكييف** | حوّل، أضف، أنشئ أعمالاً مشتقة |
| **استخدام AI/ML** | تدريب النماذج، خطوط RAG، التضمينات |
| **الاستخدام البحثي** | الأوراق العلمية، التقارير، التحليلات |

### ما يجب عليك فعله

| | |
|---|---|
| **ذكر المصدر** | يجب عليك **إلزامياً** ذكر المصدر عند كل استخدام - انظر الأمثلة أدناه |
| **ذكر التغييرات** | إذا عدّلت البيانات، يجب عليك **إلزامياً** ذكر ما تم تغييره |
| **الحفاظ على الترخيص** | أدرج رابط CC BY-NC 4.0 عند التوزيع |

### ذكر المصدر - الصيغة الإلزامية

كل مشروع أو منتج أو منشور أو تطبيق يستخدم بيانات DDC CWICR **يجب** أن يتضمن:

```
DDC CWICR by Artem Boiko / DataDrivenConstruction
https://github.com/datadrivenconstruction/OpenConstructionEstimate-DDC-CWICR
Licensed under CC BY-NC 4.0
```

**أمثلة على ذكر المصدر:**

| أين | كيف |
|-----|-----|
| **README / التوثيق** | `Data source: DDC CWICR by Artem Boiko / DataDrivenConstruction (CC BY-NC 4.0)` |
| **تطبيق ويب (التذييل أو "حول")** | `Construction cost data © Artem Boiko / DataDrivenConstruction - CC BY-NC 4.0` |
| **ورقة علمية** | `Boiko, A. (2025). DDC CWICR - Construction Work Items, Costs & Resources. DataDrivenConstruction.` |
| **تطبيق جوال / سطح مكتب** | شاشة "حول التطبيق": `Data: DDC CWICR by DataDrivenConstruction (CC BY-NC 4.0)` |
| **API / SaaS** | توثيق API: `Powered by DDC CWICR (CC BY-NC 4.0) - datadrivenconstruction.io` |

## دعم المشروع

إذا وجدت هذا مفيداً، يرجى التفكير في الدعم:

[![GitHub Sponsors](https://img.shields.io/badge/رعاية_على-GitHub-ea4aaa?style=for-the-badge&logo=github)](https://github.com/sponsors/datadrivenconstruction)
[![Buy Me A Coffee](https://img.shields.io/badge/Buy_Me_A_Coffee-ffdd00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black)](https://buymeacoffee.com/boikoartem)


<p align="right">
  <br/>
  <b>أطلق قوة البيانات في البناء</b><br/>
  <sub>انتقل إلى إدارة بيانات دورة كاملة حيث تبقى فقط البيانات والعمليات الموحدة المنظمة</sub>
</p>

<p align="right">
  <a href="https://datadrivenconstruction.io">
    <img src="https://datadrivenconstruction.io/wp-content/uploads/2023/07/DataDrivenConstruction-1-1.png.webp" alt="DataDrivenConstruction" width="180">
  </a>
</p>

<p align="right">
  <sub>© 2025 Artem Boiko · <a href="https://datadrivenconstruction.io">datadrivenconstruction.io</a></sub>
</p>

---

## العلامات التجارية

Autodesk® و Revit® و AutoCAD® و DWG™ هي علامات تجارية مسجلة أو علامات تجارية لشركة Autodesk, Inc. OpenAI™ هي علامة تجارية لـ OpenAI, Inc. Qdrant هي علامة تجارية لـ Qdrant Solutions GmbH. جميع أسماء العلامات التجارية الأخرى وأسماء المنتجات أو العلامات التجارية هي ملك لأصحابها.

هذا المشروع غير منتسب أو معتمد أو برعاية Autodesk أو OpenAI أو Qdrant أو أي من مالكي العلامات التجارية المذكورين أعلاه.

</div>
