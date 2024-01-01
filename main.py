import requests
from send_email import send_email

api_key = 'c0085be4acde41e787412d941d3bcfe7'
url = 'https://newsapi.org/v2/everything?q=tesla&' \
      'from=2023-12-01&sortBy=publishedAt&apiKey=' \
      'c0085be4acde41e787412d941d3bcfe7'

# Make a request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article title and descriptions
body = ""
for article in content['articles']:
    body = body + article['title'] + '\n' + article['description'] + 2*'\n'

body = body.encode('utf-8')
send_email(message=body)
