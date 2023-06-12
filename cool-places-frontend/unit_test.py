import pytest
import httpx
from streamlit_app import app
 

@pytest.mark.asyncio
async def test_frontend():
    async with httpx.AsyncClient(app=app) as client:
        # Make HTTP requests to your Streamlit app and assert the expected responses
        response = await client.get("http://localhost:8501")
        assert response.status_code == 200
        assert "Cool Places App" in response.text
        # Add more assertions as needed
