from bs4 import BeautifulSoup
import cfscrape

def nffn():
    scraper = cfscrape.create_scraper()
    r = scraper.get("https://www.newsfirst.lk/feed/",timeout=15)
    if r.status_code == 200:
        try:
            soup = BeautifulSoup(r.content, 'xml')
            item = soup.find('item')
            description = item.find('description').text
            image_url = [x for x in description.split('"') if x.startswith('https://') and x.endswith('.jpg')]
            image_url = image_url[0] if len(image_url) != 0 else ''
            paragraph = [x for x in description.split(">") if x.startswith('COLOMBO')][0].replace("</p", "")
            title = item.find("title").text
            pub_date = item.find("pubDate").text
            return {
                "title": title,
                "pub_date": pub_date,
                "details": paragraph,
                "image_url": image_url
            }
        except:
            return {}
    return "can't fetch"