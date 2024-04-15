import subprocess
from Crypto.Cipher import AES
import base64

def download_zip_from_url(url):
    # Use wget or curl to download the zip file from the provided URL
    subprocess.run(["wget", url])

def extract_txt_from_image():
    # Use steghide to extract the txt file from the image
    subprocess.run(["steghide", "extract", "-sf", "embedded_image.jpg"])

def decrypt_text_from_file():
    # Read the extracted txt file
    with open("hidden_text.txt", "r") as file:
        encrypted_text = file.read().strip()

    # Decrypt the encrypted text using AES 128 decryption
    cipher = AES.new(b'cmucylabintern24', AES.MODE_ECB)
    decrypted_text = cipher.decrypt(base64.b64decode(encrypted_text)).decode("utf-8")

    return decrypted_text

def main():
    # Download the zip file from the provided URL
    download_zip_from_url("https://github.com/olusecc/CTFChallenge.git/open_for_a_surprise/")

    # Extract the txt file from the image
    extract_txt_from_image()

    # Decrypt the encrypted text
    decrypted_text = decrypt_text_from_file()

    # Print the flag
    print("Flag:", decrypted_text)

if __name__ == "__main__":
    main()

