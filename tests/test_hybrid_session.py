from session.session_manager import SessionManager



manager = SessionManager()



print("Create Session:")


print(
    manager.create_session(
        "session_001",
        "iphone_001"
    )
)



print("App Open:")


print(
    manager.connect_device(
        "session_001"
    )
)



print("App Close:")


print(
    manager.disconnect_device(
        "session_001"
    )
)
