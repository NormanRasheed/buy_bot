from selenium import webdriver

browser = webdriver.Chrome()

browser.implicitly_wait(10)

browser.get('https://www.newegg.com/msi-geforce-rtx-4090-rtx-4090-gaming-x-trio-24g/p/N82E16814137761?Description=RTX%204090&cm_re=RTX_4090-_-14-137-761-_-Product&quicklink=true')

add_to_cart_button = browser.find_element_by_xpath('//*[@id="ProductBuy"]/div/div[2]/button')

add_to_cart_button.click()
