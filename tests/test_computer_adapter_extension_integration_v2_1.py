from core.computer_extension.computer_manager import (
    ComputerExtensionManager
)

from core.computer_extension.adapter_manager import (
    ComputerAdapterManager
)

from core.computer_extension.permission_manager import (
    ComputerPermissionManager
)


class MockComputerAdapter:

    def execute(
        self,
        action,
        payload
    ):

        return {
            "device": "computer_001",
            "action": action,
            "result": "file operation completed"
        }


class MockComputerCapability:

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
            "mock_computer",
            action,
            context
        )


def test_computer_adapter_extension_integration_v2_1():

    permission = ComputerPermissionManager()

    adapter_manager = ComputerAdapterManager()

    computer_manager = ComputerExtensionManager()


    permission.grant(
        "file_access"
    )


    permission_result = permission.validate(
        "file_access"
    )

    assert permission_result["authorized"] is True


    adapter_manager.register_adapter(
        "mock_computer",
        MockComputerAdapter()
    )


    computer_manager.register_capability(
        "file",
        MockComputerCapability(
            adapter_manager
        )
    )


    response = computer_manager.execute(
        "file",
        "read_file",
        {
            "file": "test.txt"
        }
    )


    assert response["status"] == "completed"

    assert response["result"]["device"] == "computer_001"

    assert response["result"]["result"] == "file operation completed"


    print(
        "Computer Adapter Extension Integration V2.1 PASS"
    )


if __name__ == "__main__":
    test_computer_adapter_extension_integration_v2_1()
