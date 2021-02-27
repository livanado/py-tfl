import requests

url = "https://api.tfl.gov.uk/Line/Mode/tube/Status"
response = requests.get(url)

print("Get TFL status")
# print(response.json())

print(response.json()[0]['lineStatuses'][0]['statusSeverityDescription'])