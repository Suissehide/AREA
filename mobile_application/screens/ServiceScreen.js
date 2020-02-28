import React, { Fragment } from "react";
import { StyleSheet, View } from 'react-native';
import { ScrollView } from 'react-native-gesture-handler';
import { withWidget } from "../core/Context";
import MyCard from '../components/CardService';
import PotterService from '../services/PotterService';
import WeatherService from '../services/WeatherService';
import ChuckService from '../services/ChuckService';
import MovieService from '../services/MovieService';
import JinkanService from '../services/JinkanService';

export default withWidget(({ potterS, setPotterS, potterSpell, setPotterSpell, potterCharacter, setPotterCharacter,
    weatherS, setWeatherS, weatherW, setWeatherW,
    chuckS, setChuckS, chuckW, setChuckW,
    movieS, setMovieS, movieW, setMovieW,
    jinkanS, setJinkanS, jinkanAnime, setJinkanAnime, jinkanCharacter, setJinkanCharacter }) => (
        <View style={styles.container} >
            <Fragment>
                <ScrollView style={styles.container} contentContainerStyle={styles.contentContainer}>
                    <MyCard title="Harry Potter Service" value={potterS} setValue={setPotterS}
                        widget={<PotterService potterS={potterS} spell={potterSpell} setSpell={setPotterSpell} character={potterCharacter} setCharacter={setPotterCharacter} />}
                    />
                    <MyCard title="Weather Service" value={weatherS} setValue={setWeatherS}
                        widget={<WeatherService weatherS={weatherS} weatherW={weatherW} setWeatherW={setWeatherW} />}
                    />
                    <MyCard title="Chuck Norris Service" value={chuckS} setValue={setChuckS}
                        widget={<ChuckService chuckS={chuckS} chuckW={chuckW} setChuckW={setChuckW} />}
                    />
                    <MyCard title="The Movie Database Service" value={movieS} setValue={setMovieS}
                        widget={<MovieService movieS={movieS} movieW={movieW} setMovieW={setMovieW} />}
                    />
                    <MyCard title="Jinkan Service" value={jinkanS} setValue={setJinkanS}
                        widget={<JinkanService jinkanS={jinkanS} jinkanAnime={jinkanAnime} setJinkanAnime={setJinkanAnime} jinkanCharacter={jinkanCharacter} setJinkanCharacter={setJinkanCharacter} />}
                    />
                </ScrollView>
            </Fragment>
        </View >
    ));

const styles = StyleSheet.create({
    container: {
        flex: 1,
        backgroundColor: '#fff',
    },
    contentContainer: {
        paddingTop: 30,
    },
    getStartedContainer: {
        alignItems: 'center',
        marginHorizontal: 50,
    },
});
