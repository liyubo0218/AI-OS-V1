from core.brain.providers.chatgpt.protocol import ChatGPTBridge

from core.brain.providers.chatgpt.request import ChatGPTRequest



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
