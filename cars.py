#classmethod
class Car(object):
#constructor
    def __init__(self, make, model, year, mileage, salvTitle, cleanTitle):
        self.__make= make
        self.__model= model
        self.__year= year
        self.__mileage= mileage
        self.__salvTitle= salvTitle
        self.__cleanTitle = cleanTitle

#toString
    def __str__ (self):
        rep = ""
        rep += "Make: " + self.__make + "\n"
        rep += "Model: " + self.__model + "\n"
        rep += "Year: " + str(self.__year) + "\n"
        rep += "Mileage: " + str(self.__mileage) + " miles\n"
        rep += "salvTitle: " + str(self.__salvTitle) + "\n"
        rep += "cleanTitle: " + str(self.__cleanTitle) + "\n"
        if self.__salvTitle == True:
            print("Needs fixing.")
        return rep

#Getters
    def getMake(self):
        return self.__make
    def getModel(self):
        return self.__model
    def getYear(self):
        return self.__year
    def getMileage(self):
        return self.__mileage
    def getsalvTitle(self):
        return self.__salvTitle
    def getcleanTitle(self):
        return self.__cleanTitle

#Setters
    def setMake(self, newMake):
        self.__make= newMake
    def setModel(self, newModel):
        self.__model= newModel
    def setYear(self, newYear):
        if newYear< 0 or newYear> 2023:
            raise Exception("Invalid year: ", year)
        else:
            self.__year= newYear
    def setMileage(self, newMileage):
        if newMileage< 0 :
            raise Exception("Mileage cannot be less than 0: ", mileage)
        else:
            self.__mileage= newMileage
    def setSalvTitle(self, newsalvTitle):
        self.__salvTitle= newsalvTitle
    def setCleanTitle(self, newCleanTitle):
        self.__cleanTitle= newCleanTitle





