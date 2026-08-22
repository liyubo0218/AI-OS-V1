from chatgpt_bridge.response import ChatGPTResponse


class ChatGPTConnector:


    def send(
        self,
        request
    ):

        return ChatGPTResponse(
            request.request_id,
            "ChatGPT Bridge 模拟回复: "
            + request.user_input
        )
