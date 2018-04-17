data = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

data = data.split()

for i in range(len(data)):
    ans = len(data[i].strip(','))
    print(ans, end="")
print("")
