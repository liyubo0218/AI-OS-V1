class Orchestrator:

    def __init__(
        self,
        context_manager,
        brain,
        planner,
        security_manager,
        execution_engine,
        agent_manager,
        memory_manager,
        goal_monitor
    ):

        self.context_manager = context_manager
        self.brain = brain
        self.planner = planner
        self.security_manager = security_manager
        self.execution_engine = execution_engine
        self.agent_manager = agent_manager
        self.memory_manager = memory_manager
        self.goal_monitor = goal_monitor


    def run(self, user_input):

        print("AI-OS Workflow Started")


        context = self.context_manager.create_context(
            user_input
        )

        print("Context Created")


        goal = self.goal_monitor.create_goal(
            "goal_task_001",
            user_input
        )

        print("Goal Created:")
        print(goal)


        understanding = self.brain.understand(
            context
        )

        print("Brain Understanding:")
        print(understanding)


        plan = self.planner.create_plan(
            understanding
        )

        print("Plan Created")


        # Security Check
        security_result = self.security_manager.check_permission(
            {
                "task": user_input
            }
        )

        print("Security Check:")
        print(security_result)


        if not security_result["allowed"]:

            return {
                "status": "blocked",
                "security": security_result
            }


        execution_result = self.execution_engine.execute(
            plan
        )

        print("Execution Completed")


        agent_result = self.agent_manager.execute_agent(
            "test_task",
            user_input
        )

        print("Agent Result:")
        print(agent_result)


        goal = self.goal_monitor.update_status(
            "goal_task_001",
            "completed"
        )

        print("Goal Updated:")
        print(goal)


        memory = self.memory_manager.save_memory(
            "memory_task_002",
            "task_history",
            "完成任务: " + user_input
        )


        print("Memory Saved")


        return {
            "status": "completed",
            "security": security_result,
            "execution": execution_result,
            "agent_result": agent_result,
            "memory": memory
        }
