from ai_gateway.router import ModelRouter

from ai_gateway.llm_gateway import LLMGateway

from ai_gateway.providers.mock_provider import MockProvider

from ai_gateway.providers.real_provider import RealProvider


router = ModelRouter()


router.register_provider(
    MockProvider()
)

router.register_provider(
    RealProvider()
)


gateway = LLMGateway(
    router
)


print("Default Model:")

print(
    gateway.generate(
        "测试默认模型"
    )
)


router.switch_model(
    "real-model"
)


print("After Switch:")

print(
    gateway.generate(
        "测试真实Provider"
    )
)
