from ai_gateway.router import ModelRouter

from ai_gateway.llm_gateway import LLMGateway

from ai_gateway.providers.mock_provider import MockProvider

from ai_gateway.providers.cloud_provider import CloudProvider

from ai_gateway.providers.chatgpt_provider import ChatGPTProvider



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
