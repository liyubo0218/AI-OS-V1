class ExecutionMonitor:
    """
    AI-OS Execution Monitor V2.4

    负责：
    - 记录执行状态
    - 更新执行状态
    - 查询执行状态

    不负责：
    - 执行任务
    - 控制设备
    - 自动恢复
    """

    def __init__(self):
        self.records = []


    def create_record(
        self,
        task_id,
        status="pending"
    ):
        record = {
            "task_id": task_id,
            "status": status
        }

        self.records.append(
            record
        )

        return record


    def update_status(
        self,
        task_id,
        status
    ):
        for record in self.records:
            if record["task_id"] == task_id:
                record["status"] = status
                return record

        return None


    def get_status(
        self,
        task_id
    ):
        for record in self.records:
            if record["task_id"] == task_id:
                return record

        return None


    def get_records(
        self
    ):
        return self.records
