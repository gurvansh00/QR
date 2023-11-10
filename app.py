import streamlit as st
import qrcode
st.title('Free QR creator')
st.subheader('Created by: :red[Gurvansh Singh] Senior Associate Tech Mentor- ML :green[Athena Education]',divider = 'rainbow')
st.write('Just Enter your url and hit Enter/Return')

# Create a QR code object with a larger size and higher error correction
qr = qrcode.QRCode(version=3, box_size=20, border=10, error_correction=qrcode.constants.ERROR_CORRECT_H)

val = st.text_input('Enter the URL')
# Define the data to be encoded in the QR code

# Add the data to the QR code object
qr.add_data(val)

# Make the QR code
qr.make(fit=True)

# Create an image from the QR code with a black fill color and white background
img = qr.make_image(fill_color="black", back_color="white")
img.save("image.png")
# Save the QR code image
st.image('image.png')
