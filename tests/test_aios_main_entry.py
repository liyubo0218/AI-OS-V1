from core.aios import AIOS



class DemoBrain:


    def understand(
        self,
        context
    ):

        return {

            "goal":
            context["user_input"],

            "type":
            "device_task"

        }



class DemoRouter:


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



class DemoMemory:


    def save(
        self,
        t,
        c
    ):

        print(
            "Memory Saved"
        )



aios = AIOS(

    DemoBrain(),

    DemoRouter(),

    DemoMemory()

)



result = aios.run(

    "帮我拍一张照片"

)



print(result)

