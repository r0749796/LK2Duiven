
import cgitb; cgitb.enable()
import spidev
import smtplib
from email.mime.text import MIMEText
import random
import mysql.connector
import time
import inspect
print inspect.getfile(inspect.currentframe()) 

from ISStreamer.Streamer import Streamer

spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz=(1000000)

def readabc(adcnum):
	if((adcnum > 7) or (adcnum < 0)):
		return -1
	r = spi.xfer2([1, (8 + adcnum) << 4, 0])
	time.sleep(0.000005)
	adcout = ((r[1]&3) << 8) + r[2]
	return adcout
	
bucket_namestr = inspect.getfile(inspect.currentframe())
bucket_keystr = bucket_namestr[:-3]
streamer = Streamer(bucket_name=bucket_namestr, bucket_key=bucket_keystr, access_key="ist_kh_4Iv3IJuAd4mH82Km0H0yHD5CU9QJh")


mydb = mysql.connector.connect(
  host="localhost",
  user="pi",
  passwd="raspberry",
  database="mydb"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT id, naam FROM duiven")

duif = mycursor.fetchall()

for row in duif:
	if row[1] == bucket_namestr[:-3]:
		naam = row[1]
		number = row[0]


# example data logging
mail = False
lat = random.uniform(-90.0, 90.0)
long = random.uniform(-180.0, 180.0)
while True:
	tmp1 = int((readabc(1) / 1023.0) * 100)
	tmp2 = int((readabc(2) / 1023.0) * 600)
	for num in range(1, 20):
		time.sleep(0.1)
		if num%1 == 0:
			streamer.log("Number", number)
		if num%2 == 0:
			streamer.log("Naam", naam)
		if num%3 == 0:
			streamer.log("Energie", tmp1)
		if num%4 == 0:
			streamer.log("Hartslag", tmp2)
		if num%5 == 0:
			streamer.log("myNumber", "{}, {}" .format(lat, long))
	
		if int(tmp1) < 20:
			while mail:	
					message = "Batterij van duif {} minder dan 20%. Tijd om te vervangen." .format(naam)
					msg = MIMEText(message)
					msg['Subject'] = 'Batterij {}' .format(naam)
					msg['From'] = 'LK2DUIF@gmail.com'
					msg['To'] = 'simon_duchateau@hotmail.com'

					# send the email via Gmail server
					username = 'LK2DUIF@gmail.com'
					password = 'LK2DUIVEN'
					server = smtplib.SMTP('smtp.gmail.com:587')  # Gmail rewriting port 25 to port 587
					server.starttls()  # Support SMPT AUTH
					server.login(username, password)
					server.sendmail(msg['From'], msg['To'], msg.as_string())
					server.quit()
					mail = False
		elif int(tmp2) < 150:
			while mail:	
					message = "Hartslag van duif {} is te laag." .format(naam)
					msg = MIMEText(message)
					msg['Subject'] = 'Hartslag {}' .format(naam)
					msg['From'] = 'LK2DUIF@gmail.com'
					msg['To'] = 'simon_duchateau@hotmail.com'

					# send the email via Gmail server
					username = 'LK2DUIF@gmail.com'
					password = 'LK2DUIVEN'
					server = smtplib.SMTP('smtp.gmail.com:587')  # Gmail rewriting port 25 to port 587
					server.starttls()  # Support SMPT AUTH
					server.login(username, password)
					server.sendmail(msg['From'], msg['To'], msg.as_string())
					server.quit()
					mail = False
		elif int(tmp2) > 450:
			while mail:	
					message = "Hartslag van duif {} is te hoog." .format(naam)
					msg = MIMEText(message)
					msg['Subject'] = 'Hartslag {}' .format(naam)
					msg['From'] = 'LK2DUIF@gmail.com'
					msg['To'] = 'simon_duchateau@hotmail.com'

					# send the email via Gmail server
					username = 'LK2DUIF@gmail.com'
					password = 'LK2DUIVEN'
					server = smtplib.SMTP('smtp.gmail.com:587')  # Gmail rewriting port 25 to port 587
					server.starttls()  # Support SMPT AUTH
					server.login(username, password)
					server.sendmail(msg['From'], msg['To'], msg.as_string())
					server.quit()
					mail = False
					
		elif not int(tmp1) < 20 or not int(tmp2) < 150 or not int(tmp2) > 450:
			mail = True
streamer.close()
