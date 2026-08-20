from runtime.local import LocalRuntime

from runtime.cloud import CloudRuntime

from core.runtime_router import RuntimeRouter



local = LocalRuntime()

cloud = CloudRuntime()



local.start()

cloud.start()



router = RuntimeRouter(

    local,

    cloud

)



print(
    "===== Runtime Router Ready ====="
)



print(
    "Camera Task:"
)

print(

    router.route(

        "camera_capture"

    )

)



print(
    "AI Task:"
)

print(

    router.route(

        "large_ai_analysis"

    )

)



print(
    "Local:"
)

print(

    local.get_status()

)



print(
    "Cloud:"
)

print(

    cloud.get_status()

)



print(
    "===== Runtime Router PASS ====="
)

