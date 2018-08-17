import gspread
from oauth2client.service_account import ServiceAccountCredentials


def authenticate_and_get_data():
  scope = ['https://spreadsheets.google.com/feeds',
           'https://www.googleapis.com/auth/drive']
  file_name = "./resources/Dave's Google Sheets Reader-2f423c3c3765.json"
  #file_location = open("./resources/Dave's Google Sheets Reader-2f423c3c3765.json", 'r')
  credentials = ServiceAccountCredentials.from_json_keyfile_name(file_name, scope)
  gc = gspread.authorize(credentials)
  sh = gc.open_by_key("1Wjz6h645dtkdNnTE9N0u_7Rexb4pHaOnT3rJ49URwB4")
  wks = sh.worksheet("Exercise Log")
  all_data_in_list_of_lists = wks.get_all_values()

  return all_data_in_list_of_lists