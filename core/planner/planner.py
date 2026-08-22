from .workflow import Workflow


class Planner:


    def create_plan(
        self,
        goal
    ):

        workflow = Workflow()


        if "提醒" in goal:

            workflow.add_step(
                "create_reminder"
            )

            workflow.add_step(
                "notify_user"
            )


        else:

            workflow.add_step(
                "execute_task"
            )


        return {

            "goal": goal,

            "workflow":
                workflow.to_dict()

        }
