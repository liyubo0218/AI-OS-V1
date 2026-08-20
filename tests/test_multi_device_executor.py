from device.identity import DeviceIdentity

from device.registry import DeviceRegistry

from device.permission import DevicePermissionManager

from device.router import DeviceRouter

from device.executor import DeviceExecutor


from device.agents.iphone_agent import IPhoneAgent

from device.agents.mac_agent import MacAgent

from device.agents.car_agent import CarAgent



registry = DeviceRegistry()



iphone = DeviceIdentity(
    "iphone_001",
    "My iPhone",
    "mobile",
    ["camera"]
)

iphone.online()



mac = DeviceIdentity(
    "mac_001",
    "My Mac",
    "computer",
    ["file_access"]
)

mac.online()



car = DeviceIdentity(
    "car_001",
    "XPeng P7",
    "vehicle",
    ["navigation"]
)

car.online()



registry.register(iphone)

registry.register(mac)

registry.register(car)



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



print("Multi Device Executor Ready")



print(
    executor.execute(
        "camera",
        "capture"
    )
)



print(
    executor.execute(
        "file_access",
        "open_file"
    )
)



print(
    executor.execute(
        "navigation",
        "navigate_company"
    )
)

