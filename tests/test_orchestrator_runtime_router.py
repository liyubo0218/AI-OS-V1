from runtime.local import LocalRuntime

from runtime.cloud import CloudRuntime

from core.runtime_router import RuntimeRouter

from core.orchestrator_runtime import RuntimeOrchestrator



local = LocalRuntime()

cloud = CloudRuntime()



local.start()

cloud.start()



router = RuntimeRouter(

    local,

    cloud

)



orchestrator = RuntimeOrchestrator(

    router

)



print(
    "===== Orchestrator Runtime Router Ready ====="
)



print(
    "Photo Task:"
)

print(

    orchestrator.execute(

        "camera_capture"

    )

)



print(
    "AI Task:"
)

print(

    orchestrator.execute(

        "large_ai_analysis"

    )

)



print(
    "Local State:"
)

print(

    local.get_status()

)



print(
    "Cloud State:"
)

print(

    cloud.get_status()

)



print(
    "===== Orchestrator Runtime PASS ====="
)

