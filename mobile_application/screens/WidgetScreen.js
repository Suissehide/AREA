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

export default withWidget(({ potterS, potterSpell, potterCharacter, ip, weatherS, weatherW, chuckS, chuckW, movieS, movieW, jinkanS, jinkanAnime, jinkanCharacter }) => (
    <ScrollView style={styles.container} contentContainerStyle={styles.contentContainer}>
        <Fragment>
            {potterS === true && potterSpell === true ?
                <MyCard title="Harry Potter's Random Spell" widget={<PotterSpell ip={ip} />} /> : null}
            {potterS === true && potterCharacter === true ?
                <MyCard title="Random Character from Harry Potter" widget={<PotterCharacter ip={ip} />} /> : null}
            {weatherS === true && weatherW === true ?
                <MyCard title="Weather by City" widget={<WeatherWidget ip={ip} />} /> : null}
            {chuckS === true && chuckW === true ?
                <MyCard title="Latest Chuck Norris Jokes" widget={<ChuckWidget ip={ip} />} /> : null}
            {movieS === true && movieW === true ?
                <MyCard title="Information on a Movie" widget={<MovieWidget ip={ip} />} /> : null}
            {jinkanS === true && jinkanAnime === true ?
                <MyCard title="Information on an Anime" widget={<JinkanAnimeWidget ip={ip} />} /> : null}
            {jinkanS === true && jinkanCharacter === true ?
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
