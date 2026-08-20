class BrainResponse:

    def __init__(
        self,
        request_id,
        status="understood",
        intent="unknown",
        goal="",
        entities=None,
        confidence=0.5,
        context=None,
        planning_request=None
    ):
        self.request_id = request_id
        self.status = status
        self.intent = intent
        self.goal = goal
        self.entities = entities or []
        self.confidence = confidence
        self.context = context or {}
        self.planning_request = planning_request or {}

    def to_dict(self):

        return {
            "request_id": self.request_id,
            "status": self.status,
            "intent": self.intent,
            "goal": self.goal,
            "entities": self.entities,
            "confidence": self.confidence,
            "context": self.context,
            "planning_request": self.planning_request
        }
