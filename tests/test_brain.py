from core.brain.brain import Brain


brain = Brain()


context = {
    "user_input": "帮我测试AI-OS"
}


result = brain.understand(context)


print("Brain Ready")

print("Input:")
print(context["user_input"])

print("Understanding:")
print(result)
