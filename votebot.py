#refernces
#https://towardsdatascience.com/web-scraping-101-d9170e880117]
#https://stackoverflow.com/questions/72773206/selenium-python-attributeerror-webdriver-object-has-no-attribute-find-el
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class VoteBot():
    def __init__(self):
      self.driver = webdriver.Chrome("---") #set correct path

    # 
    def vote(self):
        self.driver.get('---') #add URL here
        all_iframes = self.driver.find_elements(By.TAG_NAME, "iframe") # look for any elements with iframe tag
        if len(all_iframes) > 0: # check to see if hidden is set true, if true number is added to total count
            print("Ad Found\n")
            self.driver.execute_script("""
                var elems = document.getElementsByTagName("iframe"); 
                for(var i = 0, max = elems.length; i < max; i++)
                    {
                        elems[i].hidden=true;
                    }
                                """)
            print('Total Ads: ' + str(len(all_iframes)))
        else: # if nothing is hidden then no frames are found 
            print('No frames found')
        
        time.sleep(5) #optional 

        # https://selenium-python.readthedocs.io/locating-elements.html look at this for whatever element you need to find
        self.driver.find_element(By.XPATH, ("//a[@class='fa fa-times closebtn']")).click()
        self.driver.find_element(By.CLASS_NAME, "---").click()
        self.driver.find_element(By.ID, "---").click()
        self.driver.find_element(By.ID, "---").click()

        time.sleep(2) #optional
        self.driver.close() # close the window

while True: # this keeps it running
  bot = VoteBot()
  bot.vote()
