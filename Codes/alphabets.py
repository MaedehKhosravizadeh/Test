# noghat bala +30 va noghate payin -20 ast

from functions import *
d = 20 ## length of Daal and H_kooh


def noghte():
   fun_1point()
   goto_RU(-40, 0)
   
def AA(clr):
   tr.color(clr)
   khat_alef(False)
   goto_RU(15,70)
   mad_alef()
   goto_RU(-7,-60)

def A(clr):
   tr.color(clr)
   khat_alef(False)
   goto_RU(-15,0)

def A_connected(clr):
   tr.color(clr)
   khat_alef(True)
   goto_RU(-15, -50)

   
def b(clr):
   tr.color(clr)
   goto_RU(5,10)
   dandane()
   goto_RU(15 ,-20)
   fun_1point()
   goto_RU(-15 ,20) ### It was -10 but I had to change
   
def B(clr):
   tr.color(clr)
   goto_RU(5,10)
   tr.setheading(-90)
   boshghab()
   goto_RU(5 + 22.5 ,-30)
   fun_1point()
   goto_RU(-5 - 22.5, 20)

def p(clr):
   tr.color(clr)
   goto_RU(5,10)
   dandane()
   goto_RU(15 ,-20)
   fun_3point('down')
   goto_RU(-15, 20)

def P(clr):
   tr.color(clr)
   goto_RU(5,10)
   tr.setheading(-90)
   boshghab()
   goto_RU(5 + 22.5 ,-30)
   fun_3point('down')
   goto_RU(-5 - 22.5, 20)

   
def t(clr):
   tr.color(clr)
   goto_RU(5,10)
   dandane()
   goto_RU(20 ,30)
   fun_2point()
   goto_RU(-20 ,-30)


def T(clr):
   tr.color(clr)
   goto_RU(5,10)
   tr.setheading(-90)
   boshghab()
   goto_RU(5 + 22.5 ,20)
   fun_2point()
   goto_RU(-5 - 22.5, -30)

def th(clr):
   tr.color(clr)
   goto_RU(5,10)
   dandane()
   goto_RU(15 ,30)
   fun_3point('up')
   goto_RU(-15, -30)

def Th(clr):
   tr.color(clr)
   goto_RU(5,10)
   tr.setheading(-90)
   boshghab()
   goto_RU(5 + 22.5 ,20)
   fun_3point('up')
   goto_RU(-5 - 22.5, -30)


def jim(clr, l):
   tr.color(clr)
   H_Jimi(l)
   goto_RU(l * 15 - 20, - 30 )
   fun_1point()
   goto_RU(- l * 15 + 20, +30 )


def Jim(clr): 
   tr.color(clr)
   H_Jimi(1)
   gorde_noon(30, 1)
   goto_RU(- 15,  30 * sqrt(3) / 2 )
   fun_1point()
   goto_RU(-30,  30 )

def ch(clr, l):
   tr.color(clr)
   H_Jimi(l)
   goto_RU(l * 15 - 20, - 30 )
   fun_3point('down')
   goto_RU(- l * 15 + 20, +30 )


def Ch(clr): 
   tr.color(clr)
   H_Jimi(1)
   gorde_noon(30, 1)
   goto_RU(- 15,  30 * sqrt(3) / 2 )
   fun_3point('down')
   goto_RU(-30,  30 )

def h_jimi(clr, l):
   tr.color(clr)
   H_Jimi(l)


def H_jimi(clr): 
   tr.color(clr)
   H_Jimi(1)
   gorde_noon(30, 1)
   goto_RU(- 45,  30 * sqrt(3) / 2 + 30)


def kh(clr, l):
   tr.color(clr)
   H_Jimi(l)
   goto_RU(l * 15 - 20,  25 * sqrt(2) + 10 )
   fun_1point()
   goto_RU(- l * 15 + 20, -25 * sqrt(2) - 10 )


def Kh(clr): 
   tr.color(clr)
   H_Jimi(1)
   gorde_noon(30, 1)
   goto_RU(- 15 ,  30 * sqrt(3) / 2 + 25 * sqrt(2) + 30 + 10 )
   fun_1point()
   goto_RU(-30, - 25 * sqrt(2) - 10  )

def Daal(clr):
   tr.color(clr)
   global d
   goto_RU(- d * sqrt(2)/2, d * sqrt(2)/2)
   tr.setheading(-45)
   khat(d)
   tr.right(90)
   khat(d)
   goto_RU(-15, d * sqrt(2)/2)

def Zaal(clr):
   tr.color(clr)
   global d
   goto_RU(- d * sqrt(2)/2, d * sqrt(2)/2)
   tr.setheading(-45)
   khat(d)
   tr.right(90)
   khat(d)
   goto_RU(5, d * sqrt(2) + 30)
   fun_1point()
   goto_RU(-15, - d * sqrt(2) - 30)
   
def R(clr):
   tr.color(clr)
   tr.setheading(-120)
   khat(15)
   tr.left(180)
   semicircle(15, -30)
   tr.left(180)
   khat(15)
   goto_RU(-10, 15 * sqrt(3))

def Z_zanboor(clr):
   R(clr)
   goto_RU(5 + 15 * sqrt(3) + 10, 30)
   fun_1point()
   goto_RU(-5 -15 * sqrt(3) - 10, -30)

def Zh(clr):
   R(clr)
   goto_RU(5 + 15 * sqrt(3) + 10, 30)
   fun_3point('up')
   goto_RU(-5 -15 * sqrt(3) - 10, -30)
 
def sin(clr):
   tr.color(clr)
   goto_RU(5,10)
   dandane_sin()
   dandane_sin()
   dandane()

def Sin(clr):
   tr.color(clr)
   goto_RU(5,10)
   dandane_sin()
   dandane_sin()
   tr.setheading(-90)
   khat(20)
   tr.setheading(90)
   r = 20
   gorde_noon(r, -1)
   goto_RU( - r + r * sqrt(3)/2, 10 - r / 2)
   
def shin(clr):
   tr.color(clr)
   goto_RU(5,10)
   dandane_sin()
   dandane_sin()
   dandane()
   goto_RU(20 + 15 ,30)
   fun_3point('up')
   goto_RU(-20 - 15, -30)

def Shin(clr):
   tr.color(clr)
   goto_RU(5,10)
   dandane_sin()
   dandane_sin()
   tr.setheading(-90)
   khat(20)
   tr.setheading(90)
   r = 20
   gorde_noon(r, -1)
   goto_RU(r * sqrt(3) / 2 + r + 15 ,30)
   fun_3point('up')
   goto_RU(- 15  - 2 * r, -30)
   goto_RU( - r + r * sqrt(3)/2, 10 - r / 2)

def saad(clr):
   tr.color(clr)
   cheshmi_ta()
   tr.right(90)
   khat(10)
   tr.left(180)
   dandane()
   pass

def Saad(clr):
   global d
   tr.color(clr)
   cheshmi_ta()
   tr.left(90)
   khat(10)
   tr.left(180)
   gorde_noon(d, -1)
   goto_RU(- d + d * sqrt(3)/2 , 0)
   pass

def zaad(clr):
   tr.color(clr)
   cheshmi_ta()
   tr.right(90)
   khat(10)
   tr.left(180)
   dandane()
   goto_RU(5 * sqrt(3) + 10 + 20, 20)
   fun_1point()
   goto_RU(-5 * sqrt(3) - 30, -20)
   pass

def Zaad(clr):
   global d
   tr.color(clr)
   cheshmi_ta()
   tr.left(90)
   khat(10)
   tr.left(180)
   gorde_noon(d, -1)
   goto_RU( d * sqrt(3)/2 + d + 10 + 5 * sqrt(3), 30)
   fun_1point()
   goto_RU(-d * sqrt(3)/2 - d - 10 - 5 * sqrt(3), -30)
   pass

def Taa(clr):
   tr.color(clr)
   cheshmi_ta()
   khat(15)
   goto_RU(15, 0)
   khat_alef(False)
   goto_RU(-15, 0)
   pass

def Zaa(clr):
   tr.color(clr)
   cheshmi_ta()
   khat(15)
   goto_RU(15, 0)
   khat_alef(False)
   goto_RU(5 * sqrt(3) + 10, 20)
   fun_1point()
   goto_RU(-5 * sqrt(3) - 25, -20)
   pass

def ein(clr):
   tr.color(clr)
   goto_RU(0, 10)
   tr.setheading(180)
   khat(5)
   semicircle(5, 180)
   khat(5)
   tr.left(180)
   khat(30)
   pass

def ein_vasat(clr):
   global d
   tr.color(clr)
   tr.setheading(180)
   khat(d)
   tr.right(45)
   khat(d)
   tr.right(135)
   khat(d * sqrt(2))
   tr.right(135)
   khat(d)
   tr.right(45)
   khat(3 * d / 2)
   pass

def Ein_connected(clr):
   global d
   tr.color(clr)
   tr.setheading(180)
   khat(d / 2)
   tr.right(45)
   khat(d)
   tr.right(135)
   khat(d * sqrt(2))
   tr.right(135)
   khat(d)
   tr.right(45)
   khat(d / 2)
   gorde_noon(20, 1)
   goto_RU(- 35,  20 * sqrt(3) / 2 + 20)
   pass

def Ein(clr):
   tr.color(clr)
   goto_RU(0, 10)
   tr.setheading(180)
   khat(5)
   semicircle(5, 180)
   khat(5)
   tr.left(180)
   khat(5)
   gorde_noon(20, 1)
   goto_RU(- 35,  20 * sqrt(3) / 2 + 20)
   pass


def ghein(clr):
   tr.color(clr)
   goto_RU(0, 10)
   tr.setheading(180)
   khat(5)
   semicircle(5, 180)
   khat(5)
   tr.left(180)
   khat(30)
   goto_RU(25, 30)
   fun_1point()
   goto_RU(-25, -30)
   pass

def ghein_vasat(clr):
   global d
   tr.color(clr)
   tr.setheading(180)
   khat(d / 2)
   tr.right(45)
   khat(d)
   tr.right(135)
   khat(d * sqrt(2))
   tr.right(135)
   khat(d)
   tr.right(45)
   khat(3 * d / 2)
   goto_RU(3 * d / 2, 30)
   fun_1point()
   goto_RU(-3 * d / 2, -30)
   pass

def Ghein_connected(clr):
   global d
   tr.color(clr)
   tr.setheading(180)
   khat(d / 2)
   tr.right(45)
   khat(d)
   tr.right(135)
   khat(d * sqrt(2))
   tr.right(135)
   khat(d)
   tr.right(45)
   #khat(d / 2)
   gorde_noon(d, 1)
   goto_RU(- d / 2, d + d * sqrt(3) / 2 + 30)
   fun_1point()
   goto_RU(-d, -30)
   pass

def Ghein(clr):
   tr.color(clr)
   goto_RU(0, 10)
   tr.setheading(180)
   khat(5)
   semicircle(5, 180)
   khat(5)
   tr.left(180)
   khat(5)
   gorde_noon(20, 1)
   goto_RU(- d / 2, d + d * sqrt(3) / 2 + 30)
   fun_1point()
   goto_RU(-d, -30)
   pass
'''
def f(clr):
   tr.color(clr)
   goto_RU(5, 10)
   tr.setheading(180)
   khat(5)
   tr.left(180)
   semicircle(5, -270)
   tr.left(180)
   khat(5)
   dandane()
   goto_RU(20 - 5, 40)
   fun_1point()
   goto_RU(-20 + 5, - 40)
   pass
'''

def f(clr):
   tr.color(clr)
   tr.setheading(0)
   semicircle(5, -360)
   tr.left(180)
   khat(25)
   goto_RU(20, 30)
   fun_1point()
   goto_RU(-20, - 30)
   pass

def F(clr):
   tr.color(clr)
   tr.setheading(0)
   semicircle(5, -360)
   tr.left(180)
   khat(45)
   tr.left(180)
   semicircle(5, -90)
   tr.left(180)
   khat(5)
   goto_RU(50, 20)
   fun_1point()
   goto_RU(-50, - 30)
   pass

def ghaaf(clr):
   tr.color(clr)
   goto_RU(5, 10)
   tr.setheading(180)
   khat(5)
   tr.left(180)
   semicircle(5, -270)
   tr.left(180)
   khat(5)
   dandane()
   goto_RU(20 - 5, 40)
   fun_2point()
   goto_RU(-20 + 5, - 40)
   pass

def Ghaaf(clr):
   global d
   tr.color(clr)
   tr.setheading(180)
   khat(d / 4)
   tr.left(180)
   semicircle(d / 4, -270)
   tr.left(180)
   khat(d * 3 / 4)
   tr.left(180)
   gorde_noon(d, -1)
   goto_RU( d + d * sqrt(3)/2 - d / 4, d)
   fun_2point()
   goto_RU(- 3 * d / 4 - d, -d)
   pass


def kaaf(clr):
   tr.color(clr)
   goto_RU(0, 10)
   khat_alef(False)
   dandane()
   goto_RU(20, 55)
   sarkesh_bozorg()
   goto_RU(-20, -55)
   pass

def Kaaf(clr):
   tr.color(clr)
   goto_RU(0, 10)
   khat_alef(False)
   boshghab()
   goto_RU(55, 45)
   sarkesh_bozorg()
   goto_RU(-55, -55)
   pass

def gaaf(clr):
   tr.color(clr)
   goto_RU(0, 10)
   khat_alef(False)
   dandane()
   goto_RU(20, 55)
   sarkesh_gaaf()
   goto_RU(-20, -55)
   pass

def Gaaf(clr):
   tr.color(clr)
   goto_RU(0, 10)
   khat_alef(False)
   boshghab()
   goto_RU(55, 45)
   sarkesh_gaaf()
   goto_RU(-55, -55)
   pass

def laam(clr):
   tr.color(clr)
   goto_RU(0, 10)
   khat_alef(False)
   dandane()
   khat(10)
   pass

def Laam(clr):
   global d
   tr.color(clr)
   khat_alef(False)
   khat(d / 2)
   tr.left(180)
   gorde_noon(d, -1)
   goto_RU( - d + d * sqrt(3)/2, 0)
   pass

def mim(clr):
   tr.color(clr)
   tr.setheading(180)
   semicircle(5, 360)
   khat(20)
   pass
   
def Mim(clr):
   tr.color(clr)
   tr.setheading(180)
   semicircle(5, 360)
   khat(15)
   semicircle(5, 90)
   khat(45)
   goto_RU(0, 50)
   pass

def noon(clr):
   tr.color(clr)
   goto_RU(5,10)
   dandane()
   goto_RU(20, 30)
   fun_1point()
   goto_RU(-20, -30)
   pass
   
def Noon(clr):
   global d
   tr.color(clr)
   tr.setheading(-90)
   khat(d / 2)
   tr.left(180)
   gorde_noon(d, -1)
   goto_RU(d , 0)
   fun_1point()
   goto_RU( - 2 * d + d * sqrt(3)/2, 0)   
   pass
'''
def V(clr):
   tr.color(clr)
   goto_RU(5,5)
   tr.setheading(90)
   semicircle(5, -360)
   tr.left(180)
   khat(5)
   R(clr)
   pass
'''

def V(clr):
   tr.color(clr)
   tr.setheading(0)
   semicircle(5, -270)
   tr.left(180)
   khat(5)
   R(clr)
   pass

def H_docheshm(clr):
   tr.color(clr)
   goto_RU(-15 , 15)
   tr.setheading(-90)
   semicircle(5, 90)
   khat(10)
   tr.left(180)
   semicircle(5, -180)
   tr.left(180)
   khat(10)
   tr.left(180)
   semicircle(5, -360)
   tr.left(180)
   khat(30)
   pass

def H_vasat(clr):
   tr.color(clr)
   global d
   c = d / 4 * sqrt(2)
   tr.setheading(-180)
   khat(d / 4)
   tr.left(90)
   khat(d / 4)
   tr.left(180)
   semicircle(c, -180)
   tr.left(180)
   khat(d / 2)
   tr.left(180)
   semicircle(c, -180)
   tr.left(180)
   khat(d / 4)
   tr.right(90)
   khat(2 * c + d)
   pass

def H_akhar_bala(clr):
   global d
   tr.color(clr)
   tr.setheading(0)
   semicircle(d / 4, -90)
   tr.left(180)
   khat(d / 2)
   semicircle(d / 4, 270)
   khat(d / 4)
   goto_RU(-d / 2, -d / 2)
   pass

def H_akhar_payin(clr):
   tr.color(clr)
   semicircle(10, -60)
   tr.left(180)
   semicircle(10, 150)
   goto_RU(-15, 0)
   pass
   
def H_kooh(clr):
   tr.color(clr)
   global d
   c = d * sqrt(2)/ 4
   goto_RU(- d * sqrt(2)/2 , d * sqrt(2)/2)
   tr.setheading(-45)
   i = d - 2 * c
   khat(i + c)
   tr.left(180)
   semicircle(c, -270)
   tr.left(180)
   khat(c)
   goto_RU(-c, - d / 2)
   pass

def ee(clr):
   tr.color(clr)
   goto_RU(5,10)
   dandane()
   goto_RU(15 ,-20)
   fun_2point()
   goto_RU(-15, 20)
   pass

def Ee(clr):
   tr.color(clr)
   d = 20
   tr.setheading(180)
   khat(10)
   semicircle(5, 180)
   tr.left(180)
   semicircle((d - 10) / 2, -90)
   semicircle(d, -210)
   tr.left(180)
   khat(d / 2 / sqrt(3))
   goto_RU(-d + d * sqrt(3) / 2 , 0)
   pass






