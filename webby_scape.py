from datetime import datetime
import requests
import openpyxl
from time import time

start = time()
link = "https://api.recogmedia.net/api/search/search"

payload1 = {"PageNumber": 1, "PieceType": "true", "awards": ["Webby Winner"], "categories": [
], "years": ["2024"], "Sort": "null", "MediaType": [7], "ByEntries": "true"}

payload2 = {"PageNumber": 1, "PieceType": "true", "awards": [], "categories": [
], "years": ["2024"], "Sort": "null", "MediaType": [7], "ByEntries": "true"}

response1 = requests.post(url=link, data=payload1).json()
response2 = requests.post(url=link, data=payload2).json()

wb = openpyxl.Workbook()
sheet = wb.active
sites1 = response1["Data"]
sites2 = response2["Data"]

sites = sites1 + sites2
print(len(sites))

for i in range(0, len(sites)):
    c2 = sheet.cell(row=i+2, column=1)
    c2.value = sites[i]["OrganizationUrl"]

wb.save("Webby_2024_awards.xlsx")
end = time()
takenTime = datetime.utcfromtimestamp(end - start)
takenTime = f"""{f"{takenTime.minute} Min(s)" if takenTime.minute > 0 else ""}{f"{takenTime.second} Sec(s)" if takenTime.second > 0 else "0.0 Sec(s)"}"""
print(f"Success \nTime Taken :- {takenTime}")
