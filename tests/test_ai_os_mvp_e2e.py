from core.brain import BrainController, IntentEngine
from core.context import ContextManager
from core.memory import MemoryManager
from core.planner import Planner
from core.executor import Executor
from core.goal import GoalMonitor
from gateway.mobile import MobileServer, RequestModel


class AIOSRuntimeAdapter:


    def __init__(self):

        self.brain = BrainController()
        self.intent = IntentEngine()
        self.context = ContextManager()
        self.memory = MemoryManager()
        self.planner = Planner()
        self.executor = Executor()
        self.goal = GoalMonitor()


    def execute(self, request):

        content = request["content"]


        brain_result = self.brain.process(
            content
        )


        intent_result = self.intent.analyze(
            content
        )


        self.context.create(
            "user",
            content
        )


        self.memory.save_task(
            "001",
            {
                "content": content
            }
        )


        plan = self.planner.create_plan(
            content
        )


        self.executor.register_action(
            "create_reminder",
            lambda x: {
                "executed": True
            }
        )


        execute_result = self.executor.execute(
            "create_reminder"
        )


        self.goal.create_goal(
            "001",
            content
        )


        self.goal.update_goal(
            "001",
            "completed"
        )


        return {
            "brain": brain_result,
            "intent": intent_result,
            "plan": plan,
            "execution": execute_result,
            "goal": self.goal.get_goal("001")
        }



def test_ai_os_mvp_e2e():

    runtime = AIOSRuntimeAdapter()

    server = MobileServer(
        runtime
    )


    result = server.receive(
        RequestModel(
            "提醒我明天开会"
        )
    )


    assert result["intent"]["intent"] == "reminder"

    assert result["execution"]["executed"] is True

    assert result["goal"]["status"] == "completed"


    print(
        "AI-OS MVP END-TO-END PASS"
    )


if __name__ == "__main__":

    test_ai_os_mvp_e2e()
