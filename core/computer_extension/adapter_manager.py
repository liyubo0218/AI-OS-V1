class ComputerAdapterManager:

    def __init__(self):
        self.adapters = {}


    def register_adapter(
        self,
        system_type,
        adapter
    ):

        self.adapters[system_type] = adapter

        return {
            "status": "registered"
        }


    def execute(
        self,
        system_type,
        action,
        payload
    ):

        adapter = self.adapters.get(
            system_type
        )

        if adapter is None:
            return {
                "status": "failed",
                "error": "adapter_not_found"
            }


        return adapter.execute(
            action,
            payload
        )
