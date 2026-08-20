class RuntimeRouter:


    def __init__(
        self,
        local_runtime,
        cloud_runtime
    ):

        self.local = local_runtime

        self.cloud = cloud_runtime



    def route(
        self,
        task
    ):


        # 简单规则：

        # 设备任务、本地操作 → Local

        if (
            "camera" in task
            or
            "file" in task
            or
            "device" in task
        ):


            self.local.add_task(

                task

            )


            return {

                "runtime":
                "local",

                "task":
                task

            }



        # 长任务 → Cloud

        self.cloud.add_task(

            task

        )


        return {

            "runtime":
            "cloud",

            "task":
            task

        }

