# Title

Anomaly Detection Project

# Goals

Explore the curriculum access data to answer various questions

I will also deliver the following:
- An email that answers each question
- A Jupyter Notebook that documents my process of answering the questions from start to finish
- A Google slide that summarizes the most important findings of the project

# Data Dictionary

cohort_id: A number that corresponds to a specific cohort (Ex. Darden = cohort_id 59)

datetime: The date and time that a specific log entry was recorded

end_date: The date that a cohort ended

ip: The IP of the user who generated the entry

name: The name of a cohort

page_viewed: The page that a user viewed 

program_id: Indicates wether a user is part of the data science or web development program

start_date: The date that a cohort started

user_id: The id of a specific user

# Initial Thoughts

How will I be able to tell if web scraping occured?

I should split up the data between data science and web development to make it easier to explore them separately.

I can use the alumni page to help gather information about cohorts

# Project Plan

1. Acquire
    - Acquire log data and cohort data from provided files

2. Prep
    - Prep data as necessary for exploration
        - Combine data from provided files
        - Change data types as needed (especially dates to datetime)
        - Rename columns as needed
        - Set datetime as index to make filtering easier
        - Address null values
        - Split the data into web development and data science data frames
        - Any other changes as needed

3. Exploration
- Q1. Which lesson appears to attract the most traffic consistently across cohorts (per program)?
    - Find average views of each lesson per cohort
    - Identify lesson with highest amount of average views per cohort

- Q2. Is there a cohort that referred to a lesson significantly more that other cohorts seemed to gloss over?
    - Plot each lessons page views per cohort and look for a lesson that one cohort viewed significantly more than the other cohorts

- Q3. Are there students who, when active, hardly access the curriculum? If so, what information do you have about these students? 
    - Filter data to only display log entries that were created by a user while their cohort was active
    - Sum the amount of total page views and identify users with the lowest counts

- Q4. Is there any suspicious activity, such as users/machines/etc accessing the curriculum who shouldn’t be? Does it appear that any web-scraping is happening? Are there any suspicious IP addresses? Any odd user-agents? 
    - Identify users who have used a large amount of different IP addresses and have never had a program id assigned to them
    - Research those users in-depth to see if more suspicious activity is present
    - Use anomaly detection to find cases where a high amount of hourly web page hits were generated
    - Research the users who generated the high amount of page hits to see if more suspicious activity exists

- Q5. At some point in the last year, ability for students and alumni to cross-access curriculum (web dev to ds, ds to web dev) should have been shut off. Do you see any evidence of that happening? Did it happen before? 
    - Filter the separate program data frames for rows where the page_viewed value includes a lesson key word from the other program
        - Example: Filter the data science dataframe for page_viewed values containing "java"
    - Find the earliest and latest dates of these instances in each data frame to determing if they occured within the last year or prior

- Q6. What topics are grads continuing to reference after graduation and into their jobs (for each program)? 
    - Filter data to only show log entries that were created by users on dates past their cohort end date
    - Sum the amount of views that these pages received 
    - Identify pages with highest amount of view post-graduation

- Q7. Which lessons are least accessed? 
    - Sum the amount of views that each major lesson has received
    - Identify the lessons with the lowest counts
        - I have to approach this differently than looking for lessons with the highest amount of views since there will be probably
        be a lot more pages that have minimal view counts than those that are near the most view counts

- Q8. Anything else I should be aware of? 
    - While answering the other question, keep note of any peculiar or interesting findings so that I can present them for this question

4. Conclusion
    - Document the following
        - Most important takeaways
        - Overall conclusion

# How to Reproduce

- Download the source files to your local directory 
- Install acquire.py and prepare.py into your working directory
- Run the jupyter notebook

# Key Findings and Takeaways

## Key Findings and Takeaways

### Q1 - Which lesson appears to attract the most traffic consistently across cohorts (per program)?

The most visited lesson page on average across all __web development__ cohorts is Javascript-I.

The most visited lesson page on average across all __data science__ cohorts is Fundamentals - Intro to Data Science.

### Q2 - Is there a cohort that referred to a lesson significantly more that other cohorts seemed to gloss over? 

For __web development__, I was not able to identify any lessons that one single cohort viewed significantly more than all others. Every lesson that was referred to significantly was referred to by multiple cohorts, not just one.

For __data science__, Curie visited the SQL overview page roughly 300 more times than Darden or Bayes. Similarly, Darden visited the classification overview page roughly 600 more times than Curie or Bayes.

### Q3 - Are there students who, when active, hardly access the curriculum? If so, what information do you have about these students? 

For __web development__, 3 users were identified who all accessed the curriculum 5 times or less while their cohorts were active.

For __data science__, 3 users were identified who all accessed the curriculum 17 or less times while their cohorts were active.

### Q4 - Is there any suspicious activity, such as users/machines/etc accessing the curriculum who shouldn’t be? Does it appear that any web-scraping is happening? Are there any suspicious IP addresses? Any odd user-agents? 

__Identified odd user-agent, user 111__
- User accessed curriculum for roughly a year (well past the average cohort duration)
- User used 29 different IPs in total

__Used anomaly detection to identify 3 users (user IDs: 354, 368, 713) as possible web scrapers__
- Users have never had a program ID
- All 3 generated a high amount of web page visits within an hour
- User 354 generated 62 page visits within one hour
- Users 368 and 713 generated roughly half as much within one hour
 
### Q5 - At some point in the last year, the ability for students and alumni to cross-access curriculum (web dev to ds, ds to web dev) should have been shut off. Do you see any evidence of that happening? Did it happen before? 

Found evidence that there has been cross access by __both program's__ users both within the __past year__ and __prior to the past year__.

### Q6 - What topics are grads continuing to reference after graduation and into their jobs (for each program)? 

The top 3 topics that __web development__ codeup graduates are continuing to reference (returning to the site for after graduation) are
- JavaScript
- Spring
- HTML-CSS

The top 3 topics that __data science__ codeup graduates are continuing to reference (returning to the site for after graduation) are
- Intro to Data Science
- SQL
- Classification

### Q7 - Which lessons are least accessed? 
Of all the major __web development__ lessons, jquery is the least visited.

Of all the major __data science__ lessons, NLP (Natural Language Processing) is the least visited.

### Q8 - Anything else I should be aware of? 

__Codeup IPs__
I believe that the most common IP in our logs 97.105.19.58, belongs to Codeup since over 60% of all log entries are associated with it. I also believe the second most common IP, 97.105.19.61 also belongs to Codeup since it's still somewhat common and begins with the same seven digits as the first IP. 
Although portions of my analysis were focused on finding IPs that were rarely used, we should still be wary of activity that comes from our own IP addresses. A malicious entity could mask their IP as one of our own in order to improve help remain undetected.

__Users with no program ID__
Nearly 45,000 log entries were recorded by users who did not have a program ID assigned to them. These entries were generated by 75 different user IDs.
We should be especially cautious of activity by users without program_IDs until we've confirmed their identity.