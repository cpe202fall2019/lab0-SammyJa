def weight_on_planets():
   eWeight = float(input("What do you weigh on earth? "))
   jWeight = eWeight * 2.34
   mWeight = eWeight * 0.38
   print("\nOn Mars you would weigh %.2f"%(mWeight), "\nOn Jupiter you would weigh %.2f"%jWeight)




if __name__ == '__main__':
   weight_on_planets()
