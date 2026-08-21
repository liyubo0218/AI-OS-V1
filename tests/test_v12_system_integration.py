from core.agent.agent import Agent
from core.gateway.gateway import Gateway
from core.workflow.workflow_engine import WorkflowEngine
from core.planner.planner import Planner
from core.brain.memory_adapter import MemoryContextAdapter


def test_v12_system_integration():

    # Memory Context
    memory = MemoryContextAdapter()

    context = memory.get_memory_context(
        "AI-OS"
    )

    assert (
        "memory_context"
        in context
    )


    # Planner
    planner = Planner()

    plan = planner.create_plan(
        "完成系统集成测试"
    )

    assert (
        plan["status"]
        == "created"
    )


    # Workflow
    workflow = WorkflowEngine()

    loaded = workflow.load_plan(
        plan
    )

    assert (
        loaded["status"]
        == "created"
    )


    started = workflow.start_workflow(
        plan["plan_id"]
    )

    assert (
        started["status"]
        == "running"
    )


    # Agent
    agent = Agent()

    task = agent.create_task(
        {
            "action":"integration_test",
            "parameters":{}
        }
    )

    assert (
        task["status"]
        == "created"
    )


    result = agent.execute_task(
        task["task_id"]
    )

    assert (
        result["status"]
        == "completed"
    )


    # Gateway
    gateway = Gateway()

    device = gateway.register_device(
        {
            "device_id":"test_device_001",
            "device_type":"simulation",
            "status":"online"
        }
    )

    assert (
        device["registered"]
        is True
    )


    request = gateway.send_request(
        "test_device_001",
        {
            "command":"integration_test"
        }
    )

    assert (
        request["status"]
        == "sent"
    )


    response = gateway.handle_response(
        {
            "request_id":request["request_id"],
            "status":"completed",
            "result":"success"
        }
    )

    assert (
        response["processed"]
        is True
    )


    print(
        "AI-OS V1.2 System Integration PASS"
    )


if __name__ == "__main__":
    test_v12_system_integration()
