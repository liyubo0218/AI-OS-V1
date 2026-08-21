from core.workflow.workflow_engine import WorkflowEngine


def test_workflow_engine():

    engine = WorkflowEngine()


    plan = {
        "plan_id":"plan_001",
        "goal":"测试Workflow",
        "steps":[
            {
                "step_id":1,
                "task":"测试步骤",
                "status":"pending"
            }
        ]
    }


    workflow = engine.load_plan(
        plan
    )


    assert (
        workflow["status"]
        == "created"
    )


    started = engine.start_workflow(
        "plan_001"
    )


    assert (
        started["status"]
        == "running"
    )


    step = engine.update_step(
        1,
        "completed"
    )


    assert (
        step["status"]
        == "completed"
    )


    status = engine.get_workflow_status(
        "plan_001"
    )


    assert (
        status["status"]
        == "running"
    )


    print(
        "Workflow Engine PASS"
    )


if __name__ == "__main__":
    test_workflow_engine()
