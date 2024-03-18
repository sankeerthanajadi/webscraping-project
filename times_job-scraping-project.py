from bs4 import BeautifulSoup
import requests
import time
def find_job():
    not_known=input("enter the your skills: ")
    print('filtering jobs that are best suited for you')
    ws_text= requests.get("https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python&txtLocation=").text
    soup= BeautifulSoup(ws_text,'lxml')
    job = soup.find_all('li', class_="clearfix job-bx wht-shd-bx")
    for index,i in enumerate(job):
        date_posted=i.find('span',class_="sim-posted").text.replace(' ','')
        if 'few' in date_posted:
            c_name=i.find('h3',class_="joblist-comp-name").text.replace(' ','')
            skills=i.find('span', class_="srp-skills").text.replace(' ','')
            desc=i.header.h2.a['href']
            if not_known in skills:
                with open(f'result/{index}.txt','w') as f:
                    f.write(f'company name: {c_name.strip()}\nskills requried: {skills.strip()}\n Job Description: {desc}')
                print(f'file saved {index}')
if __name__=='__main__':
    while True:
        find_job()
        waiting_time=10
        print(f'waiting for {waiting_time} minutes')
        time.sleep(waiting_time*10)
        
