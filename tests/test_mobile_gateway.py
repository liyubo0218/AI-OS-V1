from mobile_gateway.gateway import MobileGateway

from core.context.context_manager import ContextManager
from core.brain.brain import Brain
from core.planner.planner import Planner
from core.orchestrator.orchestrator import Orchestrator

from execution.execution_engine import ExecutionEngine

from agents.agent_manager import AgentManager
from agents.demo_agent import DemoAgent

from memory.memory_manager import MemoryManager
from security.security_manager import SecurityManager


agent_manager = AgentManager()

agent_manager.register_agent(
    DemoAgent()
)


orchestrator = Orchestrator(
    ContextManager(),
    Brain(),
    Planner(),
    SecurityManager(),
    ExecutionEngine(),
    agent_manager,
    MemoryManager()
)


gateway = MobileGateway(
    orchestrator
)


request = {
    "user_input": "帮我测试AI-OS"
}


result = gateway.handle_request(
    request
)


print("Mobile Gateway Ready")

print(result)
