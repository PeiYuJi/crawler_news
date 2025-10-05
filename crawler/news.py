import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

def search_news(keyword, max_pages=2):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36'
    }

    all_news = []

    for page in range(max_pages):
        url = f"https://www.google.com/search?q={keyword}&tbm=nws&start={page*10}"
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Google News 每則新聞區塊
        articles = soup.select('div.dbsr')
        for article in articles:
            title_tag = article.select_one('div.JheGif.nDgy9d')
            link_tag = article.select_one('a')
            snippet_tag = article.select_one('div.Y3v8qd')

            title = title_tag.text if title_tag else ""
            link = link_tag['href'] if link_tag else ""
            snippet = snippet_tag.text if snippet_tag else ""

            all_news.append({
                'title': title,
                'link': link,
                'snippet': snippet
            })

        time.sleep(1)  # 避免過度請求

    return pd.DataFrame(all_news)

if __name__ == "__main__":
    keyword = input("請輸入關鍵字: ")
    df = search_news(keyword, max_pages=2)
    print(df)
    df.to_csv(f"{keyword}_news.csv", index=False, encoding='utf-8-sig')
    print(f"已存成 {keyword}_news.csv")
