import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import random
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import pandas as pd
import mysql.connector
from sqlalchemy import create_engine
from unidecode import unidecode
import pandas as pd
options = Options()
import re
# import pymssql
import requests
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import getpass
from selenium.webdriver.common.action_chains import ActionChains
import configparser
from flask import Flask,render_template,request,session, abort,send_file,send_from_directory,redirect,url_for,make_response
import io; 
import csv
import selenium
import time
import threading
from multiprocessing import Process
from threading import Thread
import datetime
from datetime import datetime
import socket
import schedule



def mysqlfunction():
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="test"
)
def hostname():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('localhost', 0))
    port = sock.getsockname()[1]
    sock.close()
    return request.host
# def driverget():
#     options = Options()
#     ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath('__file__')))
#     chromeDriverFilePath = os.path.join(ROOT_DIR,r"C:\\Users\Admin\Desktop\\Yuvaraj\Scrapping\\chromedriver.exe")
#     options = webdriver.ChromeOptions()
#     # options.add_argument("--headless")
#     options.add_argument("headless")
#     options.add_argument("--ignore-certificate-errors")
#     options.add_argument("--ignore-ssl-errors")
#     options.add_argument("--no-sandbox")
#     options.add_argument("--disable-dev-shm-usage")
#     #,chrome_options=options
#     driver = webdriver.Chrome(executable_path=chromeDriverFilePath,options=options)
                        
#     time.sleep(3)
 

#     return driver

# flag = True
def qr_img(driver):
     
    
    driver.get("https://web.whatsapp.com/")
    driver.maximize_window()
    time.sleep(3)
    print("IN qr img ")
    try:
        driver.find_element_by_xpath("/html/body/div[1]/div/div/div[3]/div[1]/div/div[2]/div").click()
        print("Clicking reload")
    except:
        print("No reload found")
    # if (flag!=True):
    time.sleep(20)
    # flag=False
    try:
        qr_code = driver.find_element_by_css_selector('[data-testid="qrcode"]')
    # qr_code=driver.find_element_by_class_name("_19vUU")
    except:
        print("No Qr avialable")
       
    qr_code.screenshot("static/files/qr_img.png")
    qr_extension='static/files/qr_img.png'
    print("save_image : ",qr_extension)
    response = hostname()
    print("response",response)
    # imageurl=os.path.join(app.config[UPLOAD_FOLDER],str(qr_code))
    # print("imageurl : ",imageurl)
    finalimageurl="http://"+response+"/"+qr_extension
    print("finalimageurl : ",finalimageurl)
    return finalimageurl
   
    
    

UPLOAD_FOLDER = 'static/files'
app = Flask(__name__)
app.secret_key = 'yuvaraj2412' 
app.config["UPLOAD_FOLDER"]=UPLOAD_FOLDER


@app.route('/',methods=["POST","GET"])
def home():
    driver=webdriver.Chrome(r"C:\\Users\Admin\Desktop\\chromedriver.exe")
    result=qr_img(driver) 
    print("response: ",result)
    return render_template("index.php",result=result)



    #     schedule.every(18).seconds.do(qr_img)

    # while True:  
    #     schedule.run_pending()  


if __name__ == '__main__':
   app.run(debug=True,port=8002)
     

