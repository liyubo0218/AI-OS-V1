import sqlite3


class MemoryStorage:

    def __init__(
        self,
        db_path="memory/aios_memory.db"
    ):

        self.db_path = db_path

        self.init_database()


    def init_database(self):

        conn = sqlite3.connect(
            self.db_path
        )

        cursor = conn.cursor()


        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS memories (

                id INTEGER PRIMARY KEY AUTOINCREMENT,

                memory_id TEXT,

                memory_type TEXT,

                content TEXT

            )
            """
        )


        conn.commit()

        conn.close()



    def save(
        self,
        memory_id,
        memory_type,
        content
    ):

        conn = sqlite3.connect(
            self.db_path
        )

        cursor = conn.cursor()


        cursor.execute(
            """
            INSERT INTO memories
            (
                memory_id,
                memory_type,
                content
            )

            VALUES (?, ?, ?)
            """,
            (
                memory_id,
                memory_type,
                content
            )
        )


        conn.commit()

        conn.close()



    def get_all(self):

        conn = sqlite3.connect(
            self.db_path
        )

        cursor = conn.cursor()


        cursor.execute(
            """
            SELECT
                memory_id,
                memory_type,
                content

            FROM memories
            """
        )


        rows = cursor.fetchall()


        conn.close()


        return [
            {
                "memory_id": row[0],
                "type": row[1],
                "content": row[2]
            }

            for row in rows
        ]
