from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from notify_run import Notify

notify = Notify()
check=1
while check==1:
	check=0
	chrome_options = webdriver.ChromeOptions()
	chrome_options.add_argument("--start-maximized")
	#chrome_options.add_argument("--headless")
	browser = webdriver.Chrome(chrome_options=chrome_options)
	browser.get(('https://in.bookmyshow.com/buytickets/avengers-endgame-national-capital-region-ncr/movie-ncr-ET00100559-MT/20190426'))
	try:
		browser.find_element_by_id("wzrk-cancel").click()
		browser.find_element_by_css_selector("PVR: Sangam, Delhi").click()
	except:
		try:
			browser.find_element_by_css_selector("PVR: Sangam, Delhi").click()
		except:
			print "Not yet"
			check=1
			browser.close()
print "avengers-endgame tickets are finally out go book them real soon"
#notify.send('Goooo !! tickets are live ')  

