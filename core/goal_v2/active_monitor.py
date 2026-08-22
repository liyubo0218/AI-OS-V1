from .goal_tracker import GoalTracker
from .reminder_engine import ReminderEngine
from .deviation_detector import DeviationDetector


class ActiveGoalMonitor:


    def __init__(self):

        self.tracker = GoalTracker()

        self.reminder = ReminderEngine()

        self.deviation = DeviationDetector()



    def create_goal(
        self,
        goal_id,
        description
    ):

        return self.tracker.create_goal(
            goal_id,
            description
        )



    def monitor_goal(
        self,
        goal_id
    ):

        goal = self.tracker.get_goal(
            goal_id
        )


        return {

            "goal": goal,

            "reminder":
                self.reminder.check(goal),

            "deviation":
                self.deviation.check(goal)

        }
