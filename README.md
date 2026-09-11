## Project Summary

Mon Personal Assistant is a Telegram-first AI scheduling assistant that lets users manage Google Calendar through natural-language conversations.

The system combines n8n, OpenAI, Google Calendar, and a custom FastAPI backend to support:

- calendar create, read, update, and delete operations
- multi-event scheduling
- proactive daily briefs
- event reminders
- weekly planning
- conflict detection
- free-slot calculation
- calendar analytics
- always-on VPS deployment

The production version runs on a Hostinger VPS, allowing the assistant to remain available without the development laptop.

---

## Architecture

```text
User
 ↓
Telegram
 ↓
Hostinger VPS
 ↓
n8n
├── Core Agent
├── Daily Brief
├── Event Reminders
├── Weekly Planner
├── OpenAI
├── Google Calendar
└── FastAPI Backend
    ├── Conflict Detection
    ├── Free-Slot Detection
    └── Calendar Analytics
```

For a detailed technical breakdown, see:

- [`docs/PRD.md`](docs/PRD.md)
- [`docs/architecture.md`](docs/architecture.md)

---

## Key Engineering Decisions

- Used **OpenAI for language understanding**, not deterministic calculations.
- Moved scheduling logic such as conflict detection and free-slot calculation into **FastAPI/Python**.
- Used **n8n** as the orchestration layer between Telegram, OpenAI, Google Calendar, and the backend.
- Added **pytest automated tests** for backend logic.
- Deployed n8n and FastAPI to a **Hostinger VPS** for always-on operation.
- Used **systemd** to keep the FastAPI service persistent across restarts.

---

## Production Status

- Core Agent: Deployed
- Daily Brief: Deployed
- Event Reminders: Deployed
- Weekly Planner: Deployed
- FastAPI Backend: Active
- Backend Tests: 3 passed
- VPS Hosting: Active
- Local Laptop Dependency: Removed