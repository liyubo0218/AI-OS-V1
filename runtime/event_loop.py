class RuntimeEventLoop:


    def __init__(
        self,
        goal_monitor,
        agent_manager
    ):

        self.goal_monitor = goal_monitor

        self.agent_manager = agent_manager



    def check_goals(self):

        goals = self.goal_monitor.get_all_goals()


        results = []


        for goal in goals:

            if goal["status"] == "active":


                result = self.agent_manager.execute_agent(
                    "test_task",
                    goal["goal"]
                )


                self.goal_monitor.update_status(
                    goal["goal_id"],
                    "completed"
                )


                results.append(
                    result
                )


        return results
