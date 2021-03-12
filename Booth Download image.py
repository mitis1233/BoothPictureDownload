# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 14:50:26 2021

@author: BaconEgg
"""

import requests, re, time,os
from bs4 import BeautifulSoup

header={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'
        }


for f in os.listdir(r'G:\List'): #磁碟位置
    f=re.sub('.unitypackage', '', f)#過濾清單 可自訂
    f=re.sub('.rar', '', f)
    f=re.sub('.zip', '', f)
    f=re.sub('.7z', '', f)
    f=re.sub('_v.+', '', f)
    f=re.sub('_V.+', '', f)
    f=re.sub('_id.+', '', f)
    f=re.sub('_ID.+', '', f)
    f=re.sub('_item.+', '', f)
    f=re.sub('_\d.+', '', f)#過濾清單 可自訂
    print(f)
    #===========================================
    SearchText=f
    try:
        URL="https://booth.pm/zh-tw/search/"+SearchText
        r = requests.get(URL,headers=header)
        soup = BeautifulSoup(r.text,"html.parser")
        sel = soup.select("div.item-card__thumbnail-images a")
        PicUrl=sel[0]["data-original"]
        #print(PicUrl)
        
        time.sleep(1)
        img = requests.get(PicUrl,headers=header)  # 下載圖片
        input_image=SearchText #命名圖片檔
        with open("images\\" + input_image + ".jpg", "wb") as file: # 儲存圖片 需在同目錄創建images資料夾
            file.write(img.content)
        time.sleep(1)
    except:
        print('ERROR!!!!',SearchText,'ERROR!!!!')#報錯
        