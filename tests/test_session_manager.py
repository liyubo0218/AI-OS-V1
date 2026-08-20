from session.manager import SessionManager



manager = SessionManager()



print("AI-OS Session Manager Ready")



print(

    "Create:"

)

print(

    manager.create_session(

        "session_001",

        "iphone_001"

    )

)



print(

    "Open:"

)

print(

    manager.open_session(

        "session_001"

    )

)



print(

    "Close:"

)

print(

    manager.close_session(

        "session_001"

    )

)



print(

    "Current:"

)

print(

    manager.get_session(

        "session_001"

    )

)

