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
        result["status"]
        ==
        "unavailable"
    )


    assert (
        result["model"]
        ==
        "none"
    )


    print(
        "Real Provider Chain PASS"
    )


if __name__ == "__main__":

    test_real_provider_chain()
