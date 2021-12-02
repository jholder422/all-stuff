class Policy:
    def __init__(self,pnum,date,pname,paddr,premiumAmount):
        self._PolicyNumber = pnum
        self._PolicyDate = date
        self._PolicyName = pname
        self._PolicyAddr = paddr
        self._PolicyPremium = premiumAmount
    def getNumber(self):
        return self._PolicyNumber
    def getName(self):
        return self._PolicyName
    def getAddr(self):
        return self._PolicyAddr
    def getPremium(self):
        return self._PolicyPremium
    def getDate(self):
        return self._PolicyDate
    def setNumber(self,num):
        self._PolicyNumber = num
    def setName(self,name):
        self._PolicyName = name
    def setAddr(self,addr):
        self._PolicyAddr = addr
    def setPremium(self,premium):
        self._PolicyPremium = premium
    def setDate(self,d):
        self._PolicyDate = d
    def __str__(self):
        astring = "Policy Number: " + self._PolicyNumber
        astring += "\nPolicy Name:  " + self._PolicyName
        astring += "\nPolicy Address:  " + self._PolicyAddr
        astring += "\nPolicy Premiumn:  " + str(self._PolicyPremium)
        return astring
if __name__== "__main__":
    aPolicy = Policy("23187","03-04-2019","John Jones","3 River St. N.Y., N.Y", 100)
    print (aPolicy)
    aPolicy.setNumber("3333")
    aPolicy.setDate("12-25-2018")
    aPolicy.setAddr("5 Highway 1")
    aPolicy.setName("Joe Thomas")
    aPolicy.setPremium(99)
    print (aPolicy.getNumber(),aPolicy.getDate(),aPolicy.getAddr(),aPolicy.getPremium())
