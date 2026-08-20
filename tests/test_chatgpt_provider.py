from ai_gateway.providers.chatgpt_provider import ChatGPTProvider


provider = ChatGPTProvider()


print("ChatGPT Provider Ready")


result = provider.generate(
    "测试AI-OS"
)


print("Model:")

print(
    result["model"]
)


print("Response:")

print(
    result["response"]
)


print("Mode:")

print(
    result["mode"]
)
