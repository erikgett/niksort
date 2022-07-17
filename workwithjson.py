import json


class Owner:
    def __init__(self, userid):
        self.userid = userid
        self.owner = 0
        self.sayhi()
        self.createjson()

    def createjson(self):
        pass

    def owner(self):
        # are pay money for service?
        pass

    def sayhi(self):
        # test func
        print("hi owner", self.userid)

    def addmoderator(self):
        #         create moder with his rules
        pass


class Moderator:

    def __init__(self, userid):
        self.userid = userid
        self.sayhi()

    def sayhi(self):
        print('hello moderator - ', self.userid)
        print()
    def mailing(self):
        pass

    def giveaccesstolesson(self):
        pass

    def giveaccessforalllessons(self):
        pass


class User:
    def __init__(self, userid):
        self.userid = userid
        print('hi', self.userid)

    def getaccessforinfomation(self):
        # get module or gide access
        pass


class Module:
    def __init__(self, productname):
        self.productname = productname
        self.access = 0
        self.lessonslist = []

    def modulelessons(self):
        pass

    def createmodule(self):
        pass

    def editmodule(self):
        pass

    def deletemodule(self):
        pass


class Lesson:
    def __init__(self, lessonname):
        self.lessonname = lessonname
        self.access = 0
        self.boolean = 0

    def addvideolesson(self):
        pass

    def addfileforlesson(self):
        pass

    def deletelesson(self):
        pass

    def createlesson(self):
        pass

    def editlesson(self):
        pass


class Homework:
    def __init__(self, lessonname, modulename):
        self.lessonname = lessonname
        self.listmadework = []
        self.modulename = modulename
        self.boolean = 0

    def checkhomework(self):
        pass

    def addhomework(self):
        pass

    def delhomework(self):
        pass


svyatoslav = Owner("svyatoslav")

erik = Moderator('erik')

uzver = User('uzver')