timeout_list = {
    "Formerhyde":"6:00AM",
    "Jether":"6:27AM",
    "Akhio":"5:59AM",
    "signed":False
}
curriculum_history = [
    "2025_Old",
    "2026_Enhanced",
]
exams_duration = { # expressed in mins
    "cs3":50,
    "english3":50,
    "biology2":75
}
admins = [
    "CD",
    "CID",
    "SSD",
    "Student_Advisor",
    "DO",
    "Advisor"

]
break_time = 50 # in mins
class CD:
    def __init__(self,admin=False):
        self.admin = admin
    def fire_admin(self,name):
        if name == "CD":
            print("You cannot remove the CD!")
            
        elif self.admin == True:
            for i in range(len(admins)):
                if name in admins:

                    if admins[i] == name:
                        buffer = admins[i]
                        status = buffer + ": Fired"
                        print(f"{name} was fired!")
                        print(status)
                        admins[i] = status
                        print(admins)
                        break
                else:
                    print(f"Employee \"{name}\" does not exist!")
                    break
        else:
            print("You're not admin!")
class CID(CD):
    @property
    def exams_duration(self):
        pass
    @exams_duration.getter
    def exams_duration(self):
        print(f"Exams duration: {exams_duration}")
    @exams_duration.setter
    def exams_duration(self,name,duration):
        exams_duration[name] = duration
    @property
    def curriculum_history(self):     
        pass
    @curriculum_history.getter 
    def curriculum_history(self):
        print(f"List of curriculums: \n{curriculum_history}\nCurrent Curriculum: {curriculum_history[len(curriculum_history)-1]}")
        return
    @curriculum_history.setter
    def curriculum_history(self,name):
        try:
            name += 5
            print("Curriculum must not be a number!")
        except ValueError:
            curriculum_history.append(name)
            print(f"Curriculum history: {curriculum_history}")
        return
    pass

class SSD(CD):
    
    @property
    def break_time(self):
        pass
    @break_time.getter
    def break_time(self):
        print(f"Breaktime for students: {break_time}")
        return
    @break_time.setter
    def break_time(self,time):
        if time < 15:
            print("Please do not set the breaktime to something lower than 15mins!")
            return
        break_time = time
        print(f"New breaktime: {break_time}")
    def append_name_to_timeoutlist(self,name,time):
        timeout_list[name] = str(time)
    def sign_timeout(self):
        timeout_list["signed"] = True  
        print("Timeout was signed by the SSD")
        print(timeout_list)
    pass
class Dormitory(SSD):
    pass
class DO(CID):
    pass
class Student_Advisor(CID):
    pass
class Advisor(CID):
    pass
class Parents(Advisor):
    pass

cd = CD(True)
cd.fire_admin("CID")
ssd = SSD(True)
cid = CID(True)
cid.fire_admin("CD")
ssd.break_time = 9999
ssd.sign_timeout()