from core.mobile.mobile_gateway import MobileGateway
from core.task.executor import TaskExecutor


def test_mobile_gateway_channels():

    gateway = MobileGateway()

    channels = gateway.available_channels()

    assert "shortcut" in channels
    assert "notification" in channels
    assert "device" in channels


def test_executor_mobile_pipeline():

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
        result["action"]
        == "notification"
    )

    assert (
        result["result"]["channel"]
        == "device"
    )
