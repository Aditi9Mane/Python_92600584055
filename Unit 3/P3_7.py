import shutil
import os

s = "scenario_based_ques.txt"

with open(s, "w") as file:
    file.write("Scenario based questions in exams.")

shutil.copy(s, "copy_sce1.txt")
print("The file is copied")

shutil.move("copy_sce1.txt", "moved_sce1.txt")
print("The file is moved")

os.remove("moved_sce1.txt")
print("File is deleted")



