#Given the military time in the argument miltime, return a string
#containing the greeting of the day.
#   0300-1159 "Good Morning"
#   1200-1559 "Good Afternoon"
#   1600-2059 "Good Evening"
#   2100-0259 "Good Night"
def Miltime(miltime):
   if 301 <= miltime < 1200:
       return 'Good Morning'
   elif 1200 <= miltime < 1600:
       return 'Good Afternoon'
   elif 1600 <= miltime < 2100:
       return 'Good Evening'
   else:
       return 'Good Night'
