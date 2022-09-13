# from urllib.request import urlopen
import urllib.request
# import requests
from bs4 import *
import re

# url = 'https://cartelescine.wordpress.com'
# url = 'https://www.airbnb.es/'
# url = 'https://www.google.com/'
# url = 'https://es.wikipedia.org/wiki/Solanum_tuberosum'
# url = 'https://www.google.com/search?q=patata'
url = 'https://www.nasa.gov/multimedia/imagegallery/index.html'

# datos = urllib2.urlopen(url).read().decode()
# soup =  BeautifulSoup(datos)
# tags = soup("img")
# for tag in tags:
#     print(tag.get("src"))

# req = urllib.request.Request(
#     url,
#     headers={
#         # 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
#         'User-Agent': 'Mozilla'
#     }
# )

opener = urllib.request.build_opener()
opener.addheaders = [('User-Agent', 'Mozilla/5.0')]
# opener.addheaders = [('User-Agent', 'Safari/537.36')]
page = opener.open( url )

# page = urllib.request.urlopen( url )
# page = requests.get(url)
soup = BeautifulSoup( page.read(), 'html.parser' )
# soup = BeautifulSoup(page.text, 'html.parser')

# print(page)
# print(soup.decode())

img_types = ( '.png', '.jpg', '.jpeg', '.gif', '.bmp' )

res = set()

# for img in soup.findAll( 'img' ):
#     # try:
#     #     # In image tag ,searching for "data-srcset"
#     #     image_link = img["data-srcset"]
            
#     # # then we will search for "data-src" in img
#     # # tag and so on..
#     # except:
#     #     try:
#     #         # In image tag ,searching for "data-src"
#     #         image_link = img["data-src"]
#     #     except:
#     #         try:
#     #             # In image tag ,searching for "data-fallback-src"
#     #             image_link = img["data-fallback-src"]
#     #         except:
#     #             try:
#     #                 # In image tag ,searching for "src"
#     #                 image_link = img["src"]

#     #             # if no Source URL found
#     #             except:
#     #                 pass

#     # print(image_link)

#     res.add( img.get( 'src' ) )


# for link in soup.findAll( 'link' ):
#     for img_type in img_types:
#         if link.get( 'href' ) and img_type in link.get( 'href' ):
#             res.add( link.get( 'href' ) )
#             break


# for a in soup.findAll( 'a' ):
#     for img_type in img_types:
#         if a.get( 'href' ) and img_type in a.get( 'href' ):
#             res.add( a.get( 'href' ) )
#             break

currentUrl = url + "/"

for img_type in img_types:

    for src in soup.findAll( src = re.compile( '.*' + img_type + '.*' ) ):
        res.add( src.get( 'src' ) )

    for src in soup.findAll( srcset = re.compile( '.*' + img_type + '.*' ) ):
        res.add( src.get( 'srcset' ) )

    for src in soup.findAll( href = re.compile( '.*' + img_type + '.*' ) ):
        res.add( src.get( 'href' ) )

    for src in soup.findAll( style = re.compile( '.*' + img_type + '.*' ) ):
        res.add( src.get( 'style' ).split( "url(" )[ 1 ].split( ")" )[ 0 ] )


for src in res:
    if " " in src:
        src = src.split(" ")[ 0 ]
    if src[ 0 ] == '"':
        src = src[ 1: ]
    if src[ -1 ] == '"':
        src = src[ :-1 ]
    if src[ 0 ] == "/":
        if src[ 1 ] == "/":
            print( currentUrl.split( "//" )[ 0 ] + src )
        else:
            print( currentUrl[ :currentUrl.index( "/", 8 ) ] + src )
    else:
            print( src )
    # break