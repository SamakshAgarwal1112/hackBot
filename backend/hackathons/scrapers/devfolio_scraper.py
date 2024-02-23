import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
import requests as req

# url_to_scrape = 'https://devfolio.co/_next/data/eVsMwiAIOGrukvTOuEz0-/hackathons.json'

class DFScraper:
    def __init__(self):
        self.options = Options()
        self.options.add_argument("--headless")
        self.options.page_load_strategy = 'eager'
        self.options.binary_location = '/usr/bin/firefox'
        self.driver = webdriver.Firefox(options=self.options)
        # self.driver.minimize_window()
        self.id_url = "https://devfolio.co/hackathons/open"
        self.url = "https://devfolio.co/_next/data/"
        
    def get_unique_id(self):
        self.driver.get(self.id_url)
        try:
            script_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, '__NEXT_DATA__'))
            )
            
            json_data = json.loads(script_element.get_attribute('innerHTML'))
            build_id = json_data.get('buildId')
            return build_id

        except Exception as e:
            print(f'Error extracting unique ID: {e}')

        return None
    
    def scrape(self):
        data = req.get(f'{self.url}{self.get_unique_id()}/hackathons.json').json()
        self.close()
        return data["pageProps"]["dehydratedState"]["queries"][0]["state"]["data"]
        # for i in res["pageProps"]["dehydratedState"]["queries"][0]["state"]["data"]["upcoming_hackathons"]:
        #     print(i["name"]," ",i["starts_at"]," ",i["ends_at"]," ",i["is_online"])
            
    def close(self):
        self.driver.close()

# Usage:
# scraper = DFScraper()
# data = scraper.scrape()
# print(data)




# url_to_scrape = 'https://devfolio.co/hackathons/open'

# def extract_unique_id(driver, url):
#     driver.get(url)

#     try:
#         script_element = WebDriverWait(driver, 10).until(
#             EC.presence_of_element_located((By.ID, '__NEXT_DATA__'))
#         )
        
#         json_data = json.loads(script_element.get_attribute('innerHTML'))
#         build_id = json_data.get('buildId')
#         return build_id

#     except Exception as e:
#         print(f'Error extracting unique ID: {e}')

#     return None

# options = Options()
# options.add_argument("--headless")
# service = webdriver.ChromeService(executable_path='chromedriver.exe')
# driver = webdriver.Chrome(service=service,options=options)

# dynamic_unique_id = extract_unique_id(driver, url_to_scrape)

# if dynamic_unique_id:
#     print(f'Extracted Unique ID: {dynamic_unique_id}')
# else:
#     print('Unable to extract the unique ID.')

# driver.quit()
# # # eVsMwiAIOGrukvTOuEz0-
# url=f'https://devfolio.co/_next/data/{dynamic_unique_id}/hackathons.json'
# res=req.get(url).json()
# # print(res)
# for i in res["pageProps"]["dehydratedState"]["queries"][0]["state"]["data"]["open_hackathons"]:
#     print(i["name"]," ",i["starts_at"]," ",i["ends_at"]," ",i["is_online"])