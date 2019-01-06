f = open('info')
l='\n'
while l != '': 
    title = f.readline()
    date = f.readline()

    desc_str = ''
    l = f.readline()
    while l != '\n':
      desc_str = desc_str + f'  <p><small>{l}</small></p>\n' 
      l = f.readline()
    print(
f"""
<tr><td>
  <div class="d-flex w-100 justify-content-between">
    <h6 class="mb-1">{title}</h6>
    <small>{date}</small>
  </div>            
  {desc_str} 
</tr></td>""")



