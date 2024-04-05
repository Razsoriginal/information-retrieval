# import requests
# from bs4 import BeautifulSoup
# import os
# from urllib.parse import urljoin

# def download_images(url):
# pip install requests
# pip install beautifulsoup4

#     os.makedirs('downloaded_images', exist_ok=True)

#     # Send a GET request to the URL
#     response = requests.get(url)

#     if response.status_code == 200:
#         # Parse the HTML content
#         soup = BeautifulSoup(response.content, 'html.parser')

#         # Find all img tags
#         img_tags = soup.find_all('img')

#         for img in img_tags:
#             img_url = img.get('src')

#             # If the image URL is a relative path, convert it to absolute URL
#             img_url = urljoin(url, img_url)

#             # Download the image
#             img_name = img_url.split('/')[-1]
#             img_data = requests.get(img_url).content

#             # Save the image to the downloaded_images folder
#             with open(f'downloaded_images/{img_name}', 'wb') as img_file:
#                 img_file.write(img_data)

#             print(f"Downloaded: {img_name}")
#     else:
#         print("Failed to fetch the page.")

# # url_to_crawl = 'https://www.google.co.in'
# url_to_crawl = 'https://genial.ly'
# # url_to_crawl = 'https://unsplash.com/wallpapers/desktop'
# # url_to_crawl = 'https://en.wikipedia.org/wiki/Main_Page'
# # url_to_crawl = 'https://www.nationalgeographic.com/photography/photo-of-the-day/'
# # url_to_crawl = 'https://unsplash.com/'

# download_images(url_to_crawl)


#urls of webpage
# import requests
# from bs4 import BeautifulSoup
# from urllib.parse import urljoin

# def url_crawler(url):
#     response = requests.get(url)
#     soup = BeautifulSoup(response.content, 'html.parser')

#     links = soup.find_all('a')

#     for link in links:
#         href = link.get('href')
#         absolute_url = urljoin(url, href)
#         print(absolute_url)

# webpage_url = 'https://unsplash.com'
# url_crawler(webpage_url)



import requests
from bs4 import BeautifulSoup

def text_crawler(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    text = soup.get_text()
    return text.strip(' ')

url = 'https://unsplash.com'
webpage_text = text_crawler(url)
print(webpage_text)