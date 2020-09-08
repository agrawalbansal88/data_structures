
cnt =10
for i in range(cnt):
    print " "*(cnt-i-1), # Note: "," in print will give an extra space
    print "*"*(i+1)

for i in range(cnt):
    print " "*(cnt-i-1) + "*"*(i+1)

for i in range(cnt):
    print "* "*(i) + "*"

for i in range(cnt):
    print " "*(cnt-i-1) + "* "*(i) + "*" + " "*(cnt-i-1)

"""
     *
    **
   ***
  ****
 *****
    *
   **
  ***
 ****
*****
*
* *
* * *
* * * *
* * * * *
    *
   * *
  * * *
 * * * *
* * * * *
"""
