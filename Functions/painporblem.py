def paint_needed(height,width,coverage):
    paint_req= round((height*width)/coverage)
    return paint_req


height = int(input("What is the height of the wall: "))
width = int(input("What is the width: "))
coverage= int(input("what is the coverage per can: "))
print("Paint required: ",paint_needed(height=height,width=width,coverage=coverage))