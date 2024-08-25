from Google_sheets.config_sheets import service, google_sheet_id_users


def update_google_sheet_register(name, age, email, gender, phone, telegram_id):
    try:
        range_name = 'Sheet1!A:F'
        row = [name, age, email, gender, phone, telegram_id]

        service.spreadsheets().values().append(
            spreadsheetId=google_sheet_id_users,
            range=range_name,
            valueInputOption='RAW',
            insertDataOption='INSERT_ROWS',
            body={'values': [row]}
        ).execute()
        print(row)
    except Exception as e:
        print(e)


def open_sheet():
    try:
        range_name = 'Sheet1!F:F'
        result = service.spreadsheets().values().get(
            spreadsheetId=google_sheet_id_users,
            range=range_name
        ).execute()
        rows = result.get('values', [])
        print(rows)

        return rows


    except Exception as e:
        print(e)
        return []


def extract_telegram_ids(rows):
    telegram_ids = [row[0] for row in rows[1:] if len(rows) > 0]
    return telegram_ids
