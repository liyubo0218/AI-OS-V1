from core.brain.providers.mock_provider import MockProvider
from core.brain.model_router import ModelRouter


def test_provider_layer():

    provider = MockProvider()

    result = provider.generate(
        "测试Provider"
    )

    assert result["status"] == "success"

    assert result["model"] == "mock-provider"


    router = ModelRouter(
        provider
    )

    routed = router.route(
        "测试Router"
    )

    assert routed["status"] == "success"


    print("Provider Layer PASS")


if __name__ == "__main__":
    test_provider_layer()
