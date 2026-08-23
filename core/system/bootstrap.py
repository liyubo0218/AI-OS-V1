from core.brain.brain import Brain
from core.brain.llm_gateway import LLMGateway
from core.brain.model_router import ModelRouter
from core.brain.providers.chatgpt_provider import ChatGPTProvider

from core.secretary.secretary_core import SecretaryCore

from core.memory.memory_service import MemoryService

from core.task.task_manager import TaskManager

from core.device.mobile_adapter import MobileAdapter
from core.mobile.mobile_gateway import MobileGateway

from core.orchestrator.orchestrator import Orchestrator

from core.runtime.runtime import Runtime
from core.interface.api import AIOSAPI

from core.event.event_bus import EventBus
from core.proactive.proactive_engine import ProactiveEngine
from core.confirmation.confirmation_manager import ConfirmationManager
from core.goal.goal_manager import GoalManager
from core.goal.goal_monitor import GoalMonitor
from core.goal.goal_insight import GoalInsight


class Bootstrap:
    """
    AI-OS 系统初始化装配器 V1.5.3

    负责：
    - 创建核心组件
    - 连接依赖

    不负责：
    - AI逻辑
    - 任务执行
    - 手机控制
    """

    def __init__(self):
        self.system = {}


    def create(self):

        goal_manager = GoalManager()

        goal_monitor = GoalMonitor(
            goal_manager
        )

        goal_insight = GoalInsight()

        proactive_engine = ProactiveEngine()

        confirmation_manager = ConfirmationManager()


        memory = MemoryService()


        event_bus = EventBus()


        # =====================
        # LLM Layer
        # =====================

        chatgpt_provider = ChatGPTProvider()

        model_router = ModelRouter(
            chatgpt_provider
        )

        llm_gateway = LLMGateway(
            model_router
        )


        # =====================
        # Brain
        # =====================

        brain = Brain(
            llm_gateway=llm_gateway,
            memory_service=memory
        )


        secretary = SecretaryCore(
            brain=brain
        )


        # =====================
        # Task
        # =====================

        task_manager = TaskManager(
            event_bus=event_bus
        )


        # =====================
        # Device
        # =====================

        device = MobileAdapter()

        mobile_gateway = MobileGateway(
            device=device
        )


        # =====================
        # Orchestrator
        # =====================

        orchestrator = Orchestrator(
            secretary=secretary,
            brain=brain,
            memory=memory,
            task_manager=task_manager,
            device=device,
            mobile_gateway=mobile_gateway
        )


        runtime = Runtime(
            orchestrator
        )


        api = AIOSAPI(
            runtime
        )


        self.system = {

            "memory": memory,

            "event_bus": event_bus,

            "goal_manager": goal_manager,

            "goal_monitor": goal_monitor,

            "goal_insight": goal_insight,

            "proactive_engine": proactive_engine,

            "confirmation_manager": confirmation_manager,

            "brain": brain,

            "llm_gateway": llm_gateway,

            "model_router": model_router,

            "chatgpt_provider": chatgpt_provider,

            "secretary": secretary,

            "task_manager": task_manager,

            "device": device,

            "mobile_gateway": mobile_gateway,

            "orchestrator": orchestrator,

            "runtime": runtime,

            "api": api
        }


        return self.system


    def get_system(self):

        return self.system
