## Project Name & Pitch

Name

Description

Built with Python. Utilized Warcraft Logs API and GraphQL.


## Installation and Setup Instructions

Clone down this repository. You will need `VS Code` installed globally on your machine.

You will need a couple of imports to run this script.
`pip install pandas`
`pip install requests`

Class/spec priority of items is scraped from this public spreadsheet. Take a note at the link below.
`1TyYdcyq2_J5GT6rsIH9mNQgKWtoOa7bxDriMf8u1d5Q` is your spreadsheet ID. `594385335` is your sheet ID

https://docs.google.com/spreadsheets/d/1TyYdcyq2_J5GT6rsIH9mNQgKWtoOa7bxDriMf8u1d5Q/edit#gid=594385335
![spreadsheet](https://github.com/johnnyj2608/LootCouncil/assets/54607786/a4cabd43-ebbb-4e07-bde6-4505d870836b)

A guild on the website below is required to access wishlists and received lists. These lists will be intersected with the priority spreadsheet to keep only the relevant items. 

https://thatsmybis.com/GUILD_ID/GUILD_NAME/export/loot/html/all
<img width="933" alt="Screen Shot 2023-06-24 at 2 46 05 AM" src="https://github.com/johnnyj2608/LootCouncil/assets/54607786/dfba4c0a-1a50-40a1-8f11-80962a09edd9">

A Warcraftlogs account is required for the next step. This is used to access player performance and role. It will also intersect with TMB wishlists and received lists to only include eligible (those who were present) people to receive loot. 

Follow the website below to acquire API access. Save the client ID and secret

https://www.warcraftlogs.com/api/clients/
<img width="1049" alt="client" src="https://github.com/johnnyj2608/LootCouncil/assets/54607786/cc43db09-04ee-4d55-8698-d8030a5661cb">

Create a new Python file called "client.py". This file will have two functions for your client ID and secret (or hard-code it into your wcl.py file)
<img width="402" alt="Screen Shot 2023-06-24 at 2 58 00 AM" src="https://github.com/johnnyj2608/LootCouncil/assets/54607786/4e0d7790-df75-4f7b-885a-e46b408e0076">

Full GraphQL documentation for Warcraft Logs API: https://www.warcraftlogs.com/v2-api-docs/warcraft/

Run main.py. User input will be required. 

<img width="206" alt="Screen Shot 2023-06-24 at 3 00 34 AM" src="https://github.com/johnnyj2608/LootCouncil/assets/54607786/4daa78d1-83a7-4caf-b9a1-172cddcd3043">

You can either insert either the code URL or the entire report URL. The end result will be outputted with the pretty print library
<img width="590" alt="result" src="https://github.com/johnnyj2608/LootCouncil/assets/54607786/1cd5231f-9acd-4a45-b898-238ed6673701">

### Docker (Optional):

1. docker -v
2. docker build -t {image_name} .
3. docker run -ti {image_name}    

## Reflection

I created this project in the summer of 2023. The goals included: practicing with Python, learning how to use docker, and reducing the amount of time spent discussing item distribution for the game World of Warcraft.

Journey

Challenges

Recreation + Next Steps
