def check(candidate):
    assert candidate("https://www.washingtonpost.com/news/football-insider/wp/2016/09/02/odell-beckhams-fame-rests-on-one-stupid-little-ball-josh-norman-tells-author/") == [('2016', '09', '02')]
    assert candidate("https://www.indiatoday.in/movies/celebrities/story/wp/2020/11/03/odeof-sushant-singh-rajput-s-death-his-brother-in-law-shares-advice-for-fans-1749646/") == [('2020', '11', '03')]
    assert candidate("https://economictimes.indiatimes.com/news/economy/2020/12/29/finance/pension-assets-under-pfrda-touch-rs-5-32-lakh-crore/articleshow/79736619.cms") == [('2020', '12', '29')]


import re

def extract_date_from_url(url):
    pattern = r'(\d{4})-(\d{2})-(\d{2})'
    match = re.match(pattern, url)
    if match:
        year, month, day = match.groups()
        return int(year), int(month), int(day)
    return None

check(extract_date_from_url)