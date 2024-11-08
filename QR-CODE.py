import qrcode
from PIL import Image
# Function to interactively generate a QR code
def generate_qr_code():
    # Get user input for the QR code
    print("Welcome to the Interactive QR Code Generator!")
    
    # User input for the URL to encode
    url = input("Enter the URL: ")

    # User input for fill color and background color
    fill_color = input("Enter the fill color : ") or 'red'
    back_color = input("Enter the background color : ") or 'yellow'

    # User input for QR code size and border
    box_size = int(input("Enter the box size : ")or 10)
    border_size = int(input("Enter the border size : ") or 4)
    
    # Create the QR code object
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=box_size,
        border=border_size
    )
    
    # Add data to the QR code
    qr.add_data(url)
    qr.make(fit=True)

    # Create the image with custom fill and background colors
    img = qr.make_image(fill_color=fill_color, back_color=back_color)

    # User input for the file name to save the QR code image
    file_name = input("Enter the name to save the QR code image: ")
    
    # Save the image to the specified file name
    img.save(file_name)
    print(f"QR code saved as {file_name}.")

    # Optionally show the image
    img.show()

# Call the function to generate QR code
generate_qr_code()

