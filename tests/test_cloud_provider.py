from ai_gateway.providers.cloud_provider import CloudProvider


provider = CloudProvider()


result = provider.generate(
    "帮我测试AI-OS"
)


print("Cloud Provider Ready")

print(result)
