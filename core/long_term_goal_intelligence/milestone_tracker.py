class MilestoneTracker:


    def __init__(self):

        self.milestones = {}



    def update(
        self,
        milestone,
        status
    ):

        self.milestones[milestone] = status


        return {

            "status": "updated"

        }



    def get(
        self,
        milestone
    ):

        return self.milestones.get(
            milestone
        )
