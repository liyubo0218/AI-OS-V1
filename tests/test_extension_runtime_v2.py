from core.extension_runtime_v2 import (
    ExtensionRegistry,
    LifecycleManager,
    RuntimeStatus,
    PermissionController
)


def test_extension_runtime_v2():


    registry = ExtensionRegistry()

    lifecycle = LifecycleManager()

    status = RuntimeStatus()

    permission = PermissionController()



    registry.register(
        "test_extension",
        {}
    )


    assert registry.get(
        "test_extension"
    ) is not None



    lifecycle.start(
        "test_extension"
    )


    status.update(
        "test_extension",
        "running"
    )


    assert status.get(
        "test_extension"
    ) == "running"



    permission.grant(
        "test_extension",
        "execute"
    )


    assert permission.check(
        "test_extension"
    )


    print(
        "Extension Runtime 2.0 PASS"
    )


if __name__ == "__main__":

    test_extension_runtime_v2()
