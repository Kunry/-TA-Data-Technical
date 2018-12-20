from bs4 import BeautifulSoup
from selenium import webdriver

# def cup_Rusia_2018_goals_locals(url):
#     driver = webdriver.Firefox()
#     driver.get(url)

#     num = 0
#     try:
#         while True:
#             button_id = driver.find_element_by_id("collapseButton"+str(num))
#             button_id.click()
#             num += 1
#     except:
#         print("limit")

#     html = driver.page_source
#     soup = BeautifulSoup(html, 'html.parser')
#     driver.quit()
#     obj = {"soup":soup, "num":num}
#     return obj

class cup_Rusia_2018_goals_locals:

    def __init__(self, url):
        self.url = url

    def use_BeatifulSoup(self):
        html = self.driver.page_source
        return BeautifulSoup(html, "html.parser")

    def close_server(self):
        self.driver.quit()

    def return_value_Firefox(self):
        number = self.open_mostrar_matches_goals()
        dic = self.return_value_Chrome()
        dic["number"] = number
        return dic

    def close_selenium(self):
        self.close_server()

    def return_soup(self):
        soup = self.use_BeatifulSoup()
        self.close_selenium()
        return({"server": soup})

class connect_Chrome(cup_Rusia_2018_goals_locals):
    def __init__(self, url):
        self.url = url
    
    def start_server(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.url)
        return self.return_soup()        
        
        
class connect_Firefox(cup_Rusia_2018_goals_locals):
    def __init__(self, url):
        self.url = url
    
    def start_server(self):
        self.driver = webdriver.Firefox()
        self.driver.get(self.url)
        number = self.open_mostrar_matches_goals()
        dic = self.return_soup()
        dic["number"] = number
        return dic
        

    def open_mostrar_matches_goals(self):
        num = 0
        try:
            while True:
                button_id = self.driver.find_element_by_id("collapseButton"+str(num))
                button_id.click()
                num += 1
        except:
            print("limit")
        return num