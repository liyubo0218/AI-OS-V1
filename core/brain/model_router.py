class ModelRouter:

    def __init__(
        self,
        default_provider=None
    ):

        self.providers = {}

        self.default_model = None

        if default_provider:

            self.register_provider(
                default_provider
            )


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

        if self.default_model:

            return self.providers.get(
                self.default_model
            )

        return None


    def switch_model(
        self,
        model_name
    ):

        if model_name in self.providers:

            self.default_model = model_name

            return True


        return False


    def route(
        self,
        prompt,
        context=None
    ):

        provider = self.select_model(
            prompt
        )


        if provider:

            return provider.generate(
                prompt,
                context
            )


        return {

            "text": "",

            "model": "none",

            "confidence": 0,

            "status": "unavailable"

        }
