import requests , json
from datetime import datetime
from time import sleep
from os import system , path  , stat
from sys import argv
from colorama import init , Fore 
try:
    import platform
except:
    system("pip install platform")

try:
    from pyfiglet import figlet_format
except:
    system("pip install pyfiglet")
    
try:
    from termcolor2 import colored
except:
    system("pip install termcolor2")
init()

red = Fore.RED
grn = Fore.GREEN
ylw = Fore.YELLOW
blu = Fore.BLUE
reset = Fore.RESET
white = Fore.WHITE
video = 0
image = 0
session = requests.session()

ban = f"""{ylw}
.___                   __           __      __ .__             .__          
|   |  ____    _______/  |_ _____  /  \    /  \|  |__    ____  |__|  ______ 
|   | /    \  /  ___/\   __\\__   \ \   \/\/   /|  |  \  /  _ \ |  | /  ___/ 
|   ||   |  \ \___ \  |  |   / __ \_\        / |   Y  \(  <_> )|  | \___ \  
|___||___|  //____  > |__|  (____  / \__/\  /  |___|  / \____/ |__|/____  > 
          \/      \/             \/       \/        \/                  \/ 

                   Version 1.0 - Developed by B4rC0d{reset}
"""
help_ban = f"""
   {red}+{ylw}-------------------------{blu}[ {red}Help tool {blu}]{ylw}----------------------------{red}+
   {ylw}|                                                              {ylw}    |
   {ylw}|   {grn}--help{ylw}/{grn}-h {red}::: {grn}python3 {red}InstaWhois.py {ylw}< {grn}--help {blu}or {grn}-h {ylw}>           |
   {ylw}|     >  {red}To see the tool help                                  {ylw}    |
   {ylw}|                                                              {ylw}    |
   {ylw}|   {grn}--acoount{ylw}/{grn}-a {red}::: {grn}python3 {red}InstaWhois.py {ylw}< {grn}--account {blu}or {grn}-a {ylw}>     |
   {ylw}|     >  {red}Login to your Instagram account                       {ylw}    |
   {ylw}|                                                              {ylw}    |
   {ylw}|   {grn}--cookie{ylw}/{grn}-c {red}::: {grn}python3 {red}InstaWhois.py {ylw}< {grn}--cookie {blu}or {grn}-c {ylw}>       |
   {ylw}|     >  {red}Login with Instagram cookies                          {ylw}    |
   {ylw}|                                                              {ylw}    |
   {ylw}|   {grn}--run{ylw}/{grn}-r {red}::: {grn}python3 {red}InstaWhois.py {ylw}< {grn}--run {blu}or {grn}-r {ylw}> < {red}Target {ylw}>  |
   {ylw}|     >  {red}Run the tool                                          {ylw}    |
   {ylw}|                                                              {ylw}    |
   {red}+{ylw}------------------------------------------------------------------{red}+
"""

def clear():
    sleep(0.2)
    if platform.system() == "Windows":
        system('cls')
    elif platform.system() == "Linux" or platform.system() == "Darwin":
        system('clear')

def Error(com) :
    clear()
    print(f""" {red}_____     
| ____|_ __ _ __ ___  _ __ 
|  _| | '__| '__/ _ \| '__|
| |___| |  | | | (_) | |   
|_____|_|  |_|  \___/|_|

{ylw}[{red}!{ylw}] {red+com}""")
    sleep(0.5)
    exit()

def Account_session():
    with open('session.txt', 'r') as file:
        session.cookies.update(json.load(file))
    with open('headers.txt', 'r') as file:
        session.headers = json.load(file)

def account_cookies():
    with open('cookie.txt', 'r') as file:
        session.cookies.update({'sessionid':file.readline()})

def Login_account():
    try:
        username = input(f"{white}iNsTaWhOiS{red}( UseName ){reset} > {grn}")
        password = input(f"{white}iNsTaWhOiS{red}( PassWord ){reset} > {grn}")                          
    except:
        Error("Input Error")
    

    session.headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36",
        "Referer": "https://www.instagram.com/"
        
        }

    Base_Requests = session.get("https://www.instagram.com/")

    session.headers.update(
        {'X-CSRFToken':Base_Requests.cookies['csrftoken']
    }
    )
    Login_Requests = session.post(f"https://www.instagram.com/accounts/login/ajax/", 
        data={
            'enc_password': "#PWD_INSTAGRAM_BROWSER:0:{}:{}".format(int(datetime.now().timestamp()),password) 
            ,'username':username,
        } 
        ,allow_redirects=True)

    session.headers.update({
            'X-CSRFToken':Login_Requests.cookies['csrftoken']
        })

    res_data = Login_Requests.json()

 
    if res_data['authenticated']:
        with open('session.txt', 'w+') as file:
            cookie = session.cookies.get_dict()
            del cookie["ds_user_id"]
            json.dump(cookie, file)
        with open('headers.txt', 'w+') as file:
            json.dump(session.headers, file)
        print(f"{red}[ {ylw}We logged in to {grn}'{username}' {ylw}account with user ID {grn}'{res_data['userId']}' {red}]{reset}")
    else:
        print(f"{red}Login Failed\n")
        Login_account()

def ext_info(target):
    data_target = session.get(f"https://www.instagram.com/{target}/?__a=1").json()
    # print(data_target)
    target_data = data_target['graphql']['user']
    mediatype = target_data['edge_owner_to_timeline_media']['edges']
    print(f''' {ylw}[{red}!{ylw}] {grn}Target {red}"{target}" {grn}data was extracted with user {red}"{target_data['id']}"
 {ylw}[{red}!{ylw}] {grn}Use the command {red}"list" {grn}to see the options{reset}\n''')
    while(True):
        try:
            command = input(f"{ylw}Command :{grn} ")
        except:
            exit()
        if command == "list":
            print(f"""
{ylw}- {red}captions        {grn}Get user's photos captions
{ylw}- {red}comments        {grn}Get total comments of target's posts
{ylw}- {red}flw             {grn}Statistics of followers and followers
{ylw}- {red}info            {grn}Get target info
{ylw}- {red}likes           {grn}Get total likes of target's posts
{ylw}- {red}mediatype       {grn}Get user's posts type (photo or video)
{ylw}- {red}photodes        {grn}Get description of target's photos
{ylw}- {red}propic          {grn}Download user's profile picture
{ylw}- {red}bio             {grn}Get a target biography 
{ylw}- {red}tagged          {grn}Get list of users tagged by target{reset}
""")
        elif command == "exit":
            exit()
        elif command == "captions":
            if target_data['is_private'] == True:
                print(f"\n     {grn}[{red}-{grn}] {red}Is Private{reset} \n")
            else:
                if len(mediatype) == 0:
                    print(f"\n     {grn}[{ylw}!{grn}] {red}No Post{reset} \n") 
                else:
                    for i in mediatype:
                        node = i['node']
                        id = node['id']
                        print(f"    {red}[{blu}+{red}] {grn}Media Id {ylw}::: {red}{id}")
                        for cap in node['edge_media_to_caption']['edges']:
                            print(f"""        {red}[{ylw}-{red}] {grn}caption {ylw}::: {red}{cap['node']['text']} 
            """)
            
        elif command == "comments":
            if target_data['is_private'] == True:
                print(f"\n     {grn}[{red}-{grn}] {red}Is Private{reset} \n")
            else:
                if len(mediatype) == 0:
                    print(f"\n     {grn}[{ylw}!{grn}] {red}No Post{reset} \n") 
                else:
                    for i in mediatype:
                        node = i['node']
                        print(f"""
    {red}[{blu}+{red}] {grn}Media Id {ylw}::: {red}{node['id']}
        {red}[{ylw}-{red}] {grn}comment {ylw}::: {red}{node['edge_media_to_comment']['count']} 
""")

        elif command == "flw":
            print(f"""
    {red}[{blu}+{red}] {grn}Followers {ylw}::: {red}{target_data['edge_followed_by']['count']}
    {red}[{blu}+{red}] {grn}Following {ylw}::: {red}{target_data['edge_follow']['count']}
""")

        elif command == "info":
            print(f"""
    {red}[{blu}+{red}] {grn}Username {ylw}::: {red}{target_data['username']}
    {red}[{blu}+{red}] {grn}Full Name {ylw}::: {red}{target_data['full_name']}
    {red}[{blu}+{red}] {grn}id {ylw}::: {red}{target_data['id']}
    {red}[{blu}+{red}] {grn}Fbid {ylw}::: {red}{target_data['fbid']}
    {red}[{blu}+{red}] {grn}Is Private {ylw}::: {red}{target_data['is_private']}
    {red}[{blu}+{red}] {grn}is_verified {ylw}::: {red}{target_data['is_verified']}
    {red}[{blu}+{red}] {grn}Business Email {ylw}::: {red}{target_data['business_email']}
    {red}[{blu}+{red}] {grn}Business Phone Number {ylw}::: {red}{target_data['business_phone_number']}
    {red}[{blu}+{red}] {grn}Business Category Name {ylw}::: {red}{target_data['business_category_name']}
    {red}[{blu}+{red}] {grn}Overall Category Name {ylw}::: {red}{target_data['overall_category_name']}
    {red}[{blu}+{red}] {grn}Category Enum {ylw}::: {red}{target_data['category_enum']}
    {red}[{blu}+{red}] {grn}Category Name {ylw}::: {red}{target_data['category_name']}
    {red}[{blu}+{red}] {grn}Edge Mutual Followed By {ylw}::: {red}{target_data['edge_mutual_followed_by']['count']}
    {red}[{blu}+{red}] {grn}Is Business Account {ylw}::: {red}{target_data['is_business_account']}
    {red}[{blu}+{red}] {grn}Blocked By Viewer {ylw}::: {red}{target_data['blocked_by_viewer']}
    {red}[{blu}+{red}] {grn}Restricted By Viewer {ylw}::: {red}{target_data['restricted_by_viewer']}
    {red}[{blu}+{red}] {grn}Country Block {ylw}::: {red}{target_data['country_block']}
    {red}[{blu}+{red}] {grn}External Url {ylw}::: {red}{target_data['external_url']}
    {red}[{blu}+{red}] {grn}Edge Felix Video Timeline {ylw}::: {red}{target_data['edge_felix_video_timeline']['count']}
    {red}[{blu}+{red}] {grn}Edge Owner To Timeline Media {ylw}::: {red}{target_data['edge_owner_to_timeline_media']['count']}
""")
        elif command == "likes":
            if target_data['is_private'] == True:
                print(f"\n     {grn}[{red}-{grn}] {red}Is Private{reset} \n")
            else:
                if len(mediatype) == 0:
                    print(f"\n     {grn}[{ylw}!{grn}] {red}No Post{reset} \n") 
                else:
                    for i in mediatype:
                        node = i['node']
                        print(f"""
    {red}[{blu}+{red}] {grn}Media Id {ylw}::: {red}{node['id']}
        {red}[{ylw}-{red}] {grn}liked {ylw}::: {red}{node['edge_liked_by']['count']} 
""")
        elif command == "mediatype":
            if target_data['is_private'] == True:
                print(f"\n     {grn}[{red}-{grn}] {red}Is Private{reset} \n")
            else:
                if len(mediatype) == 0:
                    print(f"\n     {grn}[{ylw}!{grn}] {red}No Post{reset} \n") 
                else:
                    for i in mediatype:
                        node = i['node']['__typename']
                        if node == "GraphVideo":
                            video += 1
                        elif node == "GraphImage":
                            image += 1
                        elif node == 'GraphSidecar':
                            image += 1
                    print(f"""
    {red}[{blu}+{red}] {grn}Number of videos {ylw}::: {red}{video}
    {red}[{blu}+{red}] {grn}Number of photos {ylw}::: {red}{image}
""")

        elif command == "photodes":
            if target_data['is_private'] == True:
                print(f"\n     {grn}[{red}-{grn}] {red}Is Private{reset} \n")
            else:
                if len(mediatype) == 0:
                    print(f"\n     {grn}[{ylw}!{grn}] {red}No Post{reset} \n")   
                else:
                    for i in mediatype:
                        node = i['node']
                        id = node['id']
                        print(f"""    {red}[{blu}+{red}] {grn}Photo Id {ylw}::: {red}{node['id']}
        {red}[{ylw}-{red}] {red}{node['accessibility_caption']}
                    """)


        elif command == "propic":

            print(f"""
    {red}[{blu}+{red}] {grn}Profile Pic Url {ylw}::: {red}{target_data['profile_pic_url_hd']}
""")
        elif command == "bio": 

            print(f""" 
    {red}[{blu}+{red}] {grn}biography {ylw}::: {red}{target_data['biography']}
    {red}[{blu}+{red}] {grn}BioLinks  {ylw}::: {red}{target_data['bio_links']}     
""")
        elif command == "tagged":
            if target_data['is_private'] == True:
                print(f"\n     {grn}[{red}-{grn}] {red}Is Private{reset} \n")
            else:
                if len(mediatype) == 0:
                    print(f"\n     {grn}[{ylw}!{grn}] {red}No Post{reset} \n") 
                else:
                    for i in mediatype:
                        node = i['node']
                        id = node['id']
                        tagged = node['edge_media_to_tagged_user']['edges']
                        if len(tagged) >= 0:
                            for cap in tagged:
                                print(f"     {red}[{blu}+{red}] {grn}Media Id {ylw}::: {red}{id} ")
                                print(f"""       {red}[{ylw}-{red}] {grn}username {ylw}::: {red}{cap['node']['user']['username']} 
            """)

        else:
            print(f" {grn}[{ylw}!{grn}] {red}Please use the correct command {ylw}!!")



if __name__ == "__main__":
    
    if(len(argv) <= 1 ):
        Error("Please use the correct arguments\n   Get help from the help of the argument --help/-h")
        
    elif(len(argv) >= 1):

        if argv[1] == "--cookie" or argv[1] == "-c":
            if (len(argv) <= 2):
                print(ban)
                try:
                    cookie = input(f"{white}iNsTaWhOiS{red}( Cookie ){reset} > {grn}")
                except:
                    Error("Enter the correct input")

                with open("cookie.txt" , "w+") as file:
                    file.write(cookie)
            else:
                Error("Please use the correct arguments\n   Get help from the help of the argument --help/-h")

        elif argv[1] == "--account" or argv[1] == "-a":
            if (len(argv) <= 2):
                print(ban)
                Login_account()
            else:
                Error("Please use the correct arguments\n   Get help from the help of the argument --help/-h")

        elif argv[1] == "--run" or argv[1] == "-r":
            if (len(argv) <= 3):
                print(ban)
                if(path.exists("session.txt") == True ) and (stat("session.txt").st_size > 0) and (path.exists("headers.txt") == True) and (stat("headers.txt").st_size > 0):
                    Account_session()
                    ext_info(argv[2])
                elif (path.exists("cookie.txt") == True ) and (stat("cookie.txt").st_size > 0):
                    account_cookies()
                    ext_info(argv[2])
                else:
                    Error("Please add an Instagram account\n    Use --help for more information")
            else:
                Error("Please use the correct arguments\n   Get help from the help of the argument --help/-h")

        elif argv[1] == "--help" or argv[1] == "-h":
            if (len(argv) <= 2):
                print(ban)
                print(help_ban)
            else:
                Error("Please use the correct arguments\n   Get help from the help of the argument --help/-h")
        else:
            Error("This is not an argument, get help from a guide")
            
