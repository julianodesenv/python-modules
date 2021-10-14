from string import Template
from datetime import datetime

with open('./006 - String and template/template.html', 'r') as html:
    template = Template(html.read())

    date = datetime.now().strftime('%Y-%m-%d')
    body_msg = template.substitute(name='Juliano', date=date)
    #body_msg = template.safe_substitute(name='Juliano', date=date)

print(body_msg)