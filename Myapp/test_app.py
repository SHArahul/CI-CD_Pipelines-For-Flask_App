from app import app

def test_home(monkeypatch):
    # Force ENV to 'test' so response matches test expectation
    monkeypatch.setenv("ENV", "test")
    
    client = app.test_client()
    response = client.get("/")
    
    assert response.status_code == 200
    assert response.data == b"Hello, CI_CD from Flask"