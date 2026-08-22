from core.mobile_extension.mobile_manager import (
    MobileExtensionManager
)

from core.mobile_extension.permission_manager import (
    PermissionManager
)


class MockMobileCapability:

    def execute(
        self,
        action,
        context
    ):
        return "calendar created"


def test_mobile_extension_manager_v2_1():

    manager = MobileExtensionManager()

    permission = PermissionManager()


    permission.grant(
        "calendar_access"
    )


    result = permission.validate(
        "calendar_access"
    )

    assert result["authorized"] is True


    manager.register_capability(
        "mobile_calendar",
        MockMobileCapability()
    )


    response = manager.execute(
        "mobile_calendar",
        "create_event",
        {
            "title": "meeting"
        }
    )


    assert response["status"] == "completed"

    assert response["result"] == "calendar created"


    print(
        "Mobile Extension Manager V2.1 PASS"
    )


if __name__ == "__main__":
    test_mobile_extension_manager_v2_1()
