import os
import requests

url = "https://raw.githubusercontent.com/nasa4rayan/Let-it-happen-/main/-%20Tame%20Impala%20-%20Let%20it%20happen%20%20sped%20up%20-.mp3"
file_name = "- Tame Impala - Let it happen  sped up -.mp3"

print("[+] Downloading...")
r = requests.get(url)

with open(file_name, "wb") as f:
    f.write(r.content)

print("[+] Done saved as:", file_name)

os.system(f'ffplay -nodisp -autoexit -- "{file_name}"')
