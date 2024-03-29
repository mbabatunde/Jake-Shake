from urllib.request import urlopen
from bs4 import BeautifulSoup 
import re
from datetime import datetime, date
import colorama
from colorama import Fore, Back, Style
import calendar
from twilio.rest import Client
import os

def main():
    quote_page = 'https://www.nhl.com/player/jake-guentzel-8477404'
    page = urlopen(quote_page)

    colorama.init()
    # parser = etree.HTMLParser()
    # tree = etree.parse(StringIO(soup), parser)
    # result = etree.tostring(tree.getroot(), pretty_print=True, method="html")
    # print("result time")
    # print(result)
    # twilio_account = input("What is your Twilio account number ")
    # twilio_auth = input("What is your Twilio authentication token ")
    client = Client(os.environ['TWILIO_ACCOUNT_SID'], os.environ['TWILIO_ACCOUNT_TOKEN'])
    # Parsing
    soup = BeautifulSoup(page, 'html.parser')
    name_box = soup.find_all('div', attrs={'class': 'responsive-datatable__scrollable'})
    str_date = str(soup.find_all('td', attrs={'data-col':'1', 'data-row': '0'})[2])
    goals = str(soup.find_all('td', attrs={'data-col':'2', 'data-row': '0'})[2])
    cleanr = re.compile('<.*?>')
    clean_date = re.sub(cleanr, '', str_date).strip()
    clean_goals = int(re.sub(cleanr, '', goals).strip())
    # print(name_box[1])
    # print(clean_date)
    # print(clean_goals)

    months = {"JAN": 1, "FEB": 2, "MAR": 3, "APR": 4, "MAY": 5, "JUN": 6, 
                "JUL": 7, "AUG": 8, "SEP": 9, "OCT": 10, "NOV": 11, 
                "DEC": 12}
    # print("month")
    # print(now.month)
    correct_month = clean_date[:3]
    correct_day = int(clean_date[4:].strip())
    # print("cm")
    # print(months[correct_month])
    # print("cd")
    # print(correct_day)

    coverted_now = date(datetime.now().year, datetime.now().month, datetime.now().day)
    if (datetime.now().month == 1 and months[correct_month] == 12):
        # Grabs last year
        coverted_jake_date = date(datetime.now().year - 1, months[correct_month], correct_day) #Bad assumption with year
    else:
        coverted_jake_date = date(datetime.now().year, months[correct_month], correct_day)
    # Possible exceptions could have to be with how many days in between, etc.

    game_month = correct_month.capitalize()
    new_game_month = ""
    for i in range(len(calendar.month_abbr)):
        if game_month == calendar.month_abbr[i]:
            new_game_month = calendar.month_name[i]

    print("🗓  Last Game Date: " + new_game_month + " " + str(coverted_jake_date.day) + ", " + str(coverted_jake_date.year))
    lastgame = (coverted_now - coverted_jake_date).days
    result = ""
    if (lastgame < 4):
        if (clean_goals > 1):
            result = "\n✅ 🥛 HALF OFF! Jake scored " + str(clean_goals) + " goals today."
            print(Fore.GREEN + "✅ 🥛 HALF OFF! Jake scored " + str(clean_goals) + " goals today.")
        elif (clean_goals > 0):
            result = "\n✅ 🥛 HALF OFF! Jake scored " + str(clean_goals) + " goal today."
            print(Fore.GREEN + "✅ 🥛 HALF OFF! Jake scored " + str(clean_goals) + " goal today.")
        else:
            result = "\n❌ 👎 Jake didn't score. He's a bum"
            print(Fore.RED + "❌ 👎 Jake didn't score. He's a bum")
    elif (lastgame > 4 and clean_goals > 0):
        result = "\n😭 Been awhile since Jake scored"
        print(Fore.BLUE + "😭 Been awhile since Jake scored")
    else:
        result = "\n😭 Jake didn't score in his last game and Penguins haven't played in awhile "
        print(Fore.YELLOW + "😭 Jake didn't score in his last game and Penguins haven't played in awhile ")

    # number = input("Number you're sending this to: ")
    # TODO: Don't hardcode the number. Another environment variable?
    
    for i in numbers:
        client.messages.create(to= "+1" + i,
                            from_='+12053033977',
                            body=result)
    #     elif (last_days < 0 and last_days > - 4):
    #         print ("Exception since it's the start of the month and the last game was the end of the month")
    #     else:
    #         print("Greater than 4 days since Jake scored")
    # else:
    #     print("Not even the correct month lol")
if __name__ == "__main__":
    main()