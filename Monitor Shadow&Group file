#grabs read write access and execute permissions
auditctl -w /etc/passwd -p wrax -k password-file
auditctl -w /etc/group -p wrax -k group-file
auditctl -w /etc/shadow -p wrax -k shad-file

#to check if anything is changed
#ausearch -f /etc/passwd
#ausearch -f /etc/group
#ausearch -f /etc/shadow 
