# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
import re
import mysql.connector

#---——————————————————————————————————python的str默认是ascii编码，和unicode编码冲突
import sys
reload(sys)
sys.setdefaultencoding('utf8')
#-----------------------------------

# url='https://en.wikipedia.org/wiki/Paul_Dirac'
# r=requests.get(url).text
# soup=BeautifulSoup(r)
#
# title=soup.h1.get_text()
# maintext=soup.find(id='mw-content-text')
# infobox=maintext.find(class_='infobox vcard')


#-----------------------------储存inforbox至字典
def getinformation(url):
    r=requests.get(url).text
    soup=BeautifulSoup(r)
    maintext=soup.find(id='mw-content-text')
    infobox=maintext.find(class_='infobox vcard')
    information={}
    boxes=infobox.find_all('tr')
    information['Name']=soup.h1.get_text()
    information['photo']='http://en.wikipedia.org/'+infobox.td.a['href']
    for box in boxes:
        if box.find('th')!=None and box.find('td')!=None:
            information[box.find('th').get_text()]=box.find('td').get_text()
    return information
#------------------------------


# newhtml='<head>'+'\n<title>'+'\n'+"%s"%title+'\n'+'</title>'+'\n'+'</head>'+'\n'+'<body>'+'\n'+"%s"%maintext+'\n'+'</body>'

#--------------------------储存源代码
def getHtml(url):
    r=requests.get(url).text
    title=soup.h1.get_text()
    f=file(u'/Users/jianghuadong/wiki/'+title+'.txt','wb')
    f.write(r)
    f.close()
#--------------------------



conn = mysql.connector.connect(host='localhost',user='root',passwd='hewuli',database='wikitest1',use_unicode=True)
cursor = conn.cursor()
cursor.execute('create table user7 (id varchar(20) primary key, name varchar(20))')
cursor.execute('insert into user7 (id, name) values (%s, %s)', ['1', 'Michael'])
conn.commit()
cursor.close()

cursor = conn.cursor()
cursor.execute('select * from user7 where id = %s', ('1',))
values = cursor.fetchall()
print values
cursor.close()
conn.close()
