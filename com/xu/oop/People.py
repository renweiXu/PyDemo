class People():
    #私有属性
    __age = 0
    name = ""

    def set_age(self,age):
        self.__age = age
    def get_age(self):
        return  self.__age

class Student(People):
    grade = 0
    def exam(self):
        print("%d岁的%s在%d年级，参加了一次考试"%(self.get_age(),self.name,self.grade))
st = Student();
st.set_age(7)
st.name = "李四"
st.grade = 5
st.exam();