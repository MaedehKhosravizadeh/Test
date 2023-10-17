
from alphabets import *

SET = {"ب", "پ", "ت", "ث", "ج", "چ", "ح", "خ", "س", "ش",
       "ص", "ض", "ط", "ظ", "ع", "غ", "ف", "ق", "ک", "گ", "ل", "م", "ن", "ه", "ي"} 
SET_not_past_connect = {"آ", "ا", "د", "ذ", "ر", "ز", "ژ", "و"}
SET_fasele = {" ", "."}
SET_asvat ={"َ", "ُ", "ِ"}

def avvale_kalame(str, i):
   if i == 0:
      return True
   elif str[i - 1] == " ":
      return True
   else:
      return False

def akhare_kalame(str, i):
   if i == len(str) - 1:
      return True
   elif str[i + 1] in SET_fasele:
      return True
   elif i < len(str) - 1 and (str[i + 1] == "ِ" and str[i + 2] == " "):
      return True
   else:
      return False
   
def past_connected(str, i): # ghablesh ye chize chasban bashe
   if i > 0 and str[i - 1] not in set.union(SET_not_past_connect, SET_fasele):
      return True
   elif i > 1 and str[i - 1 ] in SET_asvat and str[i - 2] not in SET_not_past_connect:
      return True
   else:    #elif i < len(str) - 1 and str[i - 1] in SET_not_past_connect:
      return False
   pass

def write(str, clr):
   tr.showturtle()
   tr.pendown()
   for i in range(len(str)):
      
      if str[i] == " ":
         if i > 0 and str[i - 1] in SET_not_past_connect:
            goto_RU(-30, 0)
         else:
            goto_RU(-40, 0)
         pass
      if str[i] == "-":
         goto_RU(-30, 10)
         tr.setheading(180)
         tr.forward(20)
         goto_RU(-30, -10)
         
      if str[i] == ".":
         if i > 0 and str[i - 1] in SET_not_past_connect:
            pass
         else:
            goto_RU(-10, 0)
         noghte()
         goto_RU(-40, 0)
         pass
      
      if str[i] == "آ":
         AA(clr)
         pass
      
      if str[i] == "ا":
         if avvale_kalame(str, i):
            A(clr)
         elif not past_connected(str, i):
            A(clr)
         elif str[i - 1] == "ل":
            goto_RU(5, 0)
            A(clr)
         else:
            A_connected(clr)
         pass
      
      if str[i] == "َ":
         a()
         pass
      
      if str[i] == "ُ":
         o()
         pass
      
      if str[i] == "ِ":
         e()
         pass
      
      if str[i] == "ب":
         if akhare_kalame(str, i):
            B(clr)
         else:
            b(clr)
         pass
      
      if str[i] == "پ":
         if akhare_kalame(str, i):
            P(clr)
         else:
            p(clr)
         pass
      
      if str[i] == "ت":
         if akhare_kalame(str, i):
            T(clr)
         else:
            t(clr)
         pass
      
      if str[i] == "ث":
         if akhare_kalame(str, i):
            Th(clr)
         else:
            th(clr)
         pass
      
      if str[i] == "ج":
         if akhare_kalame(str, i):
            Jim(clr)
         else:
            jim(clr, 3)
         pass
      
      if str[i] == "چ":
         if akhare_kalame(str, i):
            Ch(clr)
         else:
            ch(clr, 3)
         pass
      
      if str[i] == "ح":
         if akhare_kalame(str, i):
            H_jimi(clr)
         else:
            h_jimi(clr, 3)
         pass
      
      if str[i] == "خ":
         if akhare_kalame(str, i):
            Kh(clr)
         else:
            kh(clr, 3)
         pass
      
      if str[i] == "د":
         Daal(clr)
         pass
      
      if str[i] == "ذ":
         Zaal(clr)
         pass
      
      if str[i] == "ر":
         R(clr)
         pass

      if str[i] == "ز":
         Z_zanboor(clr)
         pass
      
      if str[i] == "ژ":
         Zh(clr)
         pass
      
      if str[i] == "س":
         if akhare_kalame(str, i):
            Sin(clr)
         else:
            sin(clr)
         pass

      if str[i] == "ش":
         if akhare_kalame(str, i):
            Shin(clr)
         else:
            shin(clr)   
         pass
      
      if str[i] == "ص":
         if akhare_kalame(str, i):
            Saad(clr)
         else:
            saad(clr)
         pass
      
      if str[i] == "ض":
         if akhare_kalame(str, i):
            Zaad(clr)
         else:
            zaad(clr)
         pass

      if str[i] == "ط":
         Taa(clr)
         pass
      
      if str[i] == "ظ":
         Zaa(clr)
         pass
      
      if str[i] == "ع":
         if avvale_kalame(str, i):
            if i > 0 and str[i-1] == " " and i < len(str) - 2 and str[i + 1] == "ا":
               goto_RU(20, 0)
            ein(clr)
         elif akhare_kalame(str, i):
            if past_connected(str, i):
               Ein_connected(clr)
            else:
               Ein(clr)
         elif str[i - 1] in SET_not_past_connect:
            ein(clr)
         else:
            ein_vasat(clr)
         pass

      if str[i] == "غ":
         if avvale_kalame(str, i):
            if i > 0 and str[i-1] == " " and i < len(str) - 2 and str[i + 1] == "ا":
               goto_RU(20, 0)
            ghein(clr)
         elif akhare_kalame(str, i):
            if past_connected(str, i):
               Ghein_connected(clr)
            else:
               Ghein(clr)
         elif str[i - 1] in SET_not_past_connect:
            ghein(clr)
         else:
            ghein_vasat(clr)
         pass
      
      if str[i] == "ف":
         if akhare_kalame(str, i):
            F(clr)
         else:
            f(clr)   
         pass
      
      if str[i] == "ق":
         if akhare_kalame(str, i):
            Ghaaf(clr)
         else:
            ghaaf(clr)
         pass

      if str[i] == "ک":
         if akhare_kalame(str, i):
            Kaaf(clr)
         else:
            kaaf(clr)
         pass
      
      if str[i] == "گ":
         if akhare_kalame(str, i):
            Gaaf(clr)
         else:
            gaaf(clr)
         pass
      
      if str[i] == "ل":
         if akhare_kalame(str, i):
            Laam(clr)
         else:
            laam(clr)         
         pass

      if str[i] == "م":
         if akhare_kalame(str, i):
            Mim(clr)
         else:
            mim(clr)
         pass
      
      if str[i] == "ن":
         if akhare_kalame(str, i):
            Noon(clr)
         else:
            noon(clr)
         pass
      
      if str[i] == "و":
         V(clr)
         pass

      if str[i] == "ه":
         if avvale_kalame(str, i):
            if i > 0 and str[i-1] == " " and i < len(str) - 2 and str[i + 1] == "ا":
               goto_RU(20, 0)
            H_docheshm(clr)
         elif akhare_kalame(str, i):
            if past_connected(str, i):
               H_akhar_bala(clr)
            else:
               H_kooh(clr)
         elif str[i - 1] in SET_not_past_connect:
            H_docheshm(clr)
         else:
            H_vasat(clr)
         pass
      
      if str[i] == "ي":
         if akhare_kalame(str, i):
            if i > 0 and str[i-1] == " ":
               goto_RU(30,0)
            Ee(clr) 
         else:
            ee(clr)         
         pass
      
      if str[i] == "ئ":
         #####
         pass
      
      
      
      

