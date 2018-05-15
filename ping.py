import os
#taking input url from user
URL = input("enter the URL: ") 
response = os.system('ping %s -n 1' % (URL,))

#checking for response
if response == 0:
  print (URL, 'is up!')
  f = open("pinghistory.txt", "a+")
  f.write(URL+" is up!  ")
  f.close()

else:
  print (URL, 'is down!')
  f = open("pinghistory.txt", "a+")
  f.write(URL+" is down!  ")
  f.close()


  
