from Train import *

# OR
# from Train import Training
# from Train import Trainee
# from Train import Trainer
# from Train import Organization
# from Train import Course
# from Train import Module
# from Train import Unit
# from Train import Topic

training = Training(10, "10 seconds LTD.", 60)
print("Number of Trainees =", training.getNumOfTrainees())
print("Name of the Organization =", training.getTrainingOrganizationName())
print("Training Duration In Hours =", training.getTrainingDurationInHrs(), "Hrs")

print("----------------------------------------------------------------------")

trainer = Trainer("10 second LTD.")
print("Organization =", trainer.getOrganization())

print("----------------------------------------------------------------------")

organization = Organization("10 second LTD.")
print("Name =", organization.getname())

print("----------------------------------------------------------------------")

mods = ["Java", "Python", "C/C++"]
course = Course(mods)
print("Modules in Course =", course.getModules())

print("----------------------------------------------------------------------")

uts = ["String Methods", "Class n Objects", "Packages"]
module = Module(uts)
print("Units in Module =", module.getUnits())

print("----------------------------------------------------------------------")

unit = Unit(3)
print("Duration in Hours =",unit.getDurationHrs(), "Hrs")

print("----------------------------------------------------------------------")

topic = Topic("Inheritence")
print("Topic Name =", topic.name)

print("\n *===============**===============**===============**===============*\n")