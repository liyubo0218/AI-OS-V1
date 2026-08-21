from core.brain.providers.real_provider import RealProvider


def test_real_provider_full_chain():

    provider = RealProvider()

    result = provider.generate(
        "测试RealProvider完整链路"
    )


    assert (
        result["status"]
        ==
        "unavailable"
    )


    assert (
        "text" in result
    )


    assert (
        "model" in result
    )


    assert (
        "confidence" in result
    )


    print(
        "Real Provider Full Chain PASS"
    )


if __name__ == "__main__":

    test_real_provider_full_chain()
