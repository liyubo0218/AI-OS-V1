from core.brain.providers.cloud.cloud_provider import CloudProvider


provider = CloudProvider()


result = provider.generate(
    "帮我测试AI-OS"
)


print("Cloud Provider Ready")

print(result)
