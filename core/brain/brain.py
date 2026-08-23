from .context.brain_adapter import BrainAdapter
from .memory_adapter import MemoryContextAdapter


class Brain:

    def __init__(
        self,
        llm_gateway=None,
        memory_service=None
    ):

        self.llm_gateway = llm_gateway
        self.context_adapter = BrainAdapter()
        self.memory_adapter = MemoryContextAdapter(
            memory_service=memory_service
        )


    def understand(
        self,
        context
    ):

        user_input = context.get(
            "user_input",
            ""
        )

        context_result = self.context_adapter.understand(
            user_input
        )
        memory_context = self.memory_adapter.get_memory_context(
            user_input
        )


        result = {
            "intent": "unknown",
            "goal": user_input,
            "entities": [],
            "confidence": 0.5,
            "context": context_result,
            "memory_context": memory_context
        }


        # Rule Engine

        if "测试" in user_input:

            result["intent"] = "test_system"

            result["entities"] = [
                "AI-OS"
            ]

            result["confidence"] = 0.95


            return result


        elif "文件" in user_input:

            result["intent"] = "file_task"

            result["entities"] = [
                "文件"
            ]

            result["confidence"] = 0.8


            return result



        # LLM fallback

        if self.llm_gateway:

            response = self.llm_gateway.generate(
                user_input
            )


            return {

                "intent":
                "llm_reasoning",


                "goal":
                user_input,


                "entities":
                [],


                "confidence":
                response.get(
                    "confidence",
                    0.7
                ),


                "llm_response":
                response,
                "context":
                context_result,
                "memory_context":
                memory_context

            }


        return result
