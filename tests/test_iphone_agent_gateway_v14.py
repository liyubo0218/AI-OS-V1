from core.application.iphone_agent.iphone_agent_gateway import iPhoneAgentGateway


def test_iphone_agent_gateway_v14():

    gateway = iPhoneAgentGateway()

    request = gateway.create_request(
        "帮我准备明天会议"
    )

    assert request["input"] == "帮我准备明天会议"
    assert request["source"] == "iphone_agent"


    response = gateway.handle_response(
        {
            "status": "completed",
            "result": "会议准备完成"
        }
    )

    assert response["status"] == "completed"
    assert response["result"] == "会议准备完成"


    print(
        "iPhone Agent Gateway V1.4 PASS"
    )


if __name__ == "__main__":
    test_iphone_agent_gateway_v14()
