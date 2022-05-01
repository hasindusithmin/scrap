import requests
from bs4 import BeautifulSoup
def dtv_fn():
  r = requests.get('http://www.adaderana.lk/rss.php',headers={'user-agent':'Mozilla/5.0'},timeout=15)
  if r.status_code == 200:
    try:
      soup = BeautifulSoup(r.content,'xml')
      item = soup.find('item')
      description = item.find('description').text
      image_url = [x for x in description.split("'") if x.startswith('https://') and x.endswith('.jpg')]
      image_url = image_url[0] if len(image_url) else ''
      detail = description.split('>')[1]
      title = item.find('title').text
      pub_date = item.find('pubDate').text
      return {
          'pub_date':pub_date,
          'title':title,
          'detail':detail,
          'image_url':image_url
      }
    except:
      return {}
  return "can't fetch"
