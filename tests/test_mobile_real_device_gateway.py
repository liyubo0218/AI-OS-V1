from mobile_gateway.aios_adapter import MobileAIOSAdapter

from core.aios import AIOS

from chatgpt_bridge.task_adapter import ChatGPTTaskAdapter


from device.identity import DeviceIdentity

from device.registry import DeviceRegistry

from device.permission import DevicePermissionManager

from device.router import DeviceRouter

from device.executor import DeviceExecutor

from device.agents.iphone_agent import IPhoneAgent



class Brain:


    def understand(
        self,
        context
    ):

        task = ChatGPTTaskAdapter().convert(

            context["user_input"]

        )


        return task



class TaskRouter:


    def __init__(
        self,
        executor
    ):

        self.executor = executor



    def execute(
        self,
        task
    ):

        return self.executor.execute(

            task["capability"],

            task["command"]

        )



class Memory:


    def save(
        self,
        t,
        c
    ):

        print(
            "Memory Saved"
        )



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



# Router + Executor

device_router = DeviceRouter(

    registry,

    permission

)



executor = DeviceExecutor(

    device_router

)



executor.register_agent(

    "iphone_001",

    IPhoneAgent()

)



task_router = TaskRouter(

    executor

)



aios = AIOS(

    Brain(),

    task_router,

    Memory()

)



mobile = MobileAIOSAdapter(

    aios

)



print(
    "===== Mobile Real Device Gateway ====="
)



result = mobile.handle(

    {
        "text":
        "帮我拍一张照片"
    }

)



print(result)



print(
    "===== Completed ====="
)

