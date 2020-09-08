#!/usr/bin/expect -f
#set -x
set timeout 60
spawn ssh -oKexAlgorithms=+diffie-hellman-group1-sha1 root@bgl-mitg-sim448

expect "This is your UNIX password:"
send "starent\r"
send "ls\r"
interact
