from ai_gateway.router import ModelRouter

from ai_gateway.llm_gateway import LLMGateway

from ai_gateway.providers.mock_provider import MockProvider

from ai_gateway.providers.cloud_provider import CloudProvider


router = ModelRouter()


router.register_provider(
    MockProvider()
)


router.register_provider(
    CloudProvider()
)


gateway = LLMGateway(
    router
)


print("Default Provider:")

print(
    gateway.generate(
        "测试默认模型"
    )
)


router.switch_model(
    "cloud-model"
)


print("Cloud Provider:")

print(
    gateway.generate(
        "测试云模型"
    )
)
