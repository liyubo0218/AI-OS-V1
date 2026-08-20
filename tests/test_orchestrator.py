from core.context.context_manager import ContextManager
from core.brain.brain import Brain
from core.planner.planner import Planner
from execution.execution_engine import ExecutionEngine
from agents.agent_manager import AgentManager
from agents.demo_agent import DemoAgent
from core.orchestrator.orchestrator import Orchestrator


context_manager = ContextManager()

brain = Brain()

planner = Planner()

execution_engine = ExecutionEngine()

agent_manager = AgentManager()

agent_manager.register_agent(
    DemoAgent()
)


orchestrator = Orchestrator(
    context_manager,
    brain,
    planner,
    execution_engine,
    agent_manager
)


result = orchestrator.run(
    "帮我测试AI-OS"
)


print("================")
print("AI-OS Workflow Completed")
print("================")

print(result)
