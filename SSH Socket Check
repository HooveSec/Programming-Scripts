ps -ef | grep -v grep | grep ssh  # gets a baseline 
exec 7<>/dev/tcp/localhost/22  # creates the ssh with the socket
ps -ef | grep -v grep | grep ssh # compares to baseline
pid=$(ps -ef | grep -v grep | grep ssh | tail -n 1 | cut -d' ' -f7) # grabs the pid of the file
Cd /proc/$pid/fd # goes to location of pid in proc
stat 5 2>/dev/null # grabs file permissions for pipe
Stat 6 2>/dev/null # grabs permissions for pipe
ps -ef | grep -v grep | grep ssh | tail -n 1 | cut -d' ' -f7 # grabs the pid
