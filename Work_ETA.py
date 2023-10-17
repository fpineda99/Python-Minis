import datetime
import googlemaps

def get_commute_duration():
    home_address = "home_address"
    school_address = "Calhoun Rd, Houston, TX 77004"
    
    google_maps_api_key = "API_KEY"
    gmaps = googlemaps.Client(key=google_maps_api_key)
    
    directions = gmaps.directions(home_address, school_address)
    first_leg = directions[0]['legs'][0]
    duration = first_leg['duration']['text']
    return duration

def send_text_message(message):
    twilio_account_sid = "twilio_account_sid"
    twilio_account_token = "twilio_account_token"
    twilio_phone_num = "twilio_phone_num"
    my_phone_num = "my_phone_num"
    client = Client(twilio_account_sid, twilio_account_token)

    client.message.create(
        to=my_phone_num,
        from_=twilio_phone_num
        body=message
    )

def main():
    duration = get_commute_duration()
    
    now = datetime.now()
    arrival_time = (now + duration).strftime('%I:%M %p')
    
    mesasge = (
        f"Good Morning!\n\n"
        f"Estimated commute time from home to school at 9am: {duration} minutes\n"
        f"Leave now to school at 9am to arrive at approximately {arrival_time}"
    )
    
    send_text_message(mesasge)
    
if __name__ == '__main__':
    main()