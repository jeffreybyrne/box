# Just messing around for practice. Let's make a box!
class Box:

    list_of_boxes = []

    # init function
    def __init__(self, length=1, width=1, height=1):
        self.length = float(length)
        self.width = float(width)
        self.height = float(height)

    def __str__(self):
        return "This box is {:.2f} metres long, {:.2f} metres wide, and {:.2f} metres tall.".format(self.length, self.width, self.height)

    @classmethod
    def create(cls):
        print("What is the height of the box in metres?")
        height = input()
        print("What is the width of the box in metres?")
        width = input()
        print("What is the length of the box in metres?")
        length = input()
        new_box = Box(length, width, height)
        Box.list_of_boxes.append(new_box)
        return new_box

    def main_menu(self):
        while True:
            self.print_menu()
            selection = int(input())
            self.do_action(selection)

    def print_menu(self):
        print('')
        print('What would you like to do? Options are as follows:')
        print('1. Get information about the box.')
        print('2. Increase the height of the box.')
        print('3. Increase the width of the box.')
        print('4. Increase the length of the box.')
        print('5. Decrease the height of the box.')
        print('6. Decrease the width of the box.')
        print('7. Decrease the length of the box.')
        print('8. Quit.')

    def do_action(self, resp):
        if resp == 1:
            my_box.box_info()
        elif resp == 2:
            my_box.increase_dimension('height')
            # my_box.increase_height()
        elif resp == 3:
            my_box.increase_dimension('width')
            # my_box.increase_width()
        elif resp == 4:
            my_box.increase_dimension('length')
            # my_box.increase_length()
        elif resp == 5:
            my_box.decrease_dimension('height')
            # my_box.decrease_height()
        elif resp == 6:
            my_box.decrease_dimension('width')
            # my_box.decrease_width()
        elif resp == 7:
            my_box.decrease_dimension('length')
            # my_box.decrease_length()
        elif resp == 8:
            print("Thank you for using our box script today!")
            quit()
        else:
            pass

    # Function to determine the volume of the box
    def volume(self):
        return self.width * self.height * self.length

    # Functions to determine the area of each type of face
    def base_area(self):
        return self.width * self.length

    def length_side_area(self):
        return self.length * self.height

    def width_side_area(self):
        return self.width * self.height

    def increase_dimension(self, dimension):
        if dimension == 'length':
            print("How much do you want to increase the length by? It is currently {:.2f} metres long.".format(self.length))
            num = float(input())
            self.length += num
        elif dimension == 'height':
            print("How much do you want to increase the height by? It is currently {:.2f} metres tall.".format(self.height))
            num = float(input())
            self.height += num
        elif dimension == 'width':
            print("How much do you want to increase the width by? It is currently {:.2f} metres wide.".format(self.width))
            num = float(input())
            self.width += num

    def decrease_dimension(self, dimension):
        if dimension == 'height':
            print("How much do you want to decrease the height by? It is currently {:.2f} metres tall.".format(self.height))
            num = float(input())
            while num >= self.height:
                print("Height cannot be decreased by {} metres, please enter a number less than the current height of {}.".format(num, self.height))
                num = float(input())
            self.height -= num
        elif dimension == 'width':
            print("How much do you want to decrease the width by? It is currently {:.2f} metres wide.".format(self.width))
            num = float(input())
            while num >= self.width:
                print("Width cannot be decreased by {} metres, please enter a number less than the current width of {}.".format(num, self.width))
                num = float(input())
            self.width -= num
        elif dimension == 'length':
            print("How much do you want to decrease the length by? It is currently {:.2f} metres long.".format(self.length))
            num = float(input())
            while num >= self.length:
                print("Length cannot be decreased by {} metres, please enter a number less than the current length of {}.".format(num, self.length))
                num = float(input())
            self.length -= num

    # Function to display a lot of the information about the box
    def box_info(self):
        print("")
        print(self)
        print("The box has a volume of {:.2f} cubic metres.".format(self.volume()))
        print("The box has a base area of {:.2f} squared metres.".format(self.base_area()))
        print("The lengthwise face has an area of {:.2f} squared metres.".format(self.length_side_area()))
        print("The widthwise face has an area of {:.2f} squared metres.".format(self.width_side_area()))
        print("")


print("Welcome to the box script I made to practice making classes in Python!")
# Call the function defined above and create a new box
my_box = Box.create()
my_box.main_menu()
