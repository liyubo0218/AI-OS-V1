from core.planner.planner import Planner


planner = Planner()


understanding = {
    "intent": "test_system",
    "goal": "帮我测试AI-OS"
}


plan = planner.create_plan(
    understanding
)


print("Planner Ready")

print("Goal:")
print(plan["goal"])

print("Plan:")

for step in plan["steps"]:
    print(step)

print("Status:")
print(plan["status"])
