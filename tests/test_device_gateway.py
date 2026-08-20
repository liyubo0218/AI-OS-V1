from device_gateway.gateway import DeviceGateway

from device_gateway.devices.base_device import BaseDevice



class DemoDevice(BaseDevice):

    def execute(
        self,
        command
    ):

        return {
            "device": self.name,
            "command": command,
            "result": "执行成功"
        }



gateway = DeviceGateway()


device = DemoDevice(
    "Demo-Mac",
    [
        "file_access"
    ]
)


print(
    gateway.register_device(
        device
    )
)


print("Device Gateway Ready")


print(
    gateway.execute_device(
        "Demo-Mac",
        "file_access"
    )
)
