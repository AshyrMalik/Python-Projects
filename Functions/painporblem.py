def paint_needed(height,width,coverage):
    return round((height*width)/coverage)


height = int(input("What is the height of the wall: "))
width = int(input("What is the width"))
coverage= int(input("what is the coverage per can"))
print("Pain required: ",paint_needed(height=height,width=width,coverage=coverage))