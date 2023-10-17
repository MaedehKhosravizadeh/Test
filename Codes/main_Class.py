import sys
from tkinter import PhotoImage
from Write import *
import os


'''
# Set the turtle speed
"fastest" :  0
"fast"    :  10
"normal"  :  6
"slow"    :  3
"slowest" :  1

# Set the turtle shape
tr.turtlesize(sz / 4)
tr.shape("circle")

rfrsh_sceen()
'''

# Set the page screen
wn =  tr.Screen()
wn.screensize()
wn.setup(width = 1000, height = 600, startx = 150, starty = 50)

# Set the turtle shape
tr.turtlesize(sz / 4)
tr.shape("circle")

#### به نام خدا
set_width_and_size(5, 1) # Set width
waiting("red") 
set_speed('fastest')
paintline(200, 1, "white")
paintline(200, 400, "yellow")

write("به نام خدا", '#1C86EE')


'''
class Student:
    # Class variable
    school_name = 'ABC School '

    # constructor
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
'''


class review:
   ### Review parts
   ### Set the speed, width and size and directory of media files
   speed1 = 'normal'
   width_pen = 4
   sz_pen = .8
   clrLine = "#FCE6C9"
   clrWord = "#00C957"
   time_delay = 6
   
   def __init__(self, name):
      self.__name__ = name
      print(f"speed1 of {self.__name__} :", self.speed1)
      print(f"width_pen of {self.__name__} :", self.width_pen)
      print(f"sz_pen of {self.__name__} :", self.sz_pen)
      print(f"clrLine of {self.__name__} :", self.clrLine)
      print(f"clrWord of {self.__name__} :", self.clrWord)
      print(f"time_delay of {self.__name__} :", self.time_delay)
      print()
      pass
      
   def write_words(self, A):
      rfrsh_sceen()
      set_speed(self.speed1)
      set_width_and_size(self.width_pen, self.sz_pen)
      ### Set the color lines and pencolor
      khatkeshi(20, self.clrLine)
      waiting("purple2")
      paintline(400, 1, "white")
      for theword in A:      
         write(theword, self.clrWord)
         write("-", "black")
         if tr.pos()[0] < -300:
            paintline(400, 1, "white")
            paintline(400, 1, "white")
         if tr.pos()[1] < -270:
            rfrsh_sceen()
            khatkeshi(20, self.clrLine)
         time.sleep(self.time_delay)
      paintline(400, 1, "white")
      paintline(400, 1, "white")

   def write_sentences(self, D):
      rfrsh_sceen()
      set_speed(self.speed1)
      set_width_and_size(self.width_pen, self.sz_pen)
      ### Set the color lines and pencolor
      khatkeshi(20, self.clrLine)
      waiting("purple2")
      
      for sentence in D:
         K = sentence.split(" ")
         paintline(400, 1, "white")
         for theword in K:      
            write(theword, self.clrWord)
            write(" ", self.clrWord)
            if tr.pos()[0] < -300:
               paintline(400, 1, "white")
               paintline(400, 1, "white")
            time.sleep(.5)
         if tr.pos()[1] < -240:
            rfrsh_sceen()
            khatkeshi(20, self.clrLine)
         paintline(400, 1, "white")
         time.sleep(self.time_delay)
         
   def Afarin(self):
      set_width_and_size(2,.5)
      write("آفرين", self.clrWord)
      set_width_and_size(self.width_pen, self.sz_pen)

      goto_RU(-200, 200)

class learn():
   ### New Lesson parts

   ### Set the speed, width and size and directory of media files
   ### They are changeable for every lessons
   speed2 = 'normal'
   width_pen = 4
   sz_pen = 1
   clrLine = "green"
   clrWord = "black"
   time_delay = 2
   
  
   def __init__(self, name):
      self.__name__ = name
      print(f"speed2 of {self.__name__} :", self.speed2)
      print(f"width_pen of {self.__name__} :", self.width_pen)
      print(f"sz_pen of {self.__name__} :", self.sz_pen)
      print(f"clrLine of {self.__name__} :", self.clrLine)
      print(f"clrWord of {self.__name__} :", self.clrWord)
      print(f"time_delay of {self.__name__} :", self.time_delay)
      print()
      pass
      
   ### Select the words to learn and set the color lines and pencolor
   
   def write_words(self, B, dir_file):
      set_speed(self.speed2)
      set_width_and_size(self.width_pen, self.sz_pen)
      sys.path.append(dir_file)
      for lstb in B:
         m = -250 # to position of images
         rfrsh_sceen()
         for wrds in lstb:
            paintline(-502, 2, "red")
            #waiting("purple1")
            if len(wrds['w']) > 0 :
               paintline(300, 600, self.clrLine)
               write(wrds['w'], self.clrWord)
            if isinstance(wrds['img'], str):
               time.sleep(1)
               if("Start" in wrds['img']):
                  show_img(wrds['img'] , 0, 0)
               else:
                  show_img(wrds['img'] , m, -100)
               m += 300
            paintline(302, 1, "white")
            time.sleep(self.time_delay)

      goto_RU(-200, 200)




















