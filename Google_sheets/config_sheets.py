from google.oauth2 import service_account
from googleapiclient.discovery import build


SERVICE_ACOUNT_FILE = 'homework-project.json'


creds = service_account.Credentials.from_service_account_file(
    SERVICE_ACOUNT_FILE, scopes=['https://www.googleapis.com/auth/spreadsheets']
)

service = build(serviceName='sheets', version='v4', credentials=creds)

google_sheet_id_users = '1tr1A1UBVRyJQi-Wsziy7WB_3tOuDDhz3PtfzhcdkG8w'
