# Online Quiz Application
name = input("Enter student name: ")                 # 1
usn = input("Enter student USN: ")                   # 2
subject = input("Enter subject name: ")              # 3
q1 = input("Who developed Python? ")                 # 4
q2 = input("Which symbol is used for comments in Python? ")  # 5
q3 = input("Which function is used to display output in Python? ")  # 6
q4 = input("Which keyword is used to define a function? ")  # 7
q5 = input("Which data type is used to store True or False? ")  # 8

# Calculate score
score = 0
if q1.lower() == "guido van rossum":
    score += 1
if q2 == "#":
   score += 1
if q3.lower() == "print()":
    score += 1
if q4.lower() == "def":
    score += 1
if q5.lower() == "bool":
    score += 1

# Display quiz result
print("\n--- Online Quiz Result ---")
print("Student Name:", name)
print("USN:", usn)
print("Subject:", subject)
print("Total Questions: 5")
print("Correct Answers:", score)
print("Wrong Answers:", 5 - score)
print("Total Score:", score, "/ 5")

if score >= 3:
    print("Result: PASS")
else:
    print("Result: FAIL")

# Save details to file
with open("quiz.txt", "a") as f:
    f.write(
        f"{name}, {usn}, {subject}, {score}/5\n"
    )
print("Quiz result saved successfully!")
