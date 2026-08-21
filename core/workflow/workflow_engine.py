class WorkflowEngine:

    def __init__(self):
        self.workflows = {}


    def load_plan(
        self,
        plan
    ):

        if not plan:
            return {
                "status": "failed",
                "reason": "invalid_plan"
            }


        workflow_id = (
            f"workflow_{len(self.workflows)+1:03d}"
        )


        workflow = {
            "workflow_id": workflow_id,
            "plan_id": plan.get(
                "plan_id"
            ),
            "steps": plan.get(
                "steps",
                []
            ),
            "status": "created"
        }


        self.workflows[
            workflow["plan_id"]
        ] = workflow


        return workflow


    def start_workflow(
        self,
        plan_id
    ):

        workflow = self.workflows.get(
            plan_id
        )

        if not workflow:
            return {
                "status": "not_found"
            }


        workflow["status"] = "running"

        return workflow



    def update_step(
        self,
        step_id,
        status
    ):

        for workflow in self.workflows.values():

            for step in workflow["steps"]:

                if step.get(
                    "step_id"
                ) == step_id:

                    step["status"] = status

                    return step


        return {
            "status": "step_not_found"
        }



    def get_workflow_status(
        self,
        plan_id
    ):

        workflow = self.workflows.get(
            plan_id
        )

        if not workflow:
            return {
                "status": "not_found"
            }

        return {
            "workflow_id":
                workflow["workflow_id"],
            "status":
                workflow["status"]
        }
