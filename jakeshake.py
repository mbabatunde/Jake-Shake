from urllib.request import urlopen
from bs4 import BeautifulSoup 
import re
from datetime import datetime, date

quote_page = 'https://www.nhl.com/player/jake-guentzel-8477404'
page = urlopen(quote_page)

# parser = etree.HTMLParser()
# tree = etree.parse(StringIO(soup), parser)
# result = etree.tostring(tree.getroot(), pretty_print=True, method="html")
# print("result time")
# print(result)

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

now = datetime.now()
coverted_now = date(datetime.now().year, datetime.now().month, datetime.now().day)
last_days = now.day - correct_day
coverted_jake_date = date(now.year, months[correct_month], correct_day) #Bad assumption with year
# Possible exceptions could have to be with how many days in between, etc.

if ((coverted_now - coverted_jake_date).days < 4):
    if (clean_goals > 0):
        print("Can get a jake shake today")
    else:
        print("Jake didn't score. He's a bum")
else:
    print("Been awhile since Jake scored")
#     elif (last_days < 0 and last_days > - 4):
#         print ("Exception since it's the start of the month and the last game was the end of the month")
#     else:
#         print("Greater than 4 days since Jake scored")
# else:
#     print("Not even the correct month lol")