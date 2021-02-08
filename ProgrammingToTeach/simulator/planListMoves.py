class PlanListMoves:
    def __init__(self, plan = []):
        self.plan = plan
        self.step = 0
        print("PLANOOOO: ", self.plan)
    def do(self):
        if self.step == len(self.plan):
            return (False, True)
        else:
            self.step += 1
            return (self.plan[self.step-1], False)
