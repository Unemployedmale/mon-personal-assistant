# Mon Personal Assistant — System Architecture

## 1. Overview

Mon Personal Assistant is an always-on Telegram-first AI scheduling assistant deployed on a Hostinger VPS.

The system separates:

- conversational interaction
- AI reasoning
- workflow orchestration
- external API integrations
- deterministic backend logic
- production hosting

The main design principle is:

> **Use AI for language understanding and deterministic code for calculations and rules.**

---

## 2. Production Architecture

```text
                         User
                          │
                          ▼
                      Telegram
                          │
                          ▼
                 ┌─────────────────┐
                 │  Hostinger VPS  │
                 └────────┬────────┘
                          │
                          ▼
                     ┌────────┐
                     │  n8n   │
                     └───┬────┘
                         │
        ┌────────────────┼────────────────┐
        │                │                │
        ▼                ▼                ▼
   Core Agent       Scheduled        FastAPI
                    Workflows        Backend
        │                │                │
        │        ┌───────┼────────┐       │
        │        │       │        │       │
        │     Daily   Event    Weekly     │
        │     Brief  Reminders  Planner   │
        │                                 │
        ├──────────────┐                  │
        ▼              ▼                  ▼
     OpenAI      Google Calendar    Deterministic
                                   Python Logic
                                   ├── Conflict Detection
                                   ├── Free-Slot Detection
                                   └── Calendar Analytics
```

---

## 3. Component Responsibilities

### Telegram

Telegram acts as the primary conversational user interface.

It allows the user to:

- send natural-language scheduling requests
- receive event confirmations
- receive reminders
- receive daily briefs
- receive weekly planning summaries

---

### n8n

n8n acts as the workflow orchestration layer.

It manages:

- Telegram triggers
- AI agent execution
- tool routing
- Google Calendar operations
- scheduled workflows
- HTTP communication with FastAPI
- Telegram responses

The production n8n instance runs continuously on the Hostinger VPS.

---

### Core Agent

The Core Agent handles interactive Telegram requests.

Supported actions include:

- create calendar events
- retrieve schedules
- update existing events
- delete events
- process multi-event requests
- interpret conversational follow-ups

OpenAI is used primarily for natural-language understanding and tool selection.

---

### Daily Brief Workflow

The Daily Brief workflow runs on a schedule and sends a summary of the user's calendar for the day.

It uses deterministic date handling to reduce date-related hallucinations.

---

### Event Reminder Workflow

The Event Reminder workflow periodically checks for upcoming Google Calendar events.

If an event is approaching, the workflow sends a Telegram reminder.

This workflow can operate without an LLM because the reminder logic is deterministic.

---

### Weekly Planner Workflow

The Weekly Planner reviews upcoming calendar events and creates a concise weekly planning summary.

It can identify:

- key events
- busy days
- lighter days
- useful free blocks
- potential scheduling concerns

---

### OpenAI

OpenAI provides the natural-language understanding layer.

It is responsible for:

- interpreting user intent
- understanding scheduling requests
- selecting appropriate tools
- generating conversational responses

The architecture avoids using the LLM for calculations that can be handled deterministically.

---

### Google Calendar

Google Calendar acts as the system of record for calendar events.

It supports:

- event creation
- event retrieval
- event updates
- event deletion
- schedule lookup

Authentication is handled through Google OAuth 2.0.

---

### FastAPI Backend

FastAPI provides the custom deterministic backend logic.

Current endpoints include:

```text
POST /conflicts/check
POST /schedule/free-slots
POST /analytics/calendar
```

The backend handles:

- scheduling conflict detection
- free-slot calculations
- calendar analytics

This allows calculations to be handled by tested Python logic rather than relying entirely on an LLM.

---

## 4. Deployment Architecture

The production environment runs on a Hostinger VPS using Ubuntu 24.04.

```text
Hostinger VPS
│
├── n8n
│   ├── Core Agent
│   ├── Daily Brief
│   ├── Event Reminders
│   └── Weekly Planner
│
└── FastAPI Backend
    └── systemd service
```

The FastAPI backend runs persistently through `systemd`.

This means:

- the backend starts automatically after a VPS reboot
- the assistant remains available without the local development laptop
- production execution is independent of the local development environment

---

## 5. Development Workflow

VS Code is used as the development environment and is not part of the production runtime.

```text
VS Code
   │
   ▼
Local Project
   │
   ▼
Git
   │
   ▼
GitHub
   │
   ▼
Hostinger VPS
```

Development workflow:

1. Code is written and tested locally in VS Code.
2. Changes are committed with Git.
3. Changes are pushed to GitHub.
4. The VPS can pull updated code from GitHub.
5. The FastAPI service can be restarted or redeployed.

---

## 6. Testing

The FastAPI backend is tested using pytest.

Current automated tests cover:

- calendar analytics
- overlapping event detection
- non-overlapping event detection

Current result:

```text
3 passed
```

Manual end-to-end testing verifies:

- Telegram interaction
- calendar CRUD
- multi-event scheduling
- reminders
- daily briefs
- weekly planning
- n8n-to-FastAPI HTTP communication
- always-on VPS execution

---

## 7. Reliability

Reliability measures include:

- deterministic date handling
- separate backend logic for scheduling calculations
- automated backend tests
- persistent FastAPI service
- GitHub version control
- environment files excluded from Git
- workflow backups stored in the repository

---

## 8. Security

Current security practices include:

- real API secrets are excluded from the repository
- `.env` is ignored by Git
- `.env.example` contains placeholders only
- backend logic is version controlled
- Google Calendar access uses OAuth 2.0

Planned improvement:

- move FastAPI away from the public `:8000` interface
- place the backend behind an internal/private service route or Docker network

---

## 9. Technology Stack

### Production

- Hostinger VPS
- Ubuntu 24.04
- n8n
- OpenAI
- Telegram Bot API
- Google Calendar API
- Google OAuth 2.0
- Python
- FastAPI
- systemd
- Docker

### Development

- VS Code
- Git
- GitHub
- pytest

---

## 10. Current Production Status

- Core Agent: Deployed
- Daily Brief: Deployed
- Event Reminders: Deployed
- Weekly Planner: Deployed
- FastAPI Backend: Active
- FastAPI Service: Persistent through systemd
- Backend Tests: 3 passed
- VPS Hosting: Active
- Local Laptop Dependency: Removed