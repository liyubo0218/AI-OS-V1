from core.brain.providers.response_parser import ResponseParser


def test_response_parser():

    parser = ResponseParser()


    success = parser.parse(
        {
            "text": "hello",
            "model": "test-model",
            "confidence": 0.9
        }
    )

    assert success["status"] == "success"


    invalid = parser.parse(
        None
    )

    assert invalid["status"] == "unavailable"


    missing = parser.parse(
        {
            "model": "test-model"
        }
    )

    assert missing["status"] == "unavailable"


    print(
        "Response Parser PASS"
    )


if __name__ == "__main__":

    test_response_parser()
