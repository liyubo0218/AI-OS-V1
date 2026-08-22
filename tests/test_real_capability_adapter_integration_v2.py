from core.adapter.adapter_manager import AdapterManager


class MockCalendarAdapter:

    def execute(
        self,
        action,
        parameters
    ):
        if action == "create_event":
            return {
                "status": "completed",
                "result": "会议创建完成"
            }

        return {
            "status": "failed",
            "error": "unsupported_action"
        }



def test_real_capability_adapter_integration_v2():

    manager = AdapterManager()


    manager.register_adapter(
        "calendar_adapter",
        MockCalendarAdapter()
    )


    request = {
        "adapter": "calendar_adapter",
        "action": "create_event",
        "parameters": {
            "title": "明天会议"
        }
    }


    response = manager.execute(
        request["adapter"],
        request["action"],
        request["parameters"]
    )


    assert response["status"] == "completed"
    assert response["result"] == "会议创建完成"


    print(
        "Real Capability Adapter Integration V2 PASS"
    )


if __name__ == "__main__":
    test_real_capability_adapter_integration_v2()
