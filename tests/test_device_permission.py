from device.permission import DevicePermissionManager



manager = DevicePermissionManager()



print(
    manager.set_permission(
        "iphone_001",
        "camera",
        True
    )
)



print(
    manager.set_permission(
        "iphone_001",
        "location",
        False
    )
)



print("Camera Permission:")

print(
    manager.check_permission(
        "iphone_001",
        "camera"
    )
)



print("Location Permission:")

print(
    manager.check_permission(
        "iphone_001",
        "location"
    )
)
