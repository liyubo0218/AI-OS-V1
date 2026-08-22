from .language_parser import LanguageParser
from .goal_extractor import GoalExtractor
from .context_interpreter import ContextInterpreter


class BrainAdapter:


    def __init__(self):

        self.parser = LanguageParser()

        self.goal_extractor = GoalExtractor()

        self.context_interpreter = ContextInterpreter()



    def understand(
        self,
        text
    ):

        parsed = self.parser.parse(
            text
        )


        goal = self.goal_extractor.extract(
            parsed
        )


        context = self.context_interpreter.interpret(
            parsed
        )


        return {

            "intent": self._intent(goal),

            "goal": goal["goal"],

            "context": context

        }



    def _intent(
        self,
        goal
    ):

        if goal["goal"] == "reminder_task":

            return "reminder"


        if goal["goal"] == "general_task":

            return "task"


        return "unknown"
