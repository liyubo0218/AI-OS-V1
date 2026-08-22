from core.brain.model_router import ModelRouter
from core.brain.llm_gateway import LLMGateway

from core.brain.providers.mock_provider import MockProvider


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
