from runtime.event_loop import RuntimeEventLoop

from goal_monitor.monitor import GoalMonitor

from agents.agent_manager import AgentManager

from agents.demo_agent import DemoAgent



goal_monitor = GoalMonitor()



goal_monitor.create_goal(
    "goal_runtime_001",
    "App关闭后测试AI-OS"
)


goal_monitor.update_status(
    "goal_runtime_001",
    "active"
)



agent_manager = AgentManager()


agent_manager.register_agent(
    DemoAgent()
)



loop = RuntimeEventLoop(
    goal_monitor,
    agent_manager
)



print("Runtime Goal Loop Ready")

print(
    loop.check_goals()
)



print(
    goal_monitor.get_goal(
        "goal_runtime_001"
    )
)
