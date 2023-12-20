# Guidline for parcing crypto news data from newsapi.org
# Link: https://newsapi.org/ 

import requests
from decouple import config
import pandas as pd
import datetime

keywords = ['bitcoin', 'ethereum', 'dogecoin', 'tether', 'bnb', 'xrp', 'usdcoin', 'solana', 'cardano', 'tron', 'toncoin', 'chainlink']
end_date = datetime.datetime.now().strftime('%Y-%m-%d')
start_date = (datetime.datetime.now() - datetime.timedelta(days=30)).strftime('%Y-%m-%d')
news_api_key = config('NEWS_API_KEY')
base = 'https://newsapi.org/v2/everything'

for crypto in keywords:
    # URL for API
    url = f"{base}?q={crypto}&from={start_date}&to={end_date}&sortBy=publishedAt&apiKey={news_api_key}"

    # Get data from API
    response = requests.get(url)
    data = response.json()
    
    if data['status'] != 'ok':
        print(f'❌ {crypto} is not working!')
        continue
    if data['totalResults'] == 0:
        print(f'❌ {crypto} has no data!')
        continue

    # Convert data to CSV and Save
    articles = data['articles']
    articles_df = pd.DataFrame(articles)
    articles_df.to_csv(f'data/{crypto}.csv')

    print(f'✅ {crypto}.csv is Done!')

print('✅ All Done!')