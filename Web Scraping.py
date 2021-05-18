#!/usr/bin/env python
# coding: utf-8

# In[3]:


from bs4 import BeautifulSoup
import requests
import re
import time


# In[4]:


def find_jobs(unknown_skills):
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python&txtLocation=').text
    soup = BeautifulSoup(html_text, 'lxml')

    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

    for idx, job in enumerate(jobs):
        published_date = job.find('span',class_='sim-posted').span.text
        if 'few' in published_date:
            company_name = job.find('h3', class_ = 'joblist-comp-name').text
            company_name = re.sub("\(.*?\)","",company_name)
            skills = job.find('span', class_='srp-skills').text.replace('  , ',',')
            more_info = job.header.h2.a['href']
            flag = 1
            for unfam_skill in unknown_skills:
                if unfam_skill in skills:
                    flag = 0
                    break
            if flag == 1:
                with open(f'posts/{idx}.txt','w') as f:
                    f.write(f'Company Name : {company_name.strip()}\n')
                    f.write(f'Required Skills: {skills.strip()}\n')
                    f.write(f'More Info: {more_info}\n')
                print(f'File Saved: {idx}')


# In[ ]:


if __name__ == '__main__':
    print('Put some skill you are not familiar with')
    unfamiliar_skill = list(map(str, input().split(', ')))
    print('Filtering Out ',end='')
    print(*unfamiliar_skill,sep=', ')
    print()
    while True:
        find_jobs(unfamiliar_skill)
        time_wait = 12
        print(f'Waiting {time_wait} hours...')
        print()
        time.sleep(time_wait*3600)


# In[ ]:




