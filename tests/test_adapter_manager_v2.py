from core.adapter.adapter_manager import AdapterManager


class MockCalendarAdapter:

    def execute(
        self,
        action,
        parameters
    ):
        return {
            "status": "completed",
            "result": "会议创建完成"
        }



def test_adapter_manager_v2():

    manager = AdapterManager()


    manager.register_adapter(
        "calendar_adapter",
        MockCalendarAdapter()
    )


    adapters = manager.list_adapters()

    assert "calendar_adapter" in adapters


    result = manager.execute(
        "calendar_adapter",
        "create_event",
        {
            "title": "明天会议"
        }
    )


    assert result["status"] == "completed"
    assert result["result"] == "会议创建完成"


    print(
        "Adapter Manager V2 PASS"
    )


if __name__ == "__main__":
    test_adapter_manager_v2()
