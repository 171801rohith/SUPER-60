class Organization:
    def __init__(self, name):
        self.name = name

    def getname(self):
        return self.name


class Trainer:
    def __init__(self, name, Organization):
        self.name = name
        self.Organization = Organization

    def getOrganization(self):
        return self.Organization.getname()


class Trainee:
    def __init__(self, traineeName):
        self.traineeName = traineeName


class Course:
    def __init__(self, module):
        self.module = module

    def getModules(self):
        return self.module


class Module:
    def __init__(self, unit):
        self.unit = unit

    def getUnits(self):
        return self.unit


class Unit:
    def __init__(self, durationHrs):
        self.durationHrs = durationHrs

    def getDurationHrs(self):
        return self.durationHrs


class Topic:
    def __init__(self, name):
        self.name = name


class Training:
    def __init__(self, Trainer, Trainee, Course):
        self.Trainer = Trainer
        self.Trainee = Trainee
        self.Course = Course

    def getNumOfTrainees(self):
        return len(self.Trainee)

    def getTrainingOrganizationName(self):
        return self.Trainer.getOrganization()

    def getTrainingDurationInHrs(self):
        totalDuration = 0
        for M in self.Course.getModules():
            for U in M.getUnits():
                totalDuration += U.getDurationHrs()
        return totalDuration
