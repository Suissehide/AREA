# AREA
Realization of a business application that interconnects several external services (such as Yammer, Gmail, RSS...) as Reaction components.

## Installation
Install Docker, then :
```
docker-compose build
docker-compose up
```

## Usage
Go to for web application :
```
localhost:8080
```

## API used

### Services

* #### Chuck Service
  * ##### Chuck Joke Widget : Display a random Chuck Norris joke according to a given theme.
* #### Facebook Service
  * ##### Facebook Like Widget : Display the liked page on Facebook
* #### Hero Service
  * ##### Random Hero Widget : Display the information about a random comics hero
  * ##### Get hero by name Widget : Show information about your chosen hero
* #### Ip Map Service
  * ##### Location Widget : Return the location of the user
* #### ISS Service
  * ##### Location Widget : Localize the ISS station
  * ##### Number of person Widget : Return the number of persons currently in the ISS
* #### Jikan Service
  * ##### Anime Information Widget : Display information about a choosen anime show
  * ##### Anime Character Widget : Show information about a choosen anime/manga character
  * ##### Top anime Widget : Show the 50 best ranked anime of all time
  * ##### Top manga Widget : Display the 50 best ranked manga of all time
* #### Joke service
  * ##### Random joke Widget : Display a random Joke according to a given theme
* #### BananaNews service
  * ##### BananaNews Widget : Found US News about Bananas :)
* #### Photo service
  * ##### Photo Widget : Get a photo according to a given theme
* #### Pokemon service
  * ##### Pokedex Widget : Show details about a given Pokemon
  * ##### Moveset Widget : List all moves of a given Pokemon
* #### HarryPotter service
  * ##### Random spell cast Widget : Allow the user to cast a random spell
  * ##### Random character Widget : Display a random character of Harry Potter universe
* #### StarWars service
  * ##### Random Character Widget : List informations about a random character
  * ##### Random Planet Widget : List informations about a random planet
  * ##### Random Starship Widget : List informations about a random starship
* #### Movie service
  * ##### Movie detail Widget : List information of the searched movie
* #### Weather service
  * ##### Weather Widget : Show the weather forecast of a place in the entire world
* #### Google Maps service
  * ##### Distance calculator Widget : calculate the distance (and the time) between two locations
  * ##### Place detail Widget : show details about a given location
* #### Microsoft service
  * ##### Calendar Event Widget : List all event entries present in your Microsoft Calendar
  * ##### Contacts Widget : List all your contacts
  * ##### Drive Widget : List the files of your drive
  * ##### Graph Widget : show your graph
  * ##### Outlook Widget : show your messages reiceved in your mailbox
## Team
We are 5 students at Epitech, a programming school :
[Justine Duhieu](https://github.com/Justena40) and [Thomas Lesueur](https://github.com/ThomasLesueur) working on the back-end, creating the controllers and routes to external APIs.
[Nejma Belkhanfar](https://github.com/nejnej-dev) is in charge of the Database containing all the user's informations and their settings.
[Léo Couffinhal](https://github.com/Suissehide) is our web developper.
[Idoia Reinares](https://github.com/IdoiaReina) is our mobile developper.
