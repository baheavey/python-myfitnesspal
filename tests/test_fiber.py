#import myfitnesspal
#import datetime

#mfp_day = datetime.datetime.today()
#user = 'spiccirillo1'

#client = myfitnesspal.Client('EBANutrition', '3BATrain!!')
#food_log1 = client.get_date(mfp_day.year, mfp_day.month, mfp_day.day, username=user)
#food_log1.meals
#food_log2 = client.get_date_bh(mfp_day.year, mfp_day.month, mfp_day.day, username=user)
#food_log2.meals
#food_log2.melas[0].entries


####
#import requests
#session = requests.Session()

import lxml.html
import re
#from .entry import Entry

#with open(r'html/sample_printable_diary.html', "r") as f:
with open(r'html/sample_printable_diary_w_exercise.html', "r") as f:
    page = f.read()
tree = lxml.html.document_fromstring(page)
#mfp_table = tree.xpath("//table[@id='food']")

meals   = []
entries = []

food_log_table = tree.xpath("//table[@id='food']")
for row in food_log_table[0].xpath("//tr") or []:
    tds = row.findall('td')
    print(tds[0].text)
    # Table header row    
#    if tds[0].text.lower() == 'foods':
#        print("table header")
#        for td in tds:
#            print(td.text)
    # Rows with a 'class' attribute of 'title' are meal headers
#    elif 'class' in row.attrib:
        # If a previous meal has been extracted add it to meals list and clear entries list for next meal
#        if entries:
#            meals.append(meal_name)
#            entries = []
#        meal_name = tds[0].text.lower()
#        print(meal_name)    
    # All other rows are food log entries
#    else:
#        entries.append(tds[0].text.lower())
#        for td in tds:
#            value = re.sub(r'[^\d.]+', '', td.text)
#            try:
#                num_value = int(value)
#            except:
#                num_value = 0
#            print(num_value)

# Add final meal to list
#if entries:
#    meals.append(meal_name)

#print("MEALS")
#print(meals)

