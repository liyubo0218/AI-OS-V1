from device.identity import DeviceIdentity

from device.registry import DeviceRegistry

from device.permission import DevicePermissionManager

from device.router import DeviceRouter

from device.executor import DeviceExecutor



class DemoDeviceAgent:


    def execute(
        self,
        command
    ):

        return {

            "command":
            command,

            "result":
            "设备执行成功"

        }



registry = DeviceRegistry()



iphone = DeviceIdentity(

    "iphone_001",

    "My iPhone",

    "mobile",

    [
        "camera"
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



executor = DeviceExecutor(

    router

)



executor.register_agent(

    "iphone_001",

    DemoDeviceAgent()

)



print("Device Execution Router Ready")



print(
    executor.execute(
        "camera",
        "capture"
    )
)

