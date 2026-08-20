class ModelRouter:

    def __init__(self):

        self.providers = {}

        self.default_model = None


    def register_provider(
        self,
        provider
    ):

        self.providers[
            provider.name
        ] = provider


        if self.default_model is None:

            self.default_model = provider.name


    def select_model(
        self,
        task=None
    ):

        return self.providers.get(
            self.default_model
        )


    def switch_model(
        self,
        model_name
    ):

        if model_name in self.providers:

            self.default_model = model_name

            return True


        return False
