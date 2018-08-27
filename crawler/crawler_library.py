"""
My crawler, goes to every page finds urls and adds them to the list if they are not already visited
It uses BeautifulSoup and requests as external libraries
the data retrival is exclusive to the p tag for now but can be extended to other tags
"""
def crawl(url,visited,datastore,goto,max_num_requests_per_page=10):
    import requests
    from bs4 import BeautifulSoup
    from urllib.parse import urljoin
    temp_datastore=list()
    r=requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    visited.append(url)
    counter=0
    for link in soup.find_all('a'):
        if(counter>=max_num_requests_per_page-1):
            break
        else:
            url=urljoin(url,link.get('href'))
            if (url not in visited) and 'https://' in url and (url not in goto):
                goto+=[url]
                counter+=1
    for text in soup.findAll('p'):
        temp_datastore.append(text.findAll(text=True)[0])
    datastore.append(temp_datastore)
    return
"""
My spider , controls the crawl and is the nexus of all data storage
"""
def spider(url,max_num_pages=30,max_num_requests_per_page=10):
    visited=list()
    datastore=list()
    goto=list()
    i=0
    goto.append(url)
    while((len(visited)<=max_num_pages-1) or (i==len(goto))):
        crawl(goto[i],visited,datastore,goto)
        print(i,end=" ")
        print(goto[i],end=" .\n")
        i+=1
    return datastore,visited
"""
parrallises the spider function using the inbuilt multiprocessing library with a max core limit of 5(for stability)
assumes a max page per core of 30 and number of requests per page as 10
"""

def par_spider(url_list):
    from multiprocessing.dummy import Pool as ThreadPool
    number_of_cores=min(len(url_list),5)
    results=[]
    data=[]
    weblist=[]
    pool=ThreadPool(number_of_cores)
    results+=pool.map(spider,url_list)
    for i in results:
        data+=i[0]
        weblist+=i[1]
    return data,weblist
"""
Index function that is called by the file , decides if multi core or single core execution
"""
def crawler(url_list):
    if(len(url_list)==1):
        data,weblist=spider(url_list,50)
    else:
        data,weblist=par_spider(url_list)
    return data,weblist
