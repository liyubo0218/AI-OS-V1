from core.runtime.runtime_manager import RuntimeManager


class MockPlanner:

    def create_plan(self):
        return {
            "task_id": "task_001",
            "agent": "iphone_agent",
            "capability": "calendar"
        }


class MockAgent:

    def execute(self, task):
        return {
            "status": "completed",
            "result": "会议创建完成"
        }


def test_runtime_orchestration_integration_v2():

    runtime = RuntimeManager()

    planner = MockPlanner()

    agent = MockAgent()


    plan = planner.create_plan()


    created = runtime.create_task(
        plan["task_id"],
        plan["agent"],
        "准备会议"
    )

    assert created["status"] == "created"


    runtime.update_state(
        plan["task_id"],
        "executing"
    )


    runtime.update_context(
        plan["task_id"],
        {
            "agent": plan["agent"],
            "capability": plan["capability"]
        }
    )


    result = agent.execute(
        plan
    )


    runtime.record_result(
        plan["task_id"],
        result["result"]
    )


    runtime.update_state(
        plan["task_id"],
        "completed"
    )


    task = runtime.get_task(
        plan["task_id"]
    )


    assert task["state"] == "completed"

    assert task["result"] == "会议创建完成"

    assert task["context"]["capability"] == "calendar"


    print(
        "Runtime Orchestration Integration V2 PASS"
    )


if __name__ == "__main__":
    test_runtime_orchestration_integration_v2()
