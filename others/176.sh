#!/usr/bin/expect -f
#set -x
set timeout 60
spawn ssh intucell@ic-vm-176.cisco.com

expect "intucell@ic-vm-176.cisco.com's password: "
send "intucell\r"
send "ls\r"
interact
