# -*- coding: utf-8 -*-
"""copy-of-untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/gist/saronnnn/893c8fd8121299d16ebb51fbfa376328/copy-of-untitled0.ipynb
"""

from operator import ge
import math
import cmath
import numpy as np
import matplotlib.pyplot as plt


try:
 print("Enter 1 to find t,v,a...\n")
 print("Enter 2 to plot graph x(t) , v(t) ,a(t)\n")
 print("Enter 3 to find h , v , vf by free fall concept ")

 choose = int(input("put your chose here: \n"))

 if choose == 1:
      print("            Choose one of the following to find there value \n")
      print(" Enter 1 to find time                   Enter 2 to find acceleration              Enter 3 to find average acceleration \n" )

      print(" Enter 4 to find average velocity        Enter 5 to find inital velocity           Enter 6 to find final velocity \n")

      print(" Enter 7 to find position             \n")

      print("Enter space if u don't have the input \n")

      choose_second = int(input("put your choise here: \n"))

      if choose_second == 1:
        Vf = input("Vf(m/s) = ")
        Vi = input("Vi(m/s) = ")
        Ac= input("a(m/s^2) = ")
        S = input("s(m) = ")

        if Vf != " " and Vi !=" " and Ac!=" ":
          sub = int(Vf) - int(Vi)
          final = sub / int(Ac)
          print("t = " + str(Vf) +"m/s - "+ str(Vi) + "m/s  / " + str(Ac)+"m/s^2")
          print("t = "+ str(final)+"s")
        elif S != " " and Ac != " " and Vi != "":
           v=float(Vi)
           u=float(Ac)
           s=float(S)
           underradica = v**2 + u*s*2
           result1 = -v + cmath.sqrt(underradica) /u
           result2 = -v - cmath.sqrt(underradica) /u

           print("t = -" + str(v)+" \u00B1 \u221A"+ str(v)+ "^2 + 2*"+ str(u)+"*"+str(s)+"  /  "+str(u)+"\n")
           print("t1 = " + str(result1)+"s   t2 = "+str(result2) +"s \n")
           print("#as we know time is always positive so you have to take the positive result\n")

        else:
          print("invalid input!!")
      if choose_second == 2:
          Vf = input("Vf(m/s) = ")
          Vi = input("Vi(m/s) = ")
          T= input("t(s) = ")
          S = input("s(m) = ")
          if Vf != " " and Vi !=" " and T!=" ":
            sub = int(Vf) - int(Vi)
            final = sub / int(T)
            print("a = " + str(Vf) +"m/s - "+ str(Vi) + "m/s  / " + str(T)+"s\n")
            print("a = "+ str(final)+"m/s^2\n")
          elif S != " " and T != " " and Vi != "":
            t = int(T)
            v = int(Vi)
            s = int(S)
            tp = t**2
            vt = 2*v*t
            firesult = 2*s - vt
            finalres = firesult / tp
            print("a = 2("+str(s)+"m - "+str(v)+"m/s*"+str(t)+"s)  / " + str(t) + "^2s\n")
            print("a = "+str(finalres)+"\n")
          elif Vf != " " and Vi !=" " and S!=" ":
            vf = int(Vf)
            vi = int(Vi)
            ss =int(S)
            v= vf**2
            u= vi**2
            s=2*ss
            sub = v - u
            final = sub / s
            print("a = " + str(Vf) +"^2m/s - "+ str(Vi) + "^2m/s  /  2*" + str(S)+"m\n")
            print("a = "+ str(final)+"m/s^2\n")
          else:
            print("invalid input")
      if choose_second == 3:
           Vf = input("Vf(m/s) = ")
           Vi = input("Vi(m/s) = ")
           Ti= input("ti(s) = ")
           Tf= input("tf(s) =")
           if Vf !=" " and Vi !=" " and Ti !=" " and Tf !=" ":
             vf = int(Vf)
             vi = int(Vi)
             tf = int(Tf)
             ti = int(Ti)
             v = vf - vi
             t = tf - ti
             ava = v/t
             print("average acceleration = " + str(vf) +"m/s - "+ str(vi)+"m/s  /  " + str(tf) + "s - " + str(ti)+"s")
             print("aver a = "+ str(ava)+"m/s^2")
           else:
            print("invalid input!!")

      if choose_second == 4:
         Si=input("si(s) = ")
         Sf=input("sf(s) = ")
         Ti= input("ti(s) = ")
         Tf= input("tf(s) =")

         if Sf !=" " and Si !=" " and Ti !=" " and Tf !=" ":
              sf = int(Sf)
              si = int(Si)
              tf = int(Tf)
              ti = int(Ti)
              s = sf - si
              t = tf - ti
              vav = s/t
              print("average velocity = " + str(sf) +"m - "+ str(si)+"m  /  " + str(tf) + "s - " + str(ti)+"s")
              print("aver v = "+ str(vav)+"m/s")
         else:
            print("invalid input!!")
 #~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
      if choose_second == 5:
             Vf = input("Vf(m/s) = ")
             T = input("t(s) = ")
             Ac= input("a(m/s^2) = ")
             S = input("s(m) = ")

             if Vf != " " and T !=" " and Ac!=" ":
              at= int(Ac)*int(T)
              sub = int(Vf) - int(at) ;

              print("Vi = " + str(Vf) +"m/s - " + str(Ac)+"m/s^2 * "+ str(T)+"s")
              print("Vi = "+ str(sub)+"m/s")


             elif S != " " and Ac != " " and Vf != "":
              v=int(Vf)
              a=int(Ac)
              s=int(S)
              underradica = v**2 - a*s*2
              result1 =  cmath.sqrt(underradica)


              print("Vi = \u221A" + str(v)+"^2 - "+ str(a)+ "m/s^2 *2* "+ str(s)+"m  \n")
              print("Vi = " +str(result1)+"m/s")

             else:
              print("invalid input!!")
      if choose_second == 6:
        #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
             Vi = input("Vi(m/s) = ")
             T = input("t(s) = ")
             Ac= input("a(m/s^2) = ")
             S = input("s(m) = ")

             if Vi != " " and T !=" " and Ac!=" ":
              at= int(Ac)*int(T)
              sub = int(Vi) + int(at)

              print("Vf = " + str(Vi) +"m/s + "+ str(Ac) + "m/s^2 *  " + str(T)+"s")
              print("Vf = "+ str(sub)+"m/s")

             elif S != " " and Ac != " " and Vf != "":
              v=int(Vi)
              u=int(Ac)
              s=int(S)
              underradica = v**2 + u*s*2
              result1 = cmath.sqrt(underradica)


              print("Vf = \u221A" + str(v)+"^2m/s + 2*"+ str(u)+"m/s^2 * "+str(s)+"m\n")
              print ("Vf = " +str(result1) +"m/s")


             else:
              print("invalid input!!")
      elif choose_second == 7:

             Vi = input("Vi(m/s) = ")
             Vf = input("Vf(m/s) = ")
             T = input("t(s) = ")
             Ac= input("a(m/s^2) = ")


             if Vi != " " and T !=" " and Ac!=" ":
              vt = int(Vi)*int(T)
              a=int(Ac)
              t=int(T)
              tt=t**2
              mu = 0.5*a*tt
              result = int(mu) + int(vt)

              print("s = 1/2" + str(Ac) +"m/s^2 * "+ str(T) + "^2s +  " + str(Vi)+"m/s * "+str(T)+"s")
              print("s = "+ str(result)+"m")
             elif Vi != " " and Vf !=" " and Ac!=" ":
               vi = int(Vi)
               vf = int(Vf)
               a=int(Ac)
               svi=vi**2
               svf=vf**2
               ma=2*a
               sub = svf - svi
               result = int(sub)/int(ma)
               print("s = "+ str(Vf)+ "^2 m/s - "+ str(Vi)+"^2 m/s  /  2 * " + str(Ac)+"m/s^2")
               print("s = "+str(result)+"m")
             else:
              print("invalid input!!7")
 elif choose == 2:
      print("            Choose one of the following to plot\n")
      print(" Enter 1 to plot x(t) graph                 Enter 2 to plot v(t) graph              Enter 3 to a(t) \n" )
      choose_graph = int(input("put your choose here: "))
      if choose_graph == 1:
        print("enter there coefficient")
        tt=int(input("t\u00b3: "))
        ts=int(input("t\u00b2: "))
        tn=int(input("t: "))
        k=int(input("k(constant):"))
        print("\n                          x(t) = "+str(tt)+"t\u00b3 + ("+str(ts)+")t\u00b2 + ("+str(tn)+"t) + ("+str(k)+")")
        x=np.linspace(-15,15)
        y=tt*x**3+ts*x**2 + tn*x + k
        plt.plot(x,y)
        plt.xlabel("t")
        plt.ylabel("x(t)")


        plt.show()

      elif choose_graph == 2:
        print("enter there coefficient")
        tt=int(input("t\u00b3: "))
        ts=int(input("t\u00b2: "))
        tn=int(input("t: "))
        k=int(input("k(constant):"))
        print("\n                          v(t) = "+str(tt)+"t\u00b3 + ("+str(ts)+")t\u00b2 + ("+str(tn)+"t) + ("+str(k)+")")
        x=np.linspace(-15,15)
        y=tt*x**3+ts*x**2 + tn*x + k
        plt.xlabel("t")
        plt.ylabel("v(t)")
        plt.plot(x,y)
        plt.show()

      elif choose_graph == 3:
        print("enter there coefficient")
        tt=int(input("t\u00b3: "))
        ts=int(input("t\u00b2: "))
        tn=int(input("t: "))
        k=int(input("k(constant):"))
        print("\n                          a(t) = "+str(tt)+"t\u00b3 + ("+str(ts)+")t\u00b2 + ("+str(tn)+"t) + ("+str(k)+")")
        x=np.linspace(-15,15)
        y=tt*x**3+ts*x**2 + tn*x + k
        plt.xlabel("t")
        plt.ylabel("a(t)")
        plt.plot(x,y)
        plt.show()
 elif choose == 3:
      print("            Choose one of the following to find there value \n")
      print(" Enter 1 to find distance(h)                   Enter 2 to find velocty(v)              Enter 3 to find final velocity(vf) \n" )
      choose_free = int(input("put your choise here: \n"))
      if choose_free == 1:
        t =int(input("t(s) = "))
        tt=t**2
        g = int(-9.8)
        h=0.5*g*tt
        print("h = 1/2*-g*"+str(t)+"\u00b2s \n")
        print("h = "+str(h)+"m \n")
      elif choose_free == 2:
        t = int(input("t(s) = "))
        g= int(-9.8)
        v= g * t
        print("v = -g * "+str(t)+"s \n")
        print("v = "+str(v)+"m/s \n")
      elif choose_free == 3:
        h = int(input("h(m) = "))
        g = 9.8
        mul = 2*h*g
        res = math.sqrt(mul)
        print("vf = \u221A 2* g * "+str(h)+"m \n")
        print("vf = "+str(res)+"m/s")
      else:
        print("invalid input")
 else:
  print("invalid input")

except:
  print("Sorry, something went wrong")