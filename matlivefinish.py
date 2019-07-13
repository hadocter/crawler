import matplotlib.pyplot as pit
import matplotlib.animation as animation
from matplotlib import style
from selenium import webdriver #selenium lib에서 webdriver 를 import
from bs4 import BeautifulSoup  #bs4 lib 에서 BeautifulSoup 를 import
import numpy as np

#style.use('fivethirtyeight')
fig=pit.figure()
ax1=fig.add_subplot(1,1,1)
ax2=fig.add_subplot(1,1,1)
ax3=fig.add_subplot(1,1,1)
x=0
y1=0
y2=0
y3=0

ys1=[0,]
xs1=[0,]
xs2=[0,]
ys2=[0,]
ys3=[0,]
xs3=[0,]

driver = webdriver.Chrome() #chromedriver location 지정

driver.implicitly_wait(2)                               #웹 페이지의 로딩을 위한 파싱 지연시간 추가
driver.get('https://www.webfx.com/internet-real-time/') #실시간 값을 가지고 오는 사이트의 주소

def facebook():
    html = driver.page_source                           
    soup = BeautifulSoup(html, 'html.parser')
    notices = soup.select("#Facebook > div > div > div.col-lg-7 > div > div.counter")
    val_raw = notices[0].text
    val_raw=val_raw.replace(',','')
    value_facebook=int(val_raw)
    return value_facebook

def instagram():
    html = driver.page_source                           
    soup = BeautifulSoup(html, 'html.parser')
    notices2 = soup.select("#Instagram > div > div > div.col-lg-7 > div > div.counter")
    val2_raw = notices2[0].text
    val2_raw=val2_raw.replace(',','')
    value_instagram=int(val2_raw)
    return value_instagram

def twitter():
    html = driver.page_source                           
    soup = BeautifulSoup(html, 'html.parser')
    notices3 = soup.select("#Twitter > div > div > div.col-lg-7 > div > div.counter")
    val3_raw = notices3[0].text
    val3_raw=val3_raw.replace(',','')
    value_twitter=int(val3_raw)
    return value_twitter

def anima1(i):
    global x
    global y1
    global xs1
    global ys1

    x=x+1
    y1=facebook()#y1+1 부분을 자료1 output으로 대체

    xs1.append(x)
    ys1.append(y1)

    ax1.clear()
    ax1.plot(xs1,ys1,marker='o',label='Facebook')

def anima2(i):
    global x
    global y2
    global xs2
    global ys2

    y2=instagram()#y2+1 부분을 자료2 output으로 대체

    xs2.append(x)
    ys2.append(y2)

    ax2.plot(xs2,ys2,marker='o',label='Instagram')

def anima3(i):
    
    
    global x
    global y3
    global xs3
    global ys3

    y3=twitter()#y3+1 부분을 자료3 output으로 대체

    xs3.append(x)
    ys3.append(y3)
    
    ax3.plot(xs3,ys3,marker='o',label='Twitter')
    pit.legend(loc='upper right')

ani1=animation.FuncAnimation(fig,anima1,interval=700)
ani2=animation.FuncAnimation(fig,anima2,interval=700)
ani3=animation.FuncAnimation(fig,anima3,interval=700)

pit.show()
