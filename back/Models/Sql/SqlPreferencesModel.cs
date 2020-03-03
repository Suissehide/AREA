using System;
using System.Collections.Generic;

using System.Globalization;
using Newtonsoft.Json;
using Newtonsoft.Json.Converters;

namespace back.Models.Sql
{
    public partial class SqlPreferencesModel
    {
        [JsonProperty("id")]
        public long Id { get; set; }

        [JsonProperty("email")]
        public string Email { get; set; }

        [JsonProperty("preferences")]
        public Dictionary<string, Service> services { get; set; }
    }

    
    public partial class Service
    {
        [JsonProperty("service")]
        public bool State { get; set; }

        [JsonProperty("widgets")]
        public Dictionary<string, bool> Widgets { get; set; }
    }
}
/*    public partial class SqlPreferencesModel
    {
        [JsonProperty("id")]
        public long Id { get; set; }

        [JsonProperty("email")]
        public string Email { get; set; }

        [JsonProperty("preferences")]
        public Preferences Preferences { get; set; }
    }

    public partial class Preferences
    {
        [JsonProperty("ChuckService")]
        public ChuckService ChuckService { get; set; }

        [JsonProperty("FacebookService")]
        public FacebookService FacebookService { get; set; }

        [JsonProperty("GoogleMapService")]
        public GoogleMapService GoogleMapService { get; set; }

        [JsonProperty("HeroService")]
        public HeroService HeroService { get; set; }

        [JsonProperty("JikanService")]
        public JikanService JikanService { get; set; }

        [JsonProperty("Joke")]
        public Joke Joke { get; set; }

        [JsonProperty("MicrosoftService")]
        public MicrosoftService MicrosoftService { get; set; }

        [JsonProperty("NewsService")]
        public NewsService NewsService { get; set; }

        [JsonProperty("PhotoService")]
        public PhotoService PhotoService { get; set; }

        [JsonProperty("PokemonService")]
        public PokemonService PokemonService { get; set; }

        [JsonProperty("PotterService")]
        public PotterService PotterService { get; set; }

        [JsonProperty("TheMovieDatabaseService")]
        public TheMovieDatabaseService TheMovieDatabaseService { get; set; }

        [JsonProperty("WheatherService")]
        public WheatherService WheatherService { get; set; }
    }

    public partial class ChuckService
    {
        [JsonProperty("service")]
        public bool Service { get; set; }

        [JsonProperty("widgets")]
        public ChuckServiceWidgets Widgets { get; set; }
    }

    public partial class ChuckServiceWidgets
    {
        [JsonProperty("ChuckNorrisJoke")]
        public bool ChuckNorrisJoke { get; set; }
    }

    public partial class FacebookService
    {
        [JsonProperty("service")]
        public bool Service { get; set; }

        [JsonProperty("widgets")]
        public FacebookServiceWidgets Widgets { get; set; }
    }

    public partial class FacebookServiceWidgets
    {
        [JsonProperty("Like")]
        public bool Like { get; set; }
    }

    public partial class GoogleMapService
    {
        [JsonProperty("service")]
        public bool Service { get; set; }

        [JsonProperty("widgets")]
        public GoogleMapServiceWidgets Widgets { get; set; }
    }

    public partial class GoogleMapServiceWidgets
    {
        [JsonProperty("Distance")]
        public bool Distance { get; set; }

        [JsonProperty("Location")]
        public bool Location { get; set; }
    }

    public partial class HeroService
    {
        [JsonProperty("service")]
        public bool Service { get; set; }

        [JsonProperty("widgets")]
        public HeroServiceWidgets Widgets { get; set; }
    }

    public partial class HeroServiceWidgets
    {
        [JsonProperty("RandomHero")]
        public bool RandomHero { get; set; }

        [JsonProperty("Hero")]
        public bool Hero { get; set; }
    }

    public partial class JikanService
    {
        [JsonProperty("service")]
        public bool Service { get; set; }

        [JsonProperty("widgets")]
        public JikanServiceWidgets Widgets { get; set; }
    }

    public partial class JikanServiceWidgets
    {
        [JsonProperty("Anime")]
        public bool Anime { get; set; }

        [JsonProperty("JikanCharacter")]
        public bool JikanCharacter { get; set; }

        [JsonProperty("TopAnime")]
        public bool TopAnime { get; set; }

        [JsonProperty("Topmanga")]
        public bool Topmanga { get; set; }
    }

    public partial class Joke
    {
        [JsonProperty("service")]
        public bool Service { get; set; }

        [JsonProperty("widgets")]
        public JokeWidgets Widgets { get; set; }
    }

    public partial class JokeWidgets
    {
        [JsonProperty("Joke")]
        public bool Joke { get; set; }
    }

    public partial class MicrosoftService
    {
        [JsonProperty("service")]
        public bool Service { get; set; }

        [JsonProperty("widgets")]
        public MicrosoftServiceWidgets Widgets { get; set; }
    }

    public partial class MicrosoftServiceWidgets
    {
        [JsonProperty("Contacts")]
        public bool Contacts { get; set; }

        [JsonProperty("Drive")]
        public bool Drive { get; set; }

        [JsonProperty("Calendar")]
        public bool Calendar { get; set; }

        [JsonProperty("Profile")]
        public bool Profile { get; set; }

        [JsonProperty("Outlook")]
        public bool Outlook { get; set; }
    }

    public partial class NewsService
    {
        [JsonProperty("service")]
        public bool Service { get; set; }

        [JsonProperty("widgets")]
        public NewsServiceWidgets Widgets { get; set; }
    }

    public partial class NewsServiceWidgets
    {
        [JsonProperty("Banananews")]
        public bool Banananews { get; set; }

        [JsonProperty("News")]
        public bool News { get; set; }
    }

    public partial class PhotoService
    {
        [JsonProperty("service")]
        public bool Service { get; set; }

        [JsonProperty("widgets")]
        public PhotoServiceWidgets Widgets { get; set; }
    }

    public partial class PhotoServiceWidgets
    {
        [JsonProperty("Photo")]
        public bool Photo { get; set; }
    }

    public partial class PokemonService
    {
        [JsonProperty("service")]
        public bool Service { get; set; }

        [JsonProperty("widgets")]
        public PokemonServiceWidgets Widgets { get; set; }
    }

    public partial class PokemonServiceWidgets
    {
        [JsonProperty("Pokemon")]
        public bool Pokemon { get; set; }
    }

    public partial class PotterService
    {
        [JsonProperty("service")]
        public bool Service { get; set; }

        [JsonProperty("widgets")]
        public PotterServiceWidgets Widgets { get; set; }
    }

    public partial class PotterServiceWidgets
    {
        [JsonProperty("PotterSpell")]
        public bool PotterSpell { get; set; }

        [JsonProperty("PotterCharacter")]
        public bool PotterCharacter { get; set; }
    }

    public partial class TheMovieDatabaseService
    {
        [JsonProperty("service")]
        public bool Service { get; set; }

        [JsonProperty("widgets")]
        public TheMovieDatabaseServiceWidgets Widgets { get; set; }
    }

    public partial class TheMovieDatabaseServiceWidgets
    {
        [JsonProperty("TheMovieDatabase")]
        public bool TheMovieDatabase { get; set; }
    }

    public partial class WheatherService
    {
        [JsonProperty("service")]
        public bool Service { get; set; }

        [JsonProperty("widgets")]
        public WheatherServiceWidgets Widgets { get; set; }
    }

    public partial class WheatherServiceWidgets
    {
        [JsonProperty("Wheather")]
        public bool Wheather { get; set; }
    }
*/
