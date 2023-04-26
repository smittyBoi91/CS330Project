import tkinter as tk


class CourseInfo:
    def __init__(self, courseName: str, instructor: str, code: str, secNum: int, credit: int):
        self.courseName = courseName
        self.instructor = instructor
        self.code = code
        self.secNum = secNum
        self.credit = credit

    def changeName(self, newName: str):
        self.courseName = newName

    def changeInstructor(self, newInstructor: str):
        self.instructor = newInstructor

    def changeCode(self, newCode: str):
        self.code = newCode

    def changeSecNum(self, newSecNum: int):
        self.secNum = newSecNum

    def changeCredit(self, newCredit: int):
        self.credit = newCredit


class TimeAndLocation:
    def __init__(self, time: str, days: [], location: str):
        self.time = time
        self.days = days
        self.location = location

    def changeTime(self, newTime: int):
        self.time = newTime

    def changeDays(self, newDays: []):
        self.days = newDays

    def changeLocation(self, newLocation: str):
        self.location = newLocation

class Course:
    def __init__(self, TimeAndLocation: TimeAndLocation, CourseInfo: CourseInfo, conflict: bool):
        self.TimeAndLocation = TimeAndLocation
        self.CourseInfo = CourseInfo
        self.conflict = conflict

    def changeTimeAndLocation(self, newTimeAndLoc: TimeAndLocation):
        self.TimeAndLocation = newTimeAndLoc

    def changeCourseInfo(self, newInfo: CourseInfo):
        self.info = newInfo


class Timetable:
    def __init__(self):
        self.courses = []
        self.schedule = [Course]
        self.week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        self.times = ["8am", "9am", "10am", "11am", "12pm", "1pm", "2pm", "3pm", "4pm", "5pm"]
        # dict for avail room times
        self.roomTimes = {}
        # dict for avail professor times
        self.profTimes = {}

    def checkProfTime(self, prof: str, days: [], time: str) -> bool:
        timeAvail = True
        timeDict = {"Monday": ["8am", "9am", "10am", "11am", "12pm", "1pm", "2pm", "3pm", "4pm", "5pm"],
                "Tuesday": ["8am", "9am", "10am", "11am", "12pm", "1pm", "2pm", "3pm", "4pm", "5pm"],
                "Wednesday": ["8am", "9am", "10am", "11am", "12pm", "1pm", "2pm", "3pm", "4pm", "5pm"],
                "Thursday": ["8am", "9am", "10am", "11am", "12pm", "1pm", "2pm", "3pm", "4pm", "5pm"],
                "Friday": ["8am", "9am", "10am", "11am", "12pm", "1pm", "2pm", "3pm", "4pm", "5pm"]}

        if prof in self.profTimes:
            oldProfTimes = self.profTimes.get(prof)
            for i in range(len(days)):
                availableDayTimes = oldProfTimes.get(days[i])
                if time in availableDayTimes:
                    availableDayTimes.remove(time)
                    oldProfTimes[days[i]] = availableDayTimes
                else:
                    timeAvail = False
        if prof not in self.profTimes:
            newProfTimes = timeDict
            for i in range(len(days)):
                availableDayTimes = newProfTimes.get(days[i])
                if time in availableDayTimes:
                    availableDayTimes.remove(time)
                    newProfTimes[days[i]] = availableDayTimes
            self.profTimes[prof] = newProfTimes
        return timeAvail

    def checkRoomTime(self, room: str, days: [], time: str) -> bool:
        timeAvail = True
        timeDict = {"Monday": ["8am", "9am", "10am", "11am", "12pm", "1pm", "2pm", "3pm", "4pm", "5pm"],
                "Tuesday": ["8am", "9am", "10am", "11am", "12pm", "1pm", "2pm", "3pm", "4pm", "5pm"],
                "Wednesday": ["8am", "9am", "10am", "11am", "12pm", "1pm", "2pm", "3pm", "4pm", "5pm"],
                "Thursday": ["8am", "9am", "10am", "11am", "12pm", "1pm", "2pm", "3pm", "4pm", "5pm"],
                "Friday": ["8am", "9am", "10am", "11am", "12pm", "1pm", "2pm", "3pm", "4pm", "5pm"]}

        if room in self.roomTimes:
            oldRoomTimes = self.roomTimes.get(room)
            for i in range(len(days)):
                availableRoomTimes = oldRoomTimes.get(days[i])
                if time in availableRoomTimes:
                    availableRoomTimes.remove(time)
                    oldRoomTimes[days[i]] = availableRoomTimes
                else:
                    timeAvail = False
        if room not in self.roomTimes:
            newRoomTimes = timeDict
            for i in range(len(days)):
                availableRoomTimes = newRoomTimes.get(days[i])
                if time in availableRoomTimes:
                    availableRoomTimes.remove(time)
                    newRoomTimes[days[i]] = availableRoomTimes
            self.roomTimes[room] = newRoomTimes
        return timeAvail

    def checkTimeAvailable(self, days: list, time: str) -> bool:
        timeAvail = True
        numDays = len(days)
        for i in range(numDays):
            times = self.availableTimes.get(days[i])
            if time in times:
                dayTimes = self.availableTimes[days[i]]
                dayTimes.remove(time)
                self.availableTimes[days[i]] = dayTimes
            else:
                timeAvail = False
        return timeAvail

    def getAvailableTimes(self, day: str):
        print(self.availableTimes[day])

    def addCourse(self, course: Course):
        self.courses.append(course)

    def sortByDay(self):
        temp = []
        for dayOfWeek in self.week:
            index = 0
            i = 0
            for course in self.courses:
                courseDay = self.courses[i].TimeAndLocation.days[0]
                if courseDay == dayOfWeek:
                    temp.append(self.courses[i])
                    index += 1
                    i += 1
                else:
                    i += 1
        self.courses = temp

    def printCourses(self):
        for i in range(len(self.courses)):
            print(f"{i}: {self.courses[i].CourseInfo.courseName}")

    def checkConflicts(self, days: list, time: str) -> bool:
        conflict = False
        for c in self.courses:
            if c.TimeAndLocation.days == days and c.TimeAndLocation.time \
                    == time:
                conflict = True
        return conflict

    def checkTime(self, time: str) -> bool:
        timeFound = False
        for i in self.times:
            if i == time:
                timeFound = True
        return timeFound

    def checkDay(self, day: str) -> bool:
        dayFound = False
        for i in self.week:
            if i == day:
                dayFound = True
        return dayFound

    def createCourse(self) -> Course:
        # -------------------------Time and Location-----------------------------------------
        days = []
        numDays = input("How many days will the class meet e.g. 1,2,3:")
        while numDays.isdigit() == False:
            numDays = input("Please enter a valid number of days e.g. 1, 2, 3:")
        numDays = int(numDays)
        while numDays > 3:
            numDays = input("Classes dont meet more than 3 times per week, please enter a valid number: ")
            numDays = int(numDays)
        for i in range(numDays):
            if i == 0:
                day = input("What is the first day the course meets:")
                day = day.capitalize()
                dayCheck = self.checkDay(day)
                if dayCheck == False:
                    while dayCheck == False:
                        day = input("Please enter a valid day:")
                        day = day.capitalize()
                        dayCheck = self.checkDay(day)
                days.append(day)
            else:
                day = input("What is the next day the course meets:")
                day = day.capitalize()
                dayCheck = self.checkDay(day)
                if dayCheck == False:
                    while dayCheck == False:
                        day = input("Please enter a valid day:")
                        day = day.capitalize()
                        dayCheck = self.checkDay(day)
                days.append(day)
        time = input("Please enter the start time of the course e.g. 8am, 9am, 4pm:")
        timeCheck = self.checkTime(time)
        while timeCheck == False:
            time = input("Please enter a time between 8am and 5pm e.g. 9am, 11am, 4pm:")
            timeCheck = self.checkTime(time)
        # while conflicts == False:
        #     time = input("This Start time is not available, please choose another time:")
        #     timeCheck = self.checkTime(time)
        #     conflicts = self.checkTimeAvailable(days, time)
        building = input("Please enter the 4 letter building acronym e.g. BHSN:")
        while len(building) != 4:
            building = input("Building acronym must be 4 letters, please enter a valid acronym:")
        building = building.upper()
        roomNum = input("Please enter the 3 digit room number:")
        while len(roomNum) != 3:
            roomNum = input("Room number must be 3 digits, please enter a valid room number:")
        location = building + " " + roomNum
        roomAvailable = self.checkRoomTime(location, days, time)
###-------------------TEST THIS ON WEDNESDAY-------------------###
        while roomAvailable == False:
            roomOrTime = input("That time is unavailable, press T to change the time or R to change the room")
            roomOrTime = roomOrTime.upper()
            if roomOrTime == "T":
                # can show available times here
                time = input("Please enter a time between 8am and 5pm e.g. 9am, 11am, 4pm:")
                timeCheck = self.checkTime(time)
                roomAvailable = self.checkRoomTime(location, days, time)
            if roomOrTime == "R":
                building = input("Please enter the 4 letter building acronym e.g. BHSN:")
                while len(building) != 4:
                    building = input("Building acronym must be 4 letters, please enter a valid acronym:")
                building = building.upper()
                roomNum = input("Please enter the 3 digit room number:")
                while len(roomNum) != 3:
                    roomNum = input("Room number must be 3 digits, please enter a valid room number:")
                location = building + " " + roomNum
                self.checkRoomTime(location, days, time)
        timeAndLocation = TimeAndLocation(time, days, location)
        # -------------------------Course Info-----------------------------------------
        courseName = input("Please enter the course name:")
        while len(courseName) == 0:
            courseName = input("Please enter a valid course name:")
        instructor = input("Please enter the instructors name:")
        while len(instructor) == 0:
            instructor = input("Please enter a valid instructor name:")
        instructorAvail = self.checkProfTime(instructor, days, time)
        while instructorAvail == False:
            roomOrTime = input("That time is unavailable, press I to change the instructor or T to change the room")
            roomOrTime = roomOrTime.upper()
            if roomOrTime == T:
                # can show available times here
                time = input("Please enter a time between 8am and 5pm e.g. 9am, 11am, 4pm:")
                timeCheck = self.checkTime(time)
                self.checkRoomTime(location, days, time)
            if roomOrTime == I:
                instructor = input("Please enter the instructors name:")
                while len(instructor) == 0:
                    instructor = input("Please enter a valid instructor name:")
                instructorAvail = self.checkProfTime(instructor, days, time)
                location = building + " " + roomNum
                self.checkRoomTime(location, days, time)
        code = input("Please enter the course code e.g. CS160:")
        while len(code) == 0:
            code = input("Please enter a valid course code e.g. CS160:")
        secNum = input("Please enter the section number e.g. 01, 02:")
        while len(secNum) == 0:
            secNum = input("Please enter a valid section number e.g. 01, 02:")
        secNum = int(secNum)
        credit = input("Please enter the course credit e.g. 1, 2, 3 ")
        while len(credit) == 0:
            credit = input("Please enter a valid course credit: 1, 2, 3")
        credit = int(credit)
        info = CourseInfo(courseName, instructor, code, secNum, credit)
        course = Course(timeAndLocation, info, False)
        return course

    def editCourse(self):
        stillEditing = True
        numCourses = len(self.courses)
        while (stillEditing):
            self.printCourses()
            courseToEdit = input("Please enter the number for the course you would like to edit:")
            while len(courseToEdit) > 1 or len(courseToEdit) < 1:
                courseToEdit = input("Please enter a valid number for the course you would like to edit:")
            courseToEdit = int(courseToEdit)
            while courseToEdit < 0 or courseToEdit > (numCourses - 1):
                courseToEdit = input(f"Please enter a valid number between 0 and {numCourses - 1} for "
                                     f"the course you would like to edit:")
                courseToEdit = int(courseToEdit)
            course = self.courses[courseToEdit]
            edit = input("What would you like to edit? Press I for course info or T for time and location:")
            if len(edit) != 1:
                edit = input("Please enter I to edit course info or T for time and location")
            edit = edit.upper()
            if edit == "I":
                editList = ["to edit course name", "for edit instructor name", "to edit course code",
                            "to edit section number", "to edit credits"]
                for i in range(len(editList)):
                    print(f"press {i} {editList[i]}")
                editChoice = input("Please enter the number that corresponds to the info you want to edit:")
                editChoice = int(editChoice)
                while editChoice > 4 or editChoice < 0:
                    editChoice = input("Please enter the number that corresponds to the info you want to edit:")
                    editChoice = int(editChoice)
                if editChoice == 0:
                    print(f"The current course name is {course.CourseInfo.courseName}")
                    newCourseName = input("What is the new course name?:")
                    while len(newCourseName) == 0:
                        newCourseName = input("Please enter a valid name for the course:")
                    course.CourseInfo.courseName = newCourseName
                    print(f"Course name updated to {newCourseName}")
                    done = input("Continue editing? Enter Y for yes, N for no:")
                    while len(done) != 1:
                        done = input("Please enter Y to keep editing or N to stop editing:")
                    done = done.upper()
                    if done == "N":
                        stillEditing = False
                elif editChoice == 1:
                    print(f"The current instructor name is {course.CourseInfo.instructor}")
                    newInstructorName = input("What is the new instructor name?:")
                    while len(newInstructorName) == 0:
                        newInstructorName = input("Please enter a valid name for the instructor:")
                    course.CourseInfo.instructor = newInstructorName
                    print(f"Course instructor updated to {newInstructorName}")
                    done = input("Continue editing? Enter Y for yes, N for no:")
                    while len(done) != 1:
                        done = input("Please enter Y to keep editing or N to stop editing:")
                    done = done.upper()
                    if done == "N":
                        stillEditing = False
                elif editChoice == 2:
                    print(f"The current code is {course.CourseInfo.code}")
                    newCode = input("What is the new code?:")
                    while len(newCode) == 0:
                        newCourseName = input("Please enter a valid name for the course:")
                    course.CourseInfo.code = newCode
                    print(f"Course code updated to {newCode}")
                    done = input("Continue editing? Enter Y for yes, N for no:")
                    while len(done) != 1:
                        done = input("Please enter Y to keep editing or N to stop editing:")
                    done = done.upper()
                    if done == "N":
                        stillEditing = False
                elif editChoice == 3:
                    print(f"The current section number is {course.CourseInfo.secNum}")
                    newSecNum = input("What is the new section number?:")
                    while len(newSecNum) == 0:
                        newSecNum = input("Please enter a valid section number for the course:")
                    course.CourseInfo.SecNum = newSecNum
                    print(f"Course name updated to {newSecNum}")
                    done = input("Continue editing? Enter Y for yes, N for no:")
                    while len(done) != 1:
                        done = input("Please enter Y to keep editing or N to stop editing:")
                    done = done.upper()
                    if done == "N":
                        stillEditing = False
                elif editChoice == 4:
                    print(f"The current credits for the course is {course.CourseInfo.credit}")
                    newCredit = input("What is the new number of credits?:")
                    while len(newCredit) == 0:
                        newCredit = input("Please enter a valid number of credits for the course:")
                    course.CourseInfo.credit = newCredit
                    print(f"Course credits updated to {newCredit}")
                    done = input("Continue editing? Enter Y for yes, N for no:")
                    while len(done) != 1:
                        done = input("Please enter Y to keep editing or N to stop editing:")
                    done = done.upper()
                    if done == "N":
                        stillEditing = False
            if edit == "T":
                editList = ["to edit the time", "to edit the days", "to edit the location", ]
                for i in range(len(editList)):
                    print(f"press {i} {editList[i]}")
                editChoice = input("Please enter the number that corresponds to the info you want to edit:")
                editChoice = int(editChoice)
                while editChoice > 2 or editChoice < 0:
                    editChoice = input("Please enter the number that corresponds to the info you want to edit:")
                    editChoice = int(editChoice)
                if editChoice == 0:
                    print(f"The current start time for the course is {course.TimeAndLocation.time}")
                    newTime = input("What is the new time?:")
                    timeCheck = self.checkTime(newTime)
                    while timeCheck == False:
                        time = input("Please enter a time between 8am and 5pm e.g. 9am, 11am, 4pm:")
                        timeCheck = self.checkTime(time)
                    course.TimeAndLocation.time = newTime
                    print(f"Course time updated to {newTime}")
                    done = input("Continue editing? Enter Y for yes, N for no:")
                    while len(done) != 1:
                        done = input("Please enter Y to keep editing or N to stop editing:")
                    done = done.upper()
                    if done == "N":
                        stillEditing = False
                elif editChoice == 1:
                    newDays = []
                    print(f"The current days for the course are {course.TimeAndLocation.days}")
                    numDays = input("How many days will the class meet e.g. 1,2,3:")
                    while numDays.isdigit() == False:
                        numDays = input("Please enter a valid number of days e.g. 1, 2, 3:")
                    numDays = int(numDays)
                    while numDays > 3:
                        numDays = input("Classes dont meet more than 3 times per week, please enter a valid number: ")
                        numDays = int(numDays)
                    for i in range(numDays):
                        if i == 0:
                            day = input("What is the first day the course meets:")
                            day = day.capitalize()
                            dayCheck = self.checkDay(day)
                            if dayCheck == False:
                                while dayCheck == False:
                                    day = input("Please enter a valid day:")
                                    day = day.capitalize()
                                    dayCheck = self.checkDay(day)
                            newDays.append(day)
                        else:
                            day = input("What is the next day the course meets:")
                            day = day.capitalize()
                            dayCheck = self.checkDay(day)
                            if dayCheck == False:
                                while dayCheck == False:
                                    day = input("Please enter a valid day:")
                                    day = day.capitalize()
                                    dayCheck = self.checkDay(day)
                            newDays.append(day)
                    course.TimeAndLocation.days = newDays
                    print(f"The new days for the course are{course.TimeAndLocation.days}")
                    done = input("Continue editing? Enter Y for yes, N for no:")
                    while len(done) != 1:
                        done = input("Please enter Y to keep editing or N to stop editing:")
                    done = done.upper()
                    if done == "N":
                        stillEditing = False
                elif editChoice == 2:
                    print(f"The current location is {course.TimeAndLocation.location}")
                    newLocation = input("What is the new location?:")
                    building = input("Please enter the 4 letter building acronym e.g. BHSN:")
                    while len(building) != 4:
                        building = input("Building acronym must be 4 letters, please enter a valid acronym:")
                    building = building.upper()
                    roomNum = input("Please enter the 3 digit room number:")
                    while len(roomNum) != 3:
                        roomNum = input("Room number must be 3 digits, please enter a valid room number:")
                    newLocation = building + " " + roomNum
                    course.TimeAndLocation.location = newLocation
                    print(f"Course location updated to {newLocation}")
                    done = input("Continue editing? Enter Y for yes, N for no:")
                    while len(done) != 1:
                        done = input("Please enter Y to keep editing or N to stop editing:")
                    done = done.upper()
                    if done == "N":
                        stillEditing = False

    def removeCourse(self, indexToRemove: int):
        self.courses.remove(self.courses[indexToRemove])


class CalendarUI:
    def __init__(self, master):
        self.master = master
        master.title("Calendar")
        master.configure(bg="#F2F2F2")
        self.label_color = "#1E88E5"
        self.days_of_week = ["Course Times", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        self.time_slots = ["8am", "9am", "10am", "11am", "12pm", "1pm", "2pm", "3pm", "4pm", "5pm"]
        self.frames = []

        # Create a label for the days of the week
        for i in range(len(self.days_of_week)):
            day_label = tk.Label(self.master, text=self.days_of_week[i], font=("Arial", 10), bg=self.label_color,
                                 fg="white", padx=5, pady=5)
            day_label.grid(row=0, column=i)

        # Create frames for each day of the week
        for i in range(len(self.days_of_week)):
            day_frame = tk.Frame(self.master, bd=0, bg="white")
            day_frame.grid(row=1, column=i, padx=5, pady=5, sticky="nsew")
            day_frame.columnconfigure(0, weight=1)
            self.frames.append(day_frame)

            # Add hourly time slots to each day of the week
            for j in range(len(self.time_slots)):
                # if its the first slot, show all the times
                if self.days_of_week[i] == self.days_of_week[0]:
                    hour_slot = tk.Label(day_frame, text=self.time_slots[j], bd=1, relief="solid", width=10, height=2,
                                         bg="white", padx=5, pady=5)
                    hour_slot.grid(row=j, column=0, padx=2, pady=2, sticky="nsew")

                # all the other time slots
                else:
                    hour_slot = tk.Label(day_frame, text="", bd=1, relief="solid", width=10, height=2, bg="white",
                                         padx=5, pady=5)
                    hour_slot.grid(row=j, column=0, padx=2, pady=2, sticky="nsew")

        # Configure the rows and columns to have a consistent spacing
        for i in range(len(self.days_of_week)):
            self.master.columnconfigure(i, weight=1)

    def add_course(self, course: Course):
        course_name = course.CourseInfo.courseName
        instructor_name = course.CourseInfo.instructor
        code = course.CourseInfo.code
        section = course.CourseInfo.secNum
        credit = course.CourseInfo.credit
        time_slot = course.TimeAndLocation.time
        days_of_week = course.TimeAndLocation.days
        location = course.TimeAndLocation.location

        # Find the day index for each day of the week
        day_indices = []
        for day in days_of_week:
            day_index = self.days_of_week.index(day)
            day_indices.append(day_index)

            # Get the index of the time slot
            time_slot_index = self.time_slots.index(time_slot)

            # Get the label for the specified time slot on the specified day
            label = self.frames[day_index].grid_slaves(row=time_slot_index, column=0)[0]

            # Set the label text to the course information
            label.config(
                text=f"{course_name}\n{instructor_name} {code} {section} {credit}\n{time_slot} {location}",
                bg="#B3E5FC")


def main():
    schedule = Timetable()
    info1 = CourseInfo("Intro to Python", "Dr.Reed", "CS101", 1, 3)
    time1 = TimeAndLocation("8am", ["Monday"], "BHSN 214")
    schedule.checkProfTime(info1.instructor, time1.days, time1.time)
    schedule.checkRoomTime(time1.location, time1.days, time1.time)
    course1 = Course(time1, info1, False)
    info2 = CourseInfo("math", "smith", "CS101", 1, 3)
    time2 = TimeAndLocation("8am", ["Tuesday", "Thursday"], "BHSN 200")
    course2 = Course(time2, info2, False)
    schedule.checkProfTime(info2.instructor, time2.days, time2.time)
    schedule.checkRoomTime(time2.location, time2.days, time2.time)
    schedule.addCourse(course2)
    schedule.addCourse(course1)
    interacting = True
    while (interacting):
        prompt = input(
            "What would you like to do? Enter A to add a course, R to remove a course, E to edit a course, "
            "P to print schedules,"" or D if you are done:")
        prompt = prompt.upper()
        if prompt == "A":
            course = schedule.createCourse()
            schedule.addCourse(course)
        if prompt == "R":
            courseIndex = []
            print("Courses are:")
            for i in range(len(schedule.courses)):
                courseIndex.append(i)
                print(f"{i}:{schedule.courses[i].CourseInfo.code} {schedule.courses[i].CourseInfo.courseName}-"
                      f"{schedule.courses[i].CourseInfo.secNum} {schedule.courses[i].CourseInfo.instructor} "
                      f"{schedule.courses[i].TimeAndLocation.time} {schedule.courses[i].TimeAndLocation.location} "
                      f"{schedule.courses[i].TimeAndLocation.days}")
            selection = input("Enter the number for the course you would like to remove:")
            selection = int(selection)
            validNum = False
            if selection not in courseIndex:
                validNum = False
            else:
                validNum = True
            while validNum == False:
                selection = input("That is not a valid selection, please choose again:")
                selection = int(selection)
                if selection not in courseIndex:
                    validNum = False
                else:
                    validNum = True
            schedule.removeCourse(selection)
        if prompt == "E":
            if len(schedule.courses) == 0:
                print("There are no courses in the schedule to edit, please add a course.")
            else:
                schedule.editCourse()
        if prompt == "P":
            calendarSelection = input("Press A to print all schedules or I for a specific instructors schedule:")
            calendarSelection = calendarSelection.upper()
            if calendarSelection == "A":
                instructors = list(schedule.profTimes.keys())
                root = tk.Tk()
                # calendar = CalendarUI(root)
                for i in range(len(instructors)):
                    root = tk.Tk()
                    calendar = CalendarUI(root)
                    for j in range(len(schedule.courses)):
                        if schedule.courses[j].CourseInfo.instructor == instructors[i]:
                            # root = tk.Tk()
                            # calendar = CalendarUI(root)
                            calendar.add_course(schedule.courses[j])
                root.mainloop()
            if calendarSelection == "I":
                instructors = list(schedule.profTimes.keys())
                instIndex = []
                print("Instructors with courses are:")
                for i in range(len(instructors)):
                    instIndex.append(i)
                    print(f"{i}:{instructors[i]}")
                selection = input("Please enter the number of the instructor to print their schedule:")
                selection = int(selection)
                validNum = False
                if selection not in instIndex:
                    validNum = False
                else:
                    validNum = True
                while validNum == False:
                    selection = input("That is not a valid selection, please choose again:")
                    selection = int(selection)
                    if selection not in instIndex:
                        validNum = False
                    else:
                        validNum = True
                root = tk.Tk()
                calendar = CalendarUI(root)
                for j in range(len(schedule.courses)):
                    if schedule.courses[j].CourseInfo.instructor == instructors[selection]:
                        # root = tk.Tk()
                        # calendar = CalendarUI(root)
                        calendar.add_course(schedule.courses[j])
                root.mainloop()

        if prompt == "D":
            interacting = False
    # root = tk.Tk()
    # calendar = CalendarUI(root)
    # calendar.add_course(course1)
    # calendar.add_course(course2)
    # root.mainloop()
main()

# info1 = CourseInfo("math", "smith", "CS101", 1, 3)
# time1 = TimeAndLocation("8am", ["Tuesday", "Thursday"], ("BHSN", 214))
# course1 = Course(time1, info1, False)
# info2 = CourseInfo("math", "smith", "CS101", 1, 3)
# time2 = TimeAndLocation("8am", ["Monday", "Wednesday"], ("BHSN", 214))
# course2 = Course(time2, info2, False)
# info3 = CourseInfo("math", "smith", "CS101", 1, 3)
# time3 = TimeAndLocation("8am", ["Friday"], ("BHSN", 214))
# course3 = Course(time3, info3, False)
# schedule = Timetable()
# schedule.addCourse(course1)
# schedule.addCourse(course2)
# schedule.addCourse(course3)
# schedule.sortByDay()
# check = course1.timeAndLocation.location
# print(check)