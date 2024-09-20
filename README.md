## Project Name & Pitch

Reward Allocator

A Python script that aggregates data from public websites and computes reward assignments

Built with Python. Utilized Pandas library to parse web-scraped data and GraphQL to query Warcraft Log’s API. I also used pretty print and print libraries to output the result to a text file

### Demo Video
[![Watch the demo](https://img.youtube.com/vi/STeGI4txP7M/0.jpg)](https://www.youtube.com/watch?v=STeGI4txP7M)

## Installation and Setup Instructions

Clone down this repository. You will need `VS Code` installed globally on your machine.

You will need a couple of imports to run this script.
`pip install pandas`
`pip install requests`
`pip install python-dotenv`

### Priority Spreadsheet
Class/spec priority of items is scraped from this public spreadsheet. Take a note at the link below. `1TyYdcyq2_J5GT6rsIH9mNQgKWtoOa7bxDriMf8u1d5Q` is your spreadsheet. `594385335` is your sheet ID. If you wish to change this, go to config.py and change the variables "spreadsheet" and "sheetID".

https://docs.google.com/spreadsheets/d/1TyYdcyq2_J5GT6rsIH9mNQgKWtoOa7bxDriMf8u1d5Q/edit#gid=594385335
![spreadsheet](https://github.com/johnnyj2608/LootCouncil/assets/54607786/a4cabd43-ebbb-4e07-bde6-4505d870836b)

### That's My BiS
A guild on the website below is required to access wishlists and received lists. These lists will be intersected with the priority spreadsheet to keep only the relevant items. Insert your own in config.py, "tmb" variable.

https://thatsmybis.com/GUILD_ID/GUILD_NAME/export/loot/html/all
<img width="933" alt="Screen Shot 2023-06-24 at 2 46 05 AM" src="https://github.com/johnnyj2608/LootCouncil/assets/54607786/dfba4c0a-1a50-40a1-8f11-80962a09edd9">

To access this website behind Discord OAuth, create a file called .env. Follow these steps on this Stack Overflow post:
https://stackoverflow.com/questions/23102833/how-to-scrape-a-website-which-requires-login-using-python-and-beautifulsoup

The only key-value pair you need is for cookies = {remember_web_XXXXX : XXXXXXXXXX}

In your .env file, create variables for your key-value pair named tmb_key and tmb_val respectively.

### Warcraft Logs API
A Warcraftlogs account is required for the next step. This is used to access player performance and role. It will also intersect with TMB wishlists and received lists to only include eligible (those who were present) people to receive loot. In config.py, change the variable "guildID" to your own guild's WCL ID.

Follow the website below to acquire API access. Enter any name and redirect URL for your client. Save the client ID and secret

https://www.warcraftlogs.com/api/clients/
<img width="1049" alt="client" src="https://github.com/johnnyj2608/LootCouncil/assets/54607786/cc43db09-04ee-4d55-8698-d8030a5661cb">

Revisit the .env file. Create two more variables for your client ID and secret. Here is what it should look like:

<img width="562" alt="ezgif com-gif-maker (3)" src="https://github.com/johnnyj2608/LootCouncil/assets/54607786/5e3ae3c9-5bed-4e12-a989-16503a9ea829">

Complete GraphQL documentation for Warcraft Logs API: https://www.warcraftlogs.com/v2-api-docs/warcraft/

### GitHub Actions (Optional)

You have the option to run this script via GitHub Actions. Currently, it will run main.py every Tuesday and Thursday at 8:15 EST and write to the Outputs directory. To adjust to your own raid schedule, go to .github/workflows/actions.yml and change line 6, cron. If you are unfamiliar with cron expressions, use this website:
https://crontab.guru/

You will also need to change a couple of settings. Allow for workflows with your GitHub token. Start by going to your profile settings

<img width="299" alt="Screen Shot 2023-07-05 at 12 19 27 AM" src="https://github.com/johnnyj2608/LootCouncil/assets/54607786/25d74dd5-8dfd-4879-b952-25c710b23f9e">
<br>
<img width="296" alt="Screen Shot 2023-07-05 at 12 19 40 AM" src="https://github.com/johnnyj2608/LootCouncil/assets/54607786/96bab1f5-e878-442a-b308-bd48350061f0">
<br>
<img width="563" alt="Screen Shot 2023-07-05 at 12 20 27 AM" src="https://github.com/johnnyj2608/LootCouncil/assets/54607786/c82664e0-88bd-4407-b10c-32daef1c7768">

Next, allow GitHub actions to write to your repository. Go to your repository's settings

<img width="309" alt="Screen Shot 2023-07-05 at 12 18 14 AM" src="https://github.com/johnnyj2608/LootCouncil/assets/54607786/61ff3da9-d4ae-479e-9dee-31e84cba91dd">
<br>
<img width="770" alt="Screen Shot 2023-07-05 at 12 18 21 AM" src="https://github.com/johnnyj2608/LootCouncil/assets/54607786/4d1da4a1-a39e-40f9-83fe-c864b2ec0940">

The final step is to create secret variables for your repository:

<img width="246" alt="Screen Shot 2023-07-05 at 12 44 40 AM" src="https://github.com/johnnyj2608/LootCouncil/assets/54607786/60aa3862-8e1c-4ba8-939a-a4358ae342ca">
<br>
<img width="784" alt="Screen Shot 2023-07-05 at 12 18 48 AM" src="https://github.com/johnnyj2608/LootCouncil/assets/54607786/30a069a4-4c36-45b6-b7b9-5789313c777e">

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

## Project Screenshots

<img width="392" alt="Screen Shot 2023-07-05 at 12 38 52 AM" src="https://github.com/johnnyj2608/LootCouncil/assets/54607786/73bb199e-6d70-41dd-b718-3aa32a9754ae">
<br />
<img width="447" alt="Screen Shot 2023-06-26 at 2 21 56 AM" src="https://github.com/johnnyj2608/LootCouncil/assets/54607786/2d6c6705-288d-4ab7-b9d9-92fd6a9ebbee">
