from .storage import MemoryStorage
from .user_memory import UserMemory
from .task_memory import TaskMemory


class MemoryManager:


    def __init__(self):

        self.storage = MemoryStorage()

        self.user = UserMemory(
            self.storage
        )

        self.task = TaskMemory(
            self.storage
        )


    def save_user(
        self,
        user_id,
        profile
    ):

        return self.user.save_profile(
            user_id,
            profile
        )


    def get_user(
        self,
        user_id
    ):

        return self.user.get_profile(
            user_id
        )


    def save_task(
        self,
        task_id,
        task
    ):

        return self.task.save_task(
            task_id,
            task
        )


    def get_task(
        self,
        task_id
    ):

        return self.task.get_task(
            task_id
        )
