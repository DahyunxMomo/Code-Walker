import qrcode
 
# Data to be encoded
data = 'tkm mayo'
 
# Encoding data using make() function
img = qrcode.make(data)
 
# Saving as an image file
img.save('prueba.png')