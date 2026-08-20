from mobile_gateway.aios_adapter import MobileAIOSAdapter



class DemoAIOS:


    def run(
        self,
        text
    ):

        return {

            "task":
            text,

            "result":
            "拍照完成"

        }



adapter = MobileAIOSAdapter(

    DemoAIOS()

)



print("Mobile AI-OS Entry Ready")



print(

    adapter.handle(

        {
            "text":
            "帮我拍一张照片"
        }

    )

)

