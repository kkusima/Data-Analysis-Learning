#!/usr/bin/env python
# coding: utf-8

# <h1 style='text-align: center;font-size:19px;'> Exploring the Post Engagement per Hour at HackerNews </h1>
# 
# <p style='text-align: center;font-size:17px;'> <i><b> Author : Kenneth Lucas Kusima <br> Attributor: DataQuest </b> </i> </p>
# 
# ## Project Origin:
# <p style='text-align: justify;'> $\hspace{10 mm}$This project was made per instructions from: </p> 
#        
# <center> $\textbf{The DataQuest Course: Python for Data Science Intermediate}$</center>

# ## Objectives:
# 
# We're specifically interested in posts whose titles begin with either Ask HN or Show HN. Users submit Ask HN posts to ask the Hacker News community a specific question. Likewise, users submit Show HN posts to show the Hacker News community a project, product, or just generally something interesting
# 
# We'll compare these two types of posts to determine the following:
# 
# - Do Ask HN or Show HN receive more comments on average?
# - Do posts created at a certain time receive more comments on average?
# 
# 

# In[78]:


from csv import reader
opened_file = open('hacker_news.csv')
read_file = reader(opened_file)
hn = list(read_file)
print('The first 5 rows of the dataset being used: \n')
print(hn[0:5])


# In[79]:


#Extracting the headers of the dataset
headers = hn[0]
hn = hn[1:]
print('The header : \n')
print(headers)
print('\n The first 5 rows of the dataset being used - excluding the header: \n')
print(hn[0:5])


# ## Filtering the data
# 
# ### Filtering posts according to Ask HN, Show HN and other posts:

# In[80]:


#initializing the separate lists correpsonding to the different types of posts
ask_posts = []
show_posts = []
other_posts = []

for row in hn:
    title = row[1]
    if title.lower().startswith('ask hn'): #filetering out only the lower versions of the titles that start with ..ask.
        ask_posts.append(row)
    elif title.lower().startswith('show hn'):
        show_posts.append(row)
    else:
        other_posts.append(row)
        
print('Numnber of "Ask HN" posts:', len(ask_posts))
print('Numnber of "Show HN" posts:',len(show_posts))
print('Numnber of other types of posts:',len(other_posts))

print('\n The first five rows of the ask_posts list: \n')
print(ask_posts[0:5])

print('\n The first five rows of the show_posts list: \n')
print(show_posts[0:5])


# ## Analysing the number of comments

# In[81]:


total_ask_comments = 0
for row in ask_posts:
    num_comments = int(row[4])
    total_ask_comments = total_ask_comments + num_comments
avg_ask_comments = total_ask_comments / len(ask_posts)
print('Average number of comments for the "Ask HN" posts:', avg_ask_comments)

total_show_comments = 0
for rows in show_posts:
    num_comments_ = int(rows[4])
    total_show_comments = total_show_comments + num_comments_
avg_show_comments = total_show_comments / len(show_posts)
print('Average number of comments for the "Show HN" posts:',avg_show_comments)


# From the results above we can see that the "Ask HN" posts have on average, more comments per post compared to the "Show HN" posts

# ## Analysing  which posting times attract the most comments
# 
# Since asks posts produce the most comments on average, analysis will be focused for these kinds of posts 
# 
# ###           Isolating the number of posts created in each hour and the correscponding comments generated

# In[86]:


#Calculating the amount of ask posts created per hour, along with the total amount of comments

import datetime as dt
result_list = []

for row in ask_posts:
    created_at = row[6]
    num_coments = int(row[4])
    result_list.append([created_at , num_coments])
    
counts_by_hour = {}
comments_by_hour = {}

for row in result_list:
    ob = row[0]
    comm = row[1]
    date_time = dt.datetime.strptime(ob,"%m/%d/%Y %H:%M")
    hour_ = date_time.strftime('%H')
    if hour_ not in counts_by_hour:
        counts_by_hour[hour_] = 1
        comments_by_hour[hour_] = comm
    else:
        counts_by_hour[hour_] += 1
        comments_by_hour[hour_] = comments_by_hour[hour_] + comm
    
print('Number of "Ask HN" posts created for each hour: \n', counts_by_hour)
print('\n Corresponding total number of comments "Ask HN" posts created at each hour received: \n',comments_by_hour)
    


# ###           Calculating the average number comments per posts for each hour

# In[87]:


avg_by_hour = []

for row in comments_by_hour:
    avg_by_hour.append([row, comments_by_hour[row]/counts_by_hour[row]])
    
print(avg_by_hour)


# Ordering the above list based on highest number of comments per post per hour:
# 

# In[100]:


swap_avg_by_hour = []

for row in avg_by_hour:
    element_1 = row[1]
    element_2 = row[0]
    swap_avg_by_hour.append([element_1,element_2])

#Sorting by the average number of comments
sorted_swap = sorted(swap_avg_by_hour,reverse = True)
#print(sorted_swap)  

print(' \n Top 5 Hours for "Ask HN" Posts Comments: \n')
for val in sorted_swap[0:5]:
    template = "{hour}:00: {num:.2f} average comments per post"
    result = template.format(hour = val[1], num = val[0])
    print(result)
    

