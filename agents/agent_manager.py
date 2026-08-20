class AgentManager:

    def __init__(self):
        self.agents = []


    def register_agent(self, agent):

        self.agents.append(agent)


    def find_agent(self, capability):

        for agent in self.agents:

            if agent.capability == capability:
                return agent

        return None


    def execute_agent(self, capability, task):

        agent = self.find_agent(capability)

        if agent:

            return agent.execute(task)


        return {
            "result": "没有找到对应Agent"
        }
