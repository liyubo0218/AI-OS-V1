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



agent_manager = AgentManager()


agent_manager.register_agent(
    DemoAgent()
)


goal_monitor = GoalMonitor()


orchestrator = Orchestrator(
    ContextManager(),
    Brain(),
    Planner(),
    SecurityManager(),
    ExecutionEngine(),
    agent_manager,
    MemoryManager(),
    goal_monitor
)


print("===== AI-OS Full System Test =====")


result = orchestrator.run(
    "帮我测试AI-OS"
)


print("\nFinal Result:")

print(result)


print("\nGoal Status:")

print(
    goal_monitor.get_goal(
        "goal_task_001"
    )
)


print("\nMemory:")

memory = MemoryManager()

print(
    memory.get_all_memory()
)


print("\n===== Test Completed =====")
