import React, { Fragment } from "react";
import { StyleSheet, View } from 'react-native';
import { KeyboardAwareScrollView } from 'react-native-keyboard-aware-scroll-view'
import { withWidget } from "../core/Context";
import MyCard from '../components/CardService';
import Background from '../components/Background';
import PotterService from '../services/PotterService';
import WeatherService from '../services/WeatherService';
import ChuckService from '../services/ChuckService';
import MovieService from '../services/MovieService';
import JikanService from '../services/JikanService';
import GoogleService from '../services/GoogleService';

export default withWidget(({ potter, setPotterService, setPotterSpell, setPotterCharacter,
    weather, setWeatherService, setWeatherWidget, chuck, setChuckService, setChuckWidget,
    movie, setMovieService, setMovieWidget,
    jikan, setJikanService, setJikanAnime, setJikanCharacter,
    google, setGoogleService, setGoogleIp, setGoogleDistance,
}) => (
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
                        <MyCard title={"The Movie Database" + "\n" + "Service"} value={movie.service} setValue={setMovieService}
                            widget={<MovieService movie={movie} setMovieW={setMovieWidget} />}
                        />
                        <MyCard title="Jikan Service" value={jikan.service} setValue={setJikanService}
                            widget={<JikanService jikan={jikan} setJikanAnime={setJikanAnime} setJikanCharacter={setJikanCharacter} />}
                        />
                        <MyCard title="Google Service" value={google.service} setValue={setGoogleService}
                            widget={<GoogleService google={google} setGoogleIp={setGoogleIp} setGoogleDistance={setGoogleDistance} />}
                        />
                    </View>
                </KeyboardAwareScrollView>
            </Fragment>
        </Background>
    ));

const styles = StyleSheet.create({
    container: {
        flex: 1,
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
