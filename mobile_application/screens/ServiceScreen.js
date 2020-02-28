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

export default withWidget(({ potter, setPotterService, setPotterSpell, setPotterCharacter,
    weather, setWeatherService, setWeatherWidget, chuck, setChuckService, setChuckWidget,
    movie, setMovieService, setMovieWidget,
    jinkan, setJinkanService, setJinkanAnime, setJinkanCharacter }) => (
        <View style={styles.container} >
            <Fragment>
                <ScrollView style={styles.container} contentContainerStyle={styles.contentContainer}>
                    <MyCard title="Harry Potter Service" value={potter.service} setValue={setPotterService}
                        widget={<PotterService potter={potter} setSpell={setPotterSpell} setCharacter={setPotterCharacter} />}
                    />
                    <MyCard title="Weather Service" value={weather.service} setValue={setWeatherService}
                        widget={<WeatherService weather={weather} setWeatherW={setWeatherWidget} />}
                    />
                    <MyCard title="Chuck Norris Service" value={chuck.service} setValue={setChuckService}
                        widget={<ChuckService chuck={chuck} setChuckW={setChuckWidget} />}
                    />
                    <MyCard title="The Movie Database Service" value={movie.service} setValue={setMovieService}
                        widget={<MovieService movie={movie} setMovieW={setMovieWidget} />}
                    />
                    <MyCard title="Jinkan Service" value={jinkan.service} setValue={setJinkanService}
                        widget={<JinkanService jinkan={jinkan} setJinkanAnime={setJinkanAnime} setJinkanCharacter={setJinkanCharacter} />}
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
