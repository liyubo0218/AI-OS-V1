from core.vehicle_extension.vehicle_manager import (
    VehicleExtensionManager
)

from core.vehicle_extension.adapter_manager import (
    VehicleAdapterManager
)

from core.vehicle_extension.permission_manager import (
    VehiclePermissionManager
)


class MockVehicleAdapter:

    def execute(
        self,
        action,
        payload
    ):
        return {
            "vehicle": "vehicle_001",
            "action": action,
            "result": "vehicle status ready"
        }


class MockVehicleCapability:

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
            "mock_vehicle",
            action,
            context
        )


def test_vehicle_adapter_extension_integration_v2_1():

    permission = VehiclePermissionManager()

    adapter_manager = VehicleAdapterManager()

    vehicle_manager = VehicleExtensionManager()


    permission.grant(
        "vehicle_status_access"
    )


    permission_result = permission.validate(
        "vehicle_status_access"
    )

    assert permission_result["authorized"] is True


    adapter_manager.register_adapter(
        "mock_vehicle",
        MockVehicleAdapter()
    )


    vehicle_manager.register_capability(
        "vehicle_status",
        MockVehicleCapability(
            adapter_manager
        )
    )


    response = vehicle_manager.execute(
        "vehicle_status",
        "query_status",
        {
            "vehicle_id": "vehicle_001"
        }
    )


    assert response["status"] == "completed"

    assert response["result"]["vehicle"] == "vehicle_001"

    assert response["result"]["result"] == "vehicle status ready"


    print(
        "Vehicle Adapter Extension Integration V2.1 PASS"
    )


if __name__ == "__main__":
    test_vehicle_adapter_extension_integration_v2_1()
