import requests
import datetime
import json
import time
def get_slots(date, pincode):
    url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={}&date={}".format(pincode, date)
    resp = requests.get(url)
    #time.sleep(1)
    json_data = json.loads(resp.text)
    center = []
    print("Received for %s: "%url + str(json_data))
    for i in json_data["centers"]:
        for each in i["sessions"]:
            if int(each["available_capacity"]) > 0 and datetime.datetime.strptime(each["date"], "%d-%m-%Y").date() >= datetime.date.today():
                print("Got a session")
                return (each["date"], pincode)



def lambda_handler(event, context):
    # TODO implement
    
    reply = []
    for i in [2,9]:
        d1 = datetime.date(month=5,day=i,year=2021)
        #d2 = d1 + datetime.timedelta(i)
        d2 = d1
        try:
            pincodes = ['431517']
            for pincode in pincodes:
                got_slot = get_slots(d2.strftime("%d-%m-%Y"), pincode)
                if got_slot:
                    return {
                        'statusCode': 200,
                        'body': json.dumps(str(got_slot))
                    }
        except Exception as e:
            print("Error occurred for fetching for %s: %s" % (d2.strftime("%d-%m-%Y"), str(e)) )
    raise Exception("No slots")
                
            # pincode = '413512'
            # got_slot = get_slots(d2.strftime("%d-%m-%Y"), pincode)
            # if got_slot:
            #     return {
            #         'statusCode': 200,
            #         'body': json.dumps(str(got_slot))
            #     }
            
