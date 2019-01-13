import requests
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    }
url = "http://www.image-net.org/api/text/imagenet.synset.geturls?wnid=n02127808"
response = requests.get(url)
#print(response.text)
urls=response.text
url1=urls.split('\r\n')
for ul in url1:
    try:
        p=requests.get(ul,headers=headers,timeout=1)
        imageName = ul.split('/')[-1]
        with open('/home/xxp/Desktop/{}'.format(imageName),mode='wb') as f:
            f.write(p.content)
    except Exception as e:
        print(e)

        