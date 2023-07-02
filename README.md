## Project Name & Pitch

Reward Allocator

A Python script that aggregates data from public websites and computes reward assignments

Built with Python. Utilized Pandas library to parse web-scraped data and GraphQL to query Warcraft Log’s API. Also used pretty print and print libraries to output the result to a text file


## Installation and Setup Instructions

Clone down this repository. You will need `VS Code` installed globally on your machine.

You will need a couple of imports to run this script.
`pip install pandas`
`pip install requests`

### Priority Spreadsheet
Class/spec priority of items is scraped from this public spreadsheet. Take a note at the link below. Insert your own in links.py, get_spreadsheet() and get_sheetID()

`1TyYdcyq2_J5GT6rsIH9mNQgKWtoOa7bxDriMf8u1d5Q` is your spreadsheet ID. `594385335` is your sheet ID

https://docs.google.com/spreadsheets/d/1TyYdcyq2_J5GT6rsIH9mNQgKWtoOa7bxDriMf8u1d5Q/edit#gid=594385335
![spreadsheet](https://github.com/johnnyj2608/LootCouncil/assets/54607786/a4cabd43-ebbb-4e07-bde6-4505d870836b)

### That's My BiS
A guild on the website below is required to access wishlists and received lists. These lists will be intersected with the priority spreadsheet to keep only the relevant items. Insert your own in links.py, get_tmb().

https://thatsmybis.com/GUILD_ID/GUILD_NAME/export/loot/html/all
<img width="933" alt="Screen Shot 2023-06-24 at 2 46 05 AM" src="https://github.com/johnnyj2608/LootCouncil/assets/54607786/dfba4c0a-1a50-40a1-8f11-80962a09edd9">

To access this website behind Discord OAuth, create a file called client.py. Follow these steps on this Stack Overflow post:
https://stackoverflow.com/questions/23102833/how-to-scrape-a-website-which-requires-login-using-python-and-beautifulsoup

Copy and paste the converted cURL into the client.py file. Here is an example of making your response call into a function:
<img width="480" alt="Screen Shot 2023-06-26 at 2 09 08 AM" src="https://github.com/johnnyj2608/LootCouncil/assets/54607786/e492ae9f-06b8-457f-a2a1-dd1b636e45a9">

### Warcraft Logs API
A Warcraftlogs account is required for the next step. This is used to access player performance and role. It will also intersect with TMB wishlists and received lists to only include eligible (those who were present) people to receive loot. 

Follow the website below to acquire API access. Enter any name and redirect URL for your client. Save the client ID and secret

https://www.warcraftlogs.com/api/clients/
<img width="1049" alt="client" src="https://github.com/johnnyj2608/LootCouncil/assets/54607786/cc43db09-04ee-4d55-8698-d8030a5661cb">

Revisit the client.py file. Create these two functions for your client ID and secret (or hard-code it into your wcl.py file)
<img width="386" alt="Screen Shot 2023-06-26 at 2 11 40 AM" src="https://github.com/johnnyj2608/LootCouncil/assets/54607786/eb89def2-bc3e-44a5-a1fa-16141957bfe5">

Full GraphQL documentation for Warcraft Logs API: https://www.warcraftlogs.com/v2-api-docs/warcraft/

In links.py, change get_guildID() to your own guild's WCL ID.

### Running The Script

main.py will automatically run every Tuesday and Thursday at 8:15 PM. To adjust to your own raid schedule, go to .github/workflows/actions.yml and change line 5, cron. If you are unfamiliar with cron expressions, use this website:
https://crontab.guru/

<img width="380" alt="Screen Shot 2023-06-26 at 2 21 21 AM" src="https://github.com/johnnyj2608/LootCouncil/assets/54607786/84888be1-4643-4495-8b48-7c436d5e4ada">
<br />
<img width="447" alt="Screen Shot 2023-06-26 at 2 21 56 AM" src="https://github.com/johnnyj2608/LootCouncil/assets/54607786/2d6c6705-288d-4ab7-b9d9-92fd6a9ebbee">


### Docker (Optional):

1. docker -v
2. docker build -t {image_name} .
3. docker run -ti {image_name}    

## Reflection

I created this project in the summer of 2023. The goals included: practicing with Python, learning how to use docker, and reducing the amount of time spent discussing item distribution for the game World of Warcraft.

I started by following a tutorial on web scraping and using Pandas to parse the data. After discovering one of the websites had an API associated with it, I learned about GraphQL to query it. Trying to debug the data was an eyesore, so I implemented the pretty print library to make it easier. Finally, I outputted the result into a text file so I could send it.

One of the biggest challenges was figuring out how to scrape a website that required OAuth. I could’ve downloaded the HTML page for every run, but I wanted this script to handle dynamic data. When I attempted to scrape, it would attempt it on the login page. I tried utilizing Mechanize and Selenium libraries to automate the login process, but both were unsuccessful. What did work for me was using my cookies and headers with a cURL converter.

Another challenge I had was using GraphQL to query Warcraft Log’s API. I had no prior experience with the language, and finding solutions to my bugs was scarce since this API isn’t as well known. I tried to learn by looking up other GitHub repositories that used this API, but none utilized it the way I wanted to. Luckily I then discovered a discord server dedicated to discussing the API with the original developers responding frequently.

Eventually, I want to build a GUI and have a way to apply increments during runtime. For example, one criterion for the algorithm is the number of rewards a person has received. I wish to have the option to award a person and rerun the algorithm without loading the web-scraped and API data again. It could be impactful since one increment could make the next person in line overtake the current in priority.
