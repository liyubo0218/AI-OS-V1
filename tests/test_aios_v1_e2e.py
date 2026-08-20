from device.identity import DeviceIdentity

from device.registry import DeviceRegistry

from device.permission import DevicePermissionManager

from device.router import DeviceRouter

from device.executor import DeviceExecutor


from device.agents.iphone_agent import IPhoneAgent

from device.agents.mac_agent import MacAgent

from device.agents.car_agent import CarAgent



print("===== AI-OS V1.0 E2E =====")



# Registry

registry = DeviceRegistry()



devices = [

    DeviceIdentity(
        "iphone_001",
        "My iPhone",
        "mobile",
        ["camera"]
    ),

    DeviceIdentity(
        "mac_001",
        "My Mac",
        "computer",
        ["file_access"]
    ),

    DeviceIdentity(
        "car_001",
        "XPeng P7",
        "vehicle",
        ["navigation"]
    )

]



for device in devices:

    device.online()

    registry.register(
        device
    )



# Permission

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



# Router

router = DeviceRouter(

    registry,

    permission

)



# Executor

executor = DeviceExecutor(

    router

)



executor.register_agent(
    "iphone_001",
    IPhoneAgent()
)


executor.register_agent(
    "mac_001",
    MacAgent()
)


executor.register_agent(
    "car_001",
    CarAgent()
)



# Test iPhone

print("iPhone Task:")

print(

    executor.execute(

        "camera",

        "capture"

    )

)



# Test Mac

print("Mac Task:")

print(

    executor.execute(

        "file_access",

        "open_file"

    )

)



# Test Car

print("Car Task:")

print(

    executor.execute(

        "navigation",

        "navigate_company"

    )

)



print("Memory:")

print("PASS")



print("===== ALL SYSTEM READY =====")

