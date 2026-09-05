from fastapi.testclient import TestClient
from api.app import app
client = TestClient(app)


def test_calendar_analytics():
    response = client.post(
        "/analytics/calendar",
        json={
            "events": [
                {"duration_minutes": 60},
                {"duration_minutes": 90},
            ]
        },
    )

    assert response.status_code == 200
    assert response.json()["total_events"] == 2
    assert response.json()["total_scheduled_minutes"] == 150
    assert response.json()["total_scheduled_hours"] == 2.5


def test_conflict_detected():
    response = client.post(
        "/conflicts/check",
        json={
            "new_start": "19:30",
            "new_end": "20:30",
            "events": [
                {
                    "start": "19:00",
                    "end": "20:00",
                }
            ],
        },
    )

    assert response.status_code == 200
    assert response.json()["conflict"] is True


def test_no_conflict():
    response = client.post(
        "/conflicts/check",
        json={
            "new_start": "20:30",
            "new_end": "21:30",
            "events": [
                {
                    "start": "19:00",
                    "end": "20:00",
                }
            ],
        },
    )

    assert response.status_code == 200
    assert response.json()["conflict"] is False