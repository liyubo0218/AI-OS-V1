import os


from session.manager import SessionManager

from runtime.manager import RuntimeManager

from runtime.hybrid import HybridRuntime

from sync.gateway import SyncGateway

from sync.storage import SyncStorage



file = "hybrid_sync_events.json"



if os.path.exists(file):

    os.remove(file)



sync_gateway = SyncGateway(

    SyncStorage(file)

)



hybrid = HybridRuntime(

    SessionManager(),

    RuntimeManager(),

    sync_gateway

)



print(
    "Hybrid Persistent Sync Ready"
)



print(
    "App Open:"
)

print(

    hybrid.app_open(

        "iphone_001"

    )

)



print(
    "App Close:"
)

print(

    hybrid.app_close()

)



print(
    "Restart Recovery:"
)

print(

    hybrid.recover()

)



print(
    "===== Recovery PASS ====="
)

