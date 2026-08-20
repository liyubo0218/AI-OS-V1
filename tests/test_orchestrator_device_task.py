from core.planner.device_planner import DevicePlanner

from core.orchestrator.device_orchestration import DeviceTaskOrchestrator



class DemoDeviceGateway:


    def execute_device_task(
        self,
        capability,
        command
    ):

        return {

            "device":
            "iphone_001",

            "capability":
            capability,

            "command":
            command,

            "result":
            "执行成功"

        }



planner = DevicePlanner()



gateway = DemoDeviceGateway()



orchestrator = DeviceTaskOrchestrator(

    planner,

    gateway

)



print("Device Task Orchestration Ready")



print(

    orchestrator.execute(

        {
            "goal":
            "帮我拍一张照片"
        }

    )

)

