from .preference_memory import PreferenceMemory
from .history_memory import HistoryMemory
from .memory_retriever import MemoryRetriever


class MemoryEngine:


    def __init__(self):

        self.preference = PreferenceMemory()

        self.history = HistoryMemory()

        self.retriever = MemoryRetriever()



    def save_preference(
        self,
        user_id,
        data
    ):

        return self.preference.save(
            user_id,
            data
        )



    def get_preference(
        self,
        user_id
    ):

        return self.preference.get(
            user_id
        )



    def save_history(
        self,
        record
    ):

        return self.history.save(
            record
        )



    def search(
        self,
        keyword
    ):

        return self.retriever.search(
            self.history.get_all(),
            keyword
        )
