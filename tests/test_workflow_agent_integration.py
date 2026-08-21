from core.planner.planner import Planner
from core.workflow.workflow_engine import WorkflowEngine
from core.agent.agent import Agent


def test_workflow_agent_integration():

    planner = Planner()
    workflow = WorkflowEngine()
    agent = Agent()


    # 1. Planner create plan
    plan = planner.create_plan(
        "执行测试任务"
    )

    assert (
        plan["status"]
        == "created"
    )


    # 2. Workflow load plan
    wf = workflow.load_plan(
        plan
    )

    assert (
        wf["status"]
        == "created"
    )


    # 3. Start workflow
    started = workflow.start_workflow(
        plan["plan_id"]
    )

    assert (
        started["status"]
        == "running"
    )


    # 4. Agent create task
    task = agent.create_task(
        {
            "action": "test_execution",
            "parameters": {}
        }
    )

    assert (
        task["status"]
        == "created"
    )


    # 5. Agent execute
    result = agent.execute_task(
        task["task_id"]
    )

    assert (
        result["status"]
        == "completed"
    )


    print(
        "Workflow Agent Integration PASS"
    )


if __name__ == "__main__":
    test_workflow_agent_integration()
