import csv
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

csv_file = "messages.csv"
html = open("frostbite.html")
soup = BeautifulSoup(html, "html.parser")


def get_all_user_messages(member, member_id):
    messages = []
    message_div = soup.find_all("div", {"class": "chatlog__message-group"})
    member_title = soup.find_all("span", {"data-user-id": member_id})
    if message_div and member_title:
        member_messages = soup.find_all("span", {"class": "markdown"})
        for message in member_messages:
            messages.append(get_user_message_row(member, message))
    return messages


def get_user_message_row(member, message):
    # print(f"{member}: {message.text}")
    row = [member, message.text]
    return row


def write_all_messages_to_file():
    with open(csv_file, "w", newline="") as f:
        field_names = ["Member", "Message"]

        writer = csv.DictWriter(f, fieldnames=field_names)
        writer.writeheader()

        for member in frostbite_members:
            messages = get_all_user_messages(member, frostbite_members[member])
            for message in messages:
                writer.writerow({"Member": message[0], "Message": message[1]})


if __name__ == "__main__":
    write_all_messages_to_file()
