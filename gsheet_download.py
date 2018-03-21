# |_________________________________________________________________________________________________________
# |Para que esse script funcione de acordo, e necessario baixar as libs do google para gdrive:
# |-- pip install gspread oauth2client --
# |
# |O codigo nessa pagina foi baseado no exemplo:
# |https://www.twilio.com/blog/2017/02/an-easy-way-to-read-and-write-to-a-google-spreadsheet-in-python.html
# |_________________________________________________________________________________________________________

# Importando dependencias
import gspread, csv, json, sys
from oauth2client.service_account import ServiceAccountCredentials

# Cria a conexão com o gdrive
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('C:\\workspace\\python\\PRJ_GSHEET\\py_script\\Netshoes-c2d941c81fc3.json', scope)
client = gspread.authorize(creds)

# Procura a planilha a ser baixada
sheet = client.open("Acrônimos - Códigos").sheet1

# Extrai e printa todos os resultados
list_of_hashes = sheet.get_all_records()

# Cria arquivo CSV a partir do JSON baixado
with open("C:\\workspace\\python\\PRJ_GSHEET\\py_script\\output.csv", "w", newline="") as f:
    title = "Loja,Canal,Código do Canal,Sub Canal,Código Sub Canal,Tipo da Campanha / Segmentacao,Código do Tipo da Campanha,Touch Email / Quarto nível,Codigo Touch,Acrônimo,Acrônimos Antigo".split(",")
    cw = csv.DictWriter(f, title, delimiter='|', quoting=csv.QUOTE_MINIMAL)
    cw.writeheader()
    cw.writerows(list_of_hashes)
