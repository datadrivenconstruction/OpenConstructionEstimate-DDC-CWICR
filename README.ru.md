<h3 align="center">DDC CWICR - Construction Work Items, Components & Resources </br>
  + Пайплайны n8n для расчёта смет по описаниям, фотографиям и CAD (BIM)</h3>

<p align="center">
  <a href="README.md">🇬🇧 English</a> •
  <a href="README.zh-CN.md">🇨🇳 中文</a> •
  <a href="README.es.md">🇪🇸 Español</a> •
  <a href="README.pt-BR.md">🇧🇷 Português</a> •
  <a href="README.ru.md"><b>🇷🇺 Русский</b></a> •
  <a href="README.ja.md">🇯🇵 日本語</a> •
  <a href="README.de.md">🇩🇪 Deutsch</a> •
  <a href="README.fr.md">🇫🇷 Français</a>
</p>

<p align="center">
  <img src="https://github.com/datadrivenconstruction/cad2data-Revit-IFC-DWG-DGN-pipeline-with-conversion-validation-qto/blob/main/DDC_in_additon/DDC_readme_content/OpenConstructionEstimate.jpg" alt="OpenConstructionEstimate" width="1000">
</p>

<div align="center">
  <img src="https://img.shields.io/badge/Позиций_работ-55,719-2563eb?style=for-the-badge" alt="Work Items">
  <img src="https://img.shields.io/badge/Ресурсов-27,672-059669?style=for-the-badge" alt="Resources">
  <img src="https://img.shields.io/badge/Языков-11-d97706?style=for-the-badge" alt="Languages">
  <img src="https://img.shields.io/badge/Стран-12+-dc2626?style=for-the-badge" alt="Countries">
</div>

<div align="center">
  <img src="https://img.shields.io/badge/Лицензия-CC_BY--NC_4.0-green?style=flat-square" alt="License">
  <img src="https://img.shields.io/badge/Версия-v0.1.1-blue?style=flat-square" alt="Version">
  <img src="https://img.shields.io/badge/Эмбеддинги-OpenAI_3072d-412991?style=flat-square" alt="Embeddings">
  <img src="https://img.shields.io/badge/Векторная_БД-Qdrant-dc382d?style=flat-square" alt="Qdrant">
  <img src="https://img.shields.io/badge/Автоматизация-n8n-ea4b71?style=flat-square" alt="n8n">
</div>

<p align="center">
  <img src="https://github.com/datadrivenconstruction/cad2data-Revit-IFC-DWG-DGN-pipeline-with-conversion-validation-qto/blob/main/DDC_in_additon/DDC_readme_content/OpenConstructionEstimate_bottom.jpg" alt="OpenConstructionEstimate" width="1000">
</p>

<h3 align="center">⚡ n8n Воркфлоу</h3>
<p align="center"><code>Выберите тип ввода → Получите смету</code></p>

<br>

<table width="100%">
<tr>

<td align="center" valign="top" width="33%">
<br>
<h3>📝 Текст</h3>
<p>Быстрый расчёт сметы<br>по краткому описанию</p>
<p><b>Вход:</b> Telegram / сообщение в чате<br>
<b>Выход:</b> Подобранные работы + смета</p>
<br>
<a href="#1️⃣-текстовый-бот-оценщик">📖 Документация</a>
<br><br>
<a href="./n8n_1_Telegram_Bot_Cost_Estimates_and_Rate_Finder_TEXT_DDC_CWICR.json">
<img src="https://img.shields.io/badge/Скачать_воркфлоу-0A84FF?style=for-the-badge&logo=download&logoColor=white" alt="Download"/>
</a>
<br><br>
</td>

<td align="center" valign="top" width="33%">
<br>
<h3>📷 Фото / PDF</h3>
<p>Фото объекта, отсканированные<br>BOQ, PDF с объекта</p>
<p><b>Вход:</b> Изображение или PDF<br>
<b>Выход:</b> Извлечённый объём → смета</p>
<br>
<a href="#2️⃣-фото-оценщик-стоимости">📖 Фото</a> · <a href="#3️⃣-универсальный-бот-текст--фото--pdf">📖 Универсальный бот</a>
<br><br>
<a href="./n8n_2_Photo_Cost_Estimate_DDC_CWICR.json">
<img src="https://img.shields.io/badge/Фото_воркфлоу-0A84FF?style=for-the-badge&logo=download&logoColor=white" alt="Photo"/>
</a>
&nbsp;
<a href="./n8n_3_Telegram_Bot_Cost_Estimates_and_Rate_Finder_TEXT_PHOTO_PDF_DDC_CWICR.json">
<img src="https://img.shields.io/badge/Telegram_Бот-0A84FF?style=for-the-badge&logo=telegram&logoColor=white" alt="Bot"/>
</a>
<br><br>
</td>

<td align="center" valign="top" width="33%">
<br>
<h3>🧊 CAD / BIM</h3>
<p>Расчёт объёмов и смет<br>на основе Revit / IFC / DWG</p>
<p><b>Вход:</b> Экспорт модели<br>
<b>Выход:</b> 4D/5D смета + раскладка</p>
<br>
<a href="#4️⃣-cadbim-пайплайн-оценки-стоимости">📖 Документация</a>
<br><br>
<a href="./n8n_4_CAD_(BIM)_Cost_Estimation_Pipeline_4D_5D_with_DDC_CWICR.json">
<img src="https://img.shields.io/badge/Скачать_воркфлоу-0A84FF?style=for-the-badge&logo=download&logoColor=white" alt="Download"/>
</a>
<br><br>
</td>

</tr>
</table>

<br>
<p align="center">
  <a href="https://openconstructionestimate.com">
    <img src="https://img.shields.io/badge/🌐_ДЕМО_(только_БД)-openconstructionestimate.com-2563eb?style=for-the-badge" alt="Live Demo">
  </a>
</p>
<br>
<p align="center">
 Клиенты и пользователи DataDrivenConstruction
  <br>
  <a href="https://datadrivenconstruction.io/">
  <img src="https://github.com/datadrivenconstruction/cad2data-Revit-IFC-DWG-DGN-pipeline-with-conversion-validation-qto/blob/main/DDC_in_additon/DDC_readme_content/Clients_DataDrivenConstruction_logos.png" width="95%"/>
  </a>
  <br></br>
</p>


---

## 📑 Содержание

### 🤖 AI Интеграция
- [Идеальное топливо для AI](#-идеальное-топливо-для-ваших-ai-продуктов) - Почему эта БД идеальна для AI
- [Claude Code & Google Antigravity](#-claude-code--google-antigravity--ai-ассистенты-программирования) - AI ассистенты
- [n8n](#-n8n--визуальная-автоматизация-воркфлоу) - Автоматизация воркфлоу
- [Универсальные сценарии](#-универсальные-сценарии-использования) - Что можно создать
- [Примеры для разработчиков](#-примеры-для-разработчиков) - Готовый код на нескольких языках

### 📊 База данных и данные
- [О проекте](#о-проекте) - Что такое DDC CWICR
- [Доступные форматы](#доступные-форматы) - Excel, Parquet, CSV, Qdrant
- [Схема данных](#схема-данных) - Структура из 85 полей
- [Группы полей](#группы-полей) - Классификация, Ресурсы, Труд, Механизмы
- [Методология](#методология) - Принципы ресурсного метода
- [Исторический контекст](#исторический-контекст) - 100+ лет стандартов

### ⚡ n8n Воркфлоу
- [Обзор n8n воркфлоу](#-n8n-воркфлоу) - Выберите тип ввода
- [Попробуйте сейчас - Демо боты](#-попробуйте-сейчас--демо-боты) - Тест в Telegram
- [Воркфлоу 1: Текстовый бот](#1️⃣-текстовый-бот-оценщик) - Telegram бот для текста
- [Воркфлоу 2: Фото оценщик](#2️⃣-фото-оценщик-стоимости) - Веб-форма с AI Vision
- [Воркфлоу 3: Универсальный бот](#3️⃣-универсальный-бот-текст--фото--pdf) - Текст + Фото + PDF
- [Воркфлоу 4: CAD/BIM пайплайн](#4️⃣-cadbim-пайплайн-оценки-стоимости) - Revit/IFC/DWG → смета
- [Быстрый старт воркфлоу](#быстрый-старт-воркфлоу) - Настройка за 4 шага
- [Настройка n8n 2.0+](#️-настройка-n8n-20) - Включение Execute Command

### 🏗️ CAD/BIM Пайплайн
- [Требования](#-требования) - Необходимые компоненты
- [Этапы пайплайна](#-этапы-пайплайна) - 10-этапная обработка
- [Выбор LLM модели](#️-выбор-llm-модели) - OpenAI, Claude, Gemini, Grok
- [Выходные файлы](#-выходные-файлы) - HTML и Excel отчёты
- [Устранение неполадок](#️-устранение-неполадок) - Частые проблемы

### 🔍 Векторная база данных
- [Векторная БД](#векторная-база-данных) - Семантический поиск с Qdrant
- [Снапшоты Qdrant](#снапшоты-qdrant-векторной-базы-данных) - Скачать снапшоты
- [Коллекции](#коллекции) - 11 языковых коллекций
- [Docker развёртывание](#docker-развёртывание) - Self-hosted установка

### 🌐 API
- [Pricing Search API](#-pricing-search-api--buildcalculatorio) - Бесплатный REST API для строительных расценок
- [Эндпоинты API](#эндпоинты-api) - Поиск, Языки, Статистика
- [Примеры кода](#примеры-кода-api) - cURL, Python, JavaScript

### 🚀 Начало работы
- [Быстрый старт - Python](#быстрый-старт) - Табличные данные и семантический поиск
- [Сценарии интеграции](#интеграция) - От начального до продвинутого уровня

### 👥 Сообщество
- [Ресурсы и сообщество](#ресурсы-и-сообщество) - Ссылки и каналы
- [Консалтинг и обучение](#консалтинг-и-обучение) - Профессиональные услуги
- [Участие в проекте](#участие-в-проекте) - Отправьте свои воркфлоу
- [Лицензия](#лицензия) - CC BY-NC 4.0
- [Поддержать проект](#поддержать-проект) - Спонсорство и донаты
- [🤖 AI Инструкции](#ai-инструкции) - Документация для AI ассистентов


---

## 🚀 Идеальное топливо для ваших AI продуктов

<p align="center">
  <b>Просто клонируйте репозиторий и опишите что нужно - AI сделает остальное</b>
</p>

DDC CWICR - это не просто база данных, это **готовое топливо для AI-приложений**. Создаёте ли вы ботов для оценки стоимости, автоматизируете строительные процессы или разрабатываете интеллектуальных ассистентов - эти данные работают "из коробки" с современными AI инструментами.

### Почему эта БД идеальна для AI

| Особенность | Преимущество |
|-------------|--------------|
| **Предрассчитанные эмбеддинги** | Не нужно генерировать векторы - семантический поиск работает сразу |
| **Структурированная схема из 85 полей** | AI может рассуждать о связях данных и давать точные ответы |
| **11 языков включено** | Создавайте многоязычные приложения без затрат на перевод |
| **55 000+ позиций работ** | Полное покрытие для любой задачи оценки стоимости |
| **Ресурсный метод** | Прозрачные данные, которые AI может объяснить и разложить |

### 📋 Готовые описания работ для любой системы

<p align="center">
  <img src="https://github.com/datadrivenconstruction/cad2data-Revit-IFC-DWG-DGN-pipeline-with-conversion-validation-qto/blob/main/DDC_in_additon/DDC_readme_content/A%20ready-made%20job%20description%20generator.jpg" alt="Генератор готовых описаний работ" width="1000">
</p>

DDC CWICR предоставляет **полные, структурированные описания работ**, которые можно отобразить в любой системе или формате. Каждая позиция содержит всю информацию, необходимую различным участникам проекта:

| Участник | Что он получает |
|----------|-----------------|
| 🏢 **Заказчик / Инвестор** | Полная прозрачность затрат, расшифровка ресурсов, обоснование цены для инвестиционных решений |
| 📊 **Сметчик** | Детальные расценки, трудозатраты, объёмы материалов, стоимость оборудования - готово для составления смет |
| 👷 **Прораб / Начальник участка** | Состав работ, потребность в ресурсах, нормы труда для ежедневного планирования и выполнения |
| 🔧 **Подрядчик / Исполнитель** | Полные спецификации, единичные расценки, нормативы производительности для точного ценообразования и планирования |

Экспорт в **Excel, PDF, HTML, ERP-системы, BIM-платформы** - структурированная схема из 85 полей обеспечивает целостность данных во всех форматах вывода.

### 🛠️ Отлично работает с

<table>
<tr>
<td align="center" width="20%">
<img src="https://img.shields.io/badge/Claude_Code-000000?style=for-the-badge&logo=anthropic&logoColor=white" alt="Claude Code"/><br/>
<b>Claude Code</b><br/>
<sub>AI ассистент CLI</sub>
</td>
<td align="center" width="20%">
<img src="https://img.shields.io/badge/Google_Antigravity-4285F4?style=for-the-badge&logo=google&logoColor=white" alt="Google Antigravity"/><br/>
<b>Google Antigravity</b><br/>
<sub>Google Antigravity</sub>
</td>
<td align="center" width="20%">
<img src="https://img.shields.io/badge/n8n-EA4B71?style=for-the-badge&logo=n8n&logoColor=white" alt="n8n"/><br/>
<b>n8n</b><br/>
<sub>Автоматизация</sub>
</td>
<td align="center" width="20%">
<img src="https://img.shields.io/badge/Dify-1677FF?style=for-the-badge&logo=openai&logoColor=white" alt="Dify"/><br/>
<b>Dify</b><br/>
<sub>LLM разработка</sub>
</td>
<td align="center" width="20%">
<img src="https://img.shields.io/badge/Sim_AI-6366F1?style=for-the-badge&logo=simpleicons&logoColor=white" alt="Sim AI"/><br/>
<b>Sim AI и другие</b><br/>
<sub>AI платформы</sub>
</td>
</tr>
</table>

---

## 🎯 DDC Skills

**[DDC Skills для ИИ-агентов в строительстве](https://github.com/datadrivenconstruction/DDC_Skills_for_AI_Agents_in_Construction)** - 196 навыков автоматизации с прямой интеграцией в базу данных CWICR. Клонируйте, откройте в ИИ-ассистенте, опишите задачу.

<p align="center">
  <a href="https://github.com/datadrivenconstruction/DDC_Skills_for_AI_Agents_in_Construction">
    <img src="https://img.shields.io/badge/DDC_Skills-196_AI_Automations-blue?style=for-the-badge&logo=robot" alt="DDC Skills">
  </a>
</p>

---

### 💻 Claude Code & Google Antigravity - AI ассистенты программирования

Самый быстрый способ работы с DDC CWICR. Просто откройте репозиторий в Claude Code или Google Antigravity и задавайте вопросы на естественном языке.

**Начало работы:**
```bash
# Клонируйте репозиторий
git clone https://github.com/datadrivenconstruction/OpenConstructionEstimate-DDC-CWICR.git

# Откройте в Claude Code
cd OpenConstructionEstimate-DDC-CWICR
claude
```

**Примеры запросов:**

| Задача | Запрос |
|--------|--------|
| **Исследовать данные** | "Покажи структуру этой строительной БД и объясни какие данные доступны" |
| **Найти работы** | "Найди все работы связанные с бетонными фундаментами и покажи их стоимость" |
| **Создать запросы** | "Напиши Python скрипт для поиска сантехнических работ с трудозатратами > 100 часов" |
| **Сформировать отчёты** | "Сгенерируй отчёт о стоимости работ по ремонту жилых помещений" |
| **Анализ затрат** | "Сравни стоимость материалов для разных методов возведения стен" |
| **Создать интеграции** | "Создай скрипт подключения к Qdrant и семантического поиска" |

**Советы:**
- Указывайте Claude на конкретные файлы: *"Проанализируй Parquet файл и покажи распределение стоимости"*
- Просите объяснения: *"Объясни как работает ресурсный метод калькуляции в этой БД"*
- Запрашивайте модификации: *"Модифицируй n8n воркфлоу добавив email уведомления"*

---

### ⚡ n8n - Визуальная автоматизация воркфлоу

Создавайте мощные пайплайны автоматизации без кода. Подключайте DDC CWICR к 400+ приложениям и сервисам.

**Сценарии использования:**

| Воркфлоу | Описание |
|----------|----------|
| **Telegram Бот** | Пользователь отправляет текст/фото → AI извлекает работы → Возвращает смету |
| **Email автоматизация** | Получение BOQ по email → Обработка AI → Отправка форматированной сметы |
| **CRM Интеграция** | Новый проект в CRM → Авто-генерация предварительной сметы → Обновление суммы сделки |
| **BIM Пайплайн** | Экспорт из Revit → Извлечение объёмов → Сопоставление с DDC расценками → 5D отчёт |
| **Slack Бот** | Команда задаёт вопросы → AI ищет в БД → Возвращает релевантные работы |

**Быстрый старт:**
1. Скачайте JSON воркфлоу из репозитория
2. Импортируйте в n8n: `Workflows → Import → From File`
3. Настройте credentials (OpenAI, Qdrant, Telegram)
4. Активируйте и тестируйте

Подробности в разделе [n8n Воркфлоу](#n8n-воркфлоу--подробное-описание).

---

### 📋 Универсальные сценарии использования

Независимо от выбранного AI инструмента, DDC CWICR позволяет:

| Сценарий | Описание |
|----------|----------|
| **Мгновенная оценка стоимости** | Получите стоимость строительства из текстовых описаний или фото |
| **Генерация BOQ** | Авто-генерация ведомости объёмов из описания проекта |
| **Бенчмаркинг цен** | Сравнение затрат по регионам и языкам |
| **Планирование ресурсов** | Расчёт трудозатрат, материалов и оборудования |
| **Инвестиционный анализ** | Глубокий аудит затрат с полной прозрачностью ресурсов |
| **Многоязычная поддержка** | Обслуживание пользователей на 11 языках с локализованными ценами |
| **BIM Интеграция** | Подключение к Revit/IFC для автоматизированной 4D/5D оценки |
| **Обучение AI моделей** | Использование структурированных данных для fine-tuning AI |

---

## О проекте

**DDC CWICR** (Construction Work Items, Components & Resources) - это открытая база данных для сметного расчёта в строительстве, охватывающая полный спектр строительных работ - от земляных работ и бетонирования до специализированных монтажных работ.

База данных основана на источниках, описывающих современные строительные практики в Евразии и Азиатско-Тихоокеанском регионе, где единая система технической стандартизации служит общим инженерным языком для более чем десяти динамично развивающихся экономик. DDC CWICR представляет собой усилия по гармонизации открытых стандартов путём создания единой нормативной базы для управления капитальными проектами на нескольких языках.

<p align="center">
  <br>
  <img src="https://github.com/datadrivenconstruction/cad2data-Revit-IFC-DWG-DGN-pipeline-with-conversion-validation-qto/blob/main/DDC_in_additon/DDC_readme_content/DDC%20CWICR%20GEOGRAPHIC%20COVERAGE.jpg" width="100%"/>
  <br></br>
</p>

К структурированным данным можно получить доступ через табличные форматы (XLSX, CSV, Parquet) или запрашивать в режиме диалога через LLM, что позволяет специалистам интегрировать описания строительных работ (векторная БД QDRANT) в автоматизированные пайплайны и воркфлоу, используя естественный язык или краткие запросы.

### Доступные форматы

| Формат | Расширение | Размер | Лучше всего для | Особенности |
|--------|------------|--------|-----------------|-------------|
| **Excel** | `.xlsx` | ~150–400 МБ | Ручной анализ, фильтры, сводные | Человекочитаемый, полное форматирование |
| **Parquet** | `.parquet` | ~55 МБ | ETL пайплайны, ML обучение, Big Data | Колоночный, отличное сжатие |
| **CSV** | `.csv` | ~1.3 ГБ | Импорт в БД, legacy системы | Универсальная совместимость |
| **Qdrant** | `.snapshot` | ~1 ГБ | Семантический поиск, RAG, AI ассистенты | Предрассчитанные OpenAI эмбеддинги |


Живое демо доступно на [openconstructionestimate.com](https://openconstructionestimate.com/), где вы можете исследовать данные и увидеть работу векторной БД для семантического поиска.

<p align="center">
  <img src="https://github.com/datadrivenconstruction/cad2data-Revit-IFC-DWG-DGN-pipeline-with-conversion-validation-qto/blob/main/DDC_in_additon/DDC_readme_content/DDC%20CWICR%20Resource-based%20Work%20Cost%20Norms.jpg" alt="OpenConstructionEstimate" width="1000">
</p>

---

## Схема данных

База данных содержит **85 полей**, организованных в логические группы. Каждая запись представляет собой либо позицию работы (расценку), либо ресурс с полной разбивкой стоимости.

```mermaid
erDiagram
    RATE ||--o{ RESOURCE : содержит
    RATE ||--o{ LABOR : требует
    RATE ||--o{ MACHINERY : использует
    RATE ||--o{ PRICE_VARIANT : имеет

    RATE {
        string rate_code PK "Уникальный код"
        string rate_original_name "Название работы"
        string rate_unit "Единица измерения"
        string category_type "Тип категории"
        string collection_name "Сборник"
        string department_name "Раздел"
        string section_name "Подраздел"
        text work_composition_text "Состав работ"
    }

    RESOURCE {
        string resource_code PK "Код ресурса"
        string resource_name "Название ресурса"
        string resource_unit "Единица"
        float resource_quantity "Количество"
        float resource_price_per_unit "Цена за единицу"
        float resource_cost "Стоимость"
        boolean is_material "Материал"
        boolean is_abstract "Абстрактный"
    }

    LABOR {
        string resource_code FK "Код ресурса"
        float labor_hours_workers "Часы рабочих"
        float labor_hours_operators "Часы машинистов"
        int count_workers_per_unit "Рабочих на единицу"
        int count_operators_per_unit "Машинистов"
        float cost_of_working_hours "Стоимость часов"
    }

    MACHINERY {
        string machine_class2_name "Класс техники"
        string machine_class3_name "Подкласс техники"
        float electricity_consumption_kwh "Расход электричества"
        float price_operator_wages "Зарплата машиниста"
        float total_value_machinery "Итого механизмы"
    }

    PRICE_VARIANT {
        float price_est_median "Медиана цены"
        float price_est_min "Мин. цена"
        float price_est_max "Макс. цена"
        int position_count "Кол-во позиций"
        string variable_parts "Вариации"
    }
```

### Группы полей
85 полей базы данных организованы в логические группы, отражающие ресурсный метод оценки стоимости. Каждая группа выполняет конкретную функцию в структуре разбивки затрат: от иерархической классификации и идентификации работ до детального расхода ресурсов, трудозатрат, затрат на механизмы и агрегированных итогов.

<p align="center">
  <br>
  <img src="https://github.com/datadrivenconstruction/cad2data-Revit-IFC-DWG-DGN-pipeline-with-conversion-validation-qto/blob/main/DDC_in_additon/DDC_readme_content/Resource-based%20Work%20Cost%20Norms%20table2.jpg" width="100%"/>
  <br></br>
</p>

**Классификация** - `category_type`, `collection_code`, `collection_name`, `department_code`, `department_name`, `department_type`, `section_name`, `section_type`, `subsection_code`, `subsection_name`

**Позиция работы (Расценка)** - `rate_code`, `rate_original_name`, `rate_final_name`, `rate_unit`, `row_type`, `is_scope`, `is_abstract`, `is_machine`, `is_labor`, `is_material`, `work_composition_text`

**Ресурсы** - `resource_code`, `resource_name`, `resource_unit`, `resource_quantity`, `parameter_resource_quantity`, `resource_price_per_unit_eur_current`, `resource_cost_eur`

**Труд** - `count_workers_per_unit`, `count_engineers_per_unit`, `count_operators_per_unit`, `count_total_people_per_unit`, `labor_hours_construction_workers`, `labor_hours_operators`, `labor_hours_engineers`, `total_labor_hours_workers_operators`, `total_labor_hours_all_personnel`, `cost_of_working_hours`, `count_people_per_day`

**Механизмы** - `machine_class2_name`, `machine_class3_name`, `personnel_operator_code`, `personnel_operator_grade`, `price_operator_wages`, `price_relocation_included`, `price_cost_without_wages`, `electricity_consumption_kwh_per_machine_hour`, `electricity_cost_per_unit`, `electricity_cost_total_sum`, `cost_operator_sum`, `total_value_machinery_equipment`

**Варианты цен** - `price_code_prefix`, `price_abstract_resource_common_start`, `price_abstract_resource_variable_parts`, `price_abstract_resource_position_count`, `price_abstract_resource_est_price_min`, `price_abstract_resource_est_price_max`, `price_abstract_resource_est_price_mean`, `price_abstract_resource_est_price_median`, `price_abstract_resource_unit`, `abstract_resource_tech_group`

**Агрегаты** - `total_cost_per_position`, `total_material_cost_per_position`, `total_resource_cost_per_position`, `total_value_abstract_resources`, `materials_resource_cost_eur`

**Масса и услуги** - `mass_name`, `mass_value`, `mass_unit`, `service_category`, `service_type`, `parameter_service_code`, `parameter_service_unit`, `parameter_service_name`, `parameter_service_quantity`, `service_cost_sum`

### Формула расчёта стоимости

| Компонент | Технологическая норма | × | Региональная цена | = | Стоимость |
|-----------|----------------------|---|-------------------|---|-----------|
| 👷 **Труд** | 172 час/100м² | × | €17.95/час | = | €3,088.11 |
| 🧱 **Материалы** | 632 м²/100м² | × | €5.02/м² | = | €3,170.73 |
| 🚜 **Механизмы** | 1.67 час/100м² | × | €38.42/час | = | €64.18 |
| | | | **Итого** | = | **€7,725.91 за 100м²** |

---

## Методология

Ключевая ценность **Ресурсного метода** - это разделение неизменной производственной технологии от волатильной финансовой составляющей. Он основан на физических "первых принципах" строительства:
- Трудозатраты, необходимые для конкретных работ
- Расход материалов на единицу работы
- Необходимое время работы оборудования

**Почему это важно:**

- **Прозрачность** - Ценообразование без скрытых наценок, полная ресурсная раскладка
- **Аудируемость** - Возможность глубокого анализа для инвестиционной экспертизы
- **Портативность** - Регион-независимые нормы применимы на разных рынках
- **Проверено временем** - Отраслевой стандарт с историей более 100 лет

```mermaid
flowchart TB
    subgraph Source["📦 Источник данных"]
        CWICR[(DDC CWICR<br/>────────────<br/>55,719 Позиций<br/>27,672 Ресурсов<br/>85 Полей)]
    end

    subgraph Processing["⚙️ Пайплайн обработки"]
        direction LR
        ETL[["🔄 ETL"]]
        TRANS[["🌐 Перевод"]]
        EMBED[["🧠 Векторизация"]]
        ETL --> TRANS --> EMBED
    end

    subgraph Outputs["📤 Выходные форматы"]
        XLSX[("📊 Excel")]
        PARQUET[("⚡ Parquet")]
        CSV[("📄 CSV")]
        QDRANT[("🔍 Qdrant")]
    end

    subgraph Apps["🎯 Приложения"]
        SEARCH["🔎 Поиск"]
        BIM["🏗️ BIM 5D"]
        RAG["🤖 RAG"]
        BI["📈 BI"]
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


### Исторический контекст

Описания строительных работ в этой базе данных основаны на ресурсной методологии стандартизации с корнями, уходящими от производственных норм начала 20-го века до современных цифровых справочных систем. Непрерывно развиваясь с 1920-х годов, этот подход получил особенно активное развитие в Евразийском регионе.

Региональные адаптации этой методологии работают под различными национальными обозначениями: ЕНиР, ГЭСН, ФЕР, НРР, ЕСН, AzDTN, ШНК, МКС ЧТ, СНТ, БНбД, Dinh Muc, Ding'e.

<p align="center">
  <img src="https://github.com/datadrivenconstruction/cad2data-Revit-IFC-DWG-DGN-pipeline-with-conversion-validation-qto/blob/main/DDC_in_additon/DDC_readme_content/DDC%20CWICR%20SPREAD%20OF%20METHODOLOGY%20FROM%20THE%201920s.jpg" alt="OpenConstructionEstimate" width="1000">
</p>

⭐ <b>Если вы хотите видеть новые обновления и версии базы данных, поставьте звезду нашим репозиториям.</b>
<p align="center">
  <br>
  <img src="https://github.com/datadrivenconstruction/cad2data-Revit-IFC-DWG-DGN-pipeline-with-conversion-validation-qto/blob/main/DDC_in_additon/DDC_readme_content/OCE%20star%20GitHub.gif" width="100%"/>
  <br></br>
</p>


---


## Интеграция

### Сценарии использования

- **Начальный уровень** - Бенчмаркинг стоимости, Индексация цен, Тендерная оценка

- **Средний уровень** - Локализация, ETL/BI пайплайны, Расчёт CO₂

- **Продвинутый уровень** - AI/ML обучение, CAD (BIM) 5D, Глубокий инвестиционный аудит

---

## n8n Воркфлоу - Подробное описание

Четыре готовых к production воркфлоу для автоматизированной оценки строительной стоимости.

| # | Воркфлоу | Вход | Лучше всего для | Скачать |
|---|----------|------|-----------------|---------|
| 1 | [Текстовый бот](#1️⃣-текстовый-бот-оценщик) | 💬 Текст | Быстрые сметы из текста | [JSON](./n8n_1_Telegram_Bot_Cost_Estimates_and_Rate_Finder_TEXT_DDC_CWICR.json) |
| 2 | [Фото оценщик](#2️⃣-фото-оценщик-стоимости) | 📷 Фото | Осмотры объектов | [JSON](./n8n_2_Photo_Cost_Estimate_DDC_CWICR.json) |
| 3 | [Универсальный бот](#3️⃣-универсальный-бот-текст--фото--pdf) | 💬📷📄 Все | Production использование | [JSON](./n8n_3_Telegram_Bot_Cost_Estimates_and_Rate_Finder_TEXT_PHOTO_PDF_DDC_CWICR.json) |
| 4 | [CAD/BIM пайплайн](#4️⃣-cadbim-пайплайн-оценки-стоимости) | 🏗️ Revit | BIM-based 4D/5D оценка | [JSON](./n8n_4_CAD_(BIM)_Cost_Estimation_Pipeline_4D_5D_with_DDC_CWICR.json) |

---

### 1️⃣ Текстовый бот-оценщик

**Файл:** `n8n_1_Telegram_Bot_Cost_Estimates_and_Rate_Finder_TEXT_DDC_CWICR.json`

Telegram бот для текстовой оценки стоимости. Опишите строительные работы на естественном языке - бот парсит ввод, ищет в векторной БД и возвращает детальную раскладку затрат.

<p align="center">
  <br>
  <img src="https://github.com/datadrivenconstruction/cad2data-Revit-IFC-DWG-DGN-pipeline-with-conversion-validation-qto/blob/main/DDC_in_additon/DDC_readme_content/Text_Estimator_Bot.jpg" width="100%"/>
  <br></br>
</p>

<h3 align="left">🤖 Попробуйте сейчас - Демо боты</h3>
<p><b>@TextOpenConstructionEstimate_bot</b></p>
<p>Создавайте полные сметы из текстовых описаний</p>
<a href="https://t.me/TextOpenConstructionEstimate_bot">
<img src="https://img.shields.io/badge/Открыть_бота-26A5E4?style=for-the-badge&logo=telegram&logoColor=white" alt="Text Bot"/>
</a>

**Как это работает:**

| Шаг | Действие | Технология |
|-----|----------|------------|
| 1 | Пользователь отправляет текстовое описание | Telegram Bot API |
| 2 | AI парсит и извлекает позиции работ | OpenAI / Claude / Gemini |
| 3 | Генерация эмбеддингов для каждой позиции | OpenAI `text-embedding-3-large` |
| 4 | Поиск соответствующих расценок в БД | Qdrant векторный поиск |
| 5 | AI ранжирует результаты для точности | LLM скоринг |
| 6 | Расчёт затрат и генерация отчёта | HTML / Excel / PDF |

**Возможности:**

| Функция | Описание |
|---------|----------|
| 💬 Ввод на естественном языке | Принимает любой формат - списки, предложения, структурированные описания |
| 🤖 Поддержка нескольких LLM | Работает с OpenAI, Claude или Gemini |
| 🔍 Семантический поиск | Находит лучшие совпадения даже при разных формулировках |
| 🌍 11 языков | DE, EN, RU, ES, FR, PT, ZH, AR, HI, US, UK |
| 📊 Несколько форматов экспорта | HTML отчёт, Excel таблица, PDF документ |

---

### 2️⃣ Фото-оценщик стоимости

**Файл:** `n8n_2_Photo_Cost_Estimate_DDC_CWICR.json`

Веб-форма для оценки по фото. Загрузите фото строительного объекта - AI Vision определяет элементы, оценивает размеры и автоматически рассчитывает стоимость.

<p align="center">
  <br>
  <img src="https://github.com/datadrivenconstruction/cad2data-Revit-IFC-DWG-DGN-pipeline-with-conversion-validation-qto/blob/main/DDC_in_additon/DDC_readme_content/n8n%20pipeline%20photo%20estimator.jpg" width="100%"/>
  <br></br>
</p>

**Возможности:**

| Функция | Описание |
|---------|----------|
| 📷 Анализ фото | GPT-4 Vision определяет строительные элементы |
| 📐 Авто-обмеры | Оценка размеров по референсным объектам |
| 🏠 Определение помещения | Санузел, кухня, спальня, экстерьер |
| 🔨 Типы работ | Новое строительство / Ремонт / Реконструкция |
| 🌍 9 региональных БД | Цены локализованы для разных городов |

---

### 3️⃣ Универсальный бот (Текст + Фото + PDF)

**Файл:** `n8n_3_Telegram_Bot_Cost_Estimates_and_Rate_Finder_TEXT_PHOTO_PDF_DDC_CWICR.json`

Полнофункциональный Telegram бот, поддерживающий все типы входных данных.

<p align="center">
  <br>
  <img src="https://github.com/datadrivenconstruction/cad2data-Revit-IFC-DWG-DGN-pipeline-with-conversion-validation-qto/blob/main/DDC_in_additon/DDC_readme_content/Universal%20Estimator%20Bot%20Text%20%20Photo%20PDF.jpg" width="100%"/>
  <br></br>
</p>


**Возможности:**

| Функция | Описание |
|---------|----------|
| 📷 Dual Vision AI | Gemini 2.0 Flash или GPT-4 Vision |
| 📄 PDF обработка | Планировки, отсканированные BOQ |
| 💬 Умный парсинг текста | Списки, таблицы, свободный текст |
| 🔍 AI ранжирование | Улучшает точность сопоставления |
| ✏️ Полное редактирование | Добавление, удаление, изменение позиций |

---

### 4️⃣ CAD (BIM) Пайплайн оценки стоимости

**Файл:** `n8n_4_CAD_(BIM)_Cost_Estimation_Pipeline_4D_5D_with_DDC_CWICR.json`

Автоматизированная оценка стоимости из моделей Revit/IFC/DWG.

<p align="left">
  <a href="https://datadrivenconstruction.io">
    <img src="https://github.com/datadrivenconstruction/cad2data-Revit-IFC-DWG-DGN-pipeline-with-conversion-validation-qto/blob/main/DDC_in_additon/DDC_readme_content/CAD%20(Revit)%20to%205D-4D%20Cost%20and%20Time%20Estimate.jpg" alt="DataDrivenConstruction">
  </a>
</p>

**n8n предоставляет 400+ нативных интеграций**. Каждый узел модульный - вы можете:

- 🔄 **Менять LLM провайдеров** (OpenAI ↔ Claude ↔ Gemini ↔ Grok)
- 📊 **Подключаться к вашей ERP**
- 📁 **Экспортировать результаты куда угодно**
- 🔧 **Модифицировать любой этап**

---

## 📋 Требования

| Компонент | Требование | Описание |
|-----------|------------|----------|
| **[n8n](https://n8n.io/)** | v1.0+ | Платформа автоматизации воркфлоу |
| **[Qdrant](https://qdrant.tech/)** | Cloud или self-hosted | Векторная БД для семантического поиска |
| **[OpenAI API](https://platform.openai.com/)** | Для эмбеддингов | Генерирует векторные эмбеддинги |
| **LLM API** | OpenAI / Claude / Gemini | AI модели для классификации |
| **[DDC Converter](https://github.com/datadrivenconstruction/cad2data-Revit-IFC-DWG-DGN-pipeline-with-conversion-validation-qto)** | `RvtExporter.exe` | Извлекает BIM данные |

---

## Быстрый старт воркфлоу

### Шаг 1: Импорт воркфлоу

```
n8n → New workflow → Import from File → Выберите JSON
```

### Шаг 2: Настройка credentials

В узле **🔑 TOKEN** установите ваши API ключи:

```json
{
  "bot_token": "YOUR_TELEGRAM_BOT_TOKEN",
  "OPENAI_API_KEY": "YOUR_OPENAI_KEY",
  "QDRANT_URL": "http://localhost:6333"
}
```

### Шаг 3: Загрузка DDC CWICR в Qdrant

```bash
curl -X POST "http://localhost:6333/collections/ddc_ru_stpetersburg/snapshots/upload" \
  -H "Content-Type: multipart/form-data" \
  -F "snapshot=@EN___DDC_CWICR/EN_TORONTO_workitems_costs_resources_EMBEDDINGS_3072_DDC_CWICR.snapshot"
```

### Шаг 4: Активация и тест

- Включите воркфлоу в n8n
- Для Telegram ботов: отправьте `/start` вашему боту

---

## ⚠️ Настройка n8n 2.0+

> **Начиная с версии n8n 2.0, узел Execute Command отключён по умолчанию.**

**Windows (CMD):**
```cmd
set NODES_EXCLUDE=[] && npx n8n
```

**Постоянное решение:**
Создайте файл `C:\Users\YOUR_USER\.n8n\.env`:
```
NODES_EXCLUDE=[]
```

---

## 🌍 Поддерживаемые языки

| Код | Язык | Уровень цен | Валюта | Qdrant коллекция |
|-----|------|-------------|--------|------------------|
| `AR` | Арабский | Дубай | AED | `ddc_ar_dubai` |
| `DE` | Немецкий | Берлин | EUR | `ddc_de_berlin` |
| `EN` | Английский | Торонто | CAD | `ddc_en_toronto` |
| `ES` | Испанский | Барселона | EUR | `ddc_sp_barcelona` |
| `FR` | Французский | Париж | EUR | `ddc_fr_paris` |
| `HI` | Хинди | Мумбаи | INR | `ddc_hi_mumbai` |
| `PT` | Португальский | Сан-Паулу | BRL | `ddc_pt_saopaulo` |
| `RU` | Русский | Санкт-Петербург | RUB | `ddc_ru_stpetersburg` |
| `ZH` | Китайский | Шанхай | CNY | `ddc_zh_shanghai` |
| `US`  | Английский | США | USD | `ddc_usa_usd` |
| `UK`  | Английский | Великобритания | GBP | `ddc_uk_gbp` |

---

## 📊 Этапы пайплайна

| Этап | Название | Описание |
|------|----------|----------|
| **0** | Сбор BIM данных | Извлечение элементов из Revit |
| **1** | Определение проекта | AI определяет тип проекта |
| **2** | Генерация фаз | AI создаёт строительные фазы |
| **3** | Назначение элементов | AI сопоставляет BIM типы с фазами |
| **4** | Декомпозиция работ | AI разбивает типы на работы |
| **5** | Векторный поиск | Поиск расценок в DDC CWICR |
| **6** | Маппинг единиц | Конвертация BIM единиц |
| **7** | Расчёт стоимости | Объём × Ед. цена |
| **7.5** | Валидация | Проверка на полноту |
| **8** | Агрегация | Суммирование по фазам |
| **9** | Генерация отчёта | HTML и Excel |

---

## ⚙️ Выбор LLM модели

| Модель | Название узла | Статус |
|--------|---------------|--------|
| OpenAI GPT-4o | `OpenAI LLM` | ✅ По умолчанию |
| Claude Opus 4 | `Anthropic Chat Model2` | Отключено |
| Gemini 2.5 Pro | `Google Gemini Chat Model` | Отключено |
| xAI Grok | `xAI Grok Chat Model1` | Отключено |

---

## 📁 Выходные файлы

```
project_YYYY-MM-DD.html   ← Интерактивный отчёт
project_YYYY-MM-DD.xls    ← Excel таблица
```

<p align="center">
  <img src="https://github.com/datadrivenconstruction/cad2data-Revit-IFC-DWG-DGN-pipeline-with-conversion-validation-qto/blob/main/DDC_in_additon/DDC_readme_content/The%20generated%20report%20includes.jpg" width="100%"/>
</p>

---

## ⚠️ Устранение неполадок

| Проблема | Решение |
|----------|---------|
| "Execute Command missing" | Установите `NODES_EXCLUDE=[]` |
| "No Excel file found" | Проверьте пути |
| "Qdrant connection failed" | Проверьте URL и API key |
| "Rate limit exceeded" | Уменьшите batch size |

---

## Векторная база данных

Готовые к использованию Qdrant коллекции с OpenAI `text-embedding-3-large` эмбеддингами.

### Снапшоты Qdrant векторной базы данных

Снапшоты находятся в соответствующих языковых папках этого репозитория (хранятся через Git LFS).

| Язык | Регион | Снапшот Qdrant |
|------|--------|----------------|
| 🇸🇦 Арабский | Дубай | `AR___DDC_CWICR/AR_DUBAI_workitems_costs_resources_EMBEDDINGS_3072_DDC_CWICR.snapshot` |
| 🇨🇳 Китайский | Шанхай | `ZH___DDC_CWICR/ZH_SHANGHAI_workitems_costs_resources_EMBEDDINGS_3072_DDC_CWICR.snapshot` |
| 🇩🇪 Немецкий | Берлин | `DE___DDC_CWICR/DE_BERLIN_workitems_costs_resources_EMBEDDINGS_3072_DDC_CWICR.snapshot` |
| 🇬🇧 Английский | Торонто | `EN___DDC_CWICR/EN_TORONTO_workitems_costs_resources_EMBEDDINGS_3072_DDC_CWICR.snapshot` |
| 🇪🇸 Испанский | Барселона | `ES___DDC_CWICR/SP_BARCELONA_workitems_costs_resources_EMBEDDINGS_3072_DDC_CWICR.snapshot` |
| 🇫🇷 Французский | Париж | `FR___DDC_CWICR/FR_PARIS_workitems_costs_resources_EMBEDDINGS_3072_DDC_CWICR.snapshot` |
| 🇮🇳 Хинди | Мумбаи | `HI___DDC_CWICR/HI_MUMBAI_workitems_costs_resources_EMBEDDINGS_3072_DDC_CWICR.snapshot` |
| 🇧🇷 Португальский | Сан-Паулу | `PT___DDC_CWICR/PT_SAOPAULO_workitems_costs_resources_EMBEDDINGS_3072_DDC_CWICR.snapshot` |
| 🇷🇺 Русский | Санкт-Петербург | `RU___DDC_CWICR/RU_STPETERSBURG_workitems_costs_resources_EMBEDDINGS_3072_DDC_CWICR.snapshot` |
| 🇬🇧 Английский (UK) | Великобритания (GBP) | `UK___DDC_CWICR/UK_GBP_workitems_costs_resources_EMBEDDINGS_3072_DDC_CWICR.snapshot` |
| 🇺🇸 Английский (US) | США (USD) | `US___DDC_CWICR/USA_USD_workitems_costs_resources_EMBEDDINGS_3072_DDC_CWICR.snapshot` |

### Коллекции

🇸🇦 `ddc_ar_dubai` · 🇨🇳 `ddc_zh_shanghai` · 🇩🇪 `ddc_de_berlin` · 🇬🇧 `ddc_en_toronto` · 🇪🇸 `ddc_sp_barcelona` · 🇫🇷 `ddc_fr_paris` · 🇮🇳 `ddc_hi_mumbai` · 🇧🇷 `ddc_pt_saopaulo` · 🇷🇺 `ddc_ru_stpetersburg` · 🇺🇸 `ddc_usa_usd` (США) · 🇬🇧 `ddc_uk_gbp` (Великобритания)

Каждая коллекция содержит **55,719 векторов**.

### Docker развёртывание

```yaml
services:
  qdrant:
    image: qdrant/qdrant:latest
    container_name: ddc-cwicr-qdrant
    ports:
      - "6333:6333"
    volumes:
      - qdrant_storage:/qdrant/storage
```

```bash
docker-compose up -d

curl -X POST "http://localhost:6333/collections/ddc_ru_stpetersburg/snapshots/upload" \
  -H "Content-Type: multipart/form-data" \
  -F "snapshot=@RU___DDC_CWICR/RU_STPETERSBURG_workitems_costs_resources_EMBEDDINGS_3072_DDC_CWICR.snapshot"
```

---

## 🌐 Pricing Search API - BuildCalculator.io

<p align="center">
  <a href="https://buildcalculator.io/api-docs/">
    <img src="https://img.shields.io/badge/Документация_API-buildcalculator.io-2563eb?style=for-the-badge" alt="API Docs">
  </a>
  &nbsp;
  <img src="https://img.shields.io/badge/Авторизация-Не_требуется-059669?style=for-the-badge" alt="No Auth">
  &nbsp;
  <img src="https://img.shields.io/badge/Стоимость-Бесплатно-059669?style=for-the-badge" alt="Free">
  &nbsp;
  <img src="https://img.shields.io/badge/Лимит-60_зап/мин-d97706?style=for-the-badge" alt="Rate Limit">
</p>

Бесплатный REST API для поиска строительных позиций с полной разбивкой стоимости, трудозатрат, материалов и оборудования. **55 719 позиций** на **11 языках** с **84 полями** на каждую позицию.

**Базовый URL:** `https://buildcalculator.io/api/v1`

### Эндпоинты API

#### `GET/POST /api/v1/search` - Поиск строительных позиций

| Параметр | Тип | По умолчанию | Обязательный | Описание |
|----------|-----|-------------|-------------|----------|
| `q` | string | - | Да | Поисковый запрос (мин. 2 символа). Работает на любом языке |
| `lang` | string | `en` | Нет | Язык базы данных: `en`, `ru`, `de`, `fr`, `es`, `pt`, `zh`, `ar`, `hi` |
| `top` | integer | 5 | Нет | Количество результатов (1–20) |

#### `GET /api/v1/languages` - Список поддерживаемых языков

Возвращает все доступные языки с количеством позиций.

#### `GET /api/v1/stats` - Статистика базы данных

Возвращает количество позиций, категории, языки и метаданные.

### Примеры кода API

**cURL:**
```bash
curl "https://buildcalculator.io/api/v1/search?q=бетонный+фундамент&lang=ru&top=5"
```

**Python:**
```python
import requests

response = requests.get("https://buildcalculator.io/api/v1/search",
    params={"q": "кирпичная кладка стен", "lang": "ru", "top": 5})
data = response.json()

for item in data["results"]:
    print(f"{item['name']} - {item['pricing']['total_per_unit']} EUR/{item['unit']}")
```

**JavaScript:**
```javascript
const res = await fetch(
  "https://buildcalculator.io/api/v1/search?q=бетонные+работы&lang=ru&top=3"
);
const data = await res.json();
```

**Пример ответа:**
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

**Коды ошибок:**

| Код | Значение | Действие |
|-----|----------|----------|
| 400 | Некорректный запрос | Проверьте параметр `q` (мин. 2 символа) |
| 429 | Превышен лимит запросов | Подождите и повторите (60 зап/мин) |
| 500 | Ошибка сервера | Повторите позже или обратитесь в поддержку |

> 📖 Полная документация: [buildcalculator.io/api-docs](https://buildcalculator.io/api-docs/)

---

## Быстрый старт

### Python - Табличные данные

```python
import pandas as pd

df = pd.read_parquet("DDC_CWICR_RU.parquet")
print(f"Записей: {len(df):,} | Полей: {len(df.columns)}")
print(df[['rate_code', 'rate_original_name', 'rate_unit', 'total_cost_per_position']].head())
```

### Python - Семантический поиск

```python
from qdrant_client import QdrantClient
from openai import OpenAI

client = QdrantClient("localhost", port=6333)
openai = OpenAI()

query = "заливка железобетонного фундамента"
embedding = openai.embeddings.create(
    input=query,
    model="text-embedding-3-large"
).data[0].embedding

results = client.search(
    collection_name="ddc_ru_stpetersburg",
    query_vector=embedding,
    limit=5
)

for r in results:
    print(f"[{r.score:.3f}] {r.payload['rate_code']}: {r.payload['rate_original_name']}")
```

---

## 💻 Примеры для разработчиков

Директория [`examples/`](./examples/) содержит **готовый к запуску код** на нескольких языках.

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

**→ [Смотреть все примеры](./examples/)**

---

## Ресурсы и сообщество

[![Сайт](https://img.shields.io/badge/🌐_Сайт-datadrivenconstruction.io-2563eb?style=for-the-badge)](https://datadrivenconstruction.io)
[![Демо](https://img.shields.io/badge/🎯_Демо-openconstructionestimate.com-059669?style=for-the-badge)](https://openconstructionestimate.com)
[![GitHub](https://img.shields.io/badge/💻_GitHub-datadrivenconstruction-181717?style=for-the-badge&logo=github)](https://github.com/datadrivenconstruction)
[![YouTube](https://img.shields.io/badge/📺_YouTube-@datadrivenconstruction-FF0000?style=for-the-badge&logo=youtube)](https://youtube.com/@datadrivenconstruction)
[![LinkedIn](https://img.shields.io/badge/💼_LinkedIn-datadrivenconstruction-0A66C2?style=for-the-badge&logo=linkedin)](https://linkedin.com/company/datadrivenconstruction)
[![Telegram](https://img.shields.io/badge/💬_Telegram-datadrivenconstruction-26A5E4?style=for-the-badge&logo=telegram)](https://t.me/datadrivenconstruction)

### Консалтинг и обучение

Мы работаем с ведущими строительными и технологическими компаниями по всему миру, помогая внедрять принципы открытых данных, автоматизировать обработку CAD/BIM и строить надёжные ETL пайплайны.

<a href="mailto:info@datadrivenconstruction.io">
  <img src="https://img.shields.io/badge/📧_Связаться_с_нами-info@datadrivenconstruction.io-2563eb?style=for-the-badge" alt="Contact">
</a>

### Участие в проекте

DDC CWICR - это бесплатный и открытый проект. Приглашаем присылать ваши открытые воркфлоу, пайплайны и интеграции.

<a href="https://github.com/datadrivenconstruction/cad2data-Revit-IFC-DWG-DGN-pipeline-with-conversion-validation-qto">
  <img src="https://img.shields.io/badge/cad2data_Pipeline-GitHub-181717?style=for-the-badge&logo=github" alt="cad2data Pipeline">
</a>

---

## 🤖 AI Инструкции

Папка `AI_INSTRUCTIONS/` содержит комплексную документацию для AI ассистентов программирования.

### Что такое DDC CWICR?

**DDC CWICR** - открытая база данных строительных расценок:
- **55,719 позиций работ** - детальные строительные операции
- **27,672 ресурса** - материалы, труд, оборудование
- **85 полей данных** - структурированная схема
- **11 языков** - с региональными ценами
- **Предрассчитанные эмбеддинги** - 3072-мерные OpenAI векторы

### Ресурсный метод

```
Фактическая стоимость = Технологическая норма × Региональная цена
```

### Файлы AI-инструкций

| Файл | Назначение |
|------|------------|
| `INSTRUCTIONS.md` | Основной обзор, быстрый старт |
| `CLAUDE.md` | Паттерны для Claude Code |
| `OPENCODE.md` | Инструкции для Opencode |
| `ANTIGRAVITY.md` | Интеграция с GCP |
| `DATABASE_SCHEMA.md` | Полная схема (85 полей) |

### n8n Workflows - Примеры и шаблоны

Включённые n8n воркфлоу - это **примеры и шаблоны**:
- ✅ Использовать как есть
- ✅ Адаптировать под бизнес-требования
- ✅ Изучать методологию
- ✅ Референс для интеграций

### Быстрый старт с AI

1. Откройте проект в IDE с поддержкой AI
2. Спросите: *"Покажи все работы по бетону с их стоимостью"*
3. AI использует инструкции для корректного запроса

**Книга**: [Data-Driven Construction](https://datadrivenconstruction.io/book)

---

## Лицензия - CC BY-NC 4.0

Весь репозиторий лицензирован по [**Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)**](https://creativecommons.org/licenses/by-nc/4.0/).

### Что МОЖНО делать

| | |
|---|---|
| **Коммерческое использование** | Создавайте продукты, SaaS, приложения, API - бесплатно, без запроса разрешения |
| **Копировать и распространять** | Делитесь данными в любом формате |
| **Изменять и адаптировать** | Трансформируйте, дополняйте, создавайте производные работы |
| **Использовать для AI/ML** | Обучение моделей, RAG-пайплайны, эмбеддинги |
| **Использовать в исследованиях** | Научные работы, отчёты, аналитика |

### Что ОБЯЗАТЕЛЬНО нужно делать

| | |
|---|---|
| **Указывать авторство** | Вы **обязаны** указать источник при каждом использовании - см. примеры ниже |
| **Указывать изменения** | Если вы изменили данные, вы **обязаны** указать что было изменено |
| **Сохранять лицензию** | Включайте ссылку на CC BY-NC 4.0 при распространении |

### Указание авторства - обязательный формат

Каждый проект, продукт, публикация или приложение, использующее данные DDC CWICR, **обязаны** включать:

```
DDC CWICR by Artem Boiko / DataDrivenConstruction
https://github.com/datadrivenconstruction/OpenConstructionEstimate-DDC-CWICR
Licensed under CC BY-NC 4.0
```

**Примеры указания авторства:**

| Где | Как |
|-----|-----|
| **README / документация** | `Источник данных: DDC CWICR by Artem Boiko / DataDrivenConstruction (CC BY-NC 4.0)` |
| **Веб-приложение (подвал или "О проекте")** | `Данные о стоимости строительства © Artem Boiko / DataDrivenConstruction - CC BY-NC 4.0` |
| **Научная статья** | `Boiko, A. (2025). DDC CWICR - Construction Work Items, Costs & Resources. DataDrivenConstruction.` |
| **Мобильное / десктопное приложение** | Экран "О приложении": `Данные: DDC CWICR by DataDrivenConstruction (CC BY-NC 4.0)` |
| **API / SaaS** | Документация API: `Данные предоставлены DDC CWICR (CC BY-NC 4.0) - datadrivenconstruction.io` |

## Поддержать проект

[![GitHub Sponsors](https://img.shields.io/badge/Sponsor%20на-GitHub-ea4aaa?style=for-the-badge&logo=github)](https://github.com/sponsors/datadrivenconstruction)
[![Buy Me A Coffee](https://img.shields.io/badge/Buy%20Me%20A%20Coffee-ffdd00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black)](https://buymeacoffee.com/boikoartem)


<p align="left">
  <br/>
  <b>Раскройте силу данных в строительстве</b><br/>
  <sub>Переходите к полноценному управлению данными</sub>
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

## Товарные знаки

Autodesk®, Revit®, AutoCAD® и DWG™ являются зарегистрированными товарными знаками или товарными знаками Autodesk, Inc. OpenAI™ является товарным знаком OpenAI, Inc. Qdrant является товарным знаком Qdrant Solutions GmbH. Все прочие названия брендов, продуктов или товарные знаки принадлежат их соответствующим владельцам.

Данный проект не связан, не одобрен и не спонсируется компаниями Autodesk, OpenAI, Qdrant или любыми другими упомянутыми выше владельцами товарных знаков.
