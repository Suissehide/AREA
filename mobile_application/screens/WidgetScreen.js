import React, { Fragment } from 'react';
import { StyleSheet } from 'react-native';
import { KeyboardAwareScrollView } from 'react-native-keyboard-aware-scroll-view';
import Background from '../components/Background';
import Widget from '../components/WidgetTemplate';
import { withWidget } from '../core/Context';
import * as W from './widgets';

export default withWidget((props) => (
    <Background>
        <Fragment>
            <KeyboardAwareScrollView style={styles.container}>

                {props.chuck.service === true && props.chuck.widget === true ?
                    <Widget title="Latest Chuck Norris Jokes" widget={<W.ChuckWidget ip={props.ip} />} /> : null}
                {props.facebook.service === true && props.facebook.widget === true ?
                    <Widget title="Facebook Likes" widget={<W.FacebookWidget ip={props.ip} />} /> : null}
                {props.google.service === true && props.google.ip === true ?
                    <Widget title="Display your localisation depending on your IP" widget={<W.GoogleIpWidget ip={props.ip} />} /> : null}
                {props.google.service === true && props.google.distance === true ?
                    <Widget title="Calculate distance and duration between two places" widget={<W.GoogleDistanceWidget ip={props.ip} />} /> : null}
                {props.google.service === true && props.google.place === true ?
                    <Widget title="Information on a place" widget={<W.GooglePlaceWidget ip={props.ip} />} /> : null}
                {props.hero.service === true && props.hero.random === true ?
                    <Widget title="Random Superhero" widget={<W.HeroRandomWidget ip={props.ip} />} /> : null}
                {props.hero.service === true && props.hero.name === true ?
                    <Widget title="Information on your Superhero" widget={<W.HeroNameWidget ip={props.ip} />} /> : null}
                {props.iss.service === true && props.iss.location === true ?
                    <Widget title="ISS Location" widget={<W.IssLocationWidget ip={props.ip} />} /> : null}
                {props.iss.service === true && props.iss.person === true ?
                    <Widget title="People in Space" widget={<W.IssPersonWidget ip={props.ip} />} /> : null}
                {props.jikan.service === true && props.jikan.anime === true ?
                    <Widget title="Information on an Anime" widget={<W.JikanAnimeWidget ip={props.ip} />} /> : null}
                {props.jikan.service === true && props.jikan.character === true ?
                    <Widget title="Information on an Anime Character" widget={<W.JikanCharacterWidget ip={props.ip} />} /> : null}
                {props.jikan.service === true && props.jikan.topAnime === true ?
                    <Widget title="Top Animes" widget={<W.JikanTopAnimeWidget ip={props.ip} />} /> : null}
                {props.jikan.service === true && props.jikan.topManga === true ?
                    <Widget title="Top Mangas" widget={<W.JikanTopMangaWidget ip={props.ip} />} /> : null}
                {props.joke.service === true && props.joke.widget === true ?
                    <Widget title="Get a random themed joke" widget={<W.JokeWidget ip={props.ip} />} /> : null}
                {props.microsoft.service === true && props.microsoft.calendar === true ?
                    <Widget title="Calendar Events" widget={<W.MicrosoftCalendarWidget ip={props.ip} />} /> : null}
                {props.microsoft.service === true && props.microsoft.contacts === true ?
                    <Widget title="Microsoft Contacts" widget={<W.MicrosoftContactsWidget ip={props.ip} />} /> : null}
                {props.microsoft.service === true && props.microsoft.drive === true ?
                    <Widget title="Microsoft Drive" widget={<W.MicrosoftDriveWidget ip={props.ip} />} /> : null}
                {props.microsoft.service === true && props.microsoft.graph === true ?
                    <Widget title="Microsoft Graph" widget={<W.MicrosoftGraphWidget ip={props.ip} />} /> : null}
                {props.microsoft.service === true && props.microsoft.outlook === true ?
                    <Widget title="Microsoft Outlook" widget={<W.MicrosoftOutlookWidget ip={props.ip} />} /> : null}
                {props.movie.service === true && props.movie.widget === true ?
                    <Widget title="Information on a Movie" widget={<W.MovieWidget ip={props.ip} />} /> : null}
                {props.news.service === true && props.news.banana === true ?
                    <Widget title="Bananews" widget={<W.NewsBananaWidget ip={props.ip} />} /> : null}
                {props.news.service === true && props.news.theme === true ?
                    <Widget title="News" widget={<W.NewsThemeWidget ip={props.ip} />} /> : null}
                {props.picture.service === true && props.picture.widget === true ?
                    <Widget title="Themed Picture" widget={<W.PictureWidget ip={props.ip} />} /> : null}
                {props.pokemon.service === true && props.pokemon.detail === true ?
                    <Widget title="Get information on a Pokemon" widget={<W.PokemonDetailWidget ip={props.ip} />} /> : null}
                {props.pokemon.service === true && props.pokemon.moves === true ?
                    <Widget title="Get Pokemon's 5 random abilities" widget={<W.PokemonMovesWidget ip={props.ip} />} /> : null}
                {props.potter.service === true && props.potter.spell === true ?
                    <Widget title="Harry Potter's Random Spell" widget={<W.PotterSpellWidget ip={props.ip} />} /> : null}
                {props.potter.service === true && props.potter.character === true ?
                    <Widget title="Random Character from Harry Potter" widget={<W.PotterCharacterWidget ip={props.ip} />} /> : null}
                {props.starwars.service === true && props.starwars.people === true ?
                    <Widget title="Random Character from Star Wars" widget={<W.StarwarsCharacterWidget ip={props.ip} />} /> : null}
                {props.starwars.service === true && props.starwars.planet === true ?
                    <Widget title="Random Planet from Star Wars" widget={<W.StarwarsPlanetWidget ip={props.ip} />} /> : null}
                {props.weather.service === true && props.weather.widget === true ?
                    <Widget title="Weather by City" widget={<W.WeatherWidget ip={props.ip} />} /> : null}

            </KeyboardAwareScrollView>
        </Fragment>
    </Background>
));

const styles = StyleSheet.create({
    container: {
        flex: 1,
    },
});
