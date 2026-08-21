class Planner:

    def __init__(self):
        self.plans = {}


    def create_plan(
        self,
        goal
    ):

        if not goal:
            return {
                "status": "failed",
                "reason": "invalid_goal"
            }

        plan_id = (
            f"plan_{len(self.plans)+1:03d}"
        )

        plan = {
            "plan_id": plan_id,
            "goal": goal,
            "steps": [
                {
                    "step_id": 1,
                    "task": goal,
                    "status": "pending"
                }
            ],
            "status": "created"
        }

        self.plans[plan_id] = plan

        return plan


    def get_plan(
        self,
        plan_id
    ):

        return self.plans.get(
            plan_id,
            {
                "status": "not_found"
            }
        )


    def update_plan_status(
        self,
        plan_id,
        status
    ):

        plan = self.plans.get(
            plan_id
        )

        if not plan:
            return {
                "status": "not_found"
            }

        plan["status"] = status

        return plan
