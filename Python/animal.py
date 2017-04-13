class Animal(object):
    def __init__(self,name):
        self.name = name
        self.health = 100
    def walk(self):
        self.health -= 1
        return self
    def run(self):
        self.health -= 5
        return self
    def displayHealth(self):
        print self.name
        print self.health

goat = Animal("Billy Bob")

goat.walk().walk().walk().run().run().displayHealth()

# Output #

# C:\Users\Mal\Desktop\Coding Dojo\Coding Dojo Assignments\Python>animal.py
# Billy Bob
# 87


class Dog(Animal):
    def __init__(self,name):
        super(Dog,self).__init__(name)
        self.health = 150
    def pet(self):
        self.health += 5
        return self
    def displayHealth(self):
        print self.name
        print self.health

puppy = Dog("Barkley")

puppy.walk().walk().walk().run().run().pet().displayHealth()

# Output #

# C:\Users\Mal\Desktop\Coding Dojo\Coding Dojo Assignments\Python>animal.py
# Billy Bob
# 87
# Barkley
# 142

class Dragon(Animal):
    def __init__(self,name):
        super(Dragon,self).__init__(name)
        self.health = 170
    def fly(self):
        self.health -= 10
        return self
    def displayHealth(self):
        print "This is a dragon!"
        print self.name
        print self.health

dragon = Dragon("Parthurnaax")

dragon.walk().walk().run().run().fly().fly().displayHealth()

# Output #

# C:\Users\Mal\Desktop\Coding Dojo\Coding Dojo Assignments\Python>animal.py
# Billy Bob
# 87
# Barkley
# 142
# This is a dragon!
# Parthurnaax
# 138