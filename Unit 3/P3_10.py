import re

with open("F1 Winners 2026.txt", "r") as file:
    text = file.read()

winners = re.findall(r'Winner: (.+)', text)
laps = re.findall(r'Fastest Lap: ([\d:.]+)', text)
points = re.findall(r'Points: (\d+)', text)

print("Race Winners:", winners)
print("Fastest Laps:", laps)
print("Points:", points)
