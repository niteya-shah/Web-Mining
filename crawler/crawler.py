from crawler_library import crawler
from string_library import tokenise,cos_sim,con_cat_list,text_to_vector,Jaccard,tf_idf
from json_work_library import store_list,retreive_list

##Definations: Starting urls , file locations##
start_url=['https://en.wikipedia.org/wiki/Huguenot-Walloon_half_dollar','https://en.wikipedia.org/wiki/Silver','https://en.wikipedia.org/wiki/Gold']
file_location='doc_result.json'

##start our crawler: the crawler will parrallise if more than starting url is found##
data,weblist=crawler(start_url)

##store the web pages found##
file=con_cat_list(weblist,data)
store_list(file_location,file)
file=retreive_list(file_location)

##tf-idf of the documents##
tfidf=tf_idf(file)
print(tfidf[1])
##Input our Query##
query=tokenise(input('enter your query'))
print(query)
##cosine similarity
cos_storage=dict()
for i in range(len(file)):
    cos_storage[file[i][0]]=cos_sim(file[i][1],query)
for arr in sorted(cos_storage.items(),key= lambda sort:sort[1],reverse=True)[0:10]:
    print(arr)
##Jaccard similarity
jacc_storage=dict()
for i in range(len(file)):
    jacc_storage[file[i][0]]=Jaccard(" ".join(file[i][1]),str(query))
for arr in sorted(jacc_storage.items(),key= lambda sort:sort[1],reverse=True)[0:10]:
    print(arr)
