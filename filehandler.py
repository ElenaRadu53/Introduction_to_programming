file = open("student_info.txt","a")
file.write("John Doe, Networking, 45, 50\n")
file.write("John Doe, Cyber security, 50, 25\n")
file.write("John Doe, Programming, 60, 25\n")
file.close()

with open ("student_info.txt" ,"r") as firstfile, open ("student_grades.txt","a") as secondfile:
    for line in firstfile:
        secondfile.write(line)
        print(line)

# I was able to create a program that makes a text file called student_info which includes a student name, course, grade and weight.
# This original text file is then read and copied onto another text file called student_grades.
# The text in student_grades is then printed out
# I wasn't able to figure out how to take the original information and convert it into the students final grade and mark. 
