import pandas as pd
from serpapi import GoogleSearch

def search_news(keyword, max_results=20):
    # 設定 SerpAPI 的 API 金鑰
    api_key = 'XXXX'

    # 設定搜尋參數
    params = {
        'q': keyword,
        'engine': 'google_news',
        'api_key': api_key,
        'gl': 'TW',  # 地區設定為台灣
        'hl': 'zh-TW',  # 語言設定為繁體中文
        'tbm': 'nws',  # 搜尋類型為新聞
    }

    # 建立 GoogleSearch 物件並取得資料
    search = GoogleSearch(params)
    results = search.get_dict()

    # 解析新聞結果
    news_data = []
    for article in results.get('news_results', []):
        news_data.append({
            'title': article.get('title'),
            'link': article.get('link'),
            'source': article.get('source'),
            'date': article.get('date'),
            'snippet': article.get('snippet'),
            'thumbnail': article.get('thumbnail'),
        })

    # 將資料轉換為 DataFrame
    df = pd.DataFrame(news_data)

    return df

if __name__ == "__main__":
    keyword = input("請輸入關鍵字: ")
    df = search_news(keyword)
    print(df)
    df.to_csv(f"{keyword}_news.csv", index=False, encoding='utf-8-sig')
    print(f"已存成 {keyword}_news.csv")
