import React, { Fragment } from "react";
import { StyleSheet, View } from 'react-native';
import { withWidget } from "../core/Context";
import MyCard from '../components/CardService';
import PotterService from '../services/PotterService';
import WeatherService from '../services/WeatherService';
import ChuckService from '../services/ChuckService';
import MovieService from '../services/MovieService';
import JinkanService from '../services/JinkanService';
import Background from '../components/Background';
import { KeyboardAwareScrollView } from 'react-native-keyboard-aware-scroll-view'

export default withWidget(({ potter, setPotterService, setPotterSpell, setPotterCharacter,
    weather, setWeatherService, setWeatherWidget, chuck, setChuckService, setChuckWidget,
    movie, setMovieService, setMovieWidget,
    jinkan, setJinkanService, setJinkanAnime, setJinkanCharacter }) => (
        // <View style={styles.container} >
        <Background>
            <Fragment>
                <KeyboardAwareScrollView style={styles.container} contentContainerStyle={styles.contentContainer}>
                    <View style={{ width: '90%' }}>
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
                    </View>
                </KeyboardAwareScrollView>
            </Fragment>
        </Background>
        // </View>
    ));

const styles = StyleSheet.create({
    container: {
        flex: 1,
        // backgroundColor: '#fff',
        width: '100%',
    },
    contentContainer: {
        paddingTop: 30,
    },
    getStartedContainer: {
        alignItems: 'center',
        marginHorizontal: 50,
    },
});
