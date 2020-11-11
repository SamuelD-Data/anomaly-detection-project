# Title

Anomaly Detection Project

# Goals

1) Explore the curriculum access data to answer various questions

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