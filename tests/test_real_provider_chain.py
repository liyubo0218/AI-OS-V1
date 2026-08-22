from core.brain.llm_gateway import LLMGateway
from core.brain.model_router import ModelRouter
from core.brain.providers.real_provider import RealProvider


def test_real_provider_chain():

    provider = RealProvider()

    router = ModelRouter(
        provider
    )

    gateway = LLMGateway(
        router
    )

    result = gateway.generate(
        "测试真实Provider链路"
    )

    assert (
        result["model"]
        ==
        "real-model"
    )

    assert (
        "Real Provider 收到请求"
        in result["response"]
    )

    print(
        "Real Provider Chain PASS"
    )


if __name__ == "__main__":
    test_real_provider_chain()
