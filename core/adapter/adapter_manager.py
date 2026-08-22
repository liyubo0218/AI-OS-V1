class AdapterManager:

    def __init__(self):
        self.adapters = {}


    def register_adapter(
        self,
        name,
        adapter
    ):
        self.adapters[name] = adapter

        return {
            "status": "registered",
            "adapter": name
        }


    def list_adapters(self):

        return list(
            self.adapters.keys()
        )


    def execute(
        self,
        adapter_name,
        action,
        parameters=None
    ):

        adapter = self.adapters.get(
            adapter_name
        )

        if adapter is None:
            return {
                "status": "failed",
                "error": "adapter_not_found"
            }


        return adapter.execute(
            action,
            parameters
        )
