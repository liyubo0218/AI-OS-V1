from ai_gateway.providers.chatgpt_provider import ChatGPTProvider



provider = ChatGPTProvider()



result = provider.generate(
    "帮我测试AI-OS完整ChatGPT Bridge"
)



print("ChatGPT Full Bridge Ready")


print(result)
