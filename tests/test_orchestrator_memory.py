from core.context.context_manager import ContextManager
from core.brain.brain import Brain
from core.planner.planner import Planner
from execution.execution_engine import ExecutionEngine
from agents.agent_manager import AgentManager
from agents.demo_agent import DemoAgent
from memory.memory_manager import MemoryManager
from core.orchestrator.orchestrator import Orchestrator


context_manager = ContextManager()

brain = Brain()

planner = Planner()

execution_engine = ExecutionEngine()

agent_manager = AgentManager()

agent_manager.register_agent(
    DemoAgent()
)

memory_manager = MemoryManager()


orchestrator = Orchestrator(
    context_manager,
    brain,
    planner,
    execution_engine,
    agent_manager,
    memory_manager
)


orchestrator.run(
    "帮我测试AI-OS"
)


print("Memory Retrieved:")

print(
    memory_manager.retrieve_memory(
        "AI-OS"
    )
)
