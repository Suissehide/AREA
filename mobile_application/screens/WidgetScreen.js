import React, { Fragment } from 'react';
import { StyleSheet } from 'react-native';
import { KeyboardAwareScrollView } from 'react-native-keyboard-aware-scroll-view';
import Background from '../components/Background';
import MyCard from '../components/WidgetTemplate';
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

export default withWidget(({ potter, ip, weather, chuck, movie, jikan, google, joke, pokemon, picture, news, hero, facebook, microsoft }) => (
    <Background>
        <Fragment>
            <KeyboardAwareScrollView style={styles.container} contentContainerStyle={styles.contentContainer}>

                {chuck.service === true && chuck.widget === true ?
                    <MyCard title="Latest Chuck Norris Jokes" widget={<ChuckWidget ip={ip} />} /> : null}
                {facebook.service === true && facebook.widget === true ?
                    <MyCard title="Facebook Likes" widget={<FacebookWidget ip={ip} />} /> : null}
                {google.service === true && google.ip === true ?
                    <MyCard title="Display your localisation depending on your IP" widget={<GoogleIpWidget ip={ip} />} /> : null}
                {google.service === true && google.distance === true ?
                    <MyCard title="Calculate distance and duration between two places" widget={<GoogleDistanceWidget ip={ip} />} /> : null}
                {hero.service === true && hero.random === true ?
                    <MyCard title="Random Superhero" widget={<HeroRandomWidget ip={ip} />} /> : null}
                {hero.service === true && hero.name === true ?
                    <MyCard title="Information on your Superhero" widget={<HeroNameWidget ip={ip} />} /> : null}
                {jikan.service === true && jikan.anime === true ?
                    <MyCard title="Information on an Anime" widget={<JikanAnimeWidget ip={ip} />} /> : null}
                {jikan.service === true && jikan.character === true ?
                    <MyCard title="Information on an Anime Character" widget={<JikanCharacterWidget ip={ip} />} /> : null}
                {jikan.service === true && jikan.topAnime === true ?
                    <MyCard title="Top Animes" widget={<JikanTopAnimeWidget ip={ip} />} /> : null}
                {jikan.service === true && jikan.topManga === true ?
                    <MyCard title="Top Mangas" widget={<JikanTopMangaWidget ip={ip} />} /> : null}
                {joke.service === true && joke.widget === true ?
                    <MyCard title="Get a random themed joke" widget={<JokeWidget ip={ip} />} /> : null}
                {microsoft.service === true && microsoft.calendar === true ?
                    <MyCard title="Calendar Events" widget={<MicrosoftCalendarWidget ip={ip} />} /> : null}
                {microsoft.service === true && microsoft.contacts === true ?
                    <MyCard title="Microsoft Contacts" widget={<MicrosoftContactsWidget ip={ip} />} /> : null}
                {microsoft.service === true && microsoft.drive === true ?
                    <MyCard title="Microsoft Drive" widget={<MicrosoftDriveWidget ip={ip} />} /> : null}
                {microsoft.service === true && microsoft.graph === true ?
                    <MyCard title="Microsoft Graph" widget={<MicrosoftGraphWidget ip={ip} />} /> : null}
                {microsoft.service === true && microsoft.outlook === true ?
                    <MyCard title="Microsoft Outlook" widget={<MicrosoftOutlookWidget ip={ip} />} /> : null}
                {movie.service === true && movie.widget === true ?
                    <MyCard title="Information on a Movie" widget={<MovieWidget ip={ip} />} /> : null}
                {news.service === true && news.banana === true ?
                    <MyCard title="Bananews" widget={<NewsBananaWidget ip={ip} />} /> : null}
                {news.service === true && news.theme === true ?
                    <MyCard title="News" widget={<NewsThemeWidget ip={ip} />} /> : null}
                {picture.service === true && picture.widget === true ?
                    <MyCard title="Themed Picture" widget={<PictureWidget ip={ip} />} /> : null}
                {pokemon.service === true && pokemon.detail === true ?
                    <MyCard title="Get information on a Pokemon" widget={<PokemonDetailWidget ip={ip} />} /> : null}
                {pokemon.service === true && pokemon.moves === true ?
                    <MyCard title="Get Pokemon's 5 random abilities" widget={<PokemonMovesWidget ip={ip} />} /> : null}
                {potter.service === true && potter.spell === true ?
                    <MyCard title="Harry Potter's Random Spell" widget={<PotterSpellWidget ip={ip} />} /> : null}
                {potter.service === true && potter.character === true ?
                    <MyCard title="Random Character from Harry Potter" widget={<PotterCharacterWidget ip={ip} />} /> : null}
                {weather.service === true && weather.widget === true ?
                    <MyCard title="Weather by City" widget={<WeatherWidget ip={ip} />} /> : null}

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
