class DeviceTaskOrchestrator:


    def __init__(
        self,
        device_planner,
        device_gateway
    ):

        self.device_planner = device_planner

        self.device_gateway = device_gateway



    def execute(
        self,
        understanding
    ):


        plan = self.device_planner.create_plan(
            understanding
        )


        if plan["type"] != "device_task":

            return {

                "status":
                "not_device_task"

            }



        result = self.device_gateway.execute_device_task(

            plan["capability"],

            plan["command"]

        )


        return result
