#creates dictionaries for room number, teacher, and meeting time
roomNum = dict(CSC101 = "3004", CSC102 = "4501", CSC103 = "6755", NET110 = "1244", COM241 = "1411")
teach = dict(CSC101 = "Haynes", CSC102 = "Alvarado", CSC103 = "Rich", NET110 = "Burke", COM241 = "Lee")
meetTime = dict(CSC101 = "8:00 a.m.", CSC102 = "9:00 a.m.", CSC103 = "10:00 a.m.", NET110 = "11:00 a.m.", COM241 = "1:00 p.m.")

#asks user for course number and converts to uppercase
course_num = input("Enter course number: ").upper()

#try/catch to handle if a user inputs an invalid course number
try:
    print(roomNum[course_num])
    print(teach[course_num])
    print(meetTime[course_num])
except:
    print("Invalid course number")