import React, { Fragment } from 'react';
import { StyleSheet } from 'react-native';
import { KeyboardAwareScrollView } from 'react-native-keyboard-aware-scroll-view';
import Background from '../components/Background';
import Widget from '../components/WidgetTemplate';
import { withWidget } from '../core/Context';
import ChuckWidget from '../widgets/ChuckWidget';
import FacebookWidget from '../widgets/FacebookWidget';
import GoogleDistanceWidget from '../widgets/Google/GoogleDistanceWidget';
import GoogleIpWidget from '../widgets/Google/GoogleIpWidget';
import HeroNameWidget from '../widgets/Hero/HeroNameWidget';
import HeroRandomWidget from '../widgets/Hero/HeroRandomWidget';
import JikanAnimeWidget from '../widgets/Jikan/JikanAnimeWidget';
import JikanCharacterWidget from '../widgets/Jikan/JikanCharacterWidget';
import JikanTopAnimeWidget from '../widgets/Jikan/JikanTopAnimeWidget';
import JikanTopMangaWidget from '../widgets/Jikan/JikanTopMangaWidget';
import JokeWidget from '../widgets/JokeWidget';
import MicrosoftCalendarWidget from '../widgets/Microsoft/MicrosoftCalendarWidget';
import MicrosoftContactsWidget from '../widgets/Microsoft/MicrosoftContactsWidget';
import MicrosoftDriveWidget from '../widgets/Microsoft/MicrosoftDriveWidget';
import MicrosoftGraphWidget from '../widgets/Microsoft/MicrosoftGraphWidget';
import MicrosoftOutlookWidget from '../widgets/Microsoft/MicrosoftOutlookWidget';
import MovieWidget from '../widgets/MovieWidget';
import NewsBananaWidget from '../widgets/News/NewsBananaWidget';
import NewsThemeWidget from '../widgets/News/NewsThemeWidget';
import PictureWidget from '../widgets/PictureWidget';
import PokemonDetailWidget from '../widgets/Pokemon/PokemonDetailWidget';
import PotterCharacterWidget from '../widgets/Potter/PotterCharacterWidget';
import PotterSpellWidget from '../widgets/Potter/PotterSpellWidget';
import WeatherWidget from '../widgets/WeatherWidget';
import PokemonMovesWidget from '../widgets/Pokemon/PokemonMovesWidget'
import IssLocationWidget from '../widgets/Iss/IssLocationWidget';
import IssPersonWidget from '../widgets/Iss/IssPersonWidget';
import StarwarsCharacterWidget from '../widgets/Starwars/StarwarsCharacterWidget';
import StarwarsPlanetWidget from '../widgets/Starwars/StarwarsPlanetWidget';

export default withWidget(({ potter, ip, weather, chuck, movie, jikan, google, joke, pokemon, picture, news, hero, facebook, microsoft, iss, starwars }) => (
    <Background>
        <Fragment>
            <KeyboardAwareScrollView style={styles.container} contentContainerStyle={styles.contentContainer}>

                {chuck.service === true && chuck.widget === true ?
                    <Widget title="Latest Chuck Norris Jokes" widget={<ChuckWidget ip={ip} />} /> : null}
                {facebook.service === true && facebook.widget === true ?
                    <Widget title="Facebook Likes" widget={<FacebookWidget ip={ip} />} /> : null}
                {google.service === true && google.ip === true ?
                    <Widget title="Display your localisation depending on your IP" widget={<GoogleIpWidget ip={ip} />} /> : null}
                {google.service === true && google.distance === true ?
                    <Widget title="Calculate distance and duration between two places" widget={<GoogleDistanceWidget ip={ip} />} /> : null}
                {hero.service === true && hero.random === true ?
                    <Widget title="Random Superhero" widget={<HeroRandomWidget ip={ip} />} /> : null}
                {hero.service === true && hero.name === true ?
                    <Widget title="Information on your Superhero" widget={<HeroNameWidget ip={ip} />} /> : null}
                {iss.service === true && iss.location === true ?
                    <Widget title="ISS Location" widget={<IssLocationWidget ip={ip} />} /> : null}
                {iss.service === true && iss.person === true ?
                    <Widget title="People in Space" widget={<IssPersonWidget ip={ip} />} /> : null}
                {jikan.service === true && jikan.anime === true ?
                    <Widget title="Information on an Anime" widget={<JikanAnimeWidget ip={ip} />} /> : null}
                {jikan.service === true && jikan.character === true ?
                    <Widget title="Information on an Anime Character" widget={<JikanCharacterWidget ip={ip} />} /> : null}
                {jikan.service === true && jikan.topAnime === true ?
                    <Widget title="Top Animes" widget={<JikanTopAnimeWidget ip={ip} />} /> : null}
                {jikan.service === true && jikan.topManga === true ?
                    <Widget title="Top Mangas" widget={<JikanTopMangaWidget ip={ip} />} /> : null}
                {joke.service === true && joke.widget === true ?
                    <Widget title="Get a random themed joke" widget={<JokeWidget ip={ip} />} /> : null}
                {microsoft.service === true && microsoft.calendar === true ?
                    <Widget title="Calendar Events" widget={<MicrosoftCalendarWidget ip={ip} />} /> : null}
                {microsoft.service === true && microsoft.contacts === true ?
                    <Widget title="Microsoft Contacts" widget={<MicrosoftContactsWidget ip={ip} />} /> : null}
                {microsoft.service === true && microsoft.drive === true ?
                    <Widget title="Microsoft Drive" widget={<MicrosoftDriveWidget ip={ip} />} /> : null}
                {microsoft.service === true && microsoft.graph === true ?
                    <Widget title="Microsoft Graph" widget={<MicrosoftGraphWidget ip={ip} />} /> : null}
                {microsoft.service === true && microsoft.outlook === true ?
                    <Widget title="Microsoft Outlook" widget={<MicrosoftOutlookWidget ip={ip} />} /> : null}
                {movie.service === true && movie.widget === true ?
                    <Widget title="Information on a Movie" widget={<MovieWidget ip={ip} />} /> : null}
                {news.service === true && news.banana === true ?
                    <Widget title="Bananews" widget={<NewsBananaWidget ip={ip} />} /> : null}
                {news.service === true && news.theme === true ?
                    <Widget title="News" widget={<NewsThemeWidget ip={ip} />} /> : null}
                {picture.service === true && picture.widget === true ?
                    <Widget title="Themed Picture" widget={<PictureWidget ip={ip} />} /> : null}
                {pokemon.service === true && pokemon.detail === true ?
                    <Widget title="Get information on a Pokemon" widget={<PokemonDetailWidget ip={ip} />} /> : null}
                {pokemon.service === true && pokemon.moves === true ?
                    <Widget title="Get Pokemon's 5 random abilities" widget={<PokemonMovesWidget ip={ip} />} /> : null}
                {potter.service === true && potter.spell === true ?
                    <Widget title="Harry Potter's Random Spell" widget={<PotterSpellWidget ip={ip} />} /> : null}
                {potter.service === true && potter.character === true ?
                    <Widget title="Random Character from Harry Potter" widget={<PotterCharacterWidget ip={ip} />} /> : null}
                {starwars.service === true && starwars.people === true ?
                    <Widget title="Random Character from Star Wars" widget={<StarwarsCharacterWidget ip={ip} />} /> : null}
                {starwars.service === true && starwars.planet === true ?
                    <Widget title="Random Planet from Star Wars" widget={<StarwarsPlanetWidget ip={ip} />} /> : null}
                {weather.service === true && weather.widget === true ?
                    <Widget title="Weather by City" widget={<WeatherWidget ip={ip} />} /> : null}

            </KeyboardAwareScrollView>
        </Fragment>
    </Background>
));

const styles = StyleSheet.create({
    container: {
        flex: 1,
    },
    contentContainer: {
        paddingTop: 15,
    },
});
