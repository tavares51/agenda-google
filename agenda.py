from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import os.path
from googleapiclient.discovery import build
from datetime import datetime, timedelta, timezone

class Agenda():
    SCOPES = ['https://www.googleapis.com/auth/calendar']
    TZ_OFFSET = timezone(timedelta(hours=-3))  
    
    def __init__(self, credentials_file='credentials.json', token_file='token.json'):
        self.credentials_file = credentials_file
        self.token_file = token_file
        self.creds = None
        self.authenticate_google_api()
    
    def authenticate_google_api(self):
        """Autentica e inicializa as credenciais da API do Google."""
        if os.path.exists(self.token_file):
            self.creds = Credentials.from_authorized_user_file(self.token_file, self.SCOPES)
        
        if not self.creds or not self.creds.valid:
            if self.creds and self.creds.expired and self.creds.refresh_token:
                self.creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(self.credentials_file, self.SCOPES)
                auth_url, _ = flow.authorization_url(
                    login_hint='vh2r.solutions@gmail.com',
                    access_type='offline',
                    include_granted_scopes='true'
                )
                print(f"Acesse a URL para autenticação: {auth_url}")
                self.creds = flow.run_local_server(port=8080)
            with open(self.token_file, 'w') as token:
                token.write(self.creds.to_json())

    def list_events(self, time_min, time_end):
        """Lista eventos do Google Calendar em um intervalo de tempo."""
        service = build('calendar', 'v3', credentials=self.creds)
        time_min = time_min.isoformat() + 'Z'
        time_end = time_end.isoformat() + 'Z'
        
        events_result = service.events().list(
            calendarId='primary',
            timeMin=time_min,
            timeMax=time_end,
            singleEvents=True,
            orderBy='startTime'
        ).execute()
        return events_result.get('items', [])
    
    def check_events(self, events, date_str, start_input, end_input):
        """
        Verifica se há conflitos de eventos em um intervalo de tempo fornecido.
        """
        start_date = datetime.strptime(f"{date_str} {start_input}", "%Y-%m-%d %H:%M").replace(tzinfo=self.TZ_OFFSET)
        end_date = datetime.strptime(f"{date_str} {end_input}", "%Y-%m-%d %H:%M").replace(tzinfo=self.TZ_OFFSET)

        if end_date < start_date:
            raise ValueError("Horário final não pode ser menor que o inicial.")
        
        for event in events:
            event_start = datetime.fromisoformat(event['start'].get('dateTime'))
            event_end = datetime.fromisoformat(event['end'].get('dateTime'))
            
            if start_date < event_end and end_date > event_start:
                return False, start_date, end_date
        
        return True, start_date, end_date
    
    def create_event(self, event):
        """
        Criação do evento
        """     
        if event:
            service = build('calendar', 'v3', credentials=self.creds)
            event = service.events().insert(calendarId='primary', body=event).execute()
            print("Criado")