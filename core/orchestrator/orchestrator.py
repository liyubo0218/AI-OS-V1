from core.task.scheduler import TaskScheduler
from core.task.executor import TaskExecutor
from core.mobile.action_mapper import ActionMapper
from core.mobile.mobile_gateway import MobileGateway
from core.time.time_parser import TimeParser


class Orchestrator:
    """
    AI-OS 总协调器 V1.5.3

    负责：
    - 连接核心模块
    - 编排请求流程
    - 协调 Memory / Brain / Task / Device

    不负责：
    - AI推理
    - 手机控制
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

        # 兼容旧组件
        self.secretary = secretary
        self.intent_analyzer = intent_analyzer
        self.planner = planner

        # 核心链路
        self.brain = brain
        self.memory = memory
        self.task_manager = task_manager

        self.device = device

        self.scheduler = (
            scheduler or TaskScheduler()
        )

        self.action_mapper = (
            action_mapper or ActionMapper()
        )

        self.mobile_gateway = (
            mobile_gateway or MobileGateway(
                device=device
            )
        )

        self.executor = (
            executor or TaskExecutor(
                device=device,
                mobile_gateway=self.mobile_gateway
            )
        )

        self.time_parser = TimeParser()


    def process(
        self,
        user_input
    ):

        result = {
            "input": user_input
        }


        # 1. Memory Context

        memory_context = {}

        if self.memory:

            memory_context = (
                self.memory.get_memory_context(
                    user_input
                )
            )

        result["memory"] = memory_context



        # 2. Brain Understanding

        understanding = {}

        if self.brain:

            understanding = (
                self.brain.understand(
                    {
                        "user_input": user_input,
                        "memory": memory_context
                    }
                )
            )

        result["brain"] = understanding



        # 3. Task Creation

        task_data = None

        # V1.5.4 保持任务闭环
        # 由 Orchestrator 负责进入任务流程
        task_required = True


        if self.task_manager and task_required:

            time_result = (
                self.time_parser.parse(
                    user_input
                )
            )

            task = (
                self.task_manager.create_task(
                    user_input,
                    deadline=time_result.get(
                        "deadline"
                    )
                )
            )

            task_index = len(
                self.task_manager.get_tasks()
            ) - 1

            task_data = task.to_dict()

            result["task_index"] = task_index
            result["task"] = task_data



        # 4. Schedule

        if task_data:

            result["schedule"] = (
                self.scheduler.schedule(
                    task_data
                )
            )



        # 5. Action Mapping + Execute

        if task_data:

            action = (
                self.action_mapper.map_action(
                    "notification",
                    {
                        "task": task_data
                    }
                )
            )

            result["action"] = action


            execution = (
                self.executor.execute(
                    {
                        "action": "notification",
                        "task": task_data
                    }
                )
            )

            result["execution"] = execution

            if self.task_manager and "task_index" in result:

                if execution.get(
                    "execution_status"
                ) == "completed":

                    self.task_manager.update_task_status(
                        result["task_index"],
                        "completed"
                    )

                elif execution.get(
                    "execution_status"
                ) == "failed":

                    self.task_manager.update_task_status(
                        result["task_index"],
                        "failed"
                    )



        return result
