# First, install the qrcode library if you haven't already
# You can install it by running: pip install qrcode[pil]

import qrcode

# Function to generate a QR code for a given link
def generate_qr_code(link, filename="qrcode.png"):
    # Create a QR code object with the link data
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(link)
    qr.make(fit=True)

    # Generate the QR code image
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the QR code as an image file
    img.save(filename)
    print(f"QR code saved as {filename}")

# Example usage
link = ""
generate_qr_code(link)
