from core.external_service_extension.service_manager import (
    ExternalServiceManager
)

from core.external_service_extension.adapter_manager import (
    ServiceAdapterManager
)

from core.external_service_extension.permission_manager import (
    ExternalServicePermissionManager
)


class MockExternalService:

    def execute(
        self,
        action,
        context
    ):

        return {
            "service": "calendar",
            "result": "event created"
        }


def test_external_service_extension_manager_v2_2():

    permission = ExternalServicePermissionManager()

    service_manager = ExternalServiceManager()

    adapter_manager = ServiceAdapterManager()


    permission.grant(
        "calendar_access"
    )


    permission_result = permission.validate(
        "calendar_access"
    )


    assert permission_result["authorized"] is True


    adapter_manager.register_adapter(
        "calendar",
        MockExternalService()
    )


    service_manager.register_service(
        "calendar",
        MockExternalService()
    )


    response = service_manager.execute(
        "calendar",
        "create_event",
        {
            "title": "AI-OS Meeting"
        }
    )


    assert response["status"] == "completed"

    assert response["result"]["service"] == "calendar"

    assert response["result"]["result"] == "event created"


    print(
        "External Service Extension Manager V2.2 PASS"
    )


if __name__ == "__main__":
    test_external_service_extension_manager_v2_2()
