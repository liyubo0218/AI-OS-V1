from session.manager import SessionManager

from runtime.manager import RuntimeManager

from runtime.hybrid import HybridRuntime



class SyncGateway:


    def store_event(
        self,
        event_type,
        payload
    ):

        return {

            "status":
            "stored",

            "type":
            event_type,

            "payload":
            payload

        }



hybrid = HybridRuntime(

    SessionManager(),

    RuntimeManager(),

    SyncGateway()

)



print(
    "Hybrid Runtime Session Sync Ready"
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
    "===== Hybrid Mode Ready ====="
)

