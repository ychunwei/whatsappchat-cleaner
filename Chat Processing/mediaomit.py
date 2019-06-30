with open("myside.txt","r+") as f:
    new_f = f.readlines()
    f.seek(0)
    for line in new_f:
        if "<Media omitted>" not in line:
            f.write(line)
    f.truncate()

with open("otherside.txt","r+") as f:
    new_f = f.readlines()
    f.seek(0)
    for line in new_f:
        if "<Media omitted>" not in line:
            f.write(line)
    f.truncate()