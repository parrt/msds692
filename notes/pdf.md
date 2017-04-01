# Extracting text from PDFs

PDF files are effectively restricted versions of PostScript files, what you might've heard of. PDF files are actually programs in a very simple programming language and hence can display just about anything. Much of what you see inside a PDF file is text, however, and we can grab that text without the layout information using [pdf2txt.py](https://euske.github.io/pdfminer/). Install it with:
 
```bash
$ pip install pdfminer
```

Then use `pdf2txt.py` as a command from the commandline, which will spit the text out to standard output. First download a sample PDF, such as [Dr_Maxwell_Glen_Berry.pdf](https://www.eisenhower.archives.gov/education/articles/Dr_Maxwell_Glen_Berry.pdf) then pass the filename to `pdf2txt.py`:

```bash
$ pdf2txt.py ~/data/Dr_Maxwell_Glen_Berry.pdf
World War II Remembered is a multi-year exhibition currently on display at the Eisenhower Presidential Museum.  The 
article  that  follows  is  a  special  feature  of  this  exhibition,  the  sixth  in  a  series  created  to  honor  and  educate  about  the 
...
```

Now, redirect that text to a file using the bash `>`  operator or the `-o` option on `pdf2txt.py`.

```bash
$ pdf2txt.py ~/data/Dr_Maxwell_Glen_Berry.pdf > t.txt
$ pdf2txt.py -o /tmp/t.txt ~/data/Dr_Maxwell_Glen_Berry.pdf
```

Once you have text output, you can perform whatever analysis you'd like without having to worry about the data coming in PDF form. For example, you might want to run some analysis on financial documents but they are all in PDF. First, convert to text and then perform your analysis.

**Exercise**: Read that text file and split the document into a list of words. Print out the first 100 words. It should look like:

```
['World', 'War', 'II', 'Remembered', 'is', 'a', 'multi-year', 'exhibition', ... ]
```

Now, import the `Counter` object which makes histograms from a list of elements:

```python
from collections import Counter
```

Then, if `words` is your list of words, create and print a histogram:

```python
print Counter(words)
```

The output starts like this:

```
Counter({'': 600, 'the': 52, 'of': 37, 'a': 31, 'and': 28, 'to': 26, '\n': 26, 'in': 25, 'his': 19, 'he': 17, 'was': 16, 'Max': 14, 'that': 11, 'were': 9, '.': 9, 'had': 9, 'for': 9, 'with': 9, 'at': 9, '\nand': 8, 'our': 8, 'I': 7, 'War': 6, 'on': 6, 'have': 5, 'as': 5, '\nin': 5, '1945,': 4, 'would': 4, 'two': 4, 'Maxwell': 4, 'World': 4, 'University': 4, 'Josephine': 4, ...
```