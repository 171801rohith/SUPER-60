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

organization = Organization("10 second LTD.")
print("Name =", organization.getname())

print("----------------------------------------------------------------------")

trainer1 = Trainer("Yayha", organization)
print("Trainer =", trainer1.getOrganization())

print("----------------------------------------------------------------------")

trainee1 = Trainee("Aadhithya")
trainee2 = Trainee("Abhishek")

print("----------------------------------------------------------------------")

unit1 = Unit(3)
unit2 = Unit(5)
unit3 = Unit(1)
print("Duration in Hours =", unit1.getDurationHrs(), "Hrs")
print("Duration in Hours =", unit2.getDurationHrs(), "Hrs")
print("Duration in Hours =", unit3.getDurationHrs(), "Hrs")

print("----------------------------------------------------------------------")

module1 = Module([unit1, unit2, unit3])
print("Units in Module =", module1.getUnits())

print("----------------------------------------------------------------------")

course = Course([module1])
print("Modules in Course =", course.getModules())

print("----------------------------------------------------------------------")

training = Training(trainer1, [trainee1, trainee2], course)
print("Number of Trainees =", training.getNumOfTrainees())
print("Name of the Organization =", training.getTrainingOrganizationName())
print("Training Duration In Hours =", training.getTrainingDurationInHrs(), "Hrs")

print("----------------------------------------------------------------------")

topic = Topic("Inheritence")
print("Topic Name =", topic.name)

print("\n *===============**===============**===============**===============*\n")
