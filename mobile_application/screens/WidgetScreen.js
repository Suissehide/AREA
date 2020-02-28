import React, { Fragment } from "react";
import { StyleSheet } from 'react-native';
import { ScrollView } from 'react-native-gesture-handler';
import { theme } from '../core/theme';
import { withWidget } from "../core/Context";
import MyCard from '../widgets/CardTemplate';
import PotterSpell from '../widgets/Potter/PotterSpell';
import PotterCharacter from '../widgets/Potter/PotterCharacter';
import WeatherWidget from '../widgets/WeatherWidget';
import ChuckWidget from '../widgets/ChuckWidget';
import MovieWidget from '../widgets/MovieWidget'
import JinkanAnimeWidget from '../widgets/Jinkan/JinkanAnimeWidget';
import JinkanCharacterWidget from '../widgets/Jinkan/JinkanCharacterWidget';

export default withWidget(({ potter, ip, weather, chuck, movie, jinkan }) => (
    <ScrollView style={styles.container} contentContainerStyle={styles.contentContainer}>
        <Fragment>
            {potter.service === true && potter.spell === true ?
                <MyCard title="Harry Potter's Random Spell" widget={<PotterSpell ip={ip} />} /> : null}
            {potter.service === true && potter.character === true ?
                <MyCard title="Random Character from Harry Potter" widget={<PotterCharacter ip={ip} />} /> : null}
            {weather.service === true && weather.widget === true ?
                <MyCard title="Weather by City" widget={<WeatherWidget ip={ip} />} /> : null}
            {chuck.service === true && chuck.widget === true ?
                <MyCard title="Latest Chuck Norris Jokes" widget={<ChuckWidget ip={ip} />} /> : null}
            {movie.service === true && movie.widget === true ?
                <MyCard title="Information on a Movie" widget={<MovieWidget ip={ip} />} /> : null}
            {jinkan.service === true && jinkan.anime === true ?
                <MyCard title="Information on an Anime" widget={<JinkanAnimeWidget ip={ip} />} /> : null}
            {jinkan.service === true && jinkan.character === true ?
                <MyCard title="Information on an Anime Character" widget={<JinkanCharacterWidget ip={ip} />} /> : null}
        </Fragment>
    </ScrollView>
));

const styles = StyleSheet.create({
    container: {
        flex: 1,
        backgroundColor: '#fafafa',
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
