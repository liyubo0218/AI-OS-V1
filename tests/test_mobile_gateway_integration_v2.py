from core.gateway.mobile_gateway import MobileGateway


class MockiPhoneAgent:

    def execute(
        self,
        user_input
    ):
        return {
            "status": "completed",
            "result": f"已处理:{user_input}"
        }



def test_mobile_gateway_integration_v2():

    gateway = MobileGateway()


    gateway.register_agent(
        "iphone_agent",
        MockiPhoneAgent()
    )


    device_request = {
        "request_id": "device_req_001",
        "device": {
            "device_id": "iphone_001",
            "device_type": "mobile",
            "permission_scope": [
                "assistant"
            ]
        },
        "target": "iphone_agent",
        "input": "准备明天会议"
    }


    response = gateway.handle_request(
        device_request
    )


    assert response["request_id"] == "device_req_001"
    assert response["status"] == "completed"
    assert "准备明天会议" in response["result"]


    print(
        "Mobile Gateway Integration V2 PASS"
    )


if __name__ == "__main__":
    test_mobile_gateway_integration_v2()
