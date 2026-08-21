from core.brain.providers.connection_client import ConnectionClient
from core.brain.providers.api_client import APIClient


def test_connection_error_handling():

    client = ConnectionClient()

    result = client.request(
        {
            "prompt": "测试错误处理"
        }
    )

    assert (
        result["status"]
        ==
        "unavailable"
    )


    api_client = APIClient()

    response = api_client.request(
        "测试API错误处理"
    )

    assert (
        response["status"]
        ==
        "unavailable"
    )


    print(
        "Connection Error Handling PASS"
    )


if __name__ == "__main__":

    test_connection_error_handling()
