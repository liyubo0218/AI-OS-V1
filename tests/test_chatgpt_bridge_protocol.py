from chatgpt_bridge.protocol import ChatGPTBridge

from chatgpt_bridge.request import ChatGPTRequest



bridge = ChatGPTBridge()


request = ChatGPTRequest(
    "req_001",
    "帮我测试AI-OS",
    {
        "goal":"test"
    }
)


result = bridge.chat(
    request
)


print("ChatGPT Bridge Protocol Ready")

print(result)
