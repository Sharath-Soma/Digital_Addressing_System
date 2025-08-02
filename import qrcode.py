import qrcode
import requests

# Define the data to be encoded in the QR code
data = "https://www.example.com"

# Generate the QR code as an image
img = qrcode.make(data)

# Save the image to a file
img.save("qr_code.png")

# Download the image using requests
url = "https://www.example.com/qr_code.png"
response = requests.get(url)

# Save the image to a file
with open("qr_code_downloaded.png", "wb") as f:
    f.write(response.content)
