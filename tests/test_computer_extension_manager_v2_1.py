from core.computer_extension.computer_manager import (
    ComputerExtensionManager
)

from core.computer_extension.permission_manager import (
    ComputerPermissionManager
)


class MockComputerCapability:

    def execute(
        self,
        action,
        context
    ):
        return "computer action completed"


def test_computer_extension_manager_v2_1():

    permission = ComputerPermissionManager()

    manager = ComputerExtensionManager()


    permission.grant(
        "file_access"
    )


    result = permission.validate(
        "file_access"
    )

    assert result["authorized"] is True


    manager.register_capability(
        "file",
        MockComputerCapability()
    )


    response = manager.execute(
        "file",
        "read",
        {
            "file": "test.txt"
        }
    )


    assert response["status"] == "completed"

    assert response["result"] == "computer action completed"


    print(
        "Computer Extension Manager V2.1 PASS"
    )


if __name__ == "__main__":
    test_computer_extension_manager_v2_1()
