from fastapi.testclient import TestClient

from api.server import app


client = TestClient(app)


response = client.post(
    "/chat",
    json={
        "user_input":"帮我测试AI-OS"
    }
)


print("API Server Ready")

print(
    response.json()
)
