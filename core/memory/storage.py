import json
import os
from datetime import datetime


class MemoryStorage:
    """
    AI-OS 本地记忆存储层

    负责：
    - 保存长期记忆
    - 读取用户信息
    - 保存历史数据

    不负责：
    - AI推理
    - 任务规划
    """

    def __init__(
        self,
        path="data/memory.json"
    ):
        self.path = path

        self._ensure_storage()


    def _ensure_storage(
        self
    ):
        directory = os.path.dirname(
            self.path
        )

        if directory:
            os.makedirs(
                directory,
                exist_ok=True
            )

        if not os.path.exists(
            self.path
        ):
            self._write(
                {}
            )


    def _read(
        self
    ):
        with open(
            self.path,
            "r",
            encoding="utf-8"
        ) as file:
            return json.load(
                file
            )


    def _write(
        self,
        data
    ):
        with open(
            self.path,
            "w",
            encoding="utf-8"
        ) as file:
            json.dump(
                data,
                file,
                ensure_ascii=False,
                indent=2
            )


    def save(
        self,
        key,
        value
    ):
        data = self._read()

        data[key] = {
            "value": value,
            "updated": datetime.now().isoformat()
        }

        self._write(
            data
        )

        return True


    def get(
        self,
        key
    ):
        data = self._read()

        item = data.get(
            key
        )

        if not item:
            return None

        return item.get(
            "value"
        )


    def delete(
        self,
        key
    ):
        data = self._read()

        if key in data:
            del data[key]

            self._write(
                data
            )

        return True


    def all(
        self
    ):
        return self._read()


    def clear(
        self
    ):
        self._write(
            {}
        )

        return True
