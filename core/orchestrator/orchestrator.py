from core.secretary.intent import IntentAnalyzer
from core.secretary.planner import SecretaryPlanner
from core.task.scheduler import TaskScheduler
from core.task.executor import TaskExecutor
from core.mobile.action_mapper import ActionMapper
from core.mobile.mobile_gateway import MobileGateway

class Orchestrator:
    """
    AI-OS 总协调器

    负责：
    - 连接核心模块
    - 编排请求流程
    - 返回统一结果

    不负责：
    - AI推理
    - 手机执行
    - 记忆学习
    """

    def __init__(
        self,
        secretary=None,
        brain=None,
        memory=None,
        task_manager=None,
        device=None,
        intent_analyzer=None,
        planner=None,
        scheduler=None,
        executor=None,
        action_mapper=None,
        mobile_gateway=None
    ):
        self.secretary = secretary
        self.brain = brain
        self.memory = memory
        self.task_manager = task_manager
        self.device = device

        self.intent_analyzer = (
            intent_analyzer or IntentAnalyzer()
        )
        self.planner = (
            planner or SecretaryPlanner()
        )
        self.scheduler = (
            scheduler or TaskScheduler()
        )
        self.executor = (
            executor or TaskExecutor(device)
        )
        self.action_mapper = (
            action_mapper or ActionMapper()
        )
        self.mobile_gateway = (
            mobile_gateway or MobileGateway(
                device=device
            )
        )


    def process(
        self,
        user_input
    ):
        result = {
            "input": user_input
        }


        context = {}

        if self.memory:
            context = self.memory.get_memory_context(
                user_input
            )

        result["memory"] = context


        if self.secretary:
            result["secretary"] = (
                self.secretary.process(
                    user_input,
                    context
                )
            )


        if self.brain:
            result["brain"] = (
                self.brain.understand(
                    {
                        "user_input": user_input,
                        "memory": context
                    }
                )
            )


        if self.task_manager:
            task = self.task_manager.create_task(
                user_input
            )

            result["task"] = task.to_dict()



        intent_result = self.intent_analyzer.analyze(
            user_input
        )

        result["intent"] = intent_result

        plan = self.planner.plan(
            intent_result
        )

        result["plan"] = plan

        if self.task_manager:
            task = self.task_manager.create_task(
                user_input
            )

            task_data = task.to_dict()

            result["task"] = task_data

            schedule = self.scheduler.schedule(
                task_data
            )

            result["schedule"] = schedule

            execution = self.executor.execute(
                {
                    "action": "notification",
                    "task": task_data
                }
            )

            result["execution"] = execution

        return result
