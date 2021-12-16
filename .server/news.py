import requests, json
 
def topNews():
    query_params = {
      "source": "bbc-news",
      "sortBy": "top",
      "apiKey": "10b7a1938f0b49acaa670aa9d12719d2"
    }
    main_url = " https://newsapi.org/v1/articles"
 
    # fetching data in json format
    res = requests.get(main_url, params=query_params)
    open_bbc_page = res.json()
 
    # getting all articles in a string article
    article = open_bbc_page["articles"]
 
    # empty list which will
    # contain all trending news
     
    for ar in article:
        title = ar['title']
        description = ar['description']
        image = ar['urlToImage'],
        url = ar['url']
        news = {
            'Title' : title,
            'Description' : description,
            'Photo_url' : image[0],
            'Url' : url,
        }
        results.append(news)
    return

results = []
            
# topNews()
# print(json.dumps(results, indent=2))