class ExtensionRegistry:


    def __init__(self):

        self.extensions = {}



    def register(
        self,
        name,
        extension
    ):

        self.extensions[name] = extension

        return {
            "status": "registered"
        }



    def get(
        self,
        name
    ):

        return self.extensions.get(
            name
        )
