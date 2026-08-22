from core.application.vehicle_agent.vehicle_agent_gateway import VehicleAgentGateway
from core.planner.planner_engine import PlannerEngine
from core.runtime.task_runtime import TaskRuntime
from agents.assistant.personal_assistant_agent import PersonalAssistantAgent


def test_vehicle_agent_integration_v2():

    gateway = VehicleAgentGateway()

    planner = PlannerEngine()

    runtime = TaskRuntime()

    agent = PersonalAssistantAgent()


    request = gateway.create_request(
        "打开空调"
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
    assert "打开空调" in response["result"]

    print(
        "Vehicle Agent Integration V2 PASS"
    )


if __name__ == "__main__":
    test_vehicle_agent_integration_v2()
