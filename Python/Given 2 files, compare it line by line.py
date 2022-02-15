#compare each file line by line 
def compare(f0, f1):
   diffs = []
   with open(f0) as file0, open(f1) as file1:
       lines0 = file0.readlines()
       lines1 = file1.readlines()

       for l in range(len(lines0)):
           if lines0[l] != lines1[l]:
               diffs.append(l)
   return diffs
