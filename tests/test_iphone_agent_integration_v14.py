from core.application.iphone_agent.iphone_agent_gateway import iPhoneAgentGateway
from core.planner.planner_engine import PlannerEngine
from core.runtime.task_runtime import TaskRuntime
from agents.assistant.personal_assistant_agent import PersonalAssistantAgent


def test_iphone_agent_integration_v14():

    gateway = iPhoneAgentGateway()
    planner = PlannerEngine()
    runtime = TaskRuntime()
    agent = PersonalAssistantAgent()


    request = gateway.create_request(
        "帮我准备明天会议"
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
    assert "帮我准备明天会议" in response["result"]


    print(
        "iPhone Agent Integration V1.4 PASS"
    )


if __name__ == "__main__":
    test_iphone_agent_integration_v14()
