class SystemIntegration:

    def __init__(
        self,
        brain,
        memory,
        planner,
        agent_manager,
        goal_monitor
    ):
        self.brain = brain
        self.memory = memory
        self.planner = planner
        self.agent_manager = agent_manager
        self.goal_monitor = goal_monitor


    def process(
        self,
        user_input
    ):

        brain_result = self.brain.analyze(
            user_input
        )

        memory_result = self.memory.analyze(
            user_input
        )

        plan = self.planner.create_plan(
            brain_result,
            memory_result
        )

        agents = self.agent_manager.select_agent(
            plan["required_capability"]
        )

        execution = self.agent_manager.coordinate_agents(
            agents["selected_agents"],
            plan["task"]
        )

        feedback = self.goal_monitor.monitor(
            brain_result["goal"],
            execution["result"]
        )

        return {
            "brain": brain_result,
            "memory": memory_result,
            "plan": plan,
            "execution": execution,
            "feedback": feedback
        }
