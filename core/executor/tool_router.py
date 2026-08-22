class ToolRouter:


    def __init__(self):

        self.tools = {}


    def register_tool(
        self,
        name,
        tool
    ):

        self.tools[name] = tool


        return {
            "status": "registered"
        }


    def route(
        self,
        name,
        payload=None
    ):

        tool = self.tools.get(name)


        if tool is None:

            return {
                "status": "failed",
                "error": "tool_not_found"
            }


        return tool(payload)
