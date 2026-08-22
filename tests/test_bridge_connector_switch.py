from core.brain.providers.chatgpt.protocol import ChatGPTBridge

from core.brain.providers.chatgpt.config import ChatGPTBridgeConfig

from core.brain.providers.chatgpt.request import ChatGPTRequest



request = ChatGPTRequest(
    "req_001",
    "测试Connector切换"
)



print("Mock Mode:")


mock_bridge = ChatGPTBridge(
    ChatGPTBridgeConfig(
        "mock"
    )
)


print(
    mock_bridge.chat(
        request
    )
)



print("Real Mode:")


real_bridge = ChatGPTBridge(
    ChatGPTBridgeConfig(
        "real"
    )
)


try:

    print(
        real_bridge.chat(
            request
        )
    )

except Exception as e:

    print(
        "Real Connector Status:"
    )

    print(e)
