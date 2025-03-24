# Problem Statement 5: Hiring Class
# 1. Create a Hiring class.
# 2. Attributes:
# a. Duration of technical rounds: 20 days.
# b. Duration of manager round: 5 days.
# c. Duration of HR round: 5 days.
# d. Duration of offer rollout: 10 days.
# 3. Pass the Employee and Hiring objects to the Console class and print the hiring
# process durations.


class Hiring:
    def __init__(
        self, tech_round_dur=20, manager_round=5, HR_round=5, offer_rollout=10
    ):
        self.tech_round_dur = tech_round_dur
        self.manager_round = manager_round
        self.HR_round = HR_round
        self.offer_rollout = offer_rollout

    def process_duration(self):
        print(
            "Process Duration:",
            self.tech_round_dur
            + self.HR_round
            + self.manager_round
            + self.offer_rollout,
        )
