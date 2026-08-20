from ai_gateway.router import ModelRouter
from ai_gateway.llm_gateway import LLMGateway

from ai_gateway.providers.mock_provider import MockProvider


router = ModelRouter()


router.register_provider(
    MockProvider()
)


gateway = LLMGateway(
    router
)


result = gateway.generate(
    "帮我测试AI-OS"
)


print("LLM Gateway V2 Ready")

print("Selected Model:")

print(result["model"])

print("Response:")

print(result["response"])
