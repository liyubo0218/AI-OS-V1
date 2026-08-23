from core.system.bootstrap import Bootstrap
from core.mobile.mobile_gateway import MobileGateway
from core.task.executor import TaskExecutor


def test_empty_input():

    system = Bootstrap().create()

    result = system["runtime"].handle(
        ""
    )

    assert result is not None

    assert "input" in result



def test_unknown_input():

    system = Bootstrap().create()

    result = system["runtime"].handle(
        "今天天气不错"
    )

    assert result is not None

    assert result["intent"]["intent"] == "unknown"



def test_executor_without_device():

    gateway = MobileGateway()

    executor = TaskExecutor(
        mobile_gateway=gateway
    )

    result = executor.execute(
        {
            "action": "notification",
            "message": "test"
        }
    )

    assert result["status"] == "success"

    assert (
        result["result"]["status"]
        == "simulation"
    )
