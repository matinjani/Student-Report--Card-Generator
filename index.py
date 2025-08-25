students={}

students_name=input("enter the student name.")
roll_no=input("enter the roll no of student.")
marks={}
for  i in range(1,6):
  subject=input(f"enter name of subject{i}")
  score=int(input(f"enter the marks for {subject}"))
  marks[subject]=score
students[students_name]={
     "roll no":roll_no,
     "marks":marks
}
total =sum(marks.values())

average=total/5

if average>=90:
 grade="A+"
elif average >=80:
  grade="A"
elif average>=70:
  grade="B"
elif average>=60:
  grade="C"
elif average>=50:
  grade="D"
elif average>=40:
  grade="E"
else:
  grade="F"
print("\n\tStudent report card")
print(f"Student name : {students_name}")
print(f"Marks {marks}")
print(f"Roll no : {roll_no}")
print(f"Total :  {total}")
print(f"Average : {average}")
print(f"Grade : {grade}")