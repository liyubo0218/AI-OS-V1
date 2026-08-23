from core.brain.brain import Brain
from core.secretary.secretary_core import SecretaryCore
from core.secretary.secretary_context import SecretaryContext

from core.memory.memory_service import MemoryService
from core.memory.profile import Profile
from core.memory.memory_index import MemoryIndex

from core.task.task_manager import TaskManager
from core.device.mobile_adapter import MobileAdapter
from core.mobile.mobile_gateway import MobileGateway

from core.orchestrator.orchestrator import Orchestrator

from core.runtime.runtime import Runtime
from core.interface.api import AIOSAPI
from core.event.event_bus import EventBus


class Bootstrap:
    """
    AI-OS 系统初始化装配器

    负责：
    - 创建核心组件
    - 连接模块依赖

    不负责：
    - AI逻辑
    - 业务执行
    - 手机控制
    """

    def __init__(self):
        self.system = {}


    def create(self):

        memory = MemoryService()

        event_bus = EventBus()

        brain = Brain()

        secretary = SecretaryCore(
            brain=brain
        )

        task_manager = TaskManager(
            event_bus=event_bus
        )

        device = MobileAdapter()

        
        mobile_gateway = MobileGateway(
            device=device
        )


        orchestrator = Orchestrator(
            secretary=secretary,
            brain=brain,
            memory=memory,
            task_manager=task_manager,
            device=device
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
            "brain": brain,
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
