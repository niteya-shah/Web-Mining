"""
the functions cleans the string and splits it into tokens
"""
def tokenise(string):
    bad_chars='(){}<>.,?!\/'
    for c in bad_chars:
        string = string.replace(c, " ")
    return string.split()
"""
the function converts the tokenised string into a tf vector(not normalised)
"""
def text_to_vector(tokens):
    lib=dict()
    for i in tokens:
        if i in lib:
            lib[i]+=1
        else:
            lib[i]=1
    return lib
"""
zips the two lists into 1 paired list , didnt use the zip function as json cant store zip files
"""
def con_cat_list(list1,list2):
    assert(len(list1)==len(list2))
    list_fin=list()
    for i in range(len(list1)):
        list_fin.append([list1[i],list2[i]])
    return list_fin

"""
converts a list of strings into a string and then tokenises them
"""
def pre_process(data):
    for i in range(len(data)):
        data[i]=tokenise(" ".join(data[i]))
    return data
"""
calculates the cosine similarity between 2 strings
"""
def cos_sim(string1,string2):
    import math
    lib1=text_to_vector(string1)
    lib2=text_to_vector(string2)
    inttersec=set(lib1.keys()) & set(lib2.keys())
    term1=sum([lib1[x]*lib2[x] for x in inttersec])
    term2= sum([lib1[x]**2 for x in lib1.keys()])
    term3= sum([lib2[x]**2 for x in lib2.keys()])
    denom=math.sqrt(term2)*math.sqrt(term3)
    if not denom:
        return 0
    else:
        return term1/denom
"""
calculates the Jaccard similarity between 2 strings
"""
def Jaccard(string1,string2):
    str1=tokenise(string1)
    str2=tokenise(string2)
    return len(set(str1)&set(str2))/len(set(str1)|set(str2))
"""
functions maps the locations of particular word in the document (unused in the code)
"""
def Invindex(string):
    x=0
    lib=dict()
    for i in tokenise(string):
        if i not in lib:
            lib[i]=list()
            lib[i].append(x)
        else:
            lib[i].append(x)
        x+=1
    return lib
"""
calculates the tf-idf of a group of documents
"""
def tf_idf(file):
    import math
    doc=[]
    tf_idf=[]
    for i in range(len(file)):
         doc.append(tokenise(" ".join(file[i][1])))
    N=len(doc)
    for i in doc:
        tf_1=text_to_vector(i)
        w=sum(tf_1.values())
        for i in tf_1.keys():
            tf_1[i]/=w
        tf_idf.append(tf_1)
    for dicts in tf_idf:
        for string in dicts.keys():
            dicts[string]*=math.log(N/(1+sum([string in i.keys() for i in tf_idf])))
    return tf_idf
