
import time

from IPython.core.display import display, HTML


def me():
    html = '<h1>Mark Servilla</h1>'
    display(HTML(html))


def about_me():
    html = '<h2>M.S. (1991) UNM Computer Science</h2>'
    display(HTML(html))
    time.sleep(3)

    html = '<h2>Ph.D. (1996) UNM Earth & Planetary Sciences (Volcanology)</h2>'
    display(HTML(html))
    time.sleep(3)

    html = '<h2>Principal Investigator - Environmental Data Initiative</h2>'
    display(HTML(html))


def contact():
    html = '<h2>servilla@unm.edu</h2>' + \
           '<h2>mark.servilla@gmail.com</h2>'
    display(HTML(html))


def topics():
    html = '<h2>Reading data from...</h2>'
    display(HTML(html))
    time.sleep(1)

    html = '<h3><ul>' + \
           '  <li>the desktop</li>' + \
           '  <li>HTML web pages</li>' + \
           '  <li>RESTful web services</li>' + \
           '</ul></h3>'
    display(HTML(html))
    time.sleep(6)

    html = '<h2>What to do with data when in Python</h2>'
    display(HTML(html))
    time.sleep(1)

    html = '<h3><ul>' + \
           '  <li>Clean</li>' + \
           '  <li>Visualize</li>' + \
           '  <li>Save</li>' + \
           '</ul></h3>'
    display(HTML(html))
    time.sleep(6)

    html = '<h2>What this session will not cover</h2>'
    display(HTML(html))
    time.sleep(1)

    html = '<h3><ul>' + \
           '  <li>NumPy</li>' + \
           '  <li>Pandas</li>' + \
           '  <li>Matplotlib</li>' + \
           '</ul></h3>'
    display(HTML(html))


def env():
    html = '<h2>Linux Mint 18.3 Sylvia</h2>'
    display(HTML(html))
    time.sleep(2)

    html = '<h2>Conda version 4.5.1</h2>'
    display(HTML(html))
    time.sleep(2)

    html = '<h2>Anaconda version 5.1</h2>'
    display(HTML(html))
    time.sleep(2)

    html = '<h2>Python version 3.6.5</h2>'
    display(HTML(html))
    time.sleep(2)


def caveats():
    html = '<h2>1. I am not a DATA SCIENTIST</h2>'
    display(HTML(html))
    time.sleep(4)

    html = '<h2>2. I am a Python n00b</h2>'
    display(HTML(html))
