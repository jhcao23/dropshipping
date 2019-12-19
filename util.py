import json
import subprocess

class Link:
    def __init__(self, url, id):
        self.url = url
        self.id = id
        self.subtitle = None
    def setSubtitle(self, subtitle):
        self.subtitle = subtitle


def findChapter(link):
    href = link #.get_attribute('href')
    inx = href.index('step-')
    return href[ inx+5: inx+6]

def normLinks(links):
    prev = 0
    lec = 0
    sol = []
    for link in links:
        chap = int(findChapter(link))
        if chap > prev:
            prev = chap
            lec = 1
        else:
            lec+=1
        id = str(chap)+'.'+str(lec)
        print(link, id)
        sol.append(Link(link, id))
    return sol

def dl(link: Link):
    subprocess.run(['curl', '-o', link.id+'.vtt', link.url])


links = [
'https://members.theecommclubhouse.com/step-3/how-to-buy-a-domain-name-2/'
,
'https://members.theecommclubhouse.com/step-3/how-to-remove-store-password-2/'
,
'https://members.theecommclubhouse.com/ecomm-clubhouse/step-4/how-to-add-sales-pop/'
,
'https://members.theecommclubhouse.com/ecomm-clubhouse/step-4/how-to-add-trust-icons/'
,
'https://members.theecommclubhouse.com/ecomm-clubhouse/step-4/how-to-add-discounted-pricing/'
,
'https://members.theecommclubhouse.com/ecomm-clubhouse/step-4/how-to-add-smar7-bundle-upsell/'
,
'https://members.theecommclubhouse.com/ecomm-clubhouse/step-4/how-to-add-spin-a-wheel-app/'

]

def toJsonString(normLinks):
    newArray = []
    for n in normLinks:
        dd = {'id': n.id, 'url': n.url, 'subtitle': n.subtitle}
        newArray.append(dd)
    return json.dumps(newArray)

normLinks = normLinks(links)
print(toJsonString(normLinks))
