from core.brain.brain import Brain
from core.brain.llm_gateway import LLMGateway


gateway = LLMGateway()


brain = Brain(
    gateway
)


context = {
    "user_input": "帮我测试AI-OS"
}


result = brain.understand(
    context
)


print("Brain LLM Mode Ready")

print("Understanding:")

print(result)
