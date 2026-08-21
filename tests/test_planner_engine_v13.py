from core.planner.planner_engine import PlannerEngine


def test_planner_engine_v13():

    planner = PlannerEngine()

    result = planner.create_plan(
        "准备明天会议"
    )

    assert result["goal"] == "准备明天会议"

    assert result["tasks"][0]["agent"] == "assistant_agent"

    assert result["status"] == "planned"

    print(
        "Planner Engine V1.3 PASS"
    )


if __name__ == "__main__":
    test_planner_engine_v13()
