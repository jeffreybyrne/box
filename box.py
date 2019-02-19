#Just messing around for practice. Let's make a box!
class Box:
    #init function
    def __init__(self,l=1,w=1,h=1):
        self.length = int(l)
        self.width = int(w)
        self.height = int(h)

    def __str__(self):
        return "This box is {} metres long, {} metres wide, and {} metres tall.".format(self.length,self.width,self.height)

    def volume(self):
        return self.width * self.height * self.length

print("What is the height of the box in metres?")
height = input()
print("What is the width of the box in metres?")
width = input()
print("What is the length of the box in metres?")
length = input()

my_box = Box(length,width,height)
print(my_box)
print(my_box.volume())
