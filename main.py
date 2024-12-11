from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import os.path
from googleapiclient.discovery import build
from datetime import datetime, timedelta, timezone
from agenda import Agenda

    
if __name__ == '__main__':
    try:
        date_input = "2024-12-12"
        start_input = '12:30'
        end_input = '13:30'
        
        start_date = datetime.strptime(f"{date_input} 00:00", "%Y-%m-%d %H:%M")
        end_date = start_date + timedelta(days=1)
        
        agenda = Agenda()
        events = agenda.list_events(start_date, end_date)
        
        checked, start_date, end_date = agenda.check_events(events, date_input, start_input, end_input)
        if checked:
            print("agendar")
            body = {
                'summary': 'Cliente: Victor',
                'location': 'Salão',
                'description': 'Barba e Cabelo',
                'start': {
                    'dateTime': f'{start_date.isoformat()}',
                    'timeZone': 'America/Los_Angeles',
                },
                'end': {
                    'dateTime': f'{end_date.isoformat()}',
                    'timeZone': 'America/Los_Angeles',
                },
                'reminders': {
                    'useDefault': False,
                    'overrides': [
                    {'method': 'email', 'minutes': 24 * 60},
                    {'method': 'popup', 'minutes': 10},
                    ],
                },
            }
            
            agenda.create_event(body)

        else:
            print("não agendar")
    
    except Exception as e:
        print(str(e))