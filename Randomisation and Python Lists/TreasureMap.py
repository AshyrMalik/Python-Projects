line1= ["⬛","⬛","⬛"]
line2= ["⬛","⬛","⬛"]
line3= ["⬛","⬛","⬛"]


print(f" {line1}\n {line2}\n {line3}")
maps = [line1, line2, line3]

loc= input("choose location for hiding treasure! X marks the spot: ")

if loc.__contains__("A"):
    maps[int(loc[1])-1][0]= "X"

elif loc.__contains__("B"):
    maps[int(loc[1])-1][1]= "X"

else:
    maps[int(loc[1])-1][2]= "X"

print(f"{line1}\n {line2}\n {line3}")
