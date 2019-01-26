import numpy as np
from sklearn.metrics import accuracy_score,f1_score,precision_score,recall_score,confusion_matrix,log_loss,hamming_loss
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.naive_bayes import GaussianNB
from sklearn import tree
##%%
doc=[
    'Artificial intelligence (AI), sometimes called machine intelligence, is intelligence demonstrated by machines, in contrast to the natural intelligence displayed by humans and other animals. In computer science AI research is defined as the study of "intelligent agents": any device that perceives its environment and takes actions that maximize its chance of successfully achieving its goals.Colloquially, the term "artificial intelligence" is applied when a machine mimics "cognitive" functions that humans associate with other human minds, such as "learning" and "problem solving"',
    'Machine learning is an interdisciplinary field that uses statistical techniques to give computer systems the ability to "learn" (e.g., progressively improve performance on a specific task) from data, without being explicitly programmed.',
    'Commerce relates to "the exchange of goods and services, especially on a large scale.”It includes legal, economic, political, social, cultural and technological systems " that operate in any country or internationally.',
    'Business analytics (BA) refers to the skills, technologies, practices for continuous iterative exploration and investigation of past business performance to gain insight and drive business planning. Business analytics focuses on developing new insights and understanding of business performance based on data and statistical methods.',
    'In computer science, digital image processing is the use of computer algorithms to perform image processing on digital images. As a subcategory or field of digital signal processing, digital image processing has many advantages over analog image processing.',
    'Religion may be defined as a cultural system of designated behaviors and practices, worldviews, texts, sanctified places, prophecies, ethics, or organizations, that relates humanity to supernatural, transcendental, or spiritual elements. However, there is no scholarly consensus over what precisely constitutes a religion.',
    'Traditionally, spirituality referred to a religious process of re-formation which "aims to recover the original shape of man", oriented at "the image of God" as exemplified by the founders and sacred texts of the religions of the world. The term was used within early Christianity to refer to a life oriented toward the Holy Spirit. and broadened during late medieval times to include mental aspects of life.',
    'Data mining is the process of discovering patterns in large data sets involving methods at the intersection of machine learning, statistics, and database systems.',
    'Artificial neural networks (ANN) or connectionist systems are computing systems vaguely inspired by the biological neural networks that constitute animal brains.',
    'Atheism is, in the broadest sense, the absence of belief in the existence of deities.Less broadly, atheism is the rejection of belief that any deities exist.',
    'Economics focuses on the behaviour and interactions of economic agents and how economies work. Microeconomics analyzes basic elements in the economy, including individual agents and markets, their interactions, and the outcomes of interactions. Individual agents may include, for example, households, firms, buyers, and sellers. Macroeconomics analyzes the entire economy (meaning aggregated production, consumption, savings, and investment) and issues affecting it, including unemployment of resources (labour, capital, and land), inflation, economic growth, and the public policies that address these issues (monetary, fiscal, and other policies).',
    'Christianity is an Abrahamic monotheistic religious group based on the life and teachings of Jesus of Nazareth, also known by Christians as the Christ. It is the worlds largest religion, with over 2.4 billion followers, or 33% of the global population, making up a majority of the population in about two-thirds of the countries in the world.',
    'Business is the activity of making ones living or making money by producing or buying and selling products (goods and services).Simply put, it is "any activity or enterprise entered into for profit. It does not mean it is a company, a corporation, partnership, or have any such formal organization, but it can range from a street peddler to General Motors."',
    'Islam is an Abrahamic monotheistic religion teaching that there is only one God (Allah) and that Muhammad is the messenger of God. It is the worlds second-largest religion and with over 1.8 billion followers or 24.1% of the global population, known as Muslims.',
    'In monotheistic thought, God is conceived of as the Supreme Being, creator, and principal object of faith. The concept of God, as described by theologians, commonly includes the attributes of omniscience (all-knowing), omnipotence (unlimited power), omnipresence (present everywhere), and as having an eternal and necessary existence. ',
    'Web mining is the application of data mining techniques to discover patterns from the World Wide Web. As the name proposes, this is information gathered by mining the web. It makes utilization of automated apparatuses to reveal and extricate data from servers and web2 reports, and it permits organizations to get to both organized and unstructured information from browser activities, server logs, website and link structure, page content and different sources.',
    'Natural language processing (NLP) is a subfield of computer science, information engineering, and artificial intelligence concerned with the interactions between computers and human (natural) languages, in particular how to program computers to process and analyze large amounts of natural language data.',
    'Hinduism is an Indian religion and dharma, or a way of life, widely practised in the Indian subcontinent and parts of Southeast Asia. Hinduism has been called the oldest religion in the world, and some practitioners and scholars refer to it as Sanātana Dharma, "the eternal tradition", or the "eternal way", beyond human history.',
    'A tax (from the Latin taxo) is a mandatory financial charge or some other type of levy imposed upon a taxpayer (an individual or other legal entity) by a governmental organization in order to fund various public expenditures. A failure to pay, along with evasion of or resistance to taxation, is punishable by law. Taxes consist of direct or indirect taxes and may be paid in money or as its labour equivalent.',
    'Human resource management (HRM or HR) is the strategic approach to the effective management of organization workers so that they help the business gain a competitive advantage, Commonly referred to as the HR Department, it is designed to maximize employee performance in service of an employers strategic objectives.HR is primarily concerned with the management of people within organizations, focusing on policies and on systems.',
    ]
y=['AI','ML','Commerce','BA','IP','Religion','spirituality','DM','NN','Atheism','Economics','Christianity','Business','Islam','God','WM','NLP','Hinduism','Taxation','HR management']
y_labels=[0,0,1,1,0,2,2,0,0,2,1,2,1,2,2,0,0,2,1,1]
##%%
vectorizer=TfidfVectorizer()
X=vectorizer.fit_transform(doc)
##%%
kmeans = KMeans(n_clusters=3, random_state=0).fit(X)
##%%
gnb = GaussianNB()
y_test_gauss=gnb.fit(X.toarray()[0:15],y_labels[0:15]).predict(X.toarray()[15:])
def warn(*args, **kwargs):
    pass
import warnings
warnings.warn = warn
##%%
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X[0:15],y_labels[0:15])
y_test_tree=clf.predict(X[15:])
##%%
print('Kmeans Evaluation')
confusion_matrix(y_labels,kmeans.labels_)
accuracy_score(y_labels,kmeans.labels_)
f1_score(y_labels,kmeans.labels_,average='macro')
precision_score(y_labels,kmeans.labels_,average='macro')
recall_score(y_labels,kmeans.labels_,average='macro')
hamming_loss(y_labels,kmeans.labels_)
##%%
print('Naive bayes Evaluation')
confusion_matrix(y_labels[15:],y_test_gauss)
accuracy_score(y_labels[15:],y_test_gauss)
f1_score(y_labels[15:],y_test_gauss,average='macro')
precision_score(y_labels[15:],y_test_gauss,average='macro')
recall_score(y_labels[15:],y_test_gauss,average='macro')
hamming_loss(y_labels[15:],y_test_gauss)
##%%
print('Decision Tree Classificaiton Evaluation')
confusion_matrix(y_labels[15:],y_test_tree)
accuracy_score(y_labels[15:],y_test_tree)
f1_score(y_labels[15:],y_test_tree,average='macro')
precision_score(y_labels[15:],y_test_tree,average='macro')
recall_score(y_labels[15:],y_test_tree,average='macro')
hamming_loss(y_labels[15:],y_test_tree)
