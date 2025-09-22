import os
from backend.app import app

def test_create_and_list(tmp_path, monkeypatch):
    dbfile = tmp_path / "test.db"
    monkeypatch.setenv("DATABASE_URL", f"sqlite:///{dbfile}")
    client = app.test_client()
    r = client.post("/tasks/", json={"title":"test task"})
    assert r.status_code == 201
    r2 = client.get("/tasks/")
    assert r2.status_code == 200
    assert any(t["title"] == "test task" for t in r2.get_json())