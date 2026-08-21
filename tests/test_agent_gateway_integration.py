from core.agent.agent import Agent
from core.gateway.gateway import Gateway


def test_agent_gateway_integration():

    agent = Agent()
    gateway = Gateway()


    device = gateway.register_device(
        {
            "device_id": "iphone_001",
            "device_type": "mobile",
            "status": "online"
        }
    )

    assert device["registered"] is True


    task = agent.create_task(
        {
            "action": "capture",
            "parameters": {
                "device_id": "iphone_001"
            }
        }
    )

    assert task["status"] == "created"


    request = gateway.send_request(
        "iphone_001",
        {
            "command": "capture"
        }
    )

    assert request["status"] == "sent"


    response = gateway.handle_response(
        {
            "request_id": request["request_id"],
            "status": "completed",
            "result": "capture completed"
        }
    )

    assert response["processed"] is True


    result = agent.execute_task(
        task["task_id"]
    )

    assert result["status"] == "completed"


    print(
        "Agent Gateway Integration PASS"
    )


if __name__ == "__main__":
    test_agent_gateway_integration()
