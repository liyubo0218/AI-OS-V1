from core.planner.planner import Planner


def test_planner_core():

    planner = Planner()


    plan = planner.create_plan(
        "完成AI-OS测试"
    )


    assert (
        plan["status"]
        == "created"
    )


    plan_id = plan["plan_id"]


    result = planner.get_plan(
        plan_id
    )


    assert (
        result["plan_id"]
        == plan_id
    )


    updated = planner.update_plan_status(
        plan_id,
        "running"
    )


    assert (
        updated["status"]
        == "running"
    )


    failed = planner.create_plan(
        None
    )


    assert (
        failed["status"]
        == "failed"
    )


    print(
        "Planner Core PASS"
    )


if __name__ == "__main__":
    test_planner_core()
