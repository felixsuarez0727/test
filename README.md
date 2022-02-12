# Consume Target.com Product Data

## **Introduction**
This projects was developed to retrieve data out Target.Com, to do so we try to use Scrapy, but due to the nature of the website,
its content is delivered dinamically, we had to make a little research on how the content is requested.
As result, it was necessary to perform a HTTP Get Request from the website's datasource to retrieve the data and show the asked items:
Price, Description, Specifications, Highlights, Questions, Images URLS, Title.

## **How to Run**
1. Navigate to the folder.
2. If you want, you can change Product ID in the source code.
2. Run the code with this command: py .\TargetProductData.py
3. Check results.
    
## **Reference**    
Scrapy Documentation on: "Selecting dynamically-loaded content" See URL https://docs.scrapy.org/en/latest/topics/dynamic-content.html

Consume Target.com Product Data - 2022