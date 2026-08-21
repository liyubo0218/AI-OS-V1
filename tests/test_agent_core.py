from core.agent.agent import Agent


def test_agent_core():

    agent = Agent()


    task = agent.create_task(
        {
            "action":"test_action",
            "parameters":{}
        }
    )


    assert (
        task["status"]
        == "created"
    )


    task_id = task["task_id"]


    result = agent.execute_task(
        task_id
    )


    assert (
        result["status"]
        == "completed"
    )


    status = agent.get_task_status(
        task_id
    )


    assert (
        status["status"]
        == "completed"
    )


    output = agent.get_result(
        task_id
    )


    assert (
        output["result"]
        is not None
    )


    print(
        "Agent Core PASS"
    )


if __name__ == "__main__":
    test_agent_core()
