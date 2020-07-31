# excecise for the 100th lesson
# the class of dog

class Dog :
    def __init__(self, name, age, gender, height):
        self.name = name
        self.age = age
        self.gender = gender
        self.height = height

    def jiao(self):
        print('%s jiao e'% self.name)

    def yao(self):
        print('%s wangwangwang' % self.name)

mydog = Dog('angcai',8,'male',120)
mydog.yao()
