class LifePolicy():
    def __init__(self, age, smoker, Medstatus):
        self.age = age
        self.smoker = smoker
        self.MedStatus = Medstatus
    #setage
    def set_age(self, age1):
        self.age = age1
    #getage
    def get_age(self):
        return self.age
    #setsmoker
    def set_smoker(self, smoker1):
        self.smoker = smoker1
    #getsmoker
    def get_smoker(self):
        return self.smoker
    #setmedstatus
    def set_Medstatus(self, Medstatus1):
        self.Medstatus = Medstatus1
    #getmedstatus
    def get_Medstatus(self):
        return self.Medstatus


class AutomobilePolicy():
    def __init__(self, num_ticks, num_acc, age_risk):
        self.num_ticks = num_ticks
        self.num_acc = num_acc
        self.age_risk = age_risk
    #setnumticks
    def set_num_ticks(self, num_ticks1):
        self.num_ticks = num_ticks1
    #getnumticks
    def get_num_ticks(self):
        return self.num_ticks
    #setnumacc
    def set_num_acc(self, num_acc1):
        self.num_acc = num_acc1
    #getnumacc
    def get_num_acc(self):
        return self.num_acc
    #setagerisk
    def set_age_risk(self, age_risk1):
        self.age_risk = age_risk1
    #getagerisk
    def get_age_risk(self):
        return self.age_risk
