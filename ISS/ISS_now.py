import json
import urllib.request
import time
def ISS_now():
    url='http://api.open-notify.org/iss-now.json'
    response = urllib.request.urlopen(url)
    result = json.loads(response.read())

    location = result['iss_position']
    lat = location['latitude']
    lon = location['longitude']
    msg=result['message']
    timen=result['timestamp']

    print("time:",time.asctime(time.localtime(time.time())))

    print('timestamp:',timen)

    print('message:',msg)

    print('latitude:',lat)

    print('longitude:',lon)
