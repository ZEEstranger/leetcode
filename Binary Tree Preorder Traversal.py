def Singleton(class_):
    instance = {}

    def get_instance(*args, **kwargs):
        if class_ not in instance:
            instance[class_] = class_(*args, **kwargs)
        return instance[class_]
    
    return get_instance


@Singleton
class MyClass:
    a = [10, 12]



a = MyClass()
b = MyClass()


print(id(a))
print(id(b))