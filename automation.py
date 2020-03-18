from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.youtube.com')

searchBox = driver.find_element_by_xpath('//*[@id="search"]')
searchBox.send_keys('Bunthet SAY')

searchButton = driver.find_element_by_xpath('//*[@id="search-icon-legacy"]')
searchButton.click()
