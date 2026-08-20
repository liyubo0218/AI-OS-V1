from agents.agent_manager import AgentManager

from agents.demo_agent import DemoAgent

from agents.device_agent import DeviceAgent

from device_gateway.gateway import DeviceGateway

from device_gateway.devices.base_device import BaseDevice



class DemoDevice(BaseDevice):

    def execute(self, command):

        return {
            "device": self.name,
            "command": command,
            "result": "执行成功"
        }



gateway = DeviceGateway()


gateway.register_device(
    DemoDevice(
        "Demo-Mac",
        ["file_access"]
    )
)


manager = AgentManager()


manager.register_agent(
    DemoAgent()
)


manager.register_agent(
    DeviceAgent(
        gateway
    )
)


print("Test Agent:")

print(
    manager.execute_agent(
        "test_task",
        "测试AI-OS"
    )
)


print("Device Agent:")

print(
    manager.execute_agent(
        "device_control",
        {
            "device":"Demo-Mac",
            "command":"file_access"
        }
    )
)
