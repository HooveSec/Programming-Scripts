def isprivate(ip):
   octet = ip.split('.')
   octets = list(map(int,octet))
   if octets[0] == 192 and octets[1] == 168:
       if 0 <= octets[2] <= 255 and 0 <= octets[3] <= 255:
           return True
   return False
   pass
#used to determine if its a private ip address in 192.168.0.0/16
