'''
面向对象
    封装
        封装属性和方法
        减少耦合
    继承
        提高开发效率
    多态
    类
        用来描述具有相同的属性和方法的对象集合
    变量
        类变量/成员变量/实例变量
    方法
        类中定义的函数

    定义类
    class ExampleClass():
        #类变量
        val1 = 100

        #构造函数
        def _init_(self):
            #成员变量
            self.val2 = 200
        #类方法 self 必须要有
        def func1(self , arg1):
            #局部变量
            val3 = 300
            #实例变量
            self_val4 = 400
实例化对象
    val = 类名()
    将类加载到内存中
    调用_init_()构造方法
类继承
    class ExampleClass(SuperClass1,SuperClass2)
    支持多继承
父类方法/属性的调用
    调用父类属性需要带上self参数变量
    父类的_inif_()不会自动调用

方法、属性修饰符
    单下划线、双下划綫、头尾双下划綫
        _foo()/_attr
            protected方法/protected属性
        __foo()/__attr
            私有方法/私有属性
        __foo__()/__attr__
        系统方法/系统属性

'''


class ExampleClass():
    # 类变量
    val1 = 100

    # 构造函数
    def __init__(self):
        # 成员变量
        self.val2 = 200
        print("ExamplClass")

    # 类方法
    def func1(self, arg1):
        # 局部变量
        val3 = 300
        # 实例变量
        self.val4 = 400
        print("func1")
#实例化类 必须要实例化对象 才能调用成员变量
example  = ExampleClass()
#必须先调用类方法 才能调用实例变量
example.func1(10)
print(example.val1)
print(example.val2)
print(example.val4)

class ChildClass(ExampleClass):
    def __init__(self):
        #调用父类的构造方法 不调用就不能使用父类的成员变量
        ExampleClass.__init__(self)
        self.v = 10
        print("ChildClass")
    def func2(self):
        self.func1(10)
        return "func2"
childClass = ChildClass()
print(childClass.func2())