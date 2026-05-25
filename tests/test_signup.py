from fastapi.testclient import TestClient
from src.app import app, activities

client = TestClient(app)


def test_duplicate_signup_rejected():
    activity = "Chess Club"
    email = "newstudent@mergington.edu"
    # Ensure fresh state for test
    activities[activity]["participants"] = []

    r1 = client.post(f"/activities/{activity}/signup", params={"email": email})
    assert r1.status_code == 200

    r2 = client.post(f"/activities/{activity}/signup", params={"email": email})
    assert r2.status_code == 400
    assert r2.json().get("detail") == "Student already signed up"
