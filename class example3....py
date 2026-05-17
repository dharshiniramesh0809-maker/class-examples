class cat:
    def sounds(self):
        print("meoww")
rough = cat()

print(type(rough))



class animal:
    def walk(self):
        print("walking...")

class cat(animal):
    def __int__(self, name, age):
        self.name = name
        self.age = age


    def sounds(self):
        print("meoww")

rough = cat("rough", 8)

print(rough.name)
print(rough.age)

rough.meoww()
rough.walk()



