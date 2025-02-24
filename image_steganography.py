import cv2
import os

#Load the image
image_path = "original_image.jpg"
img=cv2.imread(image_path)

#Check if the image was loaded correctly
if img is None:
    raise FileNotFoundError(f"Image not found at {image_path}")

#Input secret message and password
msg = input("Enter the secret message to hide: ")
password = input("Enter a passcode for encryption: ")

#Create encoding and decoding dictionaries for ASCII characters
d = {}
c = {}

for i in range(255):
    d[chr(i)] = i
    c[i] = chr(i)

m = 0
n = 0
z = 0

#Embed the secret message into the image
for i in range(len(msg)):
    img[n, m, z] = d[msg[i]]
    n = n + 1
    m = m + 1
    z = (z + 1) % 3

#Save the encrypted image and open it
cv2.imwrite("encrypted_image.jpg", img)
os.system("start encrypted_image.jpg")

#Decryption process
message = ""
n = 0
m = 0
z = 0

pas = input("Enter passcode for Decryption: ")
if password == pas:
    for i in range(len(msg)):
        message = message + c[img[n, m, z]]
        n = n + 1
        m = m + 1
        z = (z + 1) % 3
    print("Decryption message: ", message)
else:
    print("Authentication Failed: Incorrect Passcode")
