from core.agent.task_adapter import ChatGPTTaskAdapter


from device.identity import DeviceIdentity

from device.registry import DeviceRegistry

from device.permission import DevicePermissionManager

from device.router import DeviceRouter

from device.executor import DeviceExecutor


from device.agents.iphone_agent import IPhoneAgent



print("ChatGPT Device Workflow Ready")



# ChatGPT Task Adapter

adapter = ChatGPTTaskAdapter()



task = adapter.convert(

    "帮我拍一张照片"

)



print("Task:")

print(task)



# Device Registry


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



# Permission

permission = DevicePermissionManager()



permission.set_permission(

    "iphone_001",

    "camera",

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



# Execute Device Task


result = executor.execute(

    task["capability"],

    task["command"]

)



print("Execution:")

print(result)



print("===== Completed =====")

