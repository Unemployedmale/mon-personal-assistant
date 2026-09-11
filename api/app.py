from fastapi import FastAPI

app = FastAPI(title="Mon Personal Assistant API")


@app.get("/")
def root():
    return {"status": "ok"}


@app.post("/conflicts/check")
def check_conflict(payload: dict):
    new_start = payload["new_start"]
    new_end = payload["new_end"]
    events = payload.get("events", [])

    conflicts = []

    for event in events:
        if new_start < event["end"] and new_end > event["start"]:
            conflicts.append(event)

    return {
        "conflict": len(conflicts) > 0,
        "conflicts": conflicts,
    }


@app.post("/schedule/free-slots")
def find_free_slots(payload: dict):
    day_start = payload["day_start"]
    day_end = payload["day_end"]
    duration_minutes = payload["duration_minutes"]
    events = sorted(payload.get("events", []), key=lambda x: x["start"])

    slots = []
    current = day_start

    for event in events:
        if event["start"] > current:
            slots.append({
                "start": current,
                "end": event["start"],
            })

        if event["end"] > current:
            current = event["end"]

    if current < day_end:
        slots.append({
            "start": current,
            "end": day_end,
        })

    return {
        "duration_minutes": duration_minutes,
        "free_slots": slots,
    }


@app.post("/analytics/calendar")
def calendar_stats(payload: dict):
    events = payload.get("events", [])

    total_minutes = sum(
        event.get("duration_minutes", 0)
        for event in events
    )

    return {
        "total_events": len(events),
        "total_scheduled_minutes": total_minutes,
        "total_scheduled_hours": round(total_minutes / 60, 2),
    }
