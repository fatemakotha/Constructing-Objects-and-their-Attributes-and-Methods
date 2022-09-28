
import another_module

print(another_module.another_variable)

from turtle import Turtle, Screen
timmy = Turtle() #from turtle we fetch the blueprint or the class and name it timmy
print(timmy) #<turtle.Turtle object at 0x0000014E02E720E0>
timmy.shape("turtle") #the object in the center becomes a turle
timmy.color("blue") #turns the turtle blue
timmy.forward(100) #turtle moves forward by a 100 paces

my_screen = Screen() #created an object called my_screen
my_screen.canvheight #object.attribute calls the object and its attribute
print(my_screen.canvheight) #prints 300
my_screen.exitonclick() #object.method this method makes an action in this case makes a white screen appear

