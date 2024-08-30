from homework_3month.Google_sheets.config_sheets import service, google_sheet_id_users


def update_google_sheet_register(name, age, email, gender, phone):
    try:
        range_name = 'Sheet1!A:E'
        row = [name, age, email, gender, phone]

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
        range_name = 'Sheet1!A:E'
        result = service.spreadsheets().values().get(
            spreadsheetId=google_sheet_id_users,
            range=range_name
        ).execute()
        rows = result.get('values', [])
        for row in rows[1:]:
            print(f"{row} \n")

        return rows


    except Exception as e:
        print(e)
        return []