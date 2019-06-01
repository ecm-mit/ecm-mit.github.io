stories = []
# A story is a dictionary: {title=str, date=str, body=[str]}
with open('news.txt') as news_file:
    stage = 0
    story = {'body' : [], 'imgs' : []}
    for line in news_file:
        if line.isspace() or 'END NEWS' in line:
            stories.append(story)
            story = {'body' : [], 'imgs' : []}
        elif 'title' not in story:
            story['title'] = line.rstrip()
        elif 'date' not in story:
            story['date'] = line.rstrip()
        elif 'IMAGE:' in line:
            story['imgs'].append(line.replace('IMAGE:','').rstrip().lstrip()) 
        else:
            story['body'].append(line.rstrip())

new_home_html = ''
with open('../index.html') as home_html:
    in_news_bar = False
    for line in home_html:
        if '<!-- END NEWS BAR -->' in line:
            in_news_bar = False
            continue
        if '<!-- START NEWS BAR -->' in line:
            in_news_bar = True
            new_home_html += f"""
<!-- START NEWS BAR -->
<div class="container-fluid p-0 news-bar text-white">
    <div class="row p-0 m-0">
        <div class="col-sm-auto p-2 bg-dark">
            <div class="ecm-primary font-weight-bold text-center align-middle"> NEWS </div>
        </div>
        <div class="col-sm p-1 bg-lessdark">
            <a class="text-smaller text-white font-weight-light" href="news/index.html#news1"> {stories[0]['title']} </a>
            <br>
            <small class="ecm-primary font-italic"> {stories[0]['date']} </small>
        </div>
        <div class="col-sm p-1 bg-dark">
            <a class="text-smaller text-white font-weight-light" href="news/index.html#news2"> {stories[1]['title']} </a>
            <br>
            <small class="ecm-primary font-italic"> {stories[1]['date']} </small>
        </div>
        <div class="col-sm p-1 bg-lessdark">
            <a class="text-smaller text-white font-weight-light" href="news/index.html#news3"> {stories[2]['title']} </a>
            <br>
            <small class="ecm-primary font-italic"> {stories[2]['date']} </small>
        </div>
    </div>
</div>
<!-- END NEWS BAR -->
"""
            continue
        if not in_news_bar:
            new_home_html += line

with open('../index_test.html', 'w') as home_html:
    home_html.write(new_home_html)


new_news_html = ''
with open('../news/index.html') as news_html:
    in_news = False
    for line in news_html:
        if '<!-- END NEWS -->' in line:
            in_news = False
            new_news_html += '<!-- END NEWS -->\n'
            continue
        if '<!-- START NEWS -->' in line:
            in_news = True
            new_news_html += '<!-- START NEWS -->\n'
            for i, story in enumerate(stories):
                anchor_str = ''
                if i < 3:
                    anchor_str = f'<a class="anchor" id="news{i+1}"></a>'
                body_str = ''
                for item in story['body']:
                    body_str += f'<p><small>{item}</small></p>\n'
                img_links_str = ''
                for img in story['imgs']:
                    img_links_str += f'<a href="{img}"><i class="fas fa-camera"></i></a>'
                new_news_html += f"""
<tr><td>
    {anchor_str}
    <h6 class="mb-1">{story['title']} {img_links_str}</h6> 
    <div class='font-weight-light'>{story['date']}</div>
    {body_str}
</td></tr>
"""
            continue
        if not in_news:
            new_news_html += line

with open('../news/index.html', 'w') as news_html:
    news_html.write(new_news_html)


