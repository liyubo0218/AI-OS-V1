from mobile_gateway.gateway import MobileGateway

from sync.sync_gateway import SyncGateway


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



sync_gateway = SyncGateway()


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
    MemoryManager(),
    GoalMonitor()
)



gateway = MobileGateway(
    orchestrator,
    sync_gateway
)



result = gateway.handle_request(
    {
        "user_input":
        "测试Mobile Sync"
    }
)



print("Mobile Sync Gateway Ready")

print(result)



print("Sync State:")

print(
    sync_gateway.sync()
)
