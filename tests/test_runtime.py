from runtime.runtime_manager import RuntimeManager


runtime = RuntimeManager()


print("Initialize:")

print(
    runtime.initialize(
        [
            "ContextManager",
            "Brain",
            "Planner",
            "ExecutionEngine"
        ]
    )
)


print("Start:")

print(
    runtime.start()
)


print("Health Check:")

print(
    runtime.health_check()
)


print("Stop:")

print(
    runtime.stop()
)
