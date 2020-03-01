import React, { Fragment } from "react";
import { StyleSheet } from 'react-native';
import { KeyboardAwareScrollView } from 'react-native-keyboard-aware-scroll-view'
import { theme } from '../core/theme';
import { withWidget } from "../core/Context";
import Background from '../components/Background';
import MyCard from '../widgets/CardTemplate';
import PotterSpellWidget from '../widgets/Potter/PotterSpellWidget';
import PotterCharacterWidget from '../widgets/Potter/PotterCharacterWidget';
import WeatherWidget from '../widgets/WeatherWidget';
import ChuckWidget from '../widgets/ChuckWidget';
import MovieWidget from '../widgets/MovieWidget'
import JikanAnimeWidget from '../widgets/Jikan/JikanAnimeWidget';
import JikanCharacterWidget from '../widgets/Jikan/JikanCharacterWidget';
import GoogleIpWidget from '../widgets/Google/GoogleIpWidget';
import GoogleDistanceWidget from '../widgets/Google/GoogleDistanceWidget';
import JokeWidget from '../widgets/JokeWidget';
import PokemonWidget from '../widgets/PokemonWidget'

export default withWidget(({ potter, ip, weather, chuck, movie, jikan, google, joke, pokemon }) => (
    <Background>
        <Fragment>
            <KeyboardAwareScrollView style={styles.container} contentContainerStyle={styles.contentContainer}>
                {potter.service === true && potter.spell === true ?
                    <MyCard title="Harry Potter's Random Spell" widget={<PotterSpellWidget ip={ip} />} /> : null}
                {potter.service === true && potter.character === true ?
                    <MyCard title="Random Character from Harry Potter" widget={<PotterCharacterWidget ip={ip} />} /> : null}
                {weather.service === true && weather.widget === true ?
                    <MyCard title="Weather by City" widget={<WeatherWidget ip={ip} />} /> : null}
                {chuck.service === true && chuck.widget === true ?
                    <MyCard title="Latest Chuck Norris Jokes" widget={<ChuckWidget ip={ip} />} /> : null}
                {movie.service === true && movie.widget === true ?
                    <MyCard title="Information on a Movie" widget={<MovieWidget ip={ip} />} /> : null}
                {jikan.service === true && jikan.anime === true ?
                    <MyCard title="Information on an Anime" widget={<JikanAnimeWidget ip={ip} />} /> : null}
                {jikan.service === true && jikan.character === true ?
                    <MyCard title="Information on an Anime Character" widget={<JikanCharacterWidget ip={ip} />} /> : null}
                {google.service === true && google.ip === true ?
                    <MyCard title="Display your localisation depending on your IP" widget={<GoogleIpWidget ip={ip} />} /> : null}
                {google.service === true && google.distance === true ?
                    <MyCard title="Calculate distance and duration between two places" widget={<GoogleDistanceWidget ip={ip} />} /> : null}
                {joke.service === true && joke.widget === true ?
                    <MyCard title="Get a random themed joke" widget={<JokeWidget ip={ip} />} /> : null}
                {pokemon.service === true && pokemon.widget === true ?
                    <MyCard title="Get information on a Pokemon" widget={<PokemonWidget ip={ip} />} /> : null}
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
    title: {
        fontSize: 20,
        alignSelf: "center",
    },
    card: {
        backgroundColor: theme.colors.primary,
        borderWidth: 0,
        borderRadius: 20
    }
});
