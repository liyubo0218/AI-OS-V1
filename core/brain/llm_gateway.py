class LLMGateway:

    def __init__(
        self,
        router=None
    ):

        self.router = router


    def generate(
        self,
        prompt,
        context=None
    ):

        if not self.router:

            return {

                "text": "",

                "model": "none",

                "confidence": 0,

                "status": "unavailable"

            }


        if hasattr(
            self.router,
            "route"
        ):

            return self.router.route(
                prompt,
                context
            )


        if hasattr(
            self.router,
            "select_model"
        ):

            provider = self.router.select_model(
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
