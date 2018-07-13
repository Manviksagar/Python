# import sagpack
from FirstPython import add
from EmailConnection import emailfunction


#result=sagpack.add(2,5)
result=add(5,6)
print(result)
#p='Here is a message from python which was created using smtplib module.'
p='sagar parameter passing is working'
emailfunction(p)