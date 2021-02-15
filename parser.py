from re import M
from typing import FrozenSet
from bs4 import BeautifulSoup

frostbite_members = {
    "Zack": "161272422949978113",
    "Kameron": "179718268494413826",
    "Bitmin": "210095732785414144",
    "Chris": "170938761021095936",
    "Greg": "127215621330042880",
    "Andrew": "149687867285700608",
    "Jed": "149686178939928576",
    "Max": "121306516337852418",
    "Zain": "140858227049889793",
}

html = open("data.html")
soup = BeautifulSoup(html, "html.parser")

data = []

for member in frostbite_members:
    message_div = soup.find_all("div", {"class": "chatlog__message-group"})
    member_title = soup.find_all("span", {"data-user-id": frostbite_members[member]})
    if message_div and member_title:
        member_messages = soup.find_all("span", {"class": "markdown"})
        for message in member_messages:
            print(f"{member}: {message.text}")
