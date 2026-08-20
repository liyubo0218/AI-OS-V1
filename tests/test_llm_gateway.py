from ai_gateway.llm_gateway import LLMGateway


gateway = LLMGateway()


response = gateway.generate(
    "帮我测试AI-OS"
)


print("LLM Gateway V1.1 Ready")

print("Model:")
print(response["model"])

print("Response:")
print(response["response"])
