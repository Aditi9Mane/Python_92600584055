import re

txt = "hungry cats lash out not because they are mean, but because they are hungry."

res = re.match("mean", txt)
print("Match:", res.group() if res else "No match")

reslt = re.search("hungry", txt)
print("Search:", reslt.group() if reslt else "No match")

result = re.findall("hungry", txt)
print("Find All:", result)