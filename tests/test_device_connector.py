from core.device_connector import ConnectorManager


def test_device_connector():


    manager = ConnectorManager()


    manager.add_device(
        "phone",
        {
            "type": "mobile"
        }
    )


    result = manager.connect(
        "phone"
    )


    assert result["status"] == "connected"


    status = manager.get_status(
        "phone"
    )


    assert status == "connected"


    print(
        "Device Connector Layer PASS"
    )


if __name__ == "__main__":

    test_device_connector()
