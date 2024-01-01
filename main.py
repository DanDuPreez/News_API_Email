import requests

api_key = 'c0085be4acde41e787412d941d3bcfe7'
url = 'https://newsapi.org/v2/everything?q=tesla&'\
      'from=2023-12-01&sortBy=publishedAt&apiKey='\
      'c0085be4acde41e787412d941d3bcfe7'

# Make a request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article title and descriptions
for article in content['articles']:
      print(article['title'])
      print(article['descriptions'])
