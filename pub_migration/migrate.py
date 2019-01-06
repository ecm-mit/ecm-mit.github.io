f = open('info')
links = open('links')
for i in range(84): 
    title = f.readline()
    authors = f.readline()
    pub_info = f.readline()
    journal = pub_info.split(',',1)[0]
    paper_spec = ',' +  pub_info.split(',',1)[1]
    f.readline()
    link = links.readline()
    print(
f"""
<tr>
  <th scope="row">{84-i}</th>
  <td>
    <a {link} target="_blank">{title}</a><br>
    {authors}<br>
    <span class="font-weight-bold">{journal}</span>{paper_spec}
  </td>
</tr>""")



