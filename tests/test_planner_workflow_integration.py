from core.planner.planner import Planner
from core.workflow.workflow_engine import WorkflowEngine


def test_planner_workflow_integration():

    planner = Planner()
    workflow = WorkflowEngine()


    plan = planner.create_plan(
        "完成AI-OS任务"
    )


    assert (
        plan["status"]
        == "created"
    )


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


    step = workflow.update_step(
        1,
        "completed"
    )


    assert (
        step["status"]
        == "completed"
    )


    status = workflow.get_workflow_status(
        plan["plan_id"]
    )


    assert (
        status["status"]
        == "running"
    )


    print(
        "Planner Workflow Integration PASS"
    )


if __name__ == "__main__":
    test_planner_workflow_integration()
