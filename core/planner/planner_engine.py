class PlannerEngine:

    def __init__(self):
        pass


    def create_plan(
        self,
        goal,
        context=None
    ):
        return {
            "goal": goal,
            "tasks": [
                {
                    "task_id": "task_001",
                    "description": goal,
                    "agent": "assistant_agent"
                }
            ],
            "status": "planned",
            "context": context
        }
