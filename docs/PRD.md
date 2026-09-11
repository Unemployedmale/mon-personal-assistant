# Product Requirements Document — Mon Personal Assistant

## 1. Product Overview

**Mon Personal Assistant** is a Telegram-first AI personal assistant that helps users manage schedules and daily planning through natural-language conversations.

The system combines:
- Telegram as the user interface
- n8n as the orchestration layer
- OpenAI for natural-language understanding
- Google Calendar for event management
- FastAPI/Python for deterministic scheduling and analytics logic

The goal is to reduce the friction of manually managing calendars and provide proactive planning support.

---

## 2. Problem Statement

Managing personal schedules often requires repeatedly opening calendar apps, checking availability, creating events, rescheduling commitments, and remembering upcoming tasks.

Traditional calendar tools are functional but require manual interaction.

The product aims to provide a conversational assistant that allows users to manage their schedule using natural language while also receiving proactive reminders and planning summaries.

---

## 3. Target User

The primary target user is an individual managing multiple commitments such as:

- work
- university
- personal projects
- appointments
- exercise
- daily tasks

The assistant is designed for users who prefer messaging-based interaction instead of manually navigating calendar interfaces.

---

## 4. Product Goal

Create a reliable personal scheduling assistant that can:

1. Understand natural-language scheduling requests.
2. Perform calendar actions correctly.
3. Provide proactive reminders and summaries.
4. Detect scheduling conflicts.
5. Reduce unnecessary LLM reasoning through deterministic backend logic.
6. Remain simple enough for personal use while being extensible for future features.

---

## 5. V1 Core Features

### Conversational Calendar Management

Users can create, read, update, and delete Google Calendar events through Telegram.

Example:

> "Add gym tomorrow from 7 PM to 8:30 PM."

### Multi-Event Requests

The assistant can create or modify multiple events from a single message.

### Conflict Detection

The system checks for overlapping calendar events and can identify scheduling conflicts.

### Free-Slot Detection

The FastAPI backend can calculate available time blocks based on existing events.

### Daily Brief

A scheduled workflow sends a summary of the user's calendar for the day.

### Event Reminders

The assistant periodically checks for upcoming events and sends Telegram notifications.

### Weekly Planner

The system reviews the upcoming seven days and generates a planning summary including busy periods and available time blocks.

### Calendar Analytics

The Python backend can calculate statistics such as:

- number of scheduled events
- total scheduled minutes
- total scheduled hours

---

## 6. System Architecture

```text
User
 ↓
Telegram
 ↓
n8n
 ↓
OpenAI Agent
 ↓
Google Calendar

n8n
 ↓
FastAPI Backend
 ↓
Python Scheduling / Analytics Logic
