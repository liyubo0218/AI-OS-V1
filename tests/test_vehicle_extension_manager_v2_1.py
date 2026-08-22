from core.vehicle_extension.vehicle_manager import (
    VehicleExtensionManager
)

from core.vehicle_extension.permission_manager import (
    VehiclePermissionManager
)


class MockVehicleCapability:

    def execute(
        self,
        action,
        context
    ):
        return "vehicle status ready"



def test_vehicle_extension_manager_v2_1():

    manager = VehicleExtensionManager()

    permission = VehiclePermissionManager()


    permission.grant(
        "vehicle_status_access"
    )


    permission_result = permission.validate(
        "vehicle_status_access"
    )

    assert permission_result["authorized"] is True


    manager.register_capability(
        "vehicle_status",
        MockVehicleCapability()
    )


    response = manager.execute(
        "vehicle_status",
        "query_status",
        {
            "vehicle_id": "vehicle_001"
        }
    )


    assert response["status"] == "completed"

    assert response["result"] == "vehicle status ready"


    print(
        "Vehicle Extension Manager V2.1 PASS"
    )


if __name__ == "__main__":
    test_vehicle_extension_manager_v2_1()
