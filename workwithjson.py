import json


class Userjson:
    def __init__(self, userid):
        self.userid = userid
        self.sayhi()
        self.createjson()

    def createjson(self):
        pass

    def sayhi(self):
        print("hi", self.userid)


class Moderatorjson():
    def __init__(self, userid):
        self.userid = userid
        self.sayhi()
        self.createjson()

    def sayhi(self):
        print('hello moderator - ', self.userid)


class Module:
    pass


class Lesson:
    pass


class Homework:
    pass


erik = Userjson('ro')

svyatoslav = Moderatorjson("bro")
