import React, { Fragment, useEffect } from 'react';
import { StyleSheet, View } from 'react-native';
import { KeyboardAwareScrollView } from 'react-native-keyboard-aware-scroll-view';
import Background from '../components/Background';
import Service from '../components/CardServiceTemplate';
import { withWidget } from '../core/Context';

export default withWidget((props) => (
    <Background>
        <Fragment>
            <KeyboardAwareScrollView style={styles.container} contentContainerStyle={styles.contentContainer}>
                <View style={{ width: '90%' }}>
                    <Service title="Chuck Norris Service" service={props.chuck} setService={props.setChuckService}
                        setWidget={props.setChuckWidget} widgetTitle="Themed Chuck Norris Jokes" />

                    <Service title="Facebook Service" service={props.facebook} setService={props.setFacebookService}
                        setWidget={props.setFacebookWidget} widgetTitle="Liked Pages" />

                    <Service title="Google Service" service={props.google} setService={props.setGoogleService}
                        widget={props.google.ip} setWidget={props.setGoogleIp} widgetTitle={"Your IP Location"}
                        w2={props.google.distance} setW2={props.setGoogleDistance} t2={"Distance and Time between 2 Spots"}
                        w3={props.google.place} setW3={props.setGooglePlace} t3={"Place Information"} />

                    <Service title="Superhero Service" service={props.hero} setService={props.setHeroService}
                        widget={props.hero.random} setWidget={props.setHeroRandom} widgetTitle="Random Superhero"
                        w2={props.hero.name} setW2={props.setHeroName} t2={"Your Superhero"} />

                    <Service title="ISS Service" service={props.iss} setService={props.setIssService}
                        widget={props.iss.location} setWidget={props.setIssLocation} widgetTitle="ISS Location"
                        w2={props.iss.person} setW2={props.setIssPerson} t2={"People in Space"} />

                    <Service title="Jikan Service" service={props.jikan} setService={props.setJikanService}
                        widget={props.jikan.anime} setWidget={props.setJikanAnime} widgetTitle="Anime Information"
                        w2={props.jikan.character} setW2={props.setJikanCharacter} t2="Character Information"
                        w3={props.jikan.topAnime} setW3={props.setJikanTopAnime} t3="Highest Scored Animes"
                        w4={props.jikan.topManga} setW4={props.setJikanTopManga} t4="Highest Scored Mangas" />

                    <Service title="Joke Service" service={props.joke} setService={props.setJokeService}
                        setWidget={props.setJokeWidget} widgetTitle="Themed Joke" />

                    <Service title="Microsoft Service" service={props.microsoft} setService={props.setMicrosoftService}
                        widget={props.microsoft.calendar} setWidget={props.setMicrosoftCalendar} widgetTitle="Calendar Events"
                        w2={props.microsoft.contacts} setW2={props.setMicrosoftContacts} t2="Contact List"
                        w3={props.microsoft.drive} setW3={props.setMicrosoftDrive} t3="OneDrive Items"
                        w4={props.microsoft.graph} setW4={props.setMicrosoftGraph} t4={"Microsoft Account Information"}
                        w5={props.microsoft.outlook} setW5={props.setMicrosoftOutlook} t5="Outlook Mails" />

                    <Service title={"The Movie Database" + "\n" + "Service"} service={props.movie} setService={props.setMovieService}
                        setWidget={props.setMovieWidget} widgetTitle="Movie Information" />

                    <Service title="News Service" service={props.news} setService={props.setNewsService}
                        widget={props.news.banana} setWidget={props.setNewsBanana} widgetTitle="Bananews"
                        w2={props.news.theme} setW2={props.setNewsTheme} t2="Themed News" />

                    <Service title={"Picture Database Service"} service={props.picture} setService={props.setPictureService}
                        setWidget={props.setPictureWidget} widgetTitle="Themed Picture" />

                    <Service title="Pokemon Service" service={props.pokemon} setService={props.setPokemonService}
                        widget={props.pokemon.detail} setWidget={props.setPokemonDetail} widgetTitle="Pokemon Information"
                        w2={props.pokemon.moves} setW2={props.setPokemonMoves} t2="Pokemon Abilites" />

                    <Service title="Harry Potter Service" service={props.potter} setService={props.setPotterService}
                        widget={props.potter.spell} setWidget={props.setPotterSpell} widgetTitle="Random Spell"
                        w2={props.potter.character} setW2={props.setPotterCharacter} t2="Random Character" />

                    <Service title="Star Wars Service" service={props.starwars} setService={props.setStarwarsService}
                        widget={props.starwars.people} setWidget={props.setStarwarsPeople} widgetTitle="Random Character"
                        w2={props.starwars.planet} setW2={props.setStarwarsPlanet} t2="Random Planet" />

                    <Service title="Weather Service" service={props.weather} setService={props.setWeatherService}
                        setWidget={props.setWeatherWidget} widgetTitle="City Weather" />
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
