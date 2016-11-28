import re

def lookandsay(limit, sequence = 1):
    if limit > 1:
        return lookandsay(limit-1, "".join([str(len(match.group()))+match.group()[0] for matchNum, match in enumerate(re.finditer(r"(\w)\1*", str(sequence)))]))
    else:
        return sequence

print lookandsay(1)
#1
      
print lookandsay(2)
#11

print lookandsay(3)
#21

print lookandsay(4)
#1211

print lookandsay(5)
#111221