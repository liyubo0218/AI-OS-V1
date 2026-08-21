class MultiAgentManager:

    def __init__(self):
        self.agents = {}


    def register_agent(
        self,
        agent_id,
        capability
    ):
        self.agents[agent_id] = capability

        return {
            "registered": True,
            "agent_id": agent_id
        }


    def select_agent(
        self,
        required_capability
    ):
        selected = []

        for agent_id, capability in self.agents.items():
            if capability == required_capability:
                selected.append(agent_id)

        return {
            "selected_agents": selected
        }


    def coordinate_agents(
        self,
        agents,
        task
    ):
        return {
            "execution_plan": agents,
            "result": task
        }
