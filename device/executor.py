class DeviceExecutor:


    def __init__(
        self,
        router
    ):

        self.router = router

        self.agents = {}



    def register_agent(
        self,
        device_id,
        agent
    ):

        self.agents[device_id] = agent



    def execute(
        self,
        capability,
        command
    ):


        device = self.router.route(
            capability
        )


        if device.get("status") != "available":

            return {

                "status":
                "no_device"

            }



        device_id = device["device_id"]


        agent = self.agents.get(
            device_id
        )


        if agent is None:

            return {

                "status":
                "no_agent",

                "device_id":
                device_id

            }



        result = agent.execute(
            command
        )


        return {

            "status":
            "completed",

            "device_id":
            device_id,

            "result":
            result

        }
