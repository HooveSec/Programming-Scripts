Function get-ipconfig {
    param(
    [switch]
    $ip,
    [switch]
    $mac,
    [switch]
    $all
    )
Begin {
    Clear-host
    }
Process {
if($mac) {
Ipconfig -all | select-string “Physical”
    } 
   elseif($ip) {
    Ipconfig -all | select-string “IPv”
    }
    elseif($all) {
    Ipconfig -all
    }
Else {
    Ipconfig
   }
}
End {
    “`n “ + (get-date).datetime
     }
}
# run with # get-ipconfig (-ip|-mac|-all)

