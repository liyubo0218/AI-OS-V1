from chatgpt_bridge.session import ChatGPTSessionManager

from chatgpt_bridge.mock_connector import MockConnector

from chatgpt_bridge.request import ChatGPTRequest



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
