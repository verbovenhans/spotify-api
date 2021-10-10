#!/usr/bin/env python3

#import modules needed to get token, post en get requests en parse received data
import requests
import json

#there are different url's for authorization and api-requests
main_url = "https://api.spotify.com"
get_token_url = "https://accounts.spotify.com/api/token"

#get your own client_id & client_secret on http://developer.spotify.com
client_id = ""      #you need your own client-id, fill it in between the ""
client_secret = ""  #you need your own client-secret, fill it in between the ""


#first request a token needed to authorize requests
def get_token():
    reply = requests.post(get_token_url, {
        'grant_type':'client_credentials',
        'client_id':client_id,
        'client_secret':client_secret,
    })
    if reply.status_code == 200:
        return reply.json()['access_token']
    else:
        raise Exception(f"Status code {reply.status_code} and text {reply.text}, while trying to authorize.")


token = get_token()
#in order to do a get request, authorization is done in the header of the request
auth_text = 'Bearer '+token
header = {'Authorization':auth_text}

while True:
    query = input('Which artist are you looking for? (type quit if you want to stop looking): ')
    if query == 'quit' or query == 'Quit':
        break
    else:
        url = main_url + '/v1/search?q=' + query + '&type=artist'
        request = requests.get(url, headers=header)
        reply = request.json()
        #the format isn't as graphically pleasing as I would want it to be, I should have worked with a dictionary or
        #str().rjust or something like a table, but time was up and functionality is more important for now.
        print('Name                                  Genres')
        print('--------------------------------------------------------------------------------------')
        for each in reply["artists"]["items"]:
            print((each["name"]), end="\t\t\t\t")
            print(((each)["genres"]))
        print('---------------------------------------------------------------------------------------')
