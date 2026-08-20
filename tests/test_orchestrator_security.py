from core.context.context_manager import ContextManager
from core.brain.brain import Brain
from core.planner.planner import Planner
from execution.execution_engine import ExecutionEngine
from agents.agent_manager import AgentManager
from agents.demo_agent import DemoAgent
from memory.memory_manager import MemoryManager
from security.security_manager import SecurityManager
from core.orchestrator.orchestrator import Orchestrator


orchestrator = Orchestrator(
    ContextManager(),
    Brain(),
    Planner(),
    SecurityManager(),
    ExecutionEngine(),
    AgentManager(),
    MemoryManager()
)


orchestrator.agent_manager.register_agent(
    DemoAgent()
)


print("Normal Task Test")

result = orchestrator.run(
    "帮我测试AI-OS"
)

print(result)


print("High Risk Task Test")

result = orchestrator.run(
    "删除全部文件"
)

print(result)
