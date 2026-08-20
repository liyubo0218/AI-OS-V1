from agents.base_agent import BaseAgent


class DemoAgent(BaseAgent):

    def __init__(self):
        super().__init__(
            "DemoAgent",
            "test_task"
        )


    def execute(self, task):

        return {
            "agent": self.name,
            "task": task,
            "result": "DemoAgent完成任务"
        }
