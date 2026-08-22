from .context_model import ContextModel


class ContextManager:


    def __init__(self):

        self.context = None


    def create(
        self,
        user=None,
        task=None
    ):

        self.context = ContextModel(
            user,
            task
        )

        return self.context.to_dict()


    def get(self):

        if self.context is None:

            return None


        return self.context.to_dict()
