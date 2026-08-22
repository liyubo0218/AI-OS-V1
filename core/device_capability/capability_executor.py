class CapabilityExecutor:


    def execute(
        self,
        capability,
        data=None
    ):


        if capability is None:

            return {
                "status": "failed"
            }


        return {

            "status": "executed",

            "capability": capability,

            "data": data

        }
