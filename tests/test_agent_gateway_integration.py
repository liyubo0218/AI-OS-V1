from core.agent.agent import Agent
from core.gateway.gateway import Gateway


def test_agent_gateway_integration():

    agent = Agent()
    gateway = Gateway()


    # 1. Register device
    device = gateway.register_device(
        {
            "device_id": "iphone_001",
            "device_type": "mobile",
            "status": "online"
        }
    )

    assert (
        device["registered"]
        is True
    )


    # 2. Agent create task
    task = agent.create_task(
        {
            "action": "capture",
            "parameters": {
                "device_id": "iphone_001"
            }
        }
    )

    assert (
        task["status"]
        == "created"
    )


    # 3. Gateway send request
    request = gateway.send_request(
        "iphone_001",
        {
            "command": "capture"
        }
    )

    assert (
        request["status"]
        == "sent"
    )


    # 4. Device response simulation
    response = gateway.handle_response(
        {
            "request_id": request["request_id"],
            "status": "completed",
            "result": "capture completed"
        }
    )

    assert (
        response["processed"]
        is True
    )


    # 5. Agent execute task
    result = agent.execute_task(
        task["task_id"]
    )

    assert (
        result["status"]
        == "completed"
    )


    print(
        "Agent Gateway Integration PASS"
    )


if __name__ == "__main__":
    test_agent_gateway_integration()
