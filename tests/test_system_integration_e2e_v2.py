from core.runtime.runtime_manager import RuntimeManager
from core.memory_intelligence.memory_manager import (
    MemoryIntelligenceManager
)


class MockGateway:

    def handle_request(self, request):
        return {
            "request_id": "req_001",
            "status": "accepted",
            "request": request
        }


class MockAgent:

    def process(self, request):
        return {
            "task_id": "task_001",
            "goal": request
        }


class MockPlanner:

    def plan(self, task):
        return {
            "agent": "iphone_agent",
            "capability": "calendar"
        }


class MockAdapter:

    def execute(self):
        return {
            "status": "completed",
            "result": "会议创建完成"
        }


class MockGoalMonitor:

    def update(self, task_id, status):
        return {
            "goal_status": status
        }


def test_system_integration_e2e_v2():

    gateway = MockGateway()
    agent = MockAgent()
    planner = MockPlanner()
    adapter = MockAdapter()
    runtime = RuntimeManager()
    memory = MemoryIntelligenceManager()
    goal_monitor = MockGoalMonitor()


    request = gateway.handle_request(
        "准备会议"
    )

    assert request["status"] == "accepted"


    task = agent.process(
        request["request"]
    )


    plan = planner.plan(
        task
    )


    runtime.create_task(
        task["task_id"],
        plan["agent"],
        task["goal"]
    )


    runtime.update_state(
        task["task_id"],
        "executing"
    )


    runtime.update_context(
        task["task_id"],
        {
            "capability": plan["capability"]
        }
    )


    result = adapter.execute()


    runtime.record_result(
        task["task_id"],
        result["result"]
    )


    runtime.update_state(
        task["task_id"],
        "completed"
    )


    memory.write_memory(
        "task_history",
        "meeting_task",
        result["result"],
        "execution_result"
    )


    goal = goal_monitor.update(
        task["task_id"],
        "completed"
    )


    task_state = runtime.get_task(
        task["task_id"]
    )


    assert task_state["state"] == "completed"

    assert task_state["result"] == "会议创建完成"

    assert goal["goal_status"] == "completed"


    print(
        "AI-OS V2 System Integration E2E PASS"
    )


if __name__ == "__main__":
    test_system_integration_e2e_v2()
