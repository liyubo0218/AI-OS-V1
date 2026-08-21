from core.gateway.gateway import Gateway


def test_gateway_core():

    gateway = Gateway()


    device = gateway.register_device(
        {
            "device_id":"iphone_001",
            "device_type":"mobile",
            "status":"online"
        }
    )

    assert device["registered"]


    request = gateway.send_request(
        "iphone_001",
        {
            "command":"capture"
        }
    )

    assert (
        request["status"]
        == "sent"
    )


    status = gateway.get_device_status(
        "iphone_001"
    )

    assert (
        status["status"]
        == "online"
    )


    response = gateway.handle_response(
        {
            "request_id":request["request_id"],
            "status":"completed",
            "result":"done"
        }
    )

    assert response["processed"]


    print(
        "Gateway Core PASS"
    )


if __name__ == "__main__":
    test_gateway_core()
