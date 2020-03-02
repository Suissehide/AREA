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
import GooglePlaceWidget from '../widgets/Google/GooglePlaceWidget';

export default withWidget((props) => (
    <Background>
        <Fragment>
            <KeyboardAwareScrollView style={styles.container} contentContainerStyle={styles.contentContainer}>

                {props.chuck.service === true && props.chuck.widget === true ?
                    <Widget title="Latest Chuck Norris Jokes" widget={<ChuckWidget ip={props.ip} />} /> : null}
                {props.facebook.service === true && props.facebook.widget === true ?
                    <Widget title="Facebook Likes" widget={<FacebookWidget ip={props.ip} />} /> : null}
                {props.google.service === true && props.google.ip === true ?
                    <Widget title="Display your localisation depending on your IP" widget={<GoogleIpWidget ip={props.ip} />} /> : null}
                {props.google.service === true && props.google.distance === true ?
                    <Widget title="Calculate distance and duration between two places" widget={<GoogleDistanceWidget ip={props.ip} />} /> : null}
                {props.google.service === true && props.google.place === true ?
                    <Widget title="Information on a place" widget={<GooglePlaceWidget ip={props.ip} />} /> : null}
                {props.hero.service === true && props.hero.random === true ?
                    <Widget title="Random Superhero" widget={<HeroRandomWidget ip={props.ip} />} /> : null}
                {props.hero.service === true && props.hero.name === true ?
                    <Widget title="Information on your Superhero" widget={<HeroNameWidget ip={props.ip} />} /> : null}
                {props.iss.service === true && props.iss.location === true ?
                    <Widget title="ISS Location" widget={<IssLocationWidget ip={props.ip} />} /> : null}
                {props.iss.service === true && props.iss.person === true ?
                    <Widget title="People in Space" widget={<IssPersonWidget ip={props.ip} />} /> : null}
                {props.jikan.service === true && props.jikan.anime === true ?
                    <Widget title="Information on an Anime" widget={<JikanAnimeWidget ip={props.ip} />} /> : null}
                {props.jikan.service === true && props.jikan.character === true ?
                    <Widget title="Information on an Anime Character" widget={<JikanCharacterWidget ip={props.ip} />} /> : null}
                {props.jikan.service === true && props.jikan.topAnime === true ?
                    <Widget title="Top Animes" widget={<JikanTopAnimeWidget ip={props.ip} />} /> : null}
                {props.jikan.service === true && props.jikan.topManga === true ?
                    <Widget title="Top Mangas" widget={<JikanTopMangaWidget ip={props.ip} />} /> : null}
                {props.joke.service === true && props.joke.widget === true ?
                    <Widget title="Get a random themed joke" widget={<JokeWidget ip={props.ip} />} /> : null}
                {props.microsoft.service === true && props.microsoft.calendar === true ?
                    <Widget title="Calendar Events" widget={<MicrosoftCalendarWidget ip={props.ip} />} /> : null}
                {props.microsoft.service === true && props.microsoft.contacts === true ?
                    <Widget title="Microsoft Contacts" widget={<MicrosoftContactsWidget ip={props.ip} />} /> : null}
                {props.microsoft.service === true && props.microsoft.drive === true ?
                    <Widget title="Microsoft Drive" widget={<MicrosoftDriveWidget ip={props.ip} />} /> : null}
                {props.microsoft.service === true && props.microsoft.graph === true ?
                    <Widget title="Microsoft Graph" widget={<MicrosoftGraphWidget ip={props.ip} />} /> : null}
                {props.microsoft.service === true && props.microsoft.outlook === true ?
                    <Widget title="Microsoft Outlook" widget={<MicrosoftOutlookWidget ip={props.ip} />} /> : null}
                {props.movie.service === true && props.movie.widget === true ?
                    <Widget title="Information on a Movie" widget={<MovieWidget ip={props.ip} />} /> : null}
                {props.news.service === true && props.news.banana === true ?
                    <Widget title="Bananews" widget={<NewsBananaWidget ip={props.ip} />} /> : null}
                {props.news.service === true && props.news.theme === true ?
                    <Widget title="News" widget={<NewsThemeWidget ip={props.ip} />} /> : null}
                {props.picture.service === true && props.picture.widget === true ?
                    <Widget title="Themed Picture" widget={<PictureWidget ip={props.ip} />} /> : null}
                {props.pokemon.service === true && props.pokemon.detail === true ?
                    <Widget title="Get information on a Pokemon" widget={<PokemonDetailWidget ip={props.ip} />} /> : null}
                {props.pokemon.service === true && props.pokemon.moves === true ?
                    <Widget title="Get Pokemon's 5 random abilities" widget={<PokemonMovesWidget ip={props.ip} />} /> : null}
                {props.potter.service === true && props.potter.spell === true ?
                    <Widget title="Harry Potter's Random Spell" widget={<PotterSpellWidget ip={props.ip} />} /> : null}
                {props.potter.service === true && props.potter.character === true ?
                    <Widget title="Random Character from Harry Potter" widget={<PotterCharacterWidget ip={props.ip} />} /> : null}
                {props.starwars.service === true && props.starwars.people === true ?
                    <Widget title="Random Character from Star Wars" widget={<StarwarsCharacterWidget ip={props.ip} />} /> : null}
                {props.starwars.service === true && props.starwars.planet === true ?
                    <Widget title="Random Planet from Star Wars" widget={<StarwarsPlanetWidget ip={props.ip} />} /> : null}
                {props.weather.service === true && props.weather.widget === true ?
                    <Widget title="Weather by City" widget={<WeatherWidget ip={props.ip} />} /> : null}

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
