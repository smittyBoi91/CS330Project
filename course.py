# SWE Project by Thomas Smith and Meera Poudel

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
    def __init__(self, time: str, days: [], location: tuple):
        self.time = time
        self.days = days
        self.location = location

    def changeTime(self, newTime: int):
        self.time = newTime

    def changeDays(self, newDays: []):
        self.days = newDays

    def changeLocation(self, newLocation: tuple):
        self.location = newLocation

class Course:
    def __init__(self, timeAndLocation: TimeAndLocation, info: CourseInfo, conflict: bool):
        self.timeAndLocation = timeAndLocation
        self.info = info
        self.conflict = conflict

    def changeTimeAndLocation(self, newTimeAndLoc: TimeAndLocation):
        self.timeAndLocation = newTimeAndLoc

    def changeCourseInfo(self, newInfo: CourseInfo):
        self.info = newInfo

class Timetable:
    def __init__(self):
        self.courses = []
        self.schedule = [Course]
        self.week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        self.times = ["8am", "9am", "10am", "11am", "12pm", "1pm", "2pm", "3pm", "4pm", "5pm"]
        # self.course = course

    def addCourse(self, course: Course):
        self.courses.append(course)

    def sortByDay(self):
        temp = []
        for dayOfWeek in self.week:
            index = 0
            i = 0
            for course in self.courses:
                courseDay = self.courses[i].timeAndLocation.days[0]
                if courseDay == dayOfWeek:
                    temp.append(self.courses[i])
                    index += 1
                    i += 1
                else:
                    i += 1
        self.courses = temp

    def checkConflicts(self):
        pass

def main():
    info1 = CourseInfo("math", "smith", "CS101", 1, 3)
    time1 = TimeAndLocation("8am", ["Tuesday", "Thursday"], ("BHSN", 214))
    course1 = Course(time1, info1, False)
    info2 = CourseInfo("math", "smith", "CS101", 1, 3)
    time2 = TimeAndLocation("8am", ["Monday", "Wednesday"], ("BHSN", 214))
    course2 = Course(time2, info2, False)
    info3 = CourseInfo("math", "smith", "CS101", 1, 3)
    time3 = TimeAndLocation("8am", ["Friday"], ("BHSN", 214))
    course3 = Course(time3, info3, False)
    schedule = Timetable()
    schedule.addCourse(course1)
    schedule.addCourse(course2)
    schedule.addCourse(course3)
    schedule.sortByDay()
    check = course1.timeAndLocation.location
    print(check)

main()
