class Organization:
    name = None

    def __init__(self, name):
        self.name = name

    def getname(self):
        return self.name


class Trainer:
    def __init__(self, Organization):
        self.Organization = Organization

    def getOrganization(self):
        return self.Organization


class Trainee:
    pass


class Training:
    def __init__(self, NumOfTrainees, TrainingOrganizationName, TrainingDurationInHrs):
        self.NumOfTrainees = NumOfTrainees
        self.TrainingOrganizationName = TrainingOrganizationName
        self.TrainingDurationInHrs = TrainingDurationInHrs

    def getNumOfTrainees(self):
        return self.NumOfTrainees

    def getTrainingOrganizationName(self):
        return self.TrainingOrganizationName

    def getTrainingDurationInHrs(self):
        return self.TrainingDurationInHrs


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
    durationHrs = None

    def __init__(self, durationHrs):
        self.durationHrs = durationHrs

    def getDurationHrs(self):
        return self.durationHrs


class Topic:
    name = None

    def __init__(self, name):
        self.name = name
