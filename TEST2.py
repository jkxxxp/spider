
import urllib.request
import urllib.parse
request = urllib.request.Request('http://www.17k.com/chapter/2933095/36699279.html')
response = urllib.request.urlopen(request)
HTML=response.read().decode('utf8')
print(HTML)
with open('/home/xxp/Desktop/TEST2.txt',mode='w') as f:
    f.write(HTML)
