#Just messing around for practice. Let's make a box!
class Box:
    #init function
    def __init__(self,l=1,w=1,h=1):
        self.length = float(l)
        self.width = float(w)
        self.height = float(h)

    def __str__(self):
        return "This box is {} metres long, {} metres wide, and {} metres tall.".format(self.length,self.width,self.height)

    def volume(self):
        return self.width * self.height * self.length

    def base_area(self):
        return self.width * self.length

    def length_side_area(self):
        return self.length * self.height

    def width_side_area(self):
        return self.width * self.height

    def increase_width(self):
        print("How much do you want to increase the width by?")
        num = float(input())
        self.width += num

    def increase_height(self):
        print("How much do you want to increase the height by?")
        num = float(input())
        self.height += num

    def increase_length(self):
        print("How much do you want to increase the length by?")
        num = float(input())
        self.length += num


def info_box():
    print(my_box)
    print("The box has a volume of {} cubic metres.".format(my_box.volume()))
    print("The box has a base area of {} squared metres.".format(my_box.base_area()))
    print("The lengthwise face has an area of {} squared metres.".format(my_box.length_side_area()))
    print("The widthwise face has an area of {} squared metres.".format(my_box.width_side_area()))

def new_box():
    print("What is the height of the box in metres?")
    height = input()
    print("What is the width of the box in metres?")
    width = input()
    print("What is the length of the box in metres?")
    length = input()
    return Box(length,width,height)

def increase_length():

    my_box.increase_length(num)

def increase_width():

    my_box.increase_width(num)

my_box = new_box()
info_box()
my_box.increase_height()
info_box()
