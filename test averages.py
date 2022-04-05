#Isiah Williams
#Coding For All-P6
#Mr. Burns

studentnumber = int(input("How many students do you have?"))
testnumber = int(input("How many test scores per student?"))
total = 0

for student in range(1, studentnumber + 1):
  print(f"Student number {student}")
  print(f"--------------")
  total = 0
  for testnum in range(1, testnumber + 1):
    testscore = int(input("Please enter the test score for test number " + str(testnum)))
    total += testscore
  average = total / testnumber
  print("The average for student number " + str(student) + " is " + str(average))
  print("")