import csv

import requests
from bs4 import BeautifulSoup

def main():
    OUTPUT_PATH = 'mime-types.csv'
    URL = 'https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Complete_list_of_MIME_types'
    
    resp = requests.get(URL)
    soup = BeautifulSoup(resp.text)
    fields = soup.select('.standard-table thead')[0].text.strip().split('\n')
    
    rows = [fields]
    raw_rows = soup.select('.standard-table tbody tr')
    
    for raw_row in raw_rows:
        row = [td.text.strip().replace('\n', ',').replace(' ', '') for td in raw_row.select('td')]
        rows.append(row)
        
    with open(OUTPUT_PATH, 'w') as f:
        writer = csv.writer(f, lineterminator='\n')
        writer.writerows(rows)
    
if __name__ == '__main__':
    main()
    
    