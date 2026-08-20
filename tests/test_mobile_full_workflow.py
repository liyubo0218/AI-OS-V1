from mobile_protocol.request import MobileRequest

from mobile_gateway.protocol_handler import ProtocolHandler

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



print("===== Mobile Full Workflow Test =====")



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



mobile_gateway = MobileGateway(

    orchestrator,

    sync_gateway

)



handler = ProtocolHandler(

    mobile_gateway

)



request = MobileRequest(

    "req_mobile_001",

    "session_001",

    "task_request",

    {
        "text":
        "帮我测试AI-OS"
    }

)



response = handler.handle(
    request
)



print(
    response.to_dict()
)



print("===== Mobile Full Workflow Completed =====")
