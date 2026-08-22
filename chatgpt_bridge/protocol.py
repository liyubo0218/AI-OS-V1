from core.brain.providers.chatgpt.permission import ChatGPTPermission

from core.brain.providers.chatgpt.mock_connector import MockConnector

from core.brain.providers.chatgpt.real_connector import RealConnector

from core.brain.providers.chatgpt.config import ChatGPTBridgeConfig



class ChatGPTBridge:


    def __init__(
        self,
        config=None
    ):

        self.config = config or ChatGPTBridgeConfig()

        self.permission = ChatGPTPermission()


        if self.config.mode == "real":

            self.connector = RealConnector()

        else:

            self.connector = MockConnector()



    def chat(
        self,
        request
    ):

        check = self.permission.check(
            request
        )


        if not check["allowed"]:

            return check


        return self.connector.send(
            request
        )
