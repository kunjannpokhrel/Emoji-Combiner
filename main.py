import json
import requests

def load_data():
    with open("emojiData.json","r")as f:
     data=json.load(f)
    return data
        
def unicode(emoji):
    return "-".join(f"{ord(c):x}" for c in emoji)


def extract_date(first, second, data):
    unicode1 = unicode(first)
    unicode2 = unicode(second)

    if unicode2 not in data:
        print("Emoji not found.")
        return None
    combinations = data[unicode2]
    for i in combinations:
        if i["leftEmoji"] == unicode1:
            return unicode1, unicode2, i["date"]
    print("Emoji combination not found.")
    return None

def get_image(date,unicode1,unicode2):
        url =f"https://www.gstatic.com/android/keyboard/emojikitchen/{date}/u{unicode1}/u{unicode1}_u{unicode2}.png"
        response = requests.get(url)
        with open("combined.png", "wb") as f:
         f.write(response.content)
        print("THE FACTORY IS DONE COMBINING !!!")

def main():
    first=input("[DONT USE SPACES] \nFirst emoji: ")
    second=input("Second emoji: ")
    data=load_data()
    unicode1, unicode2, date = extract_date(first, second, data)
    get_image(date, unicode1, unicode2)

main()