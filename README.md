# Redbus_Project




Data-Scraping-with-Selenium-Dynamic-Filtering-using-Streamlit

 Introduction:

The Redbus Web Data Scraping using Selenium and Filtering with Streamlit Application' aims to revolutionize the transportation industry by providing a comprehensive solution for collecting, analysing, and visualizing bus travel data. By utilizing Selenium for web scraping, this project automates the extraction of detailed information from Redbus, including bus routes, schedules, prices, and seat availability which leads to easy usage of information. By streamlining data collection and providing powerful tools for data-driven decision-making, this project can significantly improve operational efficiency and strategic planning in the transportation industry.
  
 TECHNOLOGY USED
* Python 3.9.I
* MySQL 8.0
* Streamlit
* Selenium

 FEATURES OF APPLICATION

 Retrive the Bus Information:

Scraping dynamic websites like RedBus is made easy using Selenium, a potent web scraping technology that automates browser activities. Selenium excels when it comes to loading content using JavaScript, which is what makes dynamic websites different from static ones where data can be easily extracted using libraries like BeautifulSoup.

Selenium can mimic user behaviors in the context of RedBus, including choosing trip dates, entering the departure and destination locations, and filtering results. It can wait for items rendered with JavaScript, like bus schedules, seat availability, and prices, to load.

Through the usage of Selenium's `find_element_by_*} methods, users are able to discover elements on RedBus such as input fields, search buttons, and travel results.

The page can be navigated around and interacted with to collect data, including bus names, timings, and prices.

Selenium's ability to manage cookies, session data, and CAPTCHA prompts—common on ticket buying websites like RedBus—is one of its advantages. But, because scraping may violate site policies, it's important to take into account the terms of service on the website and refrain from flooding their servers with repetitive automated queries.

Around 11 different states were used here for this project. The states that are used here are Andhra Pradesh, Kerala, Telangana, Kadamba, Rajasthan, South Bengal, Himachal, Assam, Uttar Pradesh, West Bengal, Chandigarh. 

Store data in database:

The collected bus details data was transformed into pandas data frames. And the details of bus of different states are collected in different dataframes and they are concatenated into one. 
The concatenated dataframe is converted into csv file and stored in the SQL database.
The data is stored in the form of tables.

Web App - streamlit:

With the help of Streamlit, you can create an interactive application similar to RedBus by designing a user-friendly interface that allows users to search for bus routes, view available buses, and get details like departure times and prices. The streamlit app is built and many filters are used for easy access for the users. The code for Streamlit was done using python. 






 
     

                                
    
