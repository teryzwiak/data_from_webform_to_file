import requests
from openpyxl import load_workbook

# Adres URL do pliku Excel na SharePoint
excel_url = "https://onedrive.live.com/edit?id=F1CE4A599DAD8C9D!133878&resid=F1CE4A599DAD8C9D!133878&ithint=file%2cxlsx&wdo=2&cid=f1ce4a599dad8c9d"

# Pobranie zawartości pliku Excel bez uwierzytelniania
response = requests.get(excel_url)

if response.status_code == 200:
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
    print(f"Nieudane pobieranie pliku. Kod statusu: {response.status_code}")