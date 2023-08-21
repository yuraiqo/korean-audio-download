import requests
import re
import os
import urllib3
from bs4 import BeautifulSoup

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Create a "sounds" directory if it doesn't exist
if not os.path.exists("sounds"):
    os.makedirs("sounds")

words = input("Enter words: ").split()

# Iterate over each word to retrieve and save pronunciation sounds
for word in words:
    response = requests.get(f"https://krdict.korean.go.kr/eng/dicSearch/search?nation=eng&nationCode=6&ParaWordNo=&mainSearchWord={word}", verify=False)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        first_dt = soup.find("dt")
        if first_dt:
            # Find the <a> tag containing the link to the pronunciation sound (.mp3 file)
            sound_element = first_dt.find("a", href=lambda href: "fnSoundPlay" in href)
            if sound_element:
                mp3_url = re.search(r"fnSoundPlay\('([^']+)'", str(sound_element)).group(1)
                # Download the pronunciation sound and save it as an .mp3 file
                response_mp3 = requests.get(mp3_url, verify=False)
                if response_mp3.status_code == 200:
                    with open(f"sounds/{word}.mp3", "wb") as mp3_file:
                        mp3_file.write(response_mp3.content)
                    print(f"Downloaded sound for word {word}.")
                else:
                    print(f"Failed to download sound for word {word}.")
            else:
                print(f"No sound found for word {word}.")
        else:
            print(f"Word {word} wasnt found.")
    else:
        print("Failed to fetch the website.")
