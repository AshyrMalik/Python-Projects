student_height = input("Enter the height of students: ").split()

for n in range(0,len(student_height)):
    student_height[n]= int(student_height[n])

sum = 0
for i in range(0,len(student_height)):
    sum +=student_height[i]

Average = sum/len(student_height)

print("Average height is: " , Average)