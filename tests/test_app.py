from fastapi.testclient import TestClient

from src.app import app, activities


def test_unregister_participant_removes_them_from_activity():
    client = TestClient(app)
    activity_name = "Chess Club"
    email = "delete-test@mergington.edu"

    try:
        signup_response = client.post(
            f"/activities/{activity_name}/signup",
            params={"email": email},
        )
        assert signup_response.status_code == 200

        unregister_response = client.delete(
            f"/activities/{activity_name}/signup",
            params={"email": email},
        )

        assert unregister_response.status_code == 200
        assert email not in activities[activity_name]["participants"]
    finally:
        if email in activities[activity_name]["participants"]:
            activities[activity_name]["participants"].remove(email)
