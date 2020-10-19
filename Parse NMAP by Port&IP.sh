BEGIN { FS="[[:space:]/]+" }  #executes before file, sets field seperator
/report/ { # in awk, will search for string report, which appears before ip
	    addy=$NF  #sets variable for current field
	    gsub(/[()]/," ",addy) # regex replace to grab only ip address not the entire line 
         }

/tcp.*open/ { # searching for port number along with service name
	      port=$1 "/" $4 #field 1(port#) field4(service name)
	      addr[port]=(port in addr ? addr[port] ORS:"") addy
	    } # ^Adds spaces after the service name per output of ip's
END {   #executes after file
	 for (port in addr) { # for loop to get all of the addresses and ports with a seperator of ====== before the ip is listed
 	print port
 	print "=============="
 	print addr[port]
 	print "\n " # forces a newline
		            }
    }	
#is run with awk -f <script>.awk <file.txt>
