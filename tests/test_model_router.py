from core.brain.llm_gateway import LLMGateway
from core.brain.model_router import ModelRouter
from core.brain.model_adapter import MockModelAdapter


def test_model_router():

    router = ModelRouter(
        MockModelAdapter()
    )


    gateway = LLMGateway(
        router
    )


    result = gateway.generate(
        "测试Model Router"
    )


    assert result["model"] == "mock-llm"

    assert result["status"] == "success"


    print("Model Router PASS")


if __name__ == "__main__":

    test_model_router()
