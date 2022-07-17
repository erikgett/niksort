import json


class Owner:
    def __init__(self, userid):
        self.userid = userid
        self.owner = {'user': self.userid}
        self.sayhi()
        self.createjson()
        self.users_list = []
        self.moderators_list = []

    def create_product(self, bot_token, product_name):
        self.owner['product'] = bot_token,product_name


    def add_users_in_list(self, *users):
        for user in users:
            self.users_list.append(user)

        self.owner['users_list'] = self.users_list
        self.sayhi()

    def createjson(self):
        pass


    def sayhi(self):
        # test func
        print("hi owner", self.userid)
        print(self.owner)

    def add_moderator_list(self, *moders_id):
        #         create moder with his rules
        for moder_id in moders_id:
            self.moderators_list.append(moder_id)

        self.owner['moderators_list'] = self.moderators_list
        self.sayhi()




class Moderator:

    def __init__(self, moder_id):
        self.moder_id = moder_id
        self.access = {'module': [], 'lessons': []}
        self.moder = {'moder_id': self.moder_id,'accesses': self.access}
        self.rights = []
        self.students_list = []
        self.modules = []
        self.lessons = []


    def get_rights(self, *rights):
        for right in rights:
            self.rights.append(right)

        self.moder['rights'] = self.rights


    def add_student_list(self, *students_list):
        for student in students_list:
            self.students_list.append(student)
        self.moder['students_list'] = self.students_list


    def add_module_access(self, *modules_names):
        for module in modules_names:
            self.modules.append(module)

        self.access['module'] = self.modules

    def add_lesson_access(self, *lessons_name):
        for lesson in lessons_name:
            self.lessons.append(lesson)
        self.access['lessons'] = self.lessons

    def return_moder_info(self):
        return self.moder

    def print_moder(self):
        print(self.moder)


    def mailing(self):
        pass

    def give_access_to_lesson(self):
        pass

    def give_access_for_all_lessons(self):
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
        self.modules = {}

    def modulelessons(self):
        pass

    def create_module(self, module_name):
        self.modules['module_name'] = module_name


    def editmodule(self):
        pass

    def deletemodule(self):
        pass
    def print_info(self):
        print(self.productname)
        print(self.modules)


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
svyatoslav.create_product('1234', 'CRM')
svyatoslav.add_users_in_list('123','ghb')
svyatoslav.add_users_in_list('123','ghb')


erik = Moderator('erik')
vika = Moderator('vika')
erik.get_rights('Рассылка')
erik.add_student_list('Vika','Masha')
erik.add_module_access('ghghg','dd')
erik.add_lesson_access('1','2')
erik.print_moder()

svyatoslav.add_moderator_list(erik.return_moder_info(), vika.return_moder_info())
gide = Module('Revit')
gide.print_info()

# uzver = User('uzver')