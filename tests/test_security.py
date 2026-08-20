from security.security_manager import SecurityManager


security = SecurityManager()


low_task = {
    "task": "测试AI-OS"
}


high_task = {
    "task": "删除全部文件"
}


print("Low Risk Test:")

print(
    security.check_permission(
        low_task
    )
)


print("High Risk Test:")

print(
    security.check_permission(
        high_task
    )
)
