import pytest
from fastapi import status


class TestNoteRoutes:

    # ==================== CREATE ====================

    def test_create_note_success(self, client):
        response = client.post("/notes/", json={
            "title": "Test Note",
            "content": "This is a test content"
        })
        assert response.status_code == status.HTTP_201_CREATED
        data = response.json()
        assert data["title"] == "Test Note"
        assert data["content"] == "This is a test content"
        assert "id" in data
        assert "created_at" in data

    def test_create_note_empty_title(self, client):
        response = client.post("/notes/", json={
            "title": "",
            "content": "Some content"
        })
        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_create_note_short_title(self, client):
        response = client.post("/notes/", json={
            "title": "ab",
            "content": "Some content"
        })
        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_create_note_missing_title(self, client):
        response = client.post("/notes/", json={
            "content": "Only content"
        })
        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

    # ==================== READ (ALL) ====================

    def test_get_all_notes_empty(self, client):
        response = client.get("/notes/")
        assert response.status_code == status.HTTP_200_OK
        assert response.json() == []

    def test_get_all_notes_with_data(self, client):
        client.post("/notes/", json={"title": "Note 1", "content": "Content 1"})
        client.post("/notes/", json={"title": "Note 2", "content": "Content 2"})

        response = client.get("/notes/")
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert len(data) >= 2
        assert data[0]["title"] == "Note 1"
        assert data[1]["title"] == "Note 2"

    # ==================== READ (ONE) ====================

    def test_get_note_by_id_success(self, client):
        create_resp = client.post("/notes/", json={"title": "Get Me", "content": "Find this note"})
        note_id = create_resp.json()["id"]

        response = client.get(f"/notes/{note_id}")
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert data["id"] == note_id
        assert data["title"] == "Get Me"
        assert data["content"] == "Find this note"

    def test_get_note_by_id_not_found(self, client):
        response = client.get("/notes/99999")
        assert response.status_code == status.HTTP_404_NOT_FOUND
        assert response.json()["detail"] == "Note not found"

    # ==================== UPDATE ====================

    def test_update_note_success(self, client):
        create_resp = client.post("/notes/", json={"title": "Old Title", "content": "Old content"})
        note_id = create_resp.json()["id"]

        response = client.put(f"/notes/{note_id}", json={
            "title": "New Title"
        })
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert data["title"] == "New Title"
        assert data["content"] == "Old content"

    def test_update_note_full_update(self, client):
        create_resp = client.post("/notes/", json={"title": "Old", "content": "Old"})
        note_id = create_resp.json()["id"]

        response = client.put(f"/notes/{note_id}", json={
            "title": "New Title",
            "content": "New Content"
        })
        assert response.status_code == status.HTTP_200_OK
        data = response.json()
        assert data["title"] == "New Title"
        assert data["content"] == "New Content"

    def test_update_note_not_found(self, client):
        response = client.put("/notes/99999", json={"title": "New"})
        assert response.status_code == status.HTTP_404_NOT_FOUND

    def test_update_note_short_title(self, client):
        create_resp = client.post("/notes/", json={"title": "Valid", "content": "Content"})
        note_id = create_resp.json()["id"]

        response = client.put(f"/notes/{note_id}", json={"title": "ab"})
        assert response.status_code == status.HTTP_400_BAD_REQUEST

    # ==================== DELETE ====================

    def test_delete_note_success(self, client):
        create_resp = client.post("/notes/", json={"title": "To Delete", "content": "Bye"})
        note_id = create_resp.json()["id"]

        response = client.delete(f"/notes/{note_id}")
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert response.text == ""

        get_resp = client.get(f"/notes/{note_id}")
        assert get_resp.status_code == status.HTTP_404_NOT_FOUND

    def test_delete_note_not_found(self, client):
        response = client.delete("/notes/99999")
        assert response.status_code == status.HTTP_404_NOT_FOUND
        assert response.json()["detail"] == "Note with id 99999 not found"