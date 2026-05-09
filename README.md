# exec-agent — NAMI

**A personal AI executive assistant built on OpenClaw.**
*Navigator. Strategist. Second Brain.*

---

> *"A good navigator doesn't just know where you are — she knows where you need to be."*

---

## What Is This?

**exec-agent** is a fully configured, production-ready personal AI agent built on [OpenClaw](https://openclaw.ai). The agent is named **NAMI** — after the Straw Hat crew's navigator in One Piece — and is designed to function as a genuine second brain for a builder who runs multiple projects simultaneously.

This is not a demo or a tutorial project. It is a working system built to solve real productivity problems: context loss between sessions, scattered projects, manual tasks that should be automated, and the constant challenge of staying focused when everything demands attention at once.

---

## Built By

**Christian Kusi** — builder, teacher, founder.

- MSc student, Data Analytics for Business & Economics, HSE Saint Petersburg
- Google Certified Workspace Administrator + CEH
- Robotics engineer building [NAKAMA](https://github.com/ChrisKusi) — a social humanoid robot
- STEAM educator — founded a Robotics, IoT & AI Club, mentored 100+ students
- Founder of JCSIS community programs in Saint Petersburg
- Originally from Ghana 🇬🇭 — based in Saint Petersburg, Russia 🇷🇺

---

## What NAMI Does

| Capability | Description |
|---|---|
| 🧭 **Daily Briefing** | Morning summary — schedule, priorities, tasks for the day |
| 📝 **Context Logger** | Captures decisions and working state so nothing is lost between sessions |
| 📂 **Google Workspace** | Reads Drive docs, Gmail, Calendar — surfaces what matters |
| 🔍 **Knowledge Base** | Searches across stored notes, documents and project context |
| 🔄 **Catch-up Briefing** | Answers "where did we leave off?" across all active projects |
| ⚡ **Automation Bridge** | Triggers n8n workflows — social media, notifications, task creation |

---

## Active Projects NAMI Knows About

- **NAKAMA** — Social humanoid robot (Raspberry Pi 5, ROS 2, YOLO11n, Phi-4 Mini)
- **CHOPPER Beta** — Companion desktop robot (ESP32-S3, dual GC9A01 LCD eyes)
- **MSc at HSE** — Data Analytics coursework (ML, business analytics, behavioral economics)
- **GIJ** — Ghana Innovation Journal (Next.js + WordPress headless, Vercel)
- **theinnovationspark.com** — African Editorial Luxury media site
- **AI4SD Ghana** — French Embassy AI initiative site (Next.js, MySQL, EN/FR)
- **TSBH** — The Space Before Help — peer support platform (Firebase, 7-role RBAC)
- **JCSIS** — Community STEAM programs + social media
- **Rhythm Church** — Church website (Next.js, bilingual EN/RU)

---

## Repository Structure

```
exec-agent/
├── soul/
│   ├── SOUL.md            ← NAMI's identity, personality, and context
│   └── AGENTS.md          ← Capabilities, decision rules, skill routing
├── skills/
│   ├── daily-briefing/    ← Morning briefing skill
│   ├── context-logger/    ← Working context capture skill
│   ├── google-workspace/  ← Google Drive/Docs/Gmail/Calendar skill
│   ├── knowledge-base/    ← RAG-based document search skill
│   ├── catch-up/          ← Session context retrieval skill
│   └── n8n-bridge/        ← Automation workflow trigger skill
├── docs/
│   ├── setup.md           ← How to run this yourself
│   ├── architecture.md    ← How it all fits together
│   └── demo/              ← Screenshots and recordings
└── scripts/
    └── start-openclaw.ps1 ← Gateway startup script
```

---

## Tech Stack

- **Agent Framework:** OpenClaw
- **Primary Model:** Gemini 3.1 Flash Lite (via Google AI Studio API)
- **Fallback Model:** Llama 3.3 70B (via Groq API)
- **Local Models:** Ollama (llama3.2, granite3.1-moe, mistral)
- **Integrations:** Google Workspace API, Telegram, n8n
- **Platform:** Windows 11 / Node.js

---

## Milestones

- [x] **M1** — Agent soul, identity, and personality (SOUL.md + AGENTS.md)
- [x] **M2** — Daily briefing skill
- [x] **M3** — Context logger skill
- [x] **M4** — Google Workspace skill
- [ ] **M5** — Knowledge base / RAG skill
- [ ] **M6** — Catch-up briefing skill
- [ ] **M7** — Telegram full integration
- [ ] **M8** — n8n automation bridge

---

## Screenshots

*Coming soon — demos of NAMI in action across all milestones.*

---

## Setup

See [docs/setup.md](docs/setup.md) for full installation and configuration instructions.

---

---

# exec-agent — НАМИ

**Персональный AI-ассистент руководителя на базе OpenClaw.**
*Навигатор. Стратег. Второй мозг.*

---

## Что это такое?

**exec-agent** — полностью настроенный персональный AI-агент на базе [OpenClaw](https://openclaw.ai). Агент называется **НАМИ** — в честь навигатора команды Соломенной Шляпы из One Piece — и создан как настоящий второй мозг для человека, который одновременно ведёт несколько проектов.

Это не демо и не учебный проект. Это рабочая система, созданная для решения реальных задач: потеря контекста между сессиями, распределённые проекты, задачи которые должны быть автоматизированы, и постоянная борьба за фокус когда всё требует внимания одновременно.

---

## Автор

**Кристиан Куси** — разработчик, преподаватель, основатель.

- Студент магистратуры, Аналитика данных для бизнеса и экономики, НИУ ВШЭ Санкт-Петербург
- Сертифицированный Google Workspace Administrator + CEH
- Инженер робототехники — разрабатывает NAKAMA, социального гуманоидного робота
- STEAM-преподаватель — основал клуб робототехники и IoT, обучил 100+ студентов
- Основатель программ сообщества JCSIS в Санкт-Петербурге
- Родом из Ганы 🇬🇭 — живёт в Санкт-Петербурге 🇷🇺

---

## Что умеет НАМИ

| Возможность | Описание |
|---|---|
| 🧭 **Утренний брифинг** | Сводка на день — расписание, приоритеты, задачи |
| 📝 **Журнал контекста** | Фиксирует решения и рабочий контекст между сессиями |
| 📂 **Google Workspace** | Чтение Drive, Gmail, Calendar — подаёт важное |
| 🔍 **База знаний** | Поиск по сохранённым заметкам, документам и проектному контексту |
| 🔄 **Сводка-догонялка** | Отвечает на вопрос «на чём мы остановились?» по всем проектам |
| ⚡ **Мост автоматизации** | Запускает n8n-воркфлоу — соцсети, уведомления, задачи |

---

## Стек технологий

- **Фреймворк агента:** OpenClaw
- **Основная модель:** Gemini 3.1 Flash Lite (Google AI Studio API)
- **Резервная модель:** Llama 3.3 70B (Groq API)
- **Локальные модели:** Ollama (llama3.2, granite3.1-moe, mistral)
- **Интеграции:** Google Workspace API, Telegram, n8n
- **Платформа:** Windows 11 / Node.js

---

## Статус milestones

- [x] **M1** — Душа агента, идентичность и личность (SOUL.md + AGENTS.md)
- [x] **M2** — Навык ежедневного брифинга
- [x] **M3** — Навык журнала контекста
- [x] **M4** — Навык Google Workspace
- [ ] **M5** — База знаний / RAG
- [ ] **M6** — Навык сводки-догонялки
- [ ] **M7** — Полная интеграция с Telegram
- [ ] **M8** — Мост автоматизации n8n

---

*Создано Кристианом Куси — строим инструменты, которые решают настоящие задачи.*