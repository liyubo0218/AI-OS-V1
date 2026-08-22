from gateway.mobile import (
    MobileServer,
    RequestModel
)


class MockRuntime:


    def execute(
        self,
        data
    ):

        return {
            "status": "ok",
            "data": data
        }


def test_gateway():


    server = MobileServer(
        MockRuntime()
    )


    result = server.receive(
        RequestModel(
            "hello"
        )
    )


    assert result["status"] == "ok"


    print(
        "Mobile Gateway PASS"
    )


if __name__ == "__main__":

    test_gateway()
