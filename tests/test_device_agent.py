from device_gateway.gateway import DeviceGateway

from device_gateway.devices.base_device import BaseDevice

from agents.device_agent import DeviceAgent



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


gateway.register_device(
    device
)


agent = DeviceAgent(
    gateway
)


result = agent.execute(
    {
        "device":"Demo-Mac",
        "command":"file_access"
    }
)


print("Device Agent Ready")

print(result)
