from device.identity import DeviceIdentity

from device.registry import DeviceRegistry

from device.permission import DevicePermissionManager

from device.router import DeviceRouter



registry = DeviceRegistry()


# iPhone

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



# Mac

mac = DeviceIdentity(

    "mac_001",

    "My Mac",

    "computer",

    [
        "file_access"
    ]

)

mac.online()



# Car

car = DeviceIdentity(

    "car_001",

    "XPeng P7",

    "vehicle",

    [
        "navigation"
    ]

)

car.online()



registry.register(
    iphone
)

registry.register(
    mac
)

registry.register(
    car
)



permission = DevicePermissionManager()



permission.set_permission(

    "iphone_001",

    "camera",

    True

)



permission.set_permission(

    "mac_001",

    "file_access",

    True

)



permission.set_permission(

    "car_001",

    "navigation",

    True

)



router = DeviceRouter(

    registry,

    permission

)



print("Multi Device Routing Ready")



print(
    "Camera:"
)

print(
    router.route(
        "camera"
    )
)



print(
    "File:"
)

print(
    router.route(
        "file_access"
    )
)



print(
    "Navigation:"
)

print(
    router.route(
        "navigation"
    )
)

