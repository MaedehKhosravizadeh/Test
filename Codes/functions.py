import turtle as tr
from math import *
import keyboard
import time

w = 5 # width of pen
sz = 1 # size of pen
k = 60 #spece of between lines
sp = 'fastest' # speed of turtle
z = 300

def set_width_and_size(u, v):
   global sz, w
   w = u
   sz = v
   tr.width(w)

def set_speed(speed):
   global sp
   sp = speed
   tr.speed(sp)


def khatkeshi(n, color):
   global z, sz, k
   y = tr.pos()[1]
   z = y
   i = 0
   while i < n and z > -300:
      paintline(400, 800, color)
      i += 1
   z = y - k * sz
   tr.penup()
   tr.speed('fastest')
   tr.goto(400 ,z)

def waiting(clr_wait): #when a res circle in the corner of screen
   # it means we wait to press a key
   global sp, w
   tr.speed("fastest")
   xy = tr.pos()
   tr.hideturtle()
   tr.penup()
   tr.goto(-470,270)
   tr.color(clr_wait)
   tr.width(10)
   tr.pendown()
   tr.circle(10)
   while True:
      input = keyboard.read_key(suppress = True)
      if input != "esc":
         tr.color("white")
         tr.circle(10)
         tr.width(w)
         time.sleep(1)
#         tr.showturtle()
         tr.penup()
         tr.goto(xy)
         tr.pendown()
         tr.speed(sp)
         break

def show_img(str , x, y):
   SQUIRREL_IMAGE = str
   screen = tr.Screen()
   screen.register_shape(SQUIRREL_IMAGE)
   img = tr.Turtle(shape=SQUIRREL_IMAGE)
   img.penup()
   img.goto(x, y)
   img.stamp()
   img.hideturtle()

def paintline(start, length, color):
   global sp, z, sz, k, w
   z -= sz * k
   tr.hideturtle()
   tr.penup()
   tr.speed('fastest')
   tr.setheading(0)
   tr.goto(start-length, z)
   tr.color(color)
   tr.width(1)
   tr.pendown()
   tr.forward(length)
   goto_RU(- k * sz , 0)
   tr.width(w)
   tr.speed(sp)
#   tr.showturtle()

def rfrsh_sceen():
   global z, sz, sp
   z = 300
   waiting("pink")
   tr.speed('fastest')
   tr.clearscreen()
   time.sleep(1)
   tr.hideturtle()
   tr.penup()
   tr.turtlesize(sz / 2)
   tr.shape("circle")
   tr.goto(400 ,z)
   tr.speed(sp)

def goto_RU(R,U): ## if part is for UX
   global sz
   if sp == "slowest" or sp == "slow":
      tr.hideturtle()
   tr.penup()
   tr.setheading(0)
   tr.forward(R * sz)
   tr.left(90)
   tr.forward(U * sz)
   tr.pendown()
#   if sp == "slowest" or sp == "slow":
#      tr.showturtle()

   
def semicircle(r, angle):
   global sz
   tr.circle(r * sz, angle)
   
def khat(length):
   global sz
   for i in range(floor(length / 5)):
      tr.forward(5 * sz)
   tr.forward((length % 5) * sz)
   time.sleep(.01)

def dandane():
   tr.setheading(-90)
   khat(5)
   tr.left(180)
   semicircle(5,-90)
   tr.left(180)
   khat(15)
   
def boshghab():
   tr.setheading(-90)
   khat(5)
   tr.left(180)
   semicircle(5,-90)
   tr.left(180)
   khat(45)
   tr.left(180)
   semicircle(5,-90)
   tr.left(180)
   khat(5)

def dandane_sin():
   tr.setheading(-90)
   khat(5)
   tr.left(180)
   semicircle(5,-90)
   tr.left(180)
   khat(5)
   tr.left(180)
   semicircle(5,-90)
   tr.left(180)
   khat(5)

def mad_alef():
   tr.setheading(90)
   semicircle(5,-90)
   tr.left(180)
   khat(20)
   semicircle(5,90)

def khat_alef(connected):
   global sz
   if connected == False:
      goto_RU(0,45)
      tr.setheading(-90)
      khat(45)
   elif connected == True:
      tr.setheading(0)
      semicircle(5, -90)
      tr.setheading(90)
      khat(45)
   else:
      print("error A!")
      
def fun_1point():
   tr.circle(2 * sz, 360)   

def fun_2point():
   goto_RU(4, 0)
   fun_1point()
   goto_RU(-8, 0)
   fun_1point()
   goto_RU(4, 0)

def fun_3point(str):
   goto_RU(4, 0)
   fun_1point()
   goto_RU(-8, 0)
   fun_1point()
   if str == 'up':
      goto_RU(4, 10)
      fun_1point()
      goto_RU(0, -10)
   elif str == 'down':
      goto_RU(4, -10)
      fun_1point()
      goto_RU(0, 10)
   else:
      print("error points!")
      pass
   
def gorde_noon(r , dirtn):
   semicircle(r , dirtn * 210)

def sarkesh_bozorg():
   goto_RU(45 / sqrt(2), 45 / sqrt(2))
   tr.setheading(-135)
   khat(45)
   
def sarkesh_koochak():
   global w, sz
   tr.width(ceil(w / 2))
   goto_RU(15 / sqrt(2), 15 / sqrt(2))
   tr.setheading(-135)
   khat(15)
   tr.width(w)

def sarkesh_gaaf():
   goto_RU(45 / sqrt(2), 45 / sqrt(2))
   tr.setheading(-135)
   khat(45)
   goto_RU(20 / sqrt(2), 30 / sqrt(2))
   sarkesh_koochak()
   goto_RU(-20 / sqrt(2), -30 / sqrt(2))

   
def o():
   global w, sz
   tr.width(2)
   goto_RU(10, 50)
   goto_RU(15 / sqrt(2), 15 / sqrt(2))
   tr.setheading(90)
   semicircle(2 , -405)
   tr.left(180)
   khat(15)
   goto_RU(-10, -50)
   tr.width(w)

def a():
   goto_RU(10, 50)
   sarkesh_koochak()
   goto_RU(-10, -50)

def e():
   goto_RU(10, -40)
   sarkesh_koochak()
   goto_RU(-10, 40)

      
def H_Jimi(l):
   goto_RU(- 45 / sqrt(2), 25 / sqrt(2))
   tr.setheading(45)
   khat(5)
   tr.left(180)
   semicircle(5,-90)
   tr.left(180)
   khat(30)
   tr.setheading(180)
   khat(l * 15)

def cheshmi_ta():
   goto_RU(-5 - 10 - 5 * sqrt(3), 0)
   tr.setheading(30)
   khat(10 + 5 * sqrt(3))
   tr.left(180)
   semicircle(5, -210)
   tr.left(180)
   khat(10 + 5 * sqrt(5))
   

def rgb_to_hex(r, g, b):
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)   
      






