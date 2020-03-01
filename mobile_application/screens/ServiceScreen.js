import React, { Fragment } from "react";
import { StyleSheet, View } from 'react-native';
import { KeyboardAwareScrollView } from 'react-native-keyboard-aware-scroll-view'
import { withWidget } from "../core/Context";
import Service from '../components/CardService';
import Background from '../components/Background';

export default withWidget(({ potter, setPotterService, setPotterSpell, setPotterCharacter,
    weather, setWeatherService, setWeatherWidget, chuck, setChuckService, setChuckWidget,
    movie, setMovieService, setMovieWidget, joke, setJokeService, setJokeWidget,
    jikan, setJikanService, setJikanAnime, setJikanCharacter, setJikanTopAnime, setJikanTopManga,
    google, setGoogleService, setGoogleIp, setGoogleDistance,
    pokemon, setPokemonService, setPokemonWidget, }) => (
        <Background>
            <Fragment>
                <KeyboardAwareScrollView style={styles.container} contentContainerStyle={styles.contentContainer}>
                    <View style={{ width: '90%' }}>

                        <Service title="Harry Potter Service" service={potter} setService={setPotterService}
                            widget={potter.spell} setWidget={setPotterSpell} widgetTitle="Display a random spell"
                            w2={potter.character} setW2={setPotterCharacter} t2="Display a random character" />

                        <Service title="Weather Service" service={weather} setService={setWeatherService}
                            setWidget={setWeatherWidget} widgetTitle="Get the weather of a city" />

                        <Service title="Chuck Norris Service" service={chuck} setService={setChuckService}
                            setWidget={setChuckWidget} widgetTitle="Get 3 themed Chuck Norris jokes" />

                        <Service title={"The Movie Database" + "\n" + "Service"} service={movie} setService={setMovieService}
                            setWidget={setMovieWidget} widgetTitle="Get information on a movie" />

                        <Service title="Jikan Service" service={jikan} setService={setJikanService}
                            widget={jikan.anime} setWidget={setJikanAnime} widgetTitle="Get informations on an anime"
                            w2={jikan.character} setW2={setJikanCharacter} t2="Get informations on a character"
                            w3={jikan.topAnime} setW3={setJikanTopAnime} t3="Display the highest scored animes"
                            w4={jikan.topManga} setW4={setJikanTopManga} t4="Display the highest scored mangas" />

                        <Service title="Google Service" service={google} setService={setGoogleService}
                            widget={google.ip} setWidget={setGoogleIp} widgetTitle={"Display your localisation depending" + "\n" + "on your IP"}
                            w2={google.distance} setW2={setGoogleDistance} t2={"Get the distance and time between" + "\n" + "two points"} />

                        <Service title="Joke Service" service={joke} setService={setJokeService}
                            setWidget={setJokeWidget} widgetTitle="Get a random themed joke" />

                        <Service title="Pokemon Service" service={pokemon} setService={setPokemonService}
                            setWidget={setPokemonWidget} widgetTitle="Get informations on a Pokemon" />

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
    }
});
