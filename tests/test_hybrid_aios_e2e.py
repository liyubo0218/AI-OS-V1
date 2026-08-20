from mobile_gateway.gateway import MobileGateway

from sync.sync_gateway import SyncGateway

from runtime.runtime_manager import RuntimeManager

from runtime.task_runtime import TaskRuntime

from runtime.event_publisher import RuntimeEventPublisher

from session.session_manager import SessionManager


print("===== Hybrid AI-OS E2E Test =====")


# =========================
# App Online Mode
# =========================


print("\n[App Online Mode]")


sync_gateway = SyncGateway()


print(
    sync_gateway.sync()
)


print(
    "Mobile Gateway Ready"
)



# =========================
# Session
# =========================


print("\n[Session]")


session_manager = SessionManager()


print(
    session_manager.create_session(
        "session_e2e_001",
        "iphone_001"
    )
)


print(
    session_manager.connect_device(
        "session_e2e_001"
    )
)



# =========================
# App Offline Mode
# =========================


print("\n[App Offline Mode]")


publisher = RuntimeEventPublisher(
    sync_gateway
)


runtime = RuntimeManager(
    publisher
)


print(
    runtime.start_runtime()
)



task = TaskRuntime(
    "offline_task_001"
)


print(
    runtime.run_task(
        task
    )
)



print(
    sync_gateway.sync()
)



print("\n===== Hybrid AI-OS E2E Completed =====")
