import React, { Fragment } from "react";
import { StyleSheet } from 'react-native';
import { theme } from '../core/theme';
import { withWidget } from "../core/Context";
import MyCard from '../widgets/CardTemplate';
import PotterSpellWidget from '../widgets/Potter/PotterSpellWidget';
import PotterCharacterWidget from '../widgets/Potter/PotterCharacterWidget';
import WeatherWidget from '../widgets/WeatherWidget';
import ChuckWidget from '../widgets/ChuckWidget';
import MovieWidget from '../widgets/MovieWidget'
import JikanAnimeWidget from '../widgets/Jikan/JikanAnimeWidget';
import JikanCharacterWidget from '../widgets/Jikan/JikanCharacterWidget';
import { KeyboardAwareScrollView } from 'react-native-keyboard-aware-scroll-view'
import Background from '../components/Background';

export default withWidget(({ potter, ip, weather, chuck, movie, jikan }) => (
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
