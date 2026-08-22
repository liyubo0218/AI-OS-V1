from core.mobile_extension.mobile_manager import (
    MobileExtensionManager
)

from core.mobile_extension.adapter_manager import (
    MobileAdapterManager
)

from core.mobile_extension.permission_manager import (
    PermissionManager
)


class MockMobileAdapter:

    def execute(
        self,
        action,
        payload
    ):
        return {
            "device": "iphone",
            "action": action,
            "result": "notification created"
        }


class MockMobileCapability:

    def __init__(
        self,
        adapter_manager
    ):
        self.adapter_manager = adapter_manager


    def execute(
        self,
        action,
        context
    ):
        return self.adapter_manager.execute(
            "iphone",
            action,
            context
        )


def test_mobile_device_extension_integration_v2_1():

    permission = PermissionManager()

    adapter_manager = MobileAdapterManager()

    mobile_manager = MobileExtensionManager()


    permission.grant(
        "notification_access"
    )


    permission_result = permission.validate(
        "notification_access"
    )

    assert permission_result["authorized"] is True


    adapter_manager.register_adapter(
        "iphone",
        MockMobileAdapter()
    )


    mobile_manager.register_capability(
        "notification",
        MockMobileCapability(
            adapter_manager
        )
    )


    response = mobile_manager.execute(
        "notification",
        "create_notification",
        {
            "title": "Meeting"
        }
    )


    assert response["status"] == "completed"

    assert response["result"]["device"] == "iphone"

    assert response["result"]["result"] == "notification created"


    print(
        "Mobile Device Extension Integration V2.1 PASS"
    )


if __name__ == "__main__":
    test_mobile_device_extension_integration_v2_1()
