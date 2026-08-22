from core.application.mac_agent.mac_agent_gateway import MacAgentGateway


def test_mac_agent_gateway_v14():

    gateway = MacAgentGateway()

    request = gateway.create_request(
        "整理桌面文件"
    )

    assert request["input"] == "整理桌面文件"
    assert request["source"] == "mac_agent"


    capability = gateway.provide_capability()

    assert "file_operation" in capability["capability"]


    response = gateway.handle_response(
        {
            "status": "completed",
            "result": "文件整理完成"
        }
    )

    assert response["status"] == "completed"
    assert response["result"] == "文件整理完成"


    print(
        "Mac Agent Gateway V1.4 PASS"
    )


if __name__ == "__main__":
    test_mac_agent_gateway_v14()
