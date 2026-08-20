from goal_monitor.monitor import GoalMonitor


monitor = GoalMonitor()


created = monitor.create_goal(
    "goal_001",
    "帮我测试AI-OS"
)


print("Goal Monitor Ready")


print("Created:")

print(created)


updated = monitor.update_status(
    "goal_001",
    "completed"
)


print("Updated:")

print(updated)


print("Query:")

print(
    monitor.get_goal(
        "goal_001"
    )
)
