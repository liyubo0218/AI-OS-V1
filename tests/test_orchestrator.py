from core.orchestrator.orchestrator import Orchestrator


def test_orchestrator_task_flow():

    orchestrator = Orchestrator()

    result = orchestrator.process(
        "提醒我明天上午9点开会"
    )

    assert (
        result["intent"]["intent"]
        == "create_task"
    )

    assert (
        result["plan"]["status"]
        == "planned"
    )


def test_orchestrator_unknown_input():

    orchestrator = Orchestrator()

    result = orchestrator.process(
        "随便聊聊天"
    )

    assert (
        result["intent"]["intent"]
        == "unknown"
    )


def test_orchestrator_result_structure():

    orchestrator = Orchestrator()

    result = orchestrator.process(
        "测试"
    )

    assert "input" in result

    assert "intent" in result

    assert "plan" in result
