from office365.runtime.auth.authentication_context import AuthenticationContext
from office365.sharepoint.client_context import ClientContext
from openpyxl import load_workbook

# Dane do uwierzytelniania w SharePoint
sharepoint_url = "https://your-sharepoint-site-url"
username = "your-username"
password = "your-password"

# Ścieżka do pliku Excel na SharePoint
excel_file_path = "/sites/your-site/Shared Documents/ExcelFile.xlsx"

# Inicjalizacja kontekstu uwierzytelniania w SharePoint
ctx_auth = AuthenticationContext(sharepoint_url)
if ctx_auth.acquire_token_for_user(username, password):
    ctx = ClientContext(sharepoint_url, ctx_auth)

    # Pobranie zawartości pliku Excel
    response = ctx.web.get_file_by_server_relative_path(excel_file_path).download()
    
    # Zapisanie zawartości pliku do lokalnej kopi
    local_excel_path = "DownloadedExcelFile.xlsx"
    with open(local_excel_path, 'wb') as local_file:
        local_file.write(response.content)

    # Manipulacja zawartością pliku Excel przy użyciu openpyxl
    workbook = load_workbook(local_excel_path)
    sheet = workbook.active
    # Tutaj możesz dokonać różnych modyfikacji w arkuszu

    # Zapisanie zmodyfikowanego pliku
    modified_excel_path = "ModifiedExcelFile.xlsx"
    workbook.save(modified_excel_path)
    print(f"Zawartość Excel została pobrana i zmodyfikowana: {modified_excel_path}")

else:
    print("Błąd uwierzytelniania w SharePoint.")
