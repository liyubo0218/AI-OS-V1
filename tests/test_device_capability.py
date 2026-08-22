from core.device_capability import (
    CapabilityManager,
    CapabilityExecutor
)


def test_device_capability():


    manager = CapabilityManager()

    executor = CapabilityExecutor()



    manager.add_capability(
        "camera",
        {
            "type": "image_capture"
        }
    )


    result = manager.enable(
        "camera"
    )


    assert result["status"] == "enabled"



    status = manager.get_status(
        "camera"
    )


    assert status == "enabled"



    execute_result = executor.execute(
        "camera",
        {
            "mode": "photo"
        }
    )


    assert execute_result["status"] == "executed"



    print(
        "Device Capability Layer PASS"
    )


if __name__ == "__main__":

    test_device_capability()
