f_copy = open('image.jpg','rb')
img = f_copy.read()
f_copy.close

copy = open('copy.jpg','wb')
copy.write(img)
copy.close()