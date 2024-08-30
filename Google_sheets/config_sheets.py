from google.oauth2 import service_account
from googleapiclient.discovery import build


SERVICE_ACCOUNT_FILE = 'lesson_7.json'


creds = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=['https://www.googleapis.com/auth/spreadsheets']
)

service = build(serviceName='sheets', version='v4', credentials=creds)

google_sheet_id_users = '1TgJOEl3imrj-2wK5s7hq1Z1Ernw3T96SE1bCCF24qYs'
