# Webscraping Project

Scraper to scrape first 100 cryptocurrencies from coinmarketcap.com and its available trading and value data.

- scrapes links to the currencies from the main page
- scrapes needed information from each link
- returns the mean and std of the values
- returns scatterplots comparing different currencies

There might be some differences between data scraped with different scrapers, as all the parameters are dynamically changing in time.

## Running crawlers - instructions

Both Selenium and Beautiful Soup crawlers should work just by running the appropriate files in the IDE or in command line.
### Running scrapy spider

#### On Linux
- download the whole "scrapy" folder
- via terminal, go to "coins" subfolder loction (cd path/to/folder/coins)
- run "scrapy crawl get_links -O links.csv"
- run "scrapy crawl get_stats -O stats.csv"

#### On Windows

#### On Mac
