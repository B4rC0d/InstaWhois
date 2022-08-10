from time import sleep
from sys import argv
import requests
from os import system  as term , path  , stat
try:
    from platform import system
except:
    system("pip install platform")

blu = "\033[96m"
red = "\033[91m"
grn = "\033[32m"
ylw = "\033[93m"
res = "\033[0;m"


ban = f"""{ylw}
.___                   __           __      __ .__             .__          
|   |  ____    _______/  |_ _____  /  \    /  \|  |__    ____  |__|  ______ 
|   | /    \  /  ___/\   __\\__   \ \   \/\/   /|  |  \  /  _ \ |  | /  ___/ 
|   ||   |  \ \___ \  |  |   / __ \_\        / |   Y  \(  <_> )|  | \___ \  
|___||___|  //____  > |__|  (____  / \__/\  /  |___|  / \____/ |__|/____  > 
          \/      \/             \/       \/        \/                  \/ 

                   Version 1.0 - Developed by B4rC0d{res}
"""

help = f"""
    {red}Usage {ylw}: {grn}python InstaWhois.py [OPTION] ...
    {ylw}To get Instagram information

    Mandatory arguments to long options are mandatory for short options too
        {red}-h {ylw}, {red}--help          {grn}display this help and exit
        {red}-s {ylw}, {red}--set           {grn}To set the session ID
        {red}-r {ylw}, {red}--run           {grn}Run the tool

    {ylw}Use help 

        {red}[{blu}SetSession{red}] {grn}python {red}InstaWhois.py {ylw}--set{red}/{ylw}-s {red}[{grn}Instagram SessionID{red}]
        {red}[{blu}Run{red}] {grn}python {red}InstaWhois.py {ylw}--run{red}/{ylw}-r {red}[{grn}Target UserName{red}]
"""


def clear():
    sleep(0.2)
    if system() == "Windows":
        term('cls')
    elif system() == "Linux" or system() == "Darwin":
        term('clear')


def ext_info(target , sessionsId):
    cookies = {'sessionid': sessionsId}
    headers = {'User-Agent': 'Instagram 64.0.0.14.96'}

    data_target = requests.get(
        f'https://www.instagram.com/{target}/?__a=1',
        headers=headers,
        cookies=cookies
    ).json()
    target_data = data_target['graphql']['user']
    mediatype = target_data['edge_owner_to_timeline_media']['edges']
    print(f''' {ylw}[{red}!{ylw}] {grn}Target {red}"{target}" {grn}data was extracted with user {red}"{target_data['id']}"
 {ylw}[{red}!{ylw}] {grn}Use the command {red}"list" {grn}to see the options{res}\n''')
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
{ylw}- {red}tagged          {grn}Get list of users tagged by target{res}
""")
        elif command == "exit":
            exit()
        elif command == "captions":
            if target_data['is_private'] == True:
                print(f"\n     {grn}[{red}-{grn}] {red}Is Private{res} \n")
            else:
                if len(mediatype) == 0:
                    print(f"\n     {grn}[{ylw}!{grn}] {red}No Post{res} \n") 
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
                print(f"\n     {grn}[{red}-{grn}] {red}Is Private{res} \n")
            else:
                if len(mediatype) == 0:
                    print(f"\n     {grn}[{ylw}!{grn}] {red}No Post{res} \n") 
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
                print(f"\n     {grn}[{red}-{grn}] {red}Is Private{res} \n")
            else:
                if len(mediatype) == 0:
                    print(f"\n     {grn}[{ylw}!{grn}] {red}No Post{res} \n") 
                else:
                    for i in mediatype:
                        node = i['node']
                        print(f"""
    {red}[{blu}+{red}] {grn}Media Id {ylw}::: {red}{node['id']}
        {red}[{ylw}-{red}] {grn}liked {ylw}::: {red}{node['edge_liked_by']['count']} 
""")
        elif command == "mediatype":
            if target_data['is_private'] == True:
                print(f"\n     {grn}[{red}-{grn}] {red}Is Private{res} \n")
            else:
                if len(mediatype) == 0:
                    print(f"\n     {grn}[{ylw}!{grn}] {red}No Post{res} \n") 
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
                print(f"\n     {grn}[{red}-{grn}] {red}Is Private{res} \n")
            else:
                if len(mediatype) == 0:
                    print(f"\n     {grn}[{ylw}!{grn}] {red}No Post{res} \n")   
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
                print(f"\n     {grn}[{red}-{grn}] {red}Is Private{res} \n")
            else:
                if len(mediatype) == 0:
                    print(f"\n     {grn}[{ylw}!{grn}] {red}No Post{res} \n") 
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






    
if(len(argv) <= 1 ):
    clear()
    print(ban)
    print(help)        
elif(len(argv) >= 1):
    if argv[1] == "--set" or argv[1] == "-s":
        if (len(argv) == 3) and (len(argv) > 2):
            clear()
            print(ban)
            with open("config/cookie.txt" , "w+") as file:
                file.write(argv[2])
            print(f"         {red}[ {grn}Cookie {ylw}Is Set {red}]{res}")
        else:
            clear()
            print(ban)
            print(help)
            
    elif argv[1] == "--run" or argv[1] == "-r":
        if (len(argv) == 3) and (len(argv) > 2):
            if (path.exists("config/cookie.txt") == True ) and (stat("config/cookie.txt").st_size > 0):
                clear()
                print(ban)
                with open("config/cookie.txt" , 'r') as file:
                    sid = file.readline()
                ext_info(target=argv[2] , sessionsId=sid)
            else:
                clear()
                print(ban)
                print(help)
        else:
            clear()
            print(ban)
            print(help)

    elif argv[1] == "--help" or argv[1] == "-h":
        if (len(argv) <= 2):
            clear()
            print(ban)
            print(help)
        else:
            clear()
            print(ban)
            print(help)
    else:
        clear()
        print(ban)
        print(help)
            
