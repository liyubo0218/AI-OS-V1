from core.brain.model_router import ModelRouter

from core.brain.llm_gateway import LLMGateway

from core.brain.providers.mock_provider import MockProvider

from core.brain.providers.cloud.cloud_provider import CloudProvider

from core.brain.providers.chatgpt_provider import ChatGPTProvider



router = ModelRouter()


router.register_provider(
    MockProvider()
)


router.register_provider(
    CloudProvider()
)


router.register_provider(
    ChatGPTProvider()
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
    "chatgpt-model"
)


print("ChatGPT Model:")

print(
    gateway.generate(
        "测试ChatGPT Bridge"
    )
)
