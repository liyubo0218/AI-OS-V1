from core.application.mac_agent.mac_agent_gateway import MacAgentGateway
from core.planner.planner_engine import PlannerEngine
from core.runtime.task_runtime import TaskRuntime
from agents.assistant.personal_assistant_agent import PersonalAssistantAgent


def test_mac_agent_integration_v14():

    gateway = MacAgentGateway()
    planner = PlannerEngine()
    runtime = TaskRuntime()
    agent = PersonalAssistantAgent()


    request = gateway.create_request(
        "整理桌面文件"
    )


    plan = planner.create_plan(
        request["input"]
    )


    task = runtime.create_task(
        plan["goal"]
    )


    execution = agent.execute(
        task["goal"]
    )


    response = gateway.handle_response(
        {
            "status": execution["status"],
            "result": execution["result"]
        }
    )


    assert response["status"] == "completed"
    assert "整理桌面文件" in response["result"]

    print(
        "Mac Agent Integration V1.4 PASS"
    )


if __name__ == "__main__":
    test_mac_agent_integration_v14()
