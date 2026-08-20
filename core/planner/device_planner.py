class DevicePlanner:


    def create_plan(
        self,
        understanding
    ):


        goal = understanding.get(
            "goal",
            ""
        )


        if "拍照" in goal or "照片" in goal:


            return {

                "type":
                "device_task",

                "capability":
                "camera",

                "command":
                "capture"

            }



        if "定位" in goal or "位置" in goal:


            return {

                "type":
                "device_task",

                "capability":
                "location",

                "command":
                "get_location"

            }



        return {

            "type":
            "normal_task"

        }
