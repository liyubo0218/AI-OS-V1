from core.workflow_v2 import WorkflowEngine


def test_workflow_v2():


    engine = WorkflowEngine()


    result = engine.create_workflow(
        [
            "step1",
            "step2"
        ]
    )


    assert result["status"] == "created"


    run_result = engine.run()


    assert run_result["status"] == "completed"


    assert run_result["state"] == "completed"


    print(
        "Workflow Engine 2.0 PASS"
    )


if __name__ == "__main__":

    test_workflow_v2()
