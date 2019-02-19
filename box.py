#Just messing around for practice. Let's make a box!
class Box:
    #init function
    def __init__(self,l=1,w=1,h=1):
        self.length = float(l)
        self.width = float(w)
        self.height = float(h)

    def __str__(self):
        return "This box is {:.2f} metres long, {:.2f} metres wide, and {:.2f} metres tall.".format(self.length,self.width,self.height)

    #Function to determine the volume of the box
    def volume(self):
        return self.width * self.height * self.length

    #Functions to determine the area of each type of face
    def base_area(self):
        return self.width * self.length

    def length_side_area(self):
        return self.length * self.height

    def width_side_area(self):
        return self.width * self.height

    #Functions to increase each dimension of the box
    def increase_width(self):
        print("How much do you want to increase the width by? It is currently {:.2f} metres wide.".format(self.width))
        num = float(input())
        self.width += num

    def increase_height(self):
        print("How much do you want to increase the height by? It is currently {:.2f} metres tall.".format(self.height))
        num = float(input())
        self.height += num

    def increase_length(self):
        print("How much do you want to increase the length by? It is currently {:.2f} metres long.".format(self.length))
        num = float(input())
        self.length += num

    #Functions to decrease each dimension of the box
    def decrease_width(self):
        print("How much do you want to decrease the width by? It is currently {:.2f} metres wide.".format(self.width))
        num = float(input())
        while num >= self.width:
            print("Width cannot be decreased by {} metres, please enter a number less than the current width of {}.".format(num,self.width))
            num = float(input())
        self.width -= num

    def decrease_height(self):
        print("How much do you want to decrease the height by? It is currently {:.2f} metres tall.".format(self.height))
        num = float(input())
        while num >= self.height:
            print("Height cannot be decreased by {} metres, please enter a number less than the current height of {}.".format(num,self.height))
            num = float(input())
        self.height -= num

    def decrease_length(self):
        print("How much do you want to decrease the length by? It is currently {:.2f} metres long.".format(self.length))
        num = float(input())
        while num >= self.length:
            print("Length cannot be decreased by {} metres, please enter a number less than the current length of {}.".format(num,self.length))
            num = float(input())
        self.length -= num

    #Function to display a lot of the information about the box
    def box_info(self):
        print("")
        print(self)
        print("The box has a volume of {:.2f} cubic metres.".format(self.volume()))
        print("The box has a base area of {:.2f} squared metres.".format(self.base_area()))
        print("The lengthwise face has an area of {:.2f} squared metres.".format(self.length_side_area()))
        print("The widthwise face has an area of {:.2f} squared metres.".format(self.width_side_area()))
        print("")

#Function to get input from the user and create a new box
def new_box():
    print("Welcome to the box script I made to practice making classes in Python!")
    print("What is the height of the box in metres?")
    height = input()
    print("What is the width of the box in metres?")
    width = input()
    print("What is the length of the box in metres?")
    length = input()
    return Box(length,width,height)

#Call the function defined above and create a new box
my_box = new_box()

#Boolean to keep track of whether the user is still giving input for the following loop
running = True

while running:
    print("What would you like to do? Options are as follows: \n1. Get information about the box.\n2. Increase the height of the box.\n3. Increase the width of the box.\n4. Increase the length of the box.\n5. Decrease the height of the box.\n6. Decrease the width of the box.\n7. Decrease the length of the box.\n8. Quit.")
    resp = int(input())
    if resp == 1:
        my_box.box_info()
    elif resp == 2:
        my_box.increase_height()
    elif resp == 3:
        my_box.increase_width()
    elif resp == 4:
        my_box.increase_length()
    elif resp == 5:
        my_box.decrease_height()
    elif resp == 6:
        my_box.decrease_width()
    elif resp == 7:
        my_box.decrease_length()
    elif resp == 8:
        print("Thank you for using our box script today!")
        running = False
    else:
        pass
