from session.manager import SessionManager

from mobile_gateway.session_adapter import MobileSessionAdapter



manager = SessionManager()



gateway = MobileSessionAdapter(

    manager

)



print(
    "Mobile Session Gateway Ready"
)



print(
    "App Open:"
)



print(

    gateway.handle(

        {
            "action":
            "open",

            "device_id":
            "iphone_001"

        }

    )

)



print(
    "App Close:"
)



print(

    gateway.handle(

        {
            "action":
            "close",

            "device_id":
            "iphone_001"

        }

    )

)

