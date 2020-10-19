#To pull out just characters other then letters, useful for grabbing numbers
def onlyletters(arg):
   result = []
   for c in arg:
       if not c.isnumeric():
           result.append(c)
   return ''.join(result)
# one liner version 
#   return ''.join([ c for c in arg if c.isalpha() ])
