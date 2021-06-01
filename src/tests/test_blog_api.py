### test code goes here
import unittest

from fastapi.testclient import TestClient

from src.main import app, Blog

client = TestClient(app)

class TestBlogApi(unittest.TestCase):

    def test_blog_count_is_zero(self):
        response = client.get('/blog')
        assert response.status_code == 200
        assert response.json() == []

    def test_add_blog_to_array(self):
        new_blog = Blog(title="1", body="These are strings! I hate strings")
        response = client.post('/blog', json=new_blog.dict())

        assert response.status_code == 200
        assert response.json() == {"data": "Blog is created with title as 1"}

        response = client.get('/blog')
        assert response.json() == [new_blog.dict()]
