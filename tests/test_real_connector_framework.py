from core.runtime.session import ChatGPTSessionManager

from core.brain.providers.chatgpt.mock_connector import MockConnector

from core.brain.providers.chatgpt.request import ChatGPTRequest



session = ChatGPTSessionManager()


result = session.create_session(
    "session_001"
)


print("Session:")

print(result)



connector = MockConnector()


request = ChatGPTRequest(
    "req_001",
    "测试Real Connector Framework"
)


response = connector.send(
    request
)


print("Real Connector Framework Ready")

print(response)
