from mobile_gateway.aios_adapter import MobileAIOSAdapter

from core.aios import AIOS



class Brain:


    def understand(
        self,
        context
    ):

        text = context["user_input"]


        if "照片" in text:

            return {

                "type":
                "device_task",

                "goal":
                text

            }


        return {

            "type":
            "normal_task",

            "goal":
            text

        }



class DeviceRouter:


    def execute(
        self,
        task
    ):

        return {

            "device":
            "iphone_001",

            "result":
            "拍照完成"

        }



class Memory:


    def save(
        self,
        t,
        c
    ):

        print(
            "Memory Saved"
        )



aios = AIOS(

    Brain(),

    DeviceRouter(),

    Memory()

)



mobile = MobileAIOSAdapter(

    aios

)



print("===== Mobile AI-OS Full Workflow =====")



result = mobile.handle(

    {
        "text":
        "帮我拍一张照片"
    }

)



print(result)

