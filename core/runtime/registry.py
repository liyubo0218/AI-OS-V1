class RuntimeRegistry:

    def __init__(self):
        self.modules = {}


    def register(
        self,
        name,
        module
    ):
        self.modules[name] = module

        return {
            "status": "registered",
            "module": name
        }


    def get(
        self,
        name
    ):
        return self.modules.get(
            name
        )


    def has(
        self,
        name
    ):
        return name in self.modules
