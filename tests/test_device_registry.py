from device.identity import DeviceIdentity

from device.registry import DeviceRegistry



registry = DeviceRegistry()



iphone = DeviceIdentity(

    "iphone_001",

    "My iPhone",

    "mobile",

    [
        "camera",
        "location"
    ]

)



mac = DeviceIdentity(

    "mac_001",

    "My Mac",

    "computer",

    [
        "file_access"
    ]

)



iphone.online()



print(
    registry.register(
        iphone
    )
)



print(
    registry.register(
        mac
    )
)



print("Devices:")



print(
    registry.list_devices()
)



print("Camera Devices:")



print(
    [
        d.to_dict()

        for d in registry.find_by_capability(
            "camera"
        )
    ]
)

