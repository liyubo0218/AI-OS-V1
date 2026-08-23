from core.system.bootstrap import Bootstrap


def test_task_full_flow():

    system = Bootstrap().create()

    result = system["runtime"].handle(
        "提醒我明天上午9点开会"
    )

    assert result["intent"]["intent"] == "create_task"

    assert result["plan"]["status"] == "planned"

    assert (
        result["task"]["deadline"]
        is not None
    )

    assert (
        result["schedule"]["status"]
        == "pending"
    )

    assert (
        result["execution"]["status"]
        == "success"
    )

    assert (
        result["execution"]["action"]
        == "notification"
    )
