Function get-square([int]$userinput)
{
     $finalment = $userinput * $userinput
     Return $finalment
}
$userinput = read-host ‘Enter your choice of number’
$finalment = get-square $userinput
Write-output “$userinput * $userinput = $finalment”
## get-circle## run like this  

