from core.orchestrator.device_integration import DeviceIntegration



class DemoDeviceFlow:


    def execute(
        self,
        data
    ):

        return {

            "type":"device",

            "device":"iphone_001",

            "result":"拍照完成"

        }



class DemoNormalFlow:


    def execute(
        self,
        data
    ):

        return {

            "type":"normal",

            "result":"任务完成"

        }



class TaskRouter:


    def __init__(
        self,
        device,
        normal
    ):

        self.device = device

        self.normal = normal



    def execute(
        self,
        data
    ):


        if "照片" in data["goal"]:

            return self.device.execute(
                data
            )


        return self.normal.execute(
            data
        )



router = TaskRouter(

    DemoDeviceFlow(),

    DemoNormalFlow()

)



integration = DeviceIntegration(

    router

)



print("AI-OS Device Integration Ready")



print(

    integration.run(

        {
            "goal":
            "帮我拍一张照片"
        }

    )

)

