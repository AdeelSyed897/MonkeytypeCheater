from flask import Flask, render_template, redirect
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
app = Flask(__name__)

  
@app.route('/')
def index():
  return render_template('index.html')

@app.route("/cheat")
def cheat():
  driver = webdriver.Chrome()

  url = 'https://monkeytype.com/'

  driver.get(url)
  driver.find_element(By.XPATH, '//*[@id="cookiePopup"]/div[2]/div[2]/div[1]').click()
  time.sleep(.5)
  driver.find_element(By.XPATH,'//*[@id="testConfig"]/div/div[3]/div[2]').click()
  time.sleep(.5)
  driver.find_element(By.XPATH,'//*[@id="testConfig"]/div/div[6]/div[2]').click()

  time.sleep(2)
  words = driver.find_elements(By.XPATH, '//*[@id="words"]')


  for word in words:
      cheat = word.text

  cheat = cheat.replace("\n", " ")

  
  driver.find_element(By.XPATH, '//*[@id="wordsInput"]').send_keys(cheat)
  time.sleep(2)
  driver.quit()

  return redirect('/')

if __name__ == '__main__':
  app.run(host='127.0.0.1', threaded=True)