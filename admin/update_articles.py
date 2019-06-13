

articles = []
# Keys: {link, title, authors, journal, pages, year, note}
# All elements are strings
# note is optional
with open('articles.txt') as articles_file:
    article = {}
    for line in articles_file:
        if line.isspace() or 'END ARTICLES' in line:
            articles.append(article)
            article = {}
        elif 'link' not in article:
            article['link'] = line.rstrip()
            if article['link'] == 'NO LINK':
                article['link'] = None
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
                    if article['link']:
                        title_str = f"""<p><a href="{article['link']}" target="_blank">{article['title']}</a>"""
                    else:
                        title_str = f"""<p><span>{article['title']}</span>"""

                    notes_str = '</p>'
                    if 'note' in article:
                        notes_str = f"""</p><div class="small text-muted">{article['note']}</div>"""

                    new_articles_html += f"""
<tr><th scope="row">{len(articles) - i}</th><td>
    {title_str}<br>
    {article['authors']}<br>
    <span class="font-weight-bold">{article['journal']}</span>, {article['pages']} ({article['year']})
    {notes_str}
</td></tr>
"""
                    i += 1

                new_articles_html += '</tbody></table>\n'

        if not in_list:
            new_articles_html += line

with open('../pubs/articles/index.html', 'w') as articles_html:
    articles_html.write(new_articles_html)


