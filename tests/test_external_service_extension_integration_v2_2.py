from core.external_service_extension.service_manager import (
    ExternalServiceManager
)

from core.external_service_extension.adapter_manager import (
    ServiceAdapterManager
)

from core.external_service_extension.permission_manager import (
    ExternalServicePermissionManager
)


class MockCalendarAdapter:

    def execute(
        self,
        action,
        payload
    ):

        return {
            "service": "calendar",
            "result": "event created"
        }


class MockCalendarCapability:

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
            "calendar",
            action,
            context
        )


def test_external_service_extension_integration_v2_2():

    permission = ExternalServicePermissionManager()

    adapter_manager = ServiceAdapterManager()

    service_manager = ExternalServiceManager()


    permission.grant(
        "calendar_access"
    )


    permission_result = permission.validate(
        "calendar_access"
    )


    assert permission_result["authorized"] is True


    adapter_manager.register_adapter(
        "calendar",
        MockCalendarAdapter()
    )


    service_manager.register_service(
        "calendar",
        MockCalendarCapability(
            adapter_manager
        )
    )


    response = service_manager.execute(
        "calendar",
        "create_event",
        {
            "title": "AI-OS Event"
        }
    )


    assert response["status"] == "completed"

    assert response["result"]["service"] == "calendar"

    assert response["result"]["result"] == "event created"


    print(
        "External Service Extension Integration V2.2 PASS"
    )


if __name__ == "__main__":
    test_external_service_extension_integration_v2_2()
