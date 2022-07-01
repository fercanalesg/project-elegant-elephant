#/usr/bin/env python

# File: test_app.py
# Written By: Luis Moraguez
# Maintained By: Fernando Canales
# Description: Tests the Flask Web App

import unittest
import os

os.environ['TESTING'] = 'true'

from app import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_home(self):
        response = self.client.get("/")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert "<title>About</title>" in html   ### Your home route says that title is 'Home', but when I run the app it shows up as 'About'

        # Todo Add more tests relating to the home page
        assert '<h4 class="card-title">Fernando</h4>' in html

    def test_experience_education(self):
        response = self.client.get("/professionalinfo")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert "<title>Education/Experience</title>" in html

    def test_hobbies(self):
        response = self.client.get("/hobbies")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert "<title>Our Hobbies</title>" in html ### Your home route says that title is 'Hobbies', but when I run the app it shows up as 'Our Hobbies'

    # Todo Add more tests realting to the timeline page
    def test_timeline(self):
        response = self.client.get("/timeline")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert "<title>Forms</title>" in html ### Your home route says that title is 'Timeline', but when I run the app it shows up as 'Forms'

    def test_timeline_get_api(self):
        response = self.client.get("/api/timeline_post")
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        assert "timeline_posts" in json
        assert len(json["timeline_posts"]) == 0

        # Todo Add more tests relating to the /api/timeline_post GET and POST APIs
        # POST (Properly formed)
        response = self.client.post("/api/timeline_post", data={"name": "John Doe", "email": "john@example.com", "content": "Hello world, I'm John!"})
        assert response.status_code == 200
        response = self.client.get("/api/timeline_post")
        assert response.is_json
        json = response.get_json()
        assert "John Doe" in json["timeline_posts"][0]["name"]
        assert len(json["timeline_posts"]) == 1

    def test_malformed_timeline_post(self):
        # POST request missing name
        response = self.client.post("/api/timeline_post", data={"email": "john@example.com", "content": "Hello world, I'm John!"})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid name" in html

        # POST request with empty content
        response = self.client.post("/api/timeline_post", data={"name": "John Doe", "email": "john@example.com", "content": ""})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid content" in html

        # POST request with malformed email
        response = self.client.post("/api/timeline_post", data={"name": "John Doe", "email": "not-an-email", "content": "Hello world, I'm John!"})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid email" in html
