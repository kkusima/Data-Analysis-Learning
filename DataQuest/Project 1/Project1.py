#!/usr/bin/env python
# coding: utf-8

# <h1 style='text-align: center;font-size:19px;'> Application Analysis to Determine a Profitable New Application for both Google Play and Apple App Stores </h1>
# <p style='text-align: center;font-size:17px;'> <i><b> Author : Kenneth Lucas Kusima <br> Attributor: DataQuest </b> </i> </p>
# 
# ## 1. Project Origin:
# <p style='text-align: justify;'> $\hspace{10 mm}$This project was made per instructions from: </p> 
#        
# <center> $\textbf{The DataQuest Course: Python for Data Science Fundamentals}$</center>
# 
# ## 2. Objective:
# <p style='text-align: justify;'> $\hspace{5 mm}$ For this project, I pretend I am working as a data analyst for a company that builds Android and iOS mobile applications (apps). They make apps available both on Google Play and the App Store. </p>
# <p style='text-align: justify;'> $\hspace{5 mm}$ The company only build apps that are free to download and install, and the main source of revenue consists of in-app ads. This means that different companies can pay to have their ads appear in various parts of the application. This means that revenue for any given app is mostly influenced by the number of users who use the app — the more users that see and engage with the ads, the better. <b> My goal for this project is to analyze application data and assist the company developers understand what type of apps are likely to attract more users. </b> </p>
# 
# After identifying and analysing the most attractive application types, the company hopes to follow the strategy outlined in the following steps: 
# 
# - Use results from the analysis to generate a minimal Android version of the "perfect" app and add it to the Google Play Store. 
# - Asses and monitor the application's user response and further develop the app if good ratings are recieved.
# - After six month, if substantial profit is seen, build an iOS version of the app and add it to the Apple App Store.
# 

# ## 3. Dataset Definition:
# <p style='text-align: justify;'> $\hspace{5 mm}$ According to Statista, in 2018, there were approximately 2 million iOS apps on the App Store and 2.1 million Andorid apps on the Google Play Store. Analysing data from more than 4 million apps across the Google Play and iOS App Stores. As a result, DataQuest offers data sets that encapsulate a select group of applications to which significant analysis can be conducted. Android apps data set holds data on approximately 10,000 Android apps collected in August 2018 from Google Play. Moreover, the data set for iOS Apps contains about 7,000 iOS apps collected in July 2017 from the App Store. </p> 
# 
# <p style='text-align: center;'> <b> Table 1: Summary of Datasets to be used <b> </p>
# 
# | Dataset          | Location          | Collection Date | Number of Apps  |
# | :---:            |    :----:         |          :---:  |         :---:   |
# | Android apps     | Google Play Store | August 2018     | 10,841          |
# | iOS apps         | Apple App Store   | July 2017       | 7,197           |

# ## 4. Exploring the Datasets:

# In[1]:


from csv import reader

#Apple Store Dataset
opened_file_1 = open('AppleStore.csv')
read_file_1 = reader(opened_file_1)
ios_apps_data = list(read_file_1)

#Google Play Store Dataset
opened_file_2 = open('googleplaystore.csv')
read_file_2 = reader(opened_file_2)
android_apps_data = list(read_file_2)

#Function for exploring the datasets inputed
def explore_data(dataset, start, end, rows_and_columns=False):
    dataset_slice = dataset[start:end]    
    for row in dataset_slice:
        print(row)
        print('\n') # adds a new (empty) line after each row

    if rows_and_columns:
        print('Number of rows:', len(dataset))
        print('Number of columns:', len(dataset[0]))
        print('\n')

        
#Exploring the Apple Store Dataset:
print('The First 2 rows of iOS App dataset: \n')
explore_data(ios_apps_data,0,2,True)

#Exploring the Google Play Store Dataset:
print('The First 2 rows of Android dataset: \n')
explore_data(android_apps_data,0,2,True)


# <p style='text-align: justify;'> $\hspace{5 mm}$ In obtaining the first few rows of the two datasets, as see in the results above, a deeper understanding of the specific data entry types  can be obtained . This can then be used to provide the basis and direction of our analysis. Looking at the column headers allows us to pick the appropriate data entries to focus on in comparing, contrasting and discovering trends between the two datasets. A full view of the data recorded in the two datasets can be found in the links below: </p>
#  
# Apple App Store    (iOS Apps)     : https://dq-content.s3.amazonaws.com/350/AppleStore.csv
# 
# Google Play Store  (Android Apps) : https://dq-content.s3.amazonaws.com/350/googleplaystore.csv
#  
# 
# ###  $\hspace{8 mm}$  <i> 4.1 Column Header Analysis: </i>
# $\hspace{5 mm}$In looking at the column headers of the two data sets, similar columns that appear beneficial for different future analysis may be summarised:
#  
# <p style='text-align: center;'> <b> Table 2: List of significant column headers guiding the type of data anlaysis to follow <b> </p>
# 
# | iOS Apps headers | <i> Column </i>   |Android Apps headers|<i> Column </i>|
# | :---:            |    :----:         |    :----:         |     :----:    |    
# | Track name       |    2              | App               |    1          |
# | size_bytes       |    3              | Size              |    2          | 
# | price            |    5              | Price             |    8          | 
# | cont_rating      |    11             | Content Rating    |    9          | 
# | prime_genre      |    12             | Genres            |    10         |       
# | user_rating      |    8              | Rating            |    3          |           
# 

# ## 5. Data Cleaning:
# 
# <p style='text-align: justify;'> $\hspace{5 mm}$ Inorder to provide accurate results, accurate data is needed. Consequently, data cleaning conducted before analysis provides assurance that results obtained would be free of human errors such as duplicates, typos and irrelevant data. The cleaning is done by removing or correcting wrong data, removing duplicate data and modifying the data so as to fit the purpose of the analysis. </p>
# 
# ###  $\hspace{8 mm}$  <i> 5.1 Detecting and Deleting Wrong Data: </i>
# 
# <p style='text-align: justify;'> $\hspace{5 mm}$ The google play dataset has been reported to have errors in a certain row. The entry (row 10,472) has been addressed to have "missing 'Rating' and a column shift happened for next columns". Since there are 10,842 apps, deleting this erroneous application entry would not provide much issues. </p>

# In[2]:


#Inspecting the suscpicious rows
for row in android_apps_data[10472:10475]:
        print(row)
        print('\n') # adds a new (empty) line after each row


# <p style='text-align: justify;'> $\hspace{5 mm} $
# It is evident that the entry for the Android application <b> 'Life Made WI-Fi Touchscreen Photo Frame'</b> (i.e. the row corresponding to android_apps_data[10473]) is erroneous. There appears to be missing data points. This application entry is therefore deleted as follows. </p>
# 

# In[3]:


#Deleting the erroneous row
del android_apps_data[10473]

#Validation
for row in android_apps_data[10472:10475]:
        print(row)
        print('\n') # adds a new (empty) line after each row


# ###  $\hspace{8 mm}$  <i> 5.2 Clearing Out Duplicates: </i>
# 
# <p style = 'text-align ; justify ;'> $\hspace{0.5mm}$ 
# Duplicates may result in an overestimation or underestimation of results. This is therefore need to investigate and correct for any repeated entries. </p>
# 
# ##### $\hspace{9 mm}$ 5.2.1 Explorinng the Duplicated Andorid Apps:
# 

# In[4]:


#Checking for duplicates in android dataset:
duplicate_apps_android = []  #Empty list for duplicate apps
unique_apps_android = []     #Empty list for unique apps

for app_android in android_apps_data:       #Extracting rows from the android dataset
    name_android = app_android[0]           #Isolating based on similar App name (i.e column 0 from dataset)
    if name_android in unique_apps_android: #Keeping track of duplicates
        duplicate_apps_android.append(name_android)
    else:
            unique_apps_android.append(name_android) #Isolating Unique entries
            
print('Number of duplicate android apps:', len(duplicate_apps_android))
print('\n')
print('Examples of duplicate android apps:', duplicate_apps_android[:10] )


# In[5]:


#Exploring a few of the duplicates from the android dataset
print('Few duplicate data entrys in the android dataset: \n')

for app_android in android_apps_data:                
    name_android = app_android[0]    
    if name_android == 'Box':
        print(app_android)
    if name_android == 'Instagram':
        print(app_android)


# The presence of 1181 duplicates pose a significant threat to the accuracy of further analysis. These duplicates need to be removed and this is done in the sections further below.

# ##### $\hspace{9 mm}$ 5.2.2 Explorinng the Duplicated iOS Apps:
# Similarly for the iOS app dataset,

# In[6]:


#Checking for duplicates in iOS dataset:
duplicate_apps_ios = []       #Empty list for duplicate apps
unique_apps_ios = []          #Empty list for unique apps

for app_ios in ios_apps_data[1:]:                #Extracting rows from the iOS dataset
    name_ios = app_ios[0]                    #Isolating based on similar App name (i.e column 0 from dataset)
    if name_ios in unique_apps_ios:          #Keeping track of duplicates
        duplicate_apps_ios.append(name_ios)
    else:
            unique_apps_ios.append(name_ios) #Isolating Unique entries
            
print('Number of duplicate iOS apps:', len(duplicate_apps_ios))
print('\n')
print('Examples of duplicate iOS apps:', duplicate_apps_ios[:40] )


# There appears to be no duplicate apps in the iOS app dataset.

# ##### $\hspace{9 mm}$ 5.2.3 Removing the Duplicated Andorid Apps:
# <p style = 'text-align ; justify ;'> $\hspace{0.5 mm}$  To remove duplicated data entries in the two application datasets, there needs to be a criteria to which only one of the entries is chosen out of the different duplicates. For the duplicated andorid apps, it can be found that a main difference among the duplicates is the number of reviews (the fourth column). They indicate that the duplicates were recorded at different times where the ones with the most reviews happen to be the most up to date entries. Consequently, to remove the android app duplicates, instead of randomly choosing applications to remove, focus is made to keep only the most up to date entry duplicate, that is, the (duplicated) row with the highest number of reviews. </p>
# 
# 

# In[7]:


reviews_max = {} #Dictionaty to contain unique apps and the corresponding (max) number of reviews
for rows in android_apps_data[1:]:
    name = rows[0]  #Isolating the name of every row entry
    n_reviews = float(rows[3])  #Isolating the reviews of the app entry

    if name in reviews_max and reviews_max[name] < n_reviews:
        reviews_max[name] = n_reviews
        
    if name not in reviews_max:
        reviews_max[name] = n_reviews


# To validate that the duplicated entries have been removed, the inspection below can be done:

# In[8]:


print('Expected length:', len(android_apps_data[1:]) - 1181)
print('Actual length:', len(reviews_max))


# ###### $\hspace{9 mm}$ 5.2.3.1 Isolating the non-duplicated andorid apps:
# 
# <p style = 'text-align ; justify ;'> $\hspace{0.5 mm}$ The dictionary : <b> 'reviews_max' </b> now holds both the non-duplicated android applications and the corresponding ratings. This can then be used to create a new dataset of android apps with non_duplicates, named, <b> 'android_apps_data_clean' </b> . Another list <b> ('already_added_android')</b> can also be made to contain the names of all the apps in this new dataset. </p>

# In[9]:


android_apps_data_clean = []
already_added_android = []

for rows in android_apps_data[1:]:
    name = rows[0]
    n_reviews = float(rows[3])
    
    if (reviews_max[name] == n_reviews) and (name not in already_added_android):
        android_apps_data_clean.append(rows)
        already_added_android.append(name)

explore_data(android_apps_data_clean, 0, 3, True) #Showing the final duplicate free android app dataset


# ###  $\hspace{8 mm}$  <i> 5.3. Removing Non-English Apps </i>
# 

# <p style = 'text-align ; justify ;'> $\hspace{0.5 mm}$ Our Company only uses English for the apps being developed therefore it is in our interest to remove any non-English applications in the datasets. The apps are filtered to only include those directed for an English-speaking audience.  </p>
# 
# <p style = 'text-align ; justify;'> $\hspace{0.5 mm}$
# The English language utilises characters which correspond to numbers that fall in the range 0 to 127 (i.e the ASCII range) . The corresponding number assigned to the different character can be found using the function <b> 'ord(  )' </b>. Hence, in order to distinguish the english applications, the function below filters the string input and checks if each character belongs in the ASCII range. All other characters and symbols (including chinese characters and emojis) fall outside of this range. As a result, to account for those english apps that have few non-english characters in their name, a maximum of 3 non-english characters is allowed in the characterisation of english applications. This means that any application with more than 3 characters not in the ASCII range will be considered non-English </p>

# In[10]:


def English_app(string):
    count = 0
    for char in string:
        val = (ord(char))
        if val > 127:
            count +=1
            if count > 3 :
                return False
        
    return True


# ##### $\hspace{9 mm}$ 5.3.1 Removing Non-English Andorid Apps:

# In[11]:


android_apps_english_data = []
for row in android_apps_data_clean:
    name = row[0]
    if English_app(name):
        android_apps_english_data.append(row)
        
explore_data(android_apps_english_data,0,3)
print('Number of English Android Apps:',len(android_apps_english_data))


# ##### $\hspace{9 mm}$ 5.3.2 Removing Non-English iOS Apps:

# In[12]:


iOS_apps_english_data = []
for row in ios_apps_data[1:]:
    name = row[1]
    if English_app(name):
        iOS_apps_english_data.append(row)
        
explore_data(iOS_apps_english_data,0,3)
print('Number of English iOS Apps:',len(iOS_apps_english_data))


# ###  $\hspace{8 mm}$  <i> 5.4. Separating the Free apps </i>
# 

# <p style = 'text-align ; justify;'> $\hspace{0.5 mm}$ Since the company's source of revenue is through in-app purchases, the applications developed are free applications. It is therefore critical to filter the datsets to include only free apps. </p> 

# In[13]:


Android_dataset = []
iOS_dataset = []

for rows in android_apps_english_data:
    price = rows[7]
    if price == '0':
        Android_dataset.append(rows)
        
for rows in iOS_apps_english_data:
    prices = rows[4]
    if prices == '0.0':
        iOS_dataset.append(rows)    

print('Actual Number of Android apps being developed:', len(Android_dataset))
print('Actual Number of iOS apps being developed:',len(iOS_dataset))


# ## 6. Data Analysis:

# <p style = 'text-align ; justify;'> $\hspace{0.5 mm}$ Since the end goal is to find the most attractive app and add it to both the Google Play Store and the Apple App Store, the app profile being looked for should be profitable in both markets. </p>
# 
# <p style = 'text-align ; justify;'> $\hspace{0.5 mm}$ To start the analysis, we will begin by getting a investigating what the most common genres for each market are. To do so, frequency tables are generated to see which the most prominent genres were. For android apps, the genres are listed in 'Genre' and 'Category' columns in the Android datasets and for iOS apps, the genres are listed in the 'prime_genre' columns in the iOS App Store datasets. </p>

# ###  $\hspace{8 mm}$  <i> 6.1 Application Frequency by Genre : </i>
# 
# <p style = 'text-align ; justify;'> $\hspace{0.5 mm}$ Below is the analysis of the most common free English applications in the Android Google Play and Apple App Stores. To do this, two functions are implemented: </p>
# - <b> Function 1: 'freq_table' : </b> To create genre based frequency tables showing the percentages
# - <b> Function 2: 'display_table' : </b> To reorder the variables and values in the frequency table from Function 1 to show the most common applications in the different app stores in descending order.

# In[14]:


def freq_table(dataset,index):
    tables = {}
    totaling = 0
    
    for row in dataset:
        totaling +=1
        values = row[index]
        
        if values in tables:
            tables[values] +=1
        else:
            tables[values] = 1
            
        table_percentage = {}
        
        for keys in tables:
            percents = (tables[keys] / totaling) * 100
            table_percentage[keys] = percents
            
    return table_percentage

    
def display_table(dataset, index):
    table = freq_table(dataset, index)
    table_display = []
    for key in table:
        key_val_as_tuple = (table[key], key)
        table_display.append(key_val_as_tuple)
        
    table_sorted = sorted(table_display, reverse = True)
    for entry in table_sorted:
        print(entry[1], ':', entry[0])
        


# ##### $\hspace{9 mm}$ 6.1.1 Most Common Free English Applications in the iOS datsets by Genre:
# 
# <p style = 'text-align ; justify;'> $\hspace{0.5 mm}$  Analysing the frequency table for the prime_genre column of the App Store data set. </p>

# In[15]:


display_table(iOS_dataset, 11) #prime_genre


# <p style = 'text-align ; justify;'> $\hspace{0.5 mm}$  From the frequency tables above, the top five most common free English application genres can be summarised as: </p>
# 
# 
# <p style='text-align: center;'> <b> Table 3: List of top five most common free English applications in the Apple App Store. <b> </p>
# 
# |Common Free English iOS Application | Percentage   |
# | :---:            |    :----:          |     
# |Games             |    58.16%          | 
# |Entertainment     |    7.88%           |
# |Photo & Video     |    4.96%           | 
# |Education         |    3.66%           | 
# |Social Networking |    3.29%           | 
# 
# 

# <p style = 'text-align ; justify;'> $\hspace{0.5 mm}$ From the data above it can be seen that the more social and entertaining applications like 'Games, Entertainment and Photo&Video' have a bigger prescence in the Apple Store amongst all the free english applications in the store. Despite there seems to be a larger offering of these application, this does not necessarily imply that these apps have the most demand and the highest number of users. </p> 

# ##### $\hspace{9 mm}$ 6.1.2 Most Common Free English Applications in the Android datsets by Genre:
# 
# <p style = 'text-align ; justify;'> $\hspace{0.5 mm}$  Analysing the frequency table for the 'Genre' and 'Categories' column of the Android Google Play Store data set. </p>
# 
# ###### $\hspace{20 mm}$ As Per Category Column of the Android Dataset

# In[16]:


display_table(Android_dataset, 1) # Category


# <p style = 'text-align ; justify;'> $\hspace{0.5 mm}$ Unlike the Apple Store dataset, there seems to a higher number of utilitarian and practical applications out of all the free English applications in the Android Google Play Store and can be summarised as seen in the table below.
# 
# 
# <p style='text-align: center;'> <b> Table 4: List of top five most common free English applications in the Google Play Store as per the Genres column. <b> </p>
# 
# |Common Free English Android Application | Percentage   |
# | :---:       |    :----:          |     
# |FAMILY       |    18.91%          | 
# |GAME         |    9.72%           |
# |TOOLS        |    8.46%           | 
# |BUSINESS     |    4.59%           | 
# |LIFESTYLE    |    3.90%           | 
# 
# 
# 

# ###### $\hspace{20 mm}$ As Per Genres Column of the Android Dataset

# In[17]:


display_table(Android_dataset, 9) #Genres


# 
# <p style = 'text-align ; justify;'> $\hspace{0.5 mm}$ It can be seen that the 'Category' column has more applications, with more variety in comparison to the 'Genres' column. The relation between the two columns is unclear, however due to the increased variety, the Category column will be used as the column corresponding to the android application genres and then to be compared with the prie_genre column in the Apple App Store. As seen from the Genres column, the most common applications have a wider range, with more of them offering a practical purpose. The top five most common free english applications as per the category column can be summarised by the table below:
# 
# <p style='text-align: center;'> <b> Table 5: List of top five most common free English applications in the Google Play Store as per the Category column. </b> </p>
# 
# |Common Free English Android Application |  Percentage of Android Apps   |
# | :---:       |    :----:          |     
# |Tools        |    8.45%           | 
# |Entertainment|    6.07%           |
# |Education    |    5.35%           | 
# |Business     |    4.59%           | 
# |Productivity |    3.89%           | 
# 
# 
# 
# 

# Similarly, the commonality of the most frequent genres in the Google Play Store do not correspond to the most in-demand/ most popular applications with the highest number of users.

# ###  $\hspace{8 mm}$  <i> 6.2 Popular Applications by Genre : </i>
# 
# <p style = 'text-align ; justify;'> $\hspace{0.5 mm}$ A good way of determing which of the most in-demand applications is to analyse the number of installs, that is, how many times the applications were installed. The more installs an application has, the more popular it is. Since the data regarding the number of installs of an app is unavailable in the Apple App Store dataset, a work around implemented is to use the number of user ratings as a proxy. Focus then becomes to represent the average number of ratings for each app as a measure of popularity </p>

# ##### $\hspace{9 mm}$ 6.2.1 Most Popular Free English Applications in the iOS datsets by Genre:
# 
# Since the App Store datasets has no number of installs recorded, the ratings are used to analyse which application genre are the most popular. To do so, we 
# - Isolate the apps of each genre.
# - Sum up the user ratings for the apps of that genre.
# - Divide the sum by the number of apps belonging to that genre (not by the total number of apps).

# In[18]:


list_iOS = freq_table(iOS_dataset,11) #prime_genre frequency table
for genre in list_iOS:
    total = 0
    len_genre = 0
    for row in iOS_dataset:
        genre_app = row[11]
        if genre_app == genre:
            rating = float(row[5])
            total += rating
            len_genre += 1
        
    avg_rating = total/len_genre
    print(genre, ':' , avg_rating)


# <p style='text-align: center;'> <b> Table 6: List of top five most popular free English applications in the iOS App Store as per the highest average number of ratings. </b> </p>
#     
# |Order |Popular iOS Application Genre|  Average Rating    |
# | :---:       | :---:       |    :----:          |     
# |1  |Navigation            |    86090           | 
# |2  |References            |    74942           |
# |3  |Social Networking     |    71548           | 
# |4  |Music                 |    57326           | 
# |5  |Weather               |    52280           | 
# 
# 
# <p style='text-align: justify;'> $\hspace{5 mm}$  From data above, the Navigation genre recieves the most ratings (86090 ratings) and appears to be the most popular in the iOS application store based on our criteria. This result however may prove misleading. This app is followed by 'References' (74942 ratings), 'Social Networking' (71548 ratings) and 'Music' (57326 ratings) applications. Out of the many applications in each genre, there may be a few applications responsible for the high number of ratings. Further analysis is done to support this: </p>

# In[19]:


print('Popular apps in the Navigation genre:')
print('Average ratings : 86090 \n')
for app in iOS_dataset:
    if app[-5] == 'Navigation':
        print(app[1], ':', app[5]) # print name and number of ratings

print('\nPopular apps in the Reference genre:')
print('Average ratings : 74942 \n')
count = 0
for app in iOS_dataset:
    if app[-5] == 'Reference' and count < 6:
        print(app[1], ':', app[5]) # print name and number of ratings
        count +=1
        
print('\nPopular apps in the Social Networking genre:')
print('Average ratings : 71548 \n')
count = 0
for app in iOS_dataset:
    if app[-5] == 'Social Networking' and count <6:
        print(app[1], ':', app[5]) # print name and number of ratings
        count +=1


# <p style='text-align: justify;'> $\hspace{5 mm}$ By analysing the individual ratings of the more popular applications, we can see that there are few giant apps whose presence dominates the specific genre group and in turn lead to the genre seeming more popular than it really easy as per our criteria. Consequently,the average number of ratings seem to be skewed by a few apps which have hundreds of thousands of user ratings, while the other apps may struggle to get past the 10,000 threshold.  </p>

# <p style='text-align: justify;'> $\hspace{5 mm}$ From the data above, the application genre that shows a potential for popularity is that which would incooperate the top 5 genres shown in Table 6. Nevertheless, despite their popularity, applications in the genres Navigation and weather are not known to have great retention. Usability of these applications do not foster and advocate for exploration and discovery hence proving less likely to be good hosts of in-app purchases(the model to which our company makes the most profit). </p>
# 
# <p style='text-align: justify;'> $\hspace{5 mm}$ Consequently, an application I would recommend is that rooted under the References genre. An application that would allow users to access different books as well as corresponding video content, in a way that allows for the sharing of thoughts and ideas regarding the books. Furthermore, this application would include cook books and tutorials that foster reading skills and allow for the building of imagination as well as practical skills.   </p>

# ##### $\hspace{9 mm}$ 6.2.2 Most Popular Free English Applications in the Android datsets by Genre:
# 
# <p style='text-align: justify;'> $\hspace{5 mm}$ This dataset includes disting number of installs, thus allowing us to know the exact number of people who installed the applications. However, the data entries are mostly estimates (eg. 1,000+) and so data cleaning is done below to assure better precision is achieved. The obtained number of ratings are then cleaned for each application and the average number of ratings is obtained for each application genre. </p>

# In[20]:


Names = freq_table(Android_dataset, 1)

for row in Names:
    total = 0
    length = 0
    for app in Android_dataset:
        category = app[1]
        if category == row:            
            installs = app[5]
            installs = installs.replace(',', '')
            installs = installs.replace('+', '')
            total += float(installs)
            length += 1
    avg_installs = total / length
    print(row, ':', avg_installs)


# <p style='text-align: center;'> <b> Table 7: List of top eleven most popular free English applications in the Google Play Store as per the highest average number of installs. </b> </p>
# 
# |Order |Popular Android Application Genre|  Average Number of Installations    |
# | :---:       | :---:       |    :----:          |     
# |1  |COMMUNICATION            |    38,456,119           |
# |2  |VIDEO_PLAYERS            |    24,727,872           |
# |3  |SOCIAL                   |    23,253,652           |
# |4  |PHOTOGRAPHY              |    17,840,110           |
# |5  |PRODUCTIVITY             |    16,787,331           |
# |6  |GAME                     |    15,588,016           |
# |7  |TRAVEL_AND_LOCAL         |    13,984,078           |
# |8  |ENTERTAINMENT            |    11,640,705           | 
# |9  |TOOLS                    |    10,801,391           |
# |10  |NEWS_AND_MAGAZINES       |    9,549,178            |
# |11  |BOOKS_AND_REFERENCE      |    8,767,812            | 
# 

# In[21]:


print('\nPopular apps in the COMMUNICATION genre:')
print('Average Installs : 38,456,119 \n')
count = 0
for app in Android_dataset:
    if app[1] == 'COMMUNICATION' and count < 6:
        print(app[0], ':', app[5]) # print name and number of ratings
        count +=1
        
print('\nPopular apps in the VIDEO_PLAYERS genre:')
print('Average Installs : 24,727,872 \n')
count = 0
for app in Android_dataset:
    if app[1] == 'VIDEO_PLAYERS' and count <6:
        print(app[0], ':', app[5]) # print name and number of ratings
        count +=1

print('\nPopular apps in the BOOKS_AND_REFERENCE genre:')
print('Average Installs : 8,767,812 \n')
count = 0
for app in Android_dataset:
    if app[1] == 'BOOKS_AND_REFERENCE' and count <6:
        print(app[0], ':', app[5]) # print name and number of ratings
        count +=1


# <p style='text-align: justify;'> $\hspace{5 mm}$ As seen in the data above, similar to the iOS applications application dataset, there appears to be few applications in the popular genres that have a many more ratings than the rest and hence causing the entire corresponding genre to appear more prominent. Moreover, the data also shows that the application suggested in section 6.2.1 would have a positive result here. The book application explained would have features that touch on the popluar applications genres. (Specifically 1, 2, 3, 5, 11) </p> 
# 
#  - <b> 1. Communications: </b> Ideally the book application would allow for virtual book clubs to be formed where people could meet via video conference calls e.t.c, to discuss various books and articles.
#  
#  - <b> 2. Video Player: </b>The application would have video player accessibility where people could post video content regarding books and articles. Content could range from tutorials to various book analysis.
#  
#  - <b> 3. Social:</b> The application would have options of connection, were people could post about their readings, their discoveries, their learning experience e.t.c
# 
# - <b> 5. Productivity: </b> This app would allow for project creation, where each project can allow for corresponding books and video contents could be collected and used as a tools for efficient learning and/or research.
# 
# - <b> 11. Books and References: </b> The propose book applictaion would result in housing a collection of different books and reference materials for users of all ages. 

# ## 7. Conclusions:
# <p style='text-align: justify;'> $\hspace{5 mm}$ The project successfuly analysed mobile phone application datasets from both Google Play Store and Apple App Stores. This was to deduce an application genre that would prove profitable in both Google Play Store and Apple App Store, where primary mode of profit is through in-app purchases. Datasets were cleaned to include only free, English-based applications. The likelihood of the applications to be installed (Application Popularity) was assesed using average number of ratings per genre in the Google Play Store dataset and the average number of installs per genre in the Apple App Store dataset. </p>
# 
# <p style='text-align: justify;'> $\hspace{5 mm}$ The resulting application genre chosen was that of a book/reference application with video content capabilities and with the intention of fostering a social environment. The application could be used as a means to learn new skills (through books and video tutorials) or simply to have exciting discussions 'book clubs' through virtual means such as video conferencing. </p>

# In[ ]:




