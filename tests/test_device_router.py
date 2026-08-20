from device.identity import DeviceIdentity

from device.registry import DeviceRegistry

from device.permission import DevicePermissionManager

from device.router import DeviceRouter



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



iphone.online()



registry.register(
    iphone
)



permission = DevicePermissionManager()



permission.set_permission(

    "iphone_001",

    "camera",

    True

)



router = DeviceRouter(

    registry,

    permission

)



print("Device Router Ready")



print(

    router.route(
        "camera"
    )

)

