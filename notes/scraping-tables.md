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