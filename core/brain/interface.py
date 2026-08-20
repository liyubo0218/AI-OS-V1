from core.brain.request import BrainRequest
from core.brain.response import BrainResponse


class BrainInterface:

    def __init__(self, brain):

        self.brain = brain


    def process(self, request: BrainRequest):

        context = {
            "user_input": request.user_input
        }

        result = self.brain.understand(
            context
        )

        return BrainResponse(
            request_id=request.request_id,
            status="understood",
            intent=result.get(
                "intent",
                "unknown"
            ),
            goal=result.get(
                "goal",
                ""
            ),
            entities=result.get(
                "entities",
                []
            ),
            confidence=result.get(
                "confidence",
                0.5
            ),
            context=request.context
        )
