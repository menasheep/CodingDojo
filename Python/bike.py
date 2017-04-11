class Bike(object):
    def __init__(self,price,max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0
    def displayInfo(self):
        print self.price
        print self.max_speed
        print self.miles
        return self
    def ride(self):
        print "Riding"
        self.miles = self.miles + 10
        return self
    def reverse(self):
        print "Reversing"
        if self.miles - 5 < 0:
            print "Too low"
        else:
            self.miles = self.miles - 5
        return self

bike1 = Bike(200, "25mph")
bike2 = Bike(5000,"1mph")
bike3 = Bike(350,"140mph")

bike1.ride().ride().ride().reverse().displayInfo()
bike2.ride().ride().reverse().reverse().displayInfo()
bike3.reverse().reverse().reverse().displayInfo()

#All of the methods can utilize return self for chaining.

## OUTPUT ##


# C:\Users\Mal\Desktop\Coding Dojo\Python\Python>bike.py
# Riding
# Riding
# Riding
# Reversing
# 200
# 25mph
# 25
# Riding
# Riding
# Reversing
# Reversing
# 5000
# 1mph
# 10
# Reversing
# Too low
# Reversing
# Too low
# Reversing
# Too low
# 350
# 140mph
# 0

# C:\Users\Mal\Desktop\Coding Dojo\Python\Python>