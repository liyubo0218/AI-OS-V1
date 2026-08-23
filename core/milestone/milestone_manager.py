class MilestoneManager:
    """
    AI-OS Milestone Manager V2.6

    负责：
    - 创建里程碑
    - 管理里程碑状态
    - 记录阶段进度

    不负责：
    - 创建任务
    - 执行任务
    - 修改目标
    """

    def __init__(self):
        self.milestones = []


    def create_milestone(
        self,
        milestone_id,
        goal_id,
        title,
        status="created",
        progress=0
    ):
        milestone = {
            "milestone_id": milestone_id,
            "goal_id": goal_id,
            "title": title,
            "status": status,
            "progress": progress
        }

        self.milestones.append(
            milestone
        )

        return milestone


    def update_milestone_status(
        self,
        milestone_id,
        status
    ):
        for milestone in self.milestones:
            if milestone["milestone_id"] == milestone_id:
                milestone["status"] = status
                return milestone

        return None


    def update_progress(
        self,
        milestone_id,
        progress
    ):
        for milestone in self.milestones:
            if milestone["milestone_id"] == milestone_id:
                milestone["progress"] = progress
                return milestone

        return None


    def get_milestone(
        self,
        milestone_id
    ):
        for milestone in self.milestones:
            if milestone["milestone_id"] == milestone_id:
                return milestone

        return None


    def get_milestones(
        self
    ):
        return self.milestones
