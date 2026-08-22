from core.capability.capability_manager import CapabilityManager


class MockCalendarCapability:

    def execute(
        self,
        action,
        parameters
    ):
        return {
            "status": "completed",
            "result": "会议创建完成"
        }


def test_capability_layer_integration_v2():

    manager = CapabilityManager()


    manager.register_capability(
        "calendar",
        MockCalendarCapability()
    )


    task = {
        "capability": "calendar",
        "action": "create_event",
        "parameters": {
            "title": "明天会议"
        }
    }


    result = manager.execute(
        task["capability"],
        task["action"],
        task["parameters"]
    )


    assert result["status"] == "completed"
    assert result["result"] == "会议创建完成"


    print(
        "Capability Layer Integration V2 PASS"
    )


if __name__ == "__main__":
    test_capability_layer_integration_v2()
