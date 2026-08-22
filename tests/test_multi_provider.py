from core.brain.model_router import ModelRouter

from core.brain.llm_gateway import LLMGateway

from core.brain.providers.mock_provider import MockProvider

from core.brain.providers.cloud.cloud_provider import CloudProvider


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
