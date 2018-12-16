import datetime
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file as oauth_file, client, tools
import json
import config


SCOPES = "https://www.googleapis.com/auth/calendar"

def build_service():
    """
    Shows basic usage of the Google Calendar API.

    Prints the start and name of the next event on the user's calendar.
    """
    store = oauth_file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('calendar', 'v3', http=creds.authorize(Http()))
    return service


def fetch_next_birthday(service):
    """
    Fetches birthday event as
    specified in the calendar
    """

    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
    print('Getting the upcoming next event')
    events_result = service.events().list(calendarId='primary', timeMin=now,
                                          maxResults=1, singleEvents=True,
                                          orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        print('No upcoming events found.')
    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        print(start, event['summary'])
        json_data = json.dumps(event, indent=4)
        print(json_data)
        

def create_event(service):
    """
    Create event in the google
    calendar
    """
    event = service.events().insert(calendarId='primary', body=config.event).execute()
    print('Event created: %s' % (event.get('htmlLink')))


def call_services():
    """
    Print the next birthday
    """
    service = build_service()
    fetch_next_birthday(service)
    create_event(service)

    
if __name__ == '__main__':
    call_services()