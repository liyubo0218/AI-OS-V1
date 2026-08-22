from core.gateway.mobile_gateway import MobileGateway


class MockAgent:

    def execute(
        self,
        user_input
    ):
        return {
            "status": "completed",
            "result": "会议准备完成"
        }



def test_mobile_gateway_v2():

    gateway = MobileGateway()


    gateway.register_agent(
        "iphone_agent",
        MockAgent()
    )


    request = {
        "request_id": "req_001",
        "device": {
            "device_id": "iphone_001",
            "permission_scope": [
                "calendar"
            ]
        },
        "target": "iphone_agent",
        "input": "准备明天会议"
    }


    response = gateway.handle_request(
        request
    )


    assert response["status"] == "completed"
    assert response["result"] == "会议准备完成"


    print(
        "Mobile Gateway V2 PASS"
    )


if __name__ == "__main__":
    test_mobile_gateway_v2()
