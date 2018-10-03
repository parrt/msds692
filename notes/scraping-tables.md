## Extracting a table of data

Let's see if we can pull academic performance data from [2012-13 Accountability Progress Reporting (APR)](http://data1.cde.ca.gov/dataquest/Acnt2013/2013GrthStAPI.aspx).

**Exercise**: Create a list of lists representation for the `2013 Growth API` table and another for the `Number of Students Included in the 2013 Growth API` table. You can start out by combining all rows from both tables. Or try list of dictionary representation. *This one is challenging*!

To get you started, here is how I extract the header and columns:

```python
def get_table_headers(soup):
    headers = set()
    for h in soup.find_all('th', {'class': 'medium_center'}):
        s = ''
        for c in h.contents:
            if c.string:
                s += c.string.strip()
        if len(s)>0:
            headers.add(s)
    return headers
```

Your function looks like (it collects all rows from both tables):

```python
def get_table_rows(soup):
    data = []
    for tbl in table tags:
        for row in tr tags within tbl:
            cols = all td tags within row
            grab the rowname from cols[0]
            for col in cols[1:]:
                if col has span tag underneath:
                    add col.span text to current row
            add current row to data
    return data
```

Then I dump everything out with the following main program:

```python
print get_table_headers(soup)

allrows = get_table_rows(soup)
for row in allrows:
    print row
```

Thanks to 2018 MSDS student Eddie Owens, we have the following cools solution that combines beautiful soup with pandas:

```python
from bs4 import BeautifulSoup
import requests
import pandas as pd

html = requests.get('https://data1.cde.ca.gov/dataquest/Acnt2013/2013GrthStAPI.aspx')
page = html.content
soup = BeautifulSoup(page, "lxml")
tables = soup.find_all('table')
growthapi = pd.read_html(str(tables[1]))[0]
growthapi = growthapi.drop(growthapi.shape[1]-1, axis=1)
growthapi.iloc[1,0] = 'category'
growthapi.columns = growthapi.iloc[1,:]
growthapi = growthapi.drop([0,1,3], axis=0)
growthapi.set_index('category')

students = pd.read_html(str(tables[2]))[0]
students = students.drop(students.shape[1]-1, axis=1)
students.iloc[1,0] = 'category'
students.columns = students.iloc[1,:]
students = students.drop([0,1,3], axis=0)
students.set_index('category')

print(growthapi)
print(students)
```