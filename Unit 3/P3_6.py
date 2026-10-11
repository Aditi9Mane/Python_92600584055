import os 
import sys

path = r"C:\Users\DELL\Desktop\tableau-ultimate-course-main\projects\sales-dashboard-project"

print("Base Name:", os.path.basename(path))

print("\nDirectory Name:", os.path.dirname(path))

print("\nIs Absolute Path:", os.path.isabs(path))

print("\nIs Directory:", os.path.isdir(path))

print("\nIs File:", os.path.isfile(path))

print("\nCommand-line Arguments:", sys.argv)

print("\nPython Version:", sys.version)