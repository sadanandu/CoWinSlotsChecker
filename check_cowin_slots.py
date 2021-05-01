import requests
import datetime
import json
import time
def get_slots(date, pincode):
    resp = requests.get(
        "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={}&date={}".format(pincode, date))
    time.sleep(1)
    json_data = json.loads(resp.text)
    center = []
    for i in json_data["centers"]:
        for each in i["sessions"]:
            if each["min_age_limit"] in (18, '18') and each["available_capacity"] > 0:
                center.append(i)
                break
    if center:
        return str(center)
    else:
        return None

def lambda_handler(event, context):
    # TODO implement
    
    reply = []
    for i in range(7):
        d2 = datetime.date.today() + datetime.timedelta(i)
        try:
            pincode = '413531'
            centers = get_slots(d2.strftime("%d-%m-%Y"), pincode)
            if centers:
                reply.append(centers)
            pincode = '413512'
            centers = get_slots(d2.strftime("%d-%m-%Y"), pincode)
            if centers:
                reply.append(centers)
            
        except Exception as e:
            print("Error occurred for fetching for %s" % d2.strftime("%d-%m-%Y") )
    if reply:
        return {
            'statusCode': 200,
            'body': json.dumps('\n'.join(reply))
        }
    
    
