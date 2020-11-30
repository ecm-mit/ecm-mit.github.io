import os.path
from os import path
import os

articles = []
# Keys: {doi, title, authors, journal, pages, year, note}
# All elements are strings
# note is optional
with open('articles.txt') as articles_file:
    article = {}
    for line in articles_file:
        if line.isspace() or 'END ARTICLES' in line:
            articles.append(article)
            article = {}
        elif 'doi' not in article:
            article['doi'] = line.rstrip()
            if article['doi'] == 'NO DOI':
                article['doi'] = None
        elif 'title' not in article:
            article['title'] = line.rstrip()
        elif 'authors' not in article:
            article['authors'] = line.rstrip()
        elif 'authors' not in article:
            article['authors'] = line.rstrip()
        elif 'journal' not in article:
            article['journal'] = line.rstrip()
        elif 'pages' not in article:
            article['pages'] = line.rstrip()
        elif 'year' not in article:
            article['year'] = line.strip()
        elif 'note' not in article:
            article['note'] = line.rstrip()
        else:
            print('Error while parsing articles.txt')

new_articles_html = ''
with open('../pubs/articles/index.html') as articles_html:
    in_list = False
    for line in articles_html:
        if '<!-- END ARTICLES -->' in line:
            in_list = False
            new_articles_html += '<!-- END ARTICLES -->\n'
            continue
        if '<!-- START ARTICLES -->' in line:
            in_list = True
            new_articles_html += '<!-- START ARTICLES -->\n'
            
            i = 0
            while i < len(articles):

                current_year = articles[i]['year']

                new_articles_html += f"""
<h4 class="text-center pb-2 font-weight-light">{current_year}</h4>
      <table class="table table-sm mx-auto">
        <tbody>
"""
                while i < len(articles) and current_year == articles[i]['year']:
                    article = articles[i]

                    title_str = ''
                    if article['doi']:
                        title_str = f"""<p><a href="http://doi.org/{article['doi']}" target="_blank">{article['title']}</a>"""
                    else:
                        title_str = f"""<p><span>{article['title']}</span>"""

                    notes_str = '</p>'
                    if 'note' in article:
                        notes_str = f"""</p><div class="small text-muted">{article['note']}</div>"""

                    pdf_str = ""
                    mod_doi = 'x'
                    if articles[i]['doi']:
                        mod_doi = articles[i]['doi'].replace('/','-')
                    if path.exists(f"../pubs/articles/{len(articles)-i}.pdf"):
                        os.rename(f"../pubs/articles/{len(articles)-i}.pdf",f"../pubs/articles/{mod_doi}.pdf")
                    if path.exists(f"../pubs/articles/{mod_doi}.pdf"):
                        pdf_str = f"""<a href="{mod_doi}.pdf" target="_blank"><i class="fas fa-file-pdf"></i></a>"""

                    if(article['pages'] != 'NO PAGES'):
                        new_articles_html += f"""
<tr><th scope="row">{len(articles) - i}</th><td>
    {title_str}<br>
    {article['authors']}<br>
    <span class="font-weight-bold">{article['journal']}</span>, {article['pages']} ({article['year']}) {pdf_str}
    {notes_str}
</td></tr>
"""
                    else:
                        new_articles_html += f"""
<tr><th scope="row">{len(articles) - i}</th><td>
    {title_str}<br>
    {article['authors']}<br>
    <span class="font-weight-bold">{article['journal']}</span> ({article['year']}) {pdf_str}
    {notes_str}
</td></tr>
"""
                    
                    i += 1

                new_articles_html += '</tbody></table>\n'

        if not in_list:
            new_articles_html += line

with open('../pubs/articles/index.html', 'w') as articles_html:
    articles_html.write(new_articles_html)


