import sys
import os 

def install_if_missing(pkg_name):
    try:
        __import__(pkg_name)
    except ImportError:
        os.system(f"{sys.executable} -m pip install {pkg_name}")

# Kiểm tra và cài đặt các thư viện
for pkg in ('pyurl', 'tabulate', 'art', 'colorama'):
    install_if_missing(pkg)

# Bây giờ chắc chắn đã có, import thật sự
import pyurl
import time
from time import sleep
import sys
import os
from art import *
from colorama import Fore
import json
import random
from tabulate import tabulate
import requests
# --- Định nghĩa lại pyurl dựa trên requests ---
class pyurl:
    @staticmethod
    def get(url, headers=None, params=None):
        """
        Gửi GET request qua requests, trả về dict JSON.
        """
        resp = requests.get(url, headers=headers, params=params)
        resp.raise_for_status()
        return resp.json()

    @staticmethod
    def post(url, headers=None, json_data=None, data=None):
        """
        Gửi POST request qua requests, trả về dict JSON.
        """
        if json_data is not None:
            resp = requests.post(url, headers=headers, json=json_data)
        else:
            resp = requests.post(url, headers=headers, data=data)
        resp.raise_for_status()
        return resp.json()

    @staticmethod
    def get_pycurl(url, headers=None):
        """
        Gửi GET request qua pycurl, trả về dict JSON.
        """
        buffer = BytesIO()
        curl = pycurl.Curl()
        curl.setopt(curl.URL, url)
        if headers:
            curl.setopt(curl.HTTPHEADER, [f"{k}: {v}" for k, v in headers.items()])
        curl.setopt(curl.WRITEDATA, buffer)
        curl.perform()
        curl.close()
        return json.loads(buffer.getvalue().decode("utf-8"))

    @staticmethod
    def post_pycurl(url, headers=None, json_data=None, data=None):
        """
        Gửi POST request qua pycurl, trả về dict JSON.
        """
        buffer = BytesIO()
        curl = pycurl.Curl()
        curl.setopt(curl.URL, url)
        curl.setopt(curl.POST, 1)
        if json_data is not None:
            payload = json.dumps(json_data)
            curl.setopt(curl.POSTFIELDS, payload)
        elif data is not None:
            curl.setopt(curl.POSTFIELDS, data)
        if headers:
            curl.setopt(curl.HTTPHEADER, [f"{k}: {v}" for k, v in headers.items()])
        curl.setopt(curl.WRITEDATA, buffer)
        curl.perform()
        curl.close()
        return json.loads(buffer.getvalue().decode("utf-8"))

def countdown(time_sec):
    for remaining_time in range(time_sec, -1, -1):
        colors = [
                "\033[1;37mN\033[1;36mD\033[1;35mK \033[1;32mT\033[1;31mO\033[1;34mO\033[1;33mL\033[1;31m\033[1;32m",
                "\033[1;34mN\033[1;31mD\033[1;37mK \033[1;36mT\033[1;32mO\033[1;35mO\033[1;37mL\033[1;31m\033[1;32m",
                "\033[1;31mN\033[1;37mD\033[1;36mK \033[1;33mT\033[1;35mO\033[1;32mO\033[1;34mL\033[1;31m\033[1;32m",
                "\033[1;32mN\033[1;33mD\033[1;34mK \033[1;35mT\033[1;36mO\033[1;37mO\033[1;36mL\033[1;31m\033[1;32m",
                "\033[1;37mN\033[1;34mD\033[1;35mK \033[1;36mT\033[1;32mO\033[1;33mO\033[1;31mL\033[1;31m\033[1;32m",
                "\033[1;34mN\033[1;33mD\033[1;37mK \033[1;35mT\033[1;31mO\033[1;36mO\033[1;36mL\033[1;31m\033[1;32m",
                "\033[1;36mN\033[1;35mD\033[1;31mK \033[1;34mT\033[1;37mO\033[1;35mO\033[1;32mL\033[1;31m\033[1;32m",
        ]
        for color in colors:
            print(f"\r{color}|{remaining_time}| \033[1;31m", end="")
            time.sleep(0.12)
                                  
    print("\r                          \r", end="") 
    print("\033[1;35mĐang Nhận Tiền         ",end = "\r")
    # while time_sec:
    #     mins, secs = divmod(time_sec, 60)
        
    #     timeformat = 'Vui Lòng Chờ : {:02d}'.format(secs)
        
    #     print(timeformat, end='\r')
    #     time.sleep(1)
    #     time_sec -= 1
def TWITTER():

    url1_2 = 'https://gateway.golike.net/api/twitter-account'

    user_twitter1 = []
    account_id1 = []
    account = []
    STT = []
    STATUS =[]
    tong = 0
    dem = 0
    i=1
    for data in response['data'] :
        usernametk = data['screen_name']
        user_twitter1.append(data['username'])
        account_id1.append(data['id'])
        STT.append(i)
        account.append(usernametk)
        STATUS.append(Fore.GREEN+"Hoạt Động"+Fore.RED)
        print(f'\033[1;97m•[🌸]➭\033[1;36m [{i}] \033[1;91m=> \033[1;97mTên Tài Khoản┊\033[1;32m🌸 :\033[1;93m {usernametk} \033[1;91m=> \033[1;97mStatus|\033[1;32m🌸 :\033[1;93m {STATUS[-1]}'+'\n') 
        i += 1
    print(Fore.RED+'_________________________________________________________')
    choose = int(input('\033[1;97m[\033[1;91m🌸\033[1;97m] \033[1;36m  Nhập Tài Khoản : '))
    os.system('cls' if os.name== 'nt' else 'clear')
    if choose >=1 or choose <= len(user_twitter1) :
        user_twitter1 = user_twitter1[choose-1:choose]
        account_id1 = account_id1[choose-1:choose]
        user_tiktok = user_twitter1[0] 
        account_id = account_id1[0]
        checkfile = os.path.isfile('AUTH'+str(account_id)+'.txt')
        if checkfile == False:
            banner()
            AUTHURX = input(Fore.GREEN+'\033[1;97m[\033[1;91m🌸\033[1;97m] \033[1;36m  \033[1;32mNHẬP Authorization Golike : ')
            createfile = open('AUTH'+str(account_id)+'.txt','w')
            createfile.write(AUTHURX)
            createfile.close()
            readfile = open('AUTH'+str(account_id)+'.txt','r')
            AUTHURX = readfile.read()
            readfile.close()
        else:
            readfile = open('AUTH'+str(account_id)+'.txt','r')
            AUTHURX = readfile.read()
            readfile.close()
        checkfile2 = os.path.isfile('COOKIE'+str(account_id)+'.txt')
        if checkfile2 == False:
            banner()
            cookieX = input(Fore.GREEN+'\033[1;97m[\033[1;91m🌸\033[1;97m] \033[1;36m  \033[1;32mNHẬP Cookie Twitter : ')
            createfile = open('COOKIE'+str(account_id)+'.txt','w')
            createfile.write(cookieX)
            createfile.close()
            readfile = open('COOKIE'+str(account_id)+'.txt','r')
            cookieX = readfile.read()
            readfile.close()
        else:
            readfile = open('COOKIE'+str(account_id)+'.txt','r')
            cookieX = readfile.read()
            readfile.close()
        os.system('cls' if os.name== 'nt' else 'clear')
        banner()
        choose = int(input(Fore.RED+'\033[1;97m[\033[1;91m🌸\033[1;97m] \033[1;36m  Nhập Số Lượng Job : '))
        DELAY = int(input(Fore.RED+'\033[1;97m[\033[1;91m🌸\033[1;97m] \033[1;36m  Nhập Delay : '))
        print("\033[97m════════════════════════════════════════════════")
        for i in range(choose):
                 job = 'https://gateway.golike.net/api/advertising/publishers/twitter/jobs?account_id=' + str(account_id)

# Khởi tạo dictionary để lưu trữ dữ liệu
response = {}

if response.get('status') == 200:
    ads_id = response['data']['id']
    object_id = response['data']['object_id']
    type = response['data']['type']
    if type == 'like':
        url = 'https://x.com/i/api/graphql/lI07N6Otwv1PhnEgXILM7A/FavoriteTweet'
        headersX = {
            'accept': '*/*',
            'accept-language': 'vi,en-US;q=0.9,en;q=0.8',
            'authorization': AUTHURX,
            'content-type': 'application/json',
            'cookie': cookieX,
            'origin': 'https://x.com',
            'priority': 'u=1, i',
            'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': User_Agent,
            'x-client-transaction-id': 'urp5610yhQLkM+CVhUdxse7V6km/w/d0jxm8ReTQ0zYMv9OrPxn4mhIlXHxcu5p9VeJWjLh903OGJv8VyMwdt6Mnr31KuQ',
            'x-client-uuid': '8a14d42e-d7a8-4d47-9e60-cd596f91ad4b',
            'x-csrf-token': cookieX.split('ct0=')[1].split(';')[0],
            'x-twitter-active-user': 'yes',
            'x-twitter-auth-type': 'OAuth2Session',
            'x-twitter-client-language': 'en',
        }

                                    
                            json_data = {
                                'variables': {
                                    'tweet_id': object_id,
                                },
                                'queryId': 'lI07N6Otwv1PhnEgXILM7A',
                            }

                            node = pyurl.post(url,headers=headersX,json=json_data).json()
                            countdown(DELAY)
                            if 'data' or 'has already favorited tweet' in str(node):
                                url = 'https://gateway.golike.net/api/advertising/publishers/twitter/complete-jobs'
                                json_data = {
                                'ads_id': ads_id,
                                'account_id': account_id,
                                'async': True,
                                }
                                time.sleep(3)
                                response3 = pyurl.post('https://gateway.golike.net/api/advertising/publishers/twitter/complete-jobs',
                                headers=headers,
                                json=json_data,
                                ).json()       
                                if response3['success']==True:
                                    dem += 1
                                    local_time = time.localtime()
                                    hour = local_time.tm_hour
                                    minute = local_time.tm_min
                                    second = local_time.tm_sec

                                    # Định dạng giờ, phút, giây
                                    h = f"{hour:02d}"
                                    m = f"{minute:02d}"
                                    s = f"{second:02d}"
                                    prices =response3['data']['prices']

                                    # Cộng dồn giá trị prices vào tổng tiền
                                    tong += prices

                                    chuoi = (
                                        f"\033[1;31m\033[1;36m{dem}\033[1;31m\033[1;97m | "
                                        f"\033[1;33m{h}:{m}:{s}\033[1;31m\033[1;97m | "
                                        f"\033[1;32msuccess\033[1;31m\033[1;97m | "
                                        f"\033[1;31mfollow\033[1;31m\033[1;32m\033[1;32m\033[1;97m |"
                                        f"\033[1;32m Ẩn ID\033[1;97m | \033[1;32m+{prices} \033[1;97m| "
                                        f"\033[1;33m{tong} vnđ"
                                    )

                                    print(chuoi) 
                                else:
                                    skipjob = 'https://gateway.golike.net/api/advertising/publishers/twitter/skip-jobs'
                                    PARAMS = {
                                    'ads_id' : ads_id,
                                    'account_id' : account_id,
                                    'object_id' : object_id ,
                                    'async': 'true',
                                    'data': 'null',
                                    'type': type,
                                    }
                                    checkskipjob = {}
                                    if checkskipjob['status'] == 200:
                                        message = checkskipjob['message']
                                        print(Fore.RED+str(message))
                                        PARAMSr = {
                                        'ads_id' : ads_id,
                                        'account_id' : account_id,
                                        'object_id' : object_id ,
                                        'async': 'true',
                                        'data': 'null',
                                        'type': type,
                                        }
                            elif 'errors' and 'Could not authenticate you' in str(node):
                                print("HẾT HẠN COOKIE")
                                os.remove('COOKIE'+str(account_id)+'.txt')
                                return 0
                        elif type == 'follow':
                            url = 'https://x.com/i/api/1.1/friendships/create.json'
                            headersY = {
                            'accept': '*/*',
                            'accept-language': 'vi,en-US;q=0.9,en;q=0.8',
                            'authorization': AUTHURX,
                            'content-type': 'application/x-www-form-urlencoded',
                            'cookie': cookieX,
                            'origin': 'https://x.com',
                            'priority': 'u=1, i',
                            'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
                            'sec-ch-ua-mobile': '?1',
                            'sec-ch-ua-platform': '"Android"',
                            'sec-fetch-dest': 'empty',
                            'sec-fetch-mode': 'cors',
                            'sec-fetch-site': 'same-origin',
                            'user-agent': 'Mozilla/5.0 (Linux; Android 8.0; Pixel 2 Build/OPD3.170816.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Mobile Safari/537.36',
                            'x-client-transaction-id': 'MPwo7xERotqe3xFS4oEGGDju3YMFR9v2gW2dSTZ/c2S4KYhQfp5ZmZYR/KcwzeyIYp3GBjKulQYFzsWftgEm6c7v0StkMw',
                            'x-csrf-token': cookieX.split('ct0=')[1].split(';')[0],
                            'x-twitter-active-user': 'yes',
                            'x-twitter-auth-type': 'OAuth2Session',
                            'x-twitter-client-language': 'en',
                        }

                            data = {
                            'include_profile_interstitial_type': '1',
                            'include_blocking': '1',
                            'include_blocked_by': '1',
                            'include_followed_by': '1',
                            'include_want_retweets': '1',
                            'include_mute_edge': '1',
                            'include_can_dm': '1',
                            'include_can_media_tag': '1',
                            'include_ext_is_blue_verified': '1',
                            'include_ext_verified_type': '1',
                            'include_ext_profile_image_shape': '1',
                            'skip_status': '1',
                            'user_id': object_id,
                        }

                            response2 = pyurl.post('https://x.com/i/api/1.1/friendships/create.json', headers=headersY, data=data).json()
                            countdown(DELAY)
                            if 'id' in response2:
                                # DELAY
                                url = 'https://gateway.golike.net/api/advertising/publishers/twitter/complete-jobs'
                                json_data = {
                                'ads_id': ads_id,
                                'account_id': account_id,
                                'async': True,
                                }
                                time.sleep(3)
                                response = pyurl.post(
                                'https://gateway.golike.net/api/advertising/publishers/twitter/complete-jobs',
                                headers=headers,
                                json=json_data,
                                ).json()
                                if response['success']==True:
                                    dem += 1
                                    local_time = time.localtime()
                                    hour = local_time.tm_hour
                                    minute = local_time.tm_min
                                    second = local_time.tm_sec

                                    # Định dạng giờ, phút, giây
                                    h = f"{hour:02d}"
                                    m = f"{minute:02d}"
                                    s = f"{second:02d}"
                                    prices =response['data']['prices']


                                    # Cộng dồn giá trị prices vào tổng tiền
                                    tong += prices

                                    chuoi = (
                                        f"\033[1;31m\033[1;36m{dem}\033[1;31m\033[1;97m | "
                                        f"\033[1;33m{h}:{m}:{s}\033[1;31m\033[1;97m | "
                                        f"\033[1;32msuccess\033[1;31m\033[1;97m | "
                                        f"\033[1;31mlike\033[1;31m\033[1;32m\033[1;32m\033[1;97m |"
                                        f"\033[1;32m Ẩn ID\033[1;97m | \033[1;32m+{prices} \033[1;97m| "
                                        f"\033[1;33m{tong} vnđ"
                                    )
                                    print(chuoi)
                                else:
                                    skipjob = 'https://gateway.golike.net/api/advertising/publishers/twitter/skip-jobs'
                                    PARAMS = {
                                    'ads_id' : ads_id,
                                    'account_id' : account_id,
                                    'object_id' : object_id ,
                                    'async': 'true',
                                    'data': 'null',
                                    'type': type,
                                    }
                                    checkskipjob = {}
                                    if checkskipjob['status'] == 200:
                                        message = checkskipjob['message']
                                        print(Fore.RED+str(message))
                                        PARAMSr = {
                                        'ads_id' : ads_id,
                                        'account_id' : account_id,
                                        'object_id' : object_id ,
                                        'async': 'true',
                                        'data': 'null',
                                        'type': type,
                                        }
                            elif 'errors' and 'Could not authenticate you' in str(response2):
                                print("Cookie Die Đổi Tài Khản Khác Chạy Đê")
                                os.remove('COOKIE'+str(account_id)+'.txt')
                                return 0
                        elif type=='comment':
                            comment = response['lock']["message"]
                            url = 'https://x.com/i/api/graphql/oB-5XsHNAbjvARJEc8CZFw/CreateTweet'
                            headersZ = {
                            'accept': '*/*',
                            'accept-language': 'vi,en-US;q=0.9,en;q=0.8',
                            'authorization': AUTHURX,
                            'content-type': 'application/json',
                            'cookie': cookieX,
                            'origin': 'https://x.com',
                            'priority': 'u=1, i',
                            'sec-ch-ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
                            'sec-ch-ua-mobile': '?1',
                            'sec-ch-ua-platform': '"Android"',
                            'sec-fetch-dest': 'empty',
                            'sec-fetch-mode': 'cors',
                            'sec-fetch-site': 'same-origin',
                            'user-agent': User_Agent,
                            'x-client-transaction-id': 'urp5610yhQLkM+CVhUdxse7V6km/w/d0jxm8ReTQ0zYMv9OrPxn4mhIlXHxcu5p9VeJWjLh903OGJv8VyMwdt6Mnr31KuQ',
                            'x-client-uuid': '8a14d42e-d7a8-4d47-9e60-cd596f91ad4b',
                            'x-csrf-token': cookieX.split('ct0=')[1].split(';')[0],
                            'x-twitter-active-user': 'yes',
                            'x-twitter-auth-type': 'OAuth2Session',
                            'x-twitter-client-language': 'en',
                                    }
                            json_data = {
                                'variables': {
                                    'tweet_text': comment,
                                    'reply': {
                                        'in_reply_to_tweet_id': object_id,
                                        'exclude_reply_user_ids': [],
                                    },
                                    'dark_request': False,
                                    'media': {
                                        'media_entities': [],
                                        'possibly_sensitive': False,
                                    },
                                    'semantic_annotation_ids': [],
                                },
                                'features': {
                                    'communities_web_enable_tweet_community_results_fetch': True,
                                    'c9s_tweet_anatomy_moderator_badge_enabled': True,
                                    'tweetypie_unmention_optimization_enabled': True,
                                    'responsive_web_edit_tweet_api_enabled': True,
                                    'graphql_is_translatable_rweb_tweet_is_translatable_enabled': True,
                                    'view_counts_everywhere_api_enabled': True,
                                    'longform_notetweets_consumption_enabled': True,
                                    'responsive_web_twitter_article_tweet_consumption_enabled': True,
                                    'tweet_awards_web_tipping_enabled': False,
                                    'creator_subscriptions_quote_tweet_preview_enabled': False,
                                    'longform_notetweets_rich_text_read_enabled': True,
                                    'longform_notetweets_inline_media_enabled': True,
                                    'articles_preview_enabled': True,
                                    'rweb_video_timestamps_enabled': True,
                                    'rweb_tipjar_consumption_enabled': True,
                                    'responsive_web_graphql_exclude_directive_enabled': True,
                                    'verified_phone_label_enabled': False,
                                    'freedom_of_speech_not_reach_fetch_enabled': True,
                                    'standardized_nudges_misinfo': True,
                                    'tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled': True,
                                    'responsive_web_graphql_skip_user_profile_image_extensions_enabled': False,
                                    'responsive_web_graphql_timeline_navigation_enabled': True,
                                    'responsive_web_enhance_cards_enabled': False,
                                },
                                'queryId': 'oB-5XsHNAbjvARJEc8CZFw',
                            }
                            cf = pyurl.post(url,headers=headersZ,json=json_data).json()
                            countdown(DELAY)  
                            if 'create_tweet' or 'Authorization: Status is a duplicate.' in str(cf):
                                url = 'https://gateway.golike.net/api/advertising/publishers/twitter/complete-jobs'
                                json_data = {
                                'ads_id': ads_id,
                                'account_id': account_id,
                                'async': True,
                                'comment_id':response['lock']['comment_id'],
                                'message':comment,
                                }
                                time.sleep(3)
                                response = pyurl.post(
                                'https://gateway.golike.net/api/advertising/publishers/twitter/complete-jobs',
                                headers=headers,
                                json=json_data,
                                ).json()
                                if response['success']==True:
                                    dem += 1
                                    local_time = time.localtime()
                                    hour = local_time.tm_hour
                                    minute = local_time.tm_min
                                    second = local_time.tm_sec

                                    # Định dạng giờ, phút, giây
                                    h = f"{hour:02d}"
                                    m = f"{minute:02d}"
                                    s = f"{second:02d}"
                                    prices =response['data']['prices']


                                    # Cộng dồn giá trị prices vào tổng tiền
                                    tong += prices

                                    chuoi = (
                                        f"\033[1;31m\033[1;36m{dem}\033[1;31m\033[1;97m | "
                                        f"\033[1;33m{h}:{m}:{s}\033[1;31m\033[1;97m | "
                                        f"\033[1;32msuccess\033[1;31m\033[1;97m | "
                                        f"\033[1;31mcomment\033[1;31m\033[1;32m\033[1;32m\033[1;97m |"
                                        f"\033[1;32m Ẩn ID\033[1;97m | \033[1;32m+{prices} \033[1;97m| "
                                        f"\033[1;33m{tong} vnđ"
                                    )
                                    print(chuoi)
                                else:
                                    skipjob = 'https://gateway.golike.net/api/advertising/publishers/twitter/skip-jobs'
                                    PARAMS = {
                                    'ads_id' : ads_id,
                                    'account_id' : account_id,
                                    'object_id' : object_id ,
                                    'async': 'true',
                                    'data': 'null',
                                    'type': type,
                                    }
                                    checkskipjob = {}
                                    if checkskipjob['status'] == 200:
                                        message = checkskipjob['message']
                                        print(Fore.RED+str(message))
                                        PARAMSr = {
                                        'ads_id' : ads_id,
                                        'account_id' : account_id,
                                        'object_id' : object_id ,
                                        'async': 'true',
                                        'data': 'null',
                                        'type': type,
                                        }
                            elif 'errors' and 'Could not authenticate you' in str(cf):
                                print("HET HAN COOKIE")
                                os.remove('COOKIE'+str(account_id)+'.txt')
                    else:
                        print(response['message'])
                        countdown(15)
def banner():
 os.system("cls" if os.name == "nt" else "clear")
 banner = f"""
\033[1;31m ██████╗ ██╗   ██╗██╗   ██╗██╗  ██╗██╗  ██╗ █████╗ ███╗   ██╗██╗  ██╗
\033[1;36m ██╔══██╗██║   ██║╚██╗ ██╔╝██║ ██╔╝██║  ██║██╔══██╗████╗  ██║██║  ██║
\033[1;32m ██║  ██║██║   ██║ ╚████╔╝ █████╔╝ ███████║███████║██╔██╗ ██║███████║
\033[1;34m ██║  ██║██║   ██║  ╚██╔╝  ██╔═██╗ ██╔══██║██╔══██║██║╚██╗██║██╔══██║
\033[1;35m ██████╔╝╚██████╔╝   ██║   ██║  ██╗██║  ██║██║  ██║██║ ╚████║██║  ██║
\033[1;31m ╚═════╝  ╚═════╝    ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝
 
               BOX ZALO: https://zalo.me/g/nguadz335
               ADMIN : DUY KHÁNH 
               YTB : REVIEWTOOL247NDK
\033[1;97m= = = = = = = = = = = = = = = = = = = = = = = = = = = = = 
"""
 for X in banner:
  sys.stdout.write(X)
  sys.stdout.flush() 
  sleep(0.00125)

def LIST():
    banner()
    print("\033[1;32mNhập \033[1;31m1 \033[1;33mđể vào \033[1;34mTool Twitter\033[1;33m")
os.system('cls' if os.name== 'nt' else 'clear')
banner()
checkfile = os.path.isfile('user.txt')
if checkfile == False:
    AUTHUR = input(Fore.GREEN+'\033[1;97m[\033[1;91m🌸\033[1;97m] \033[1;36m  \033[1;32mNHẬP Authorization Golike : ')
    createfile = open('user.txt','w')
    createfile.write(AUTHUR)
    createfile.close()
    readfile = open('user.txt','r')
    file = readfile.read()
    readfile.close()
else:
    readfile = open('user.txt','r')
    file = readfile.read()
    readfile.close()
ses = None  # không dùng requests nữa
User_Agent=random.choice([
"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Safari/605.1.15",
])
headers = {'Accept-Language':'vi,en-US;q=0.9,en;q=0.8',
            'Referer':'https://app.golike.net/',
            'Sec-Ch-Ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
            'Sec-Ch-Ua-Mobile':'?0',
            'Sec-Ch-Ua-Platform':"Windows",
            'Sec-Fetch-Dest':'empty',
            'Sec-Fetch-Mode':'cors',
            'Sec-Fetch-Site':'same-site',
            'T' : 'VFZSamQwOUVSVEpQVkVFd1RrRTlQUT09',
            'User-Agent':User_Agent,
            "Authorization" : file,
            'Content-Type':'application/json;charset=utf-8'            
}

url1 = 'https://gateway.golike.net/api/users/me'

    #user
if response['status']== 200 :
        print('DANG NHAP THANH CONG')
        time.sleep(3)
        os.system('cls' if os.name== 'nt' else 'clear')
        # banner()
        # print(Fore.BLUE + '1.Tool Golike Mobile')
        # choose = int(input(Fore.WHITE + 'Nhập Lựa Chọn : '))
        # if choose == 1 :
        username = response['data']['username']
        coin = response['data']['coin']
        user_id = response['data']['id']
        print('________________________________________________________')
        print(Fore.GREEN+'\033[1;97m[\033[1;91m🌸\033[1;97m] \033[1;36m  \033[1;32mTài Khoản : '+Fore.YELLOW+username)
        print(Fore.GREEN+'\033[1;97m[\033[1;91m🌸\033[1;97m] \033[1;36m  \033[1;32mTổng Tiền : '+Fore.YELLOW+str(coin))
        print(Fore.RED+'_________________________________________________________')
        LIST()
        print(Fore.RED+'Nhập 2 Để Xóa Authorization Hiện Tại')
        choose = int(input(Fore.WHITE+'Nhập Lựa Chọn : '))
        if choose == 1:
            os.system('cls' if os.name== 'nt' else 'clear')
            banner()
            ip = pyurl.get('https://api.ipify.org?format=json').json()
            print(Fore.GREEN + 'Danh Sách Tài Khoản'+ Fore.RED+'         Ip : '+Fore.GREEN+str(ip['ip']))
            print(Fore.RED+'_________________________________________________________\n')

            TWITTER()
        elif choose == 2:
                os.remove('user.txt')
else:
    print(Fore.RED+'DANG NHAP THAT BAI')
    os.remove('user.txt')