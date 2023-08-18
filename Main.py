import requests
import time
from colorama import Fore, Style

def check_website(url):
     start_time = time.time()

     try:
         response = requests.get(url)
         if response.status_code == 200:
             status_message = Fore.GREEN + "[OK] Site running:" + Style.RESET_ALL
         elif response.status_code == 403:
             status_message = Fore.RED + "[WEB SITE DOWN] Site is unavailable (403 Forbidden):" + Style.RESET_ALL
         else:
             status_message = Fore.RED + "[WEB SITE DOWN] Site is down (HTTP Error Code: {})" + Style.RESET_ALL
             status_message = status_message.format(response.status_code)
     except requests.ConnectionError:
         status_message = Fore.RED + "[ERROR] Connection error:" + Style.RESET_ALL

     elapsed_time = time.time() - start_time
     response_time_message = Fore.CYAN + "Response time: {:.2f} seconds".format(elapsed_time) + Style.RESET_ALL

     print(status_message, url, response_time_message)

if __name__ == '__main__':
     site_url = input("Please enter the URL of the website you want to check: ")

     while True:
         check_website(site_url)
         time.sleep(0) # 1 minute cooldown