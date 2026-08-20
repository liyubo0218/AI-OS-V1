class ChatGPTTaskAdapter:


    def convert(
        self,
        response
    ):


        device_keywords = [

            "拍照",

            "照片",

            "拍一张",

            "摄像头",

            "camera"

        ]


        for keyword in device_keywords:


            if keyword in response:


                return {

                    "type":
                    "device_task",

                    "capability":
                    "camera",

                    "command":
                    "capture"

                }



        return {

            "type":
            "normal_task",

            "goal":
            response

        }
