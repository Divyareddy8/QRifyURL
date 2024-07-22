import qrcode # type: ignore
from PIL import Image # type: ignore 
import re

def is_valid_url(url: str) -> bool:
    # Simple regex to check if the input is a valid URL
    regex = re.compile(
        r'^(?:http|ftp)s?://' # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' # domain...
        r'localhost|' # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|' # ...or ipv4
        r'\[?[A-F0-9]*:[A-F0-9:]+\]?)' # ...or ipv6
        r'(?::\d+)?' # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return re.match(regex, url) is not None

def generate_qr(data: str, version: int = 1, box_size: int = 50, border: int = 1) -> Image:
    qr = qrcode.QRCode(
        version=version,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=box_size,
        border=border,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    return img

# Example usage:
user_data = input("Enter the URL to encode in the QR code: ")

if is_valid_url(user_data):
    qr_image = generate_qr(user_data)
    qr_image.save("UserQRCode.png")
    print("QR Code generated and saved as UserQRCode.png")
else:
    print("Invalid URL. Please enter a valid URL.")
