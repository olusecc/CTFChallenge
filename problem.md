Title: "Open for Surprise"
Challenge Category: "Forensics"
Suggested by: "Oluwole"
Basic / starter action:
Download flag from this link https://github.com/olusecc/CTFChallenge.git/cylab.jpg

Description:
  Can you find the hidden treasure within this innocent picture?

hints:
  - "what is Steganography?"
  - "There are various tools and techniques you can use to detect and extract hidden data from files."
  - "key:cmucylabintern24"

files:
  - challenge.zip

tags:
  - steganography
  - encryption
  - forensics


Solution Overview :

This challenge is designed to test the participants' ability to download a file from a provided link and extract its contents. The flag is hidden within a text file embeded in a picture, which participants must download and extract, and decrypt the flag

Learning Objective :

The primary learning objective of this challenge is to familiarize participants with basic command-line tools and techniques for downloading and extracting files. Additionally, participant have to learn the act of steganography(hidden in plainsight)

Solution Details: 

To solve this challenge, participants can follow these steps

1. Use a command-line tool like `wget`, `curl`, or a web browser to download the `challenge.zip` file from the provided link.
2. Once the `challenge.zip` file is downloaded, use a ZIP extraction utility (e.g., `unzip` on Linux/macOS or a GUI tool on Windows) to extract the contents of the ZIP file.
3. The extracted files should contains a picture which looks like an ordinary picture but has an embeded infomation(a text file) in it.
4. The participant now extract the text file using a tool like steghide.
5. The text is a clue to the algorithm used to encode the flag. The key is already provided in the hint.