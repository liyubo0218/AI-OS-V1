from chatgpt_bridge.protocol import ChatGPTBridge

from chatgpt_bridge.config import ChatGPTBridgeConfig

from chatgpt_bridge.request import ChatGPTRequest



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
