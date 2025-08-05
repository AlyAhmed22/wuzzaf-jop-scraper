import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrap():
    all_titles = []
    all_companies = []
    all_locations = []
    all_occupations = []

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

    for page in range(0, 62):
        url = f'https://wuzzuf.net/search/jobs/?a=navbl&q=data%20analysis%20&start={page}'
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, "lxml")

        titles = soup.find_all('h2', {'class': "css-m604qf"})
        companies = soup.find_all('div', {'class': 'css-d7j1kk'})
        locations = soup.find_all('span', {'class': "css-5wys0k"})
        occupations = soup.find_all("div", {'class': "css-1lh32fc"})

        titles_page = [title.a.text.strip() if title.a else None for title in titles]
        companies_page = [comp.find('a').text.strip() if comp.find('a') else None for comp in companies]
        locations_page = [loc.text.strip()for loc in locations]
        occupations_page = [occ.a.text.strip() for occ in occupations]


        all_titles.extend(titles_page)
        all_companies.extend(companies_page)
        all_locations.extend(locations_page)
        all_occupations.extend(occupations_page)

    max_len = max(len(all_titles), len(all_companies), len(all_locations), len(all_occupations))

    all_titles += [None] * (max_len - len(all_titles))
    all_companies += [None] * (max_len - len(all_companies))
    all_locations += [None] * (max_len - len(all_locations))
    all_occupations += [None] * (max_len - len(all_occupations))

    data = {
        'Title': all_titles,
        'Company': all_companies,
        'Location': all_locations,
        'Occupation': all_occupations
    }

    df = pd.DataFrame(data)
    print(df.head(10))
    df.to_excel('wuzzuf_jobs.xlsx', index=False)
    print(f'Data saved to wuzzuf_jobs.xlsx with {max_len} rows.')
    return df

scrap()
