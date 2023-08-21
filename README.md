# Korean Pronunciation Audio Downloader

The **Korean Pronunciation Audio Downloader** is a Python script that allows you to retrieve and download pronunciation audio files for Korean words from the Korean Dictionary website (krdict.korean.go.kr). This script uses web scraping to extract audio URLs and save them as `.mp3` files on your local machine.

## Requirements

- Python 3.x
- Required Python packages are listed in the `requirements.txt` file.

## Installation

1. Clone or download the project repository to your local machine.
2. Install the required dependencies by running the following command:
   ```shell
   pip install -r requirements.txt
   ```

## Usage

1. Run the script using the command:
   ```shell
   python main.py
   ```
2. Enter a list of Korean words separated by spaces.
3. The script will connect to the Korean Dictionary website and retrieve the pronunciation audio files for the entered words. It will create a "sounds" directory (if not already present) and save each audio file with the corresponding word as the filename.

## Note

- The script uses the requests library to make HTTP requests. To handle unverified HTTPS requests, it suppresses the "InsecureRequestWarning" warning using the urllib3 library. Make sure you are aware of the security implications and use this approach cautiously.

