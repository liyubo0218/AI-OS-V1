from core.planner import Planner


def test_planner():

    planner = Planner()


    result = planner.create_plan(
        "提醒我明天开会"
    )


    assert len(
        result["workflow"]["steps"]
    ) > 0


    print(
        "Planner PASS"
    )


if __name__ == "__main__":

    test_planner()
