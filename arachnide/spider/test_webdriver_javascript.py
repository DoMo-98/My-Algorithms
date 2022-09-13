from selenium import webdriver as wd

DRIVER_PATH = "/workspaces/My-Algorithms/arachnide/spider/chromedriver"

driver = wd.Chrome()

# url = 'https://cartelescine.wordpress.com'
# url = 'https://www.airbnb.es/'
url = 'https://www.google.com/'
# url = 'https://es.wikipedia.org/wiki/Solanum_tuberosum'
# url = 'https://www.google.com/search?q=patata'
# url = 'https://www.nasa.gov/multimedia/imagegallery/index.html'

driver.get( url )

print( driver.page_source )