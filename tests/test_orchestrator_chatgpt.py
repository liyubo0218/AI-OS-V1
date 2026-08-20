from core.orchestrator.orchestrator import Orchestrator

from core.context.context_manager import ContextManager
from core.brain.brain import Brain
from core.planner.planner import Planner

from security.security_manager import SecurityManager

from execution.execution_engine import ExecutionEngine

from agents.agent_manager import AgentManager
from agents.demo_agent import DemoAgent

from memory.memory_manager import MemoryManager

from goal_monitor.monitor import GoalMonitor


from ai_gateway.router import ModelRouter
from ai_gateway.llm_gateway import LLMGateway

from ai_gateway.providers.chatgpt_provider import ChatGPTProvider



router = ModelRouter()


router.register_provider(
    ChatGPTProvider()
)


router.switch_model(
    "chatgpt-model"
)


llm_gateway = LLMGateway(
    router
)



agent_manager = AgentManager()


agent_manager.register_agent(
    DemoAgent()
)



orchestrator = Orchestrator(
    ContextManager(),

    Brain(
        llm_gateway
    ),

    Planner(),

    SecurityManager(),

    ExecutionEngine(),

    agent_manager,

    MemoryManager(),

    GoalMonitor()
)



result = orchestrator.run(
    "帮我测试AI-OS"
)



print("===== Orchestrator ChatGPT Test =====")

print(result)
