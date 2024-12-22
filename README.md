# Purdue-Chat-Bot


## Inspiration
Our inspiration was our lack of knowledge of general information about Purdue upon our arrival, and we were inspired by a combination of myPurdue's ability to plan out your courses, as well as other apps such as the BGR guide.

## What it does
Our chatbot takes questions that the user has related to Purdue, and searches all Purdue websites to gather all the information it can into one place, so that you don't have to skim through several sites to get to your goal. Questions can be as simple as "history of Purdue" to "tell me more about *insert course*".

## How we built it
We found that Purdue's home page had a built in Google Custom Search Element (GCSE) which was specific to Purdue and it's web pages. Using this, we created our own GCSE using the Purdue website to be able to access sites specific to a user query. We then web-scraped each of the resulting sites to scrape only the information related to the query. Finally, we cleaned the information to be a summarized short form for it to be easier for the user to read. For the actual chatbot, we used Google's DialogFlow application that makes it easy to make the interface for the chatbot. We trained the bot to some pre-written questions we expect users to say, as users' ways of writing are different by person. Finally, we took the output from our web-scraped summaries to respond to the user.

## Challenges we ran into
One of the biggest challenges we ran into was Google's privacy policies, as initially we wanted to scrape directly from the Purdue website. This is the reason we created our own GCSE, so that we could have access to the search results from a query. Another challenge we faced was processing the information scraped from the site and understanding what information is most relevant to include in the summary. Overall, most of us did not have experience with the concepts we utilized for this project, so everything was a learning experience as we were coding. 

## Accomplishments that we're proud of
We are proud overall of putting together the whole project, since we did not have much of a background in these topics. Learning how to create a Google Custom Search Element was also interesting as we had never worked with APIs before. 

## What we learned
We gained a lot of different experiences working with several new softwares. We worked with DialogFlow, BeautifulSoup, and GCSE which were all very interesting tools that we all plan to use in the future now that we have exposure to them. We also got a better experience with teamwork, and learning how to split up work and problem solve with various different ideas collaboratively. 

## What's next for PurduePal
Since we were still learning how to utilize all of the softwares so we want to eventually expand this application to be able to respond to more specific questions, and especially be capable of responding in a more concise way. We also want to make a proper web app for this project, as right now we are reliant on the interface from the DialogFlow, but we want to learn how to make our own front end.

—---
Dialog Flow was very easy to work with and simplified our chatbot a lot. 
NLTK was something we already had experience with so that was simple to navigate.
We have worked with GitHub before so we were used to working with merge conflicts and using the application in general.
The Google Custom Search Element, while easy to work with, was a challenge to understand what was actually wrong with our code initially. We did not understand the privacy policies of this application when integrated into another website, so creating our own GCSE was a challenge.
