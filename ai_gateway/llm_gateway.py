from ai_gateway.router import ModelRouter


class LLMGateway:

    def __init__(
        self,
        router
    ):

        self.router = router


    def generate(
        self,
        prompt
    ):

        provider = self.router.select_model(
            prompt
        )


        return provider.generate(
            prompt
        )
