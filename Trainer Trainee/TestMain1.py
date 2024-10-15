from Train import *

print("Entering All details :\n")

training = Training(
    int(input("Enter no. of  trainees : ")),
    input("Enter organization name : "),
    int(input("Enter training duration in hrs : ")),
)
print("-----------------------------------")
trainer = Trainer(input("Enter organization : "))
print("-----------------------------------")
organization = Organization(input("Enter organization name : "))
print("-----------------------------------")
mods = []
for i in range(int(input("Enter no. of modules : "))):
    mods.append(input("Enter the module : "))
course = Course(mods)
print("-----------------------------------")
uts = []
for i in range(int(input("Enter no. of units : "))):
    uts.append(input("Enter the unit : "))
module = Module(uts)
print("-----------------------------------")
unit = Unit(int(input("Enter duration in hours : ")))
print("-----------------------------------")
topic = Topic(input("Enter topic : "))
print("-----------------------------------")

print("Displaying All Details :\n")

print("----------------------------------------------------------------------")

print("Number of Trainees =", training.getNumOfTrainees())
print("Name of the Organization =", training.getTrainingOrganizationName())
print("Training Duration In Hours =", training.getTrainingDurationInHrs(), "Hrs")

print("----------------------------------------------------------------------")

print("Organization =", trainer.getOrganization())

print("----------------------------------------------------------------------")

print("Name =", organization.getname())

print("----------------------------------------------------------------------")

print("Modules in Course =", course.getModules())

print("----------------------------------------------------------------------")

print("Units in Module =", module.getUnits())

print("----------------------------------------------------------------------")

print("Duration in Hours =", unit.getDurationHrs(), "Hrs")

print("----------------------------------------------------------------------")

print("Topic Name =", topic.name)

print("\n *===============**===============**===============**===============*\n")
