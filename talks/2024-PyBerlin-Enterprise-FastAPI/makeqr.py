import sys
import qrcode

def generate_qr_code(link, output_file="qrcode.png"):
    """
    Generates a QR code for the given HTTP link and saves it as an image file.

    Args:
        link (str): The HTTP link to encode in the QR code.
        output_file (str): The name of the output image file (default is "qrcode.png").
    """
    # Create a QR code object
    qr = qrcode.QRCode(
        version=1,  # Controls the size of the QR code (1 is the smallest)
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
        box_size=10,  # Size of each box in the QR code
        border=4,  # Border size (minimum is 4)
    )

    # Add the data to the QR code
    qr.add_data(link)
    qr.make(fit=True)

    # Create an image of the QR code
    img = qr.make_image(fill="black", back_color="white")

    # qr.print_tty()

    # Save the QR code image
    img.save(output_file)
    print(f"QR code saved as {output_file}")

# Example usage
if __name__ == "__main__":
    link = sys.argv[1]
    generate_qr_code(link)
