import React, { Fragment } from 'react';
import { StyleSheet, View } from 'react-native';
import { KeyboardAwareScrollView } from 'react-native-keyboard-aware-scroll-view';
import Background from '../components/Background';
import Service from '../components/CardServiceTemplate';
import { withWidget } from '../core/Context';

export default withWidget(({ potter, setPotterService, setPotterSpell, setPotterCharacter,
    weather, setWeatherService, setWeatherWidget, chuck, setChuckService, setChuckWidget,
    movie, setMovieService, setMovieWidget, joke, setJokeService, setJokeWidget,
    jikan, setJikanService, setJikanAnime, setJikanCharacter, setJikanTopAnime, setJikanTopManga,
    google, setGoogleService, setGoogleIp, setGoogleDistance, facebook, setFacebookService, setFacebookWidget,
    pokemon, setPokemonService, setPokemonDetail, setPokemonMoves, picture, setPictureService, setPictureWidget,
    news, setNewsService, setNewsBanana, setNewsTheme, hero, setHeroService, setHeroRandom, setHeroName,
    microsoft, setMicrosoftService, setMicrosoftCalendar, setMicrosoftContacts, setMicrosoftDrive, setMicrosoftGraph, setMicrosoftOutlook,
}) => (
        <Background>
            <Fragment>
                <KeyboardAwareScrollView style={styles.container} contentContainerStyle={styles.contentContainer}>
                    <View style={{ width: '90%' }}>

                        <Service title="Chuck Norris Service" service={chuck} setService={setChuckService}
                            setWidget={setChuckWidget} widgetTitle="Get 3 themed Chuck Norris jokes" />

                        <Service title="Facebook Service" service={facebook} setService={setFacebookService}
                            setWidget={setFacebookWidget} widgetTitle="Display your liked contents" />

                        <Service title="Google Service" service={google} setService={setGoogleService}
                            widget={google.ip} setWidget={setGoogleIp} widgetTitle={"Display your localisation depending" + "\n" + "on your IP"}
                            w2={google.distance} setW2={setGoogleDistance} t2={"Get the distance and time between" + "\n" + "two points"} />

                        <Service title="Superhero Service" service={hero} setService={setHeroService}
                            widget={hero.random} setWidget={setHeroRandom} widgetTitle="Display a random superhero"
                            w2={hero.name} setW2={setHeroName} t2={"Display a information about your" + "\n" + "superhero"} />

                        <Service title="Jikan Service" service={jikan} setService={setJikanService}
                            widget={jikan.anime} setWidget={setJikanAnime} widgetTitle="Get informations on an anime"
                            w2={jikan.character} setW2={setJikanCharacter} t2="Get informations on a character"
                            w3={jikan.topAnime} setW3={setJikanTopAnime} t3="Display the highest scored animes"
                            w4={jikan.topManga} setW4={setJikanTopManga} t4="Display the highest scored mangas" />

                        <Service title="Joke Service" service={joke} setService={setJokeService}
                            setWidget={setJokeWidget} widgetTitle="Get a random themed joke" />

                        <Service title="Microsoft Service" service={microsoft} setService={setMicrosoftService}
                            widget={microsoft.calendar} setWidget={setMicrosoftCalendar} widgetTitle="Display your upcoming events"
                            w2={microsoft.contacts} setW2={setMicrosoftContacts} t2="Display your contacts"
                            w3={microsoft.drive} setW3={setMicrosoftDrive} t3="Display items in your drive"
                            w4={microsoft.graph} setW4={setMicrosoftGraph} t4={"Display your microsoft account" + "\n" + "informations"}
                            w5={microsoft.outlook} setW5={setMicrosoftOutlook} t5="Display your mails" />

                        <Service title={"The Movie Database" + "\n" + "Service"} service={movie} setService={setMovieService}
                            setWidget={setMovieWidget} widgetTitle="Get information on a movie" />

                        <Service title="News Service" service={news} setService={setNewsService}
                            widget={news.banana} setWidget={setNewsBanana} widgetTitle="Display news about bananas"
                            w2={news.theme} setW2={setNewsTheme} t2="Display themed news" />

                        <Service title={"Picture Database Service"} service={picture} setService={setPictureService}
                            setWidget={setPictureWidget} widgetTitle="Get a themed picture" />

                        <Service title="Pokemon Service" service={pokemon} setService={setPokemonService}
                            widget={pokemon.detail} setWidget={setPokemonDetail} widgetTitle="Get informations on a Pokemon"
                            w2={pokemon.moves} setW2={setPokemonMoves} t2="Get informations on a Pokemon" />

                        <Service title="Harry Potter Service" service={potter} setService={setPotterService}
                            widget={potter.spell} setWidget={setPotterSpell} widgetTitle="Display a random spell"
                            w2={potter.character} setW2={setPotterCharacter} t2="Display a random character" />

                        <Service title="Weather Service" service={weather} setService={setWeatherService}
                            setWidget={setWeatherWidget} widgetTitle="Get the weather of a city" />
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
