# Open for a Surprise Challenge

This is a simple "Forensic Skills - Challenge" for the CTF competition. The goal is to download and extract a ZIP file containing the flag.

## Challenge Description

The challenge description and instructions are provided in the `problem.md` file.

## Challenge Files

- `challenge.zip`: The ZIP file containing the flag that participants need to download and extract.

## Deployment

To deploy this challenge using CMGR, follow these steps:

1. Clone this repository: `git clone https://github.com/olusecc/CTFChallenge.git`
2. Navigate to the repository directory: `cd challenge`

## Testing

To test the challenge locally, follow these steps:

1. Start a local instance of the CMGR server: `cmgr server`
2. In a separate terminal, navigate to the repository directory: `cd open-for-surprise`
3. Deploy the challenge locally: `cmgr deploy .`
4. Access the challenge description and link from the local CMGR server.
5. Verify that you can download and extract the `challenge.zip` file correctly.

After testing, you can use `cmgr clean` to reset the local CMGR server.