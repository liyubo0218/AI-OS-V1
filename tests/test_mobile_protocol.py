from mobile_protocol.request import MobileRequest

from mobile_protocol.response import MobileResponse

from mobile_protocol.session_protocol import SessionProtocol



request = MobileRequest(

    "req_001",

    "session_001",

    "task_request",

    {
        "text":
        "测试AI-OS"
    }

)



print("Request:")

print(
    request.to_dict()
)



response = MobileResponse(

    "req_001",

    "success",

    {
        "task_id":
        "task_001"
    }

)



print("Response:")

print(
    response.to_dict()
)



protocol = SessionProtocol()



print("Session:")

print(
    protocol.create_session_request(
        "iphone_001"
    )
)
