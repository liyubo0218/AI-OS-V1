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



def test_capability_manager_v2():

    manager = CapabilityManager()


    manager.register_capability(
        "calendar",
        MockCalendarCapability()
    )


    capabilities = manager.list_capabilities()

    assert "calendar" in capabilities


    result = manager.execute(
        "calendar",
        "create_event",
        {
            "title": "明天会议"
        }
    )


    assert result["status"] == "completed"
    assert result["result"] == "会议创建完成"


    print(
        "Capability Manager V2 PASS"
    )



if __name__ == "__main__":
    test_capability_manager_v2()
