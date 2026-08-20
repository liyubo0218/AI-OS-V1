from agents.agent_manager import AgentManager
from agents.demo_agent import DemoAgent


manager = AgentManager()

agent = DemoAgent()

manager.register_agent(agent)

result = manager.execute_agent(
    "test_task",
    "执行AI-OS测试"
)

print("Agent Manager Ready")

print("Agent Result:")

print(result)
