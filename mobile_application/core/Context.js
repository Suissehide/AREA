import React, { Component, createContext } from "react";

export const WidgetContext = createContext({
    ip: "localhost",
    isLogged: false,
    setIsLogged: () => { },
    token: 1,
    setToken: () => { },
    //
    potter: { service: false, spell: false, character: false, },
    setPotterService: () => { },
    setPotterSpell: () => { },
    setPotterCharacter: () => { },
    //
    weather: { service: false, widget: false, },
    setWeatherService: () => { },
    setWeatherWidget: () => { },
    //
    chuck: { service: false, widget: false, },
    setChuckService: () => { },
    setChuckWidget: () => { },
    //
    movie: { service: false, widget: false, },
    setMovieService: () => { },
    setMovieWidget: () => { },
    //
    jikan: { service: false, anime: false, character: false, topAnime: false, topManga: false },
    setJikanService: () => { },
    setJikanAnime: () => { },
    setJikanCharacter: () => { },
    setJikanTopAnime: () => { },
    setJikanTopManga: () => { },
    //
    google: { service: false, ip: false, distance: false, place: false },
    setGoogleService: () => { },
    setGoogleIp: () => { },
    setGoogleDistance: () => { },
    setGooglePlace: () => { },
    //
    joke: { service: false, widget: false },
    setJokeService: () => { },
    setJokeWidget: () => { },
    //
    pokemon: { service: false, detail: false, moves: false },
    setPokemonService: () => { },
    setPokemonDetail: () => { },
    setPokemonMoves: () => { },
    //
    picture: { service: false, widget: false },
    setPictureService: () => { },
    setPictureWidget: () => { },
    //
    news: { service: false, banana: false, theme: false },
    setNewsService: () => { },
    setNewsBanana: () => { },
    setNewsTheme: () => { },
    //
    hero: { service: false, random: false, name: false },
    setHeroService: () => { },
    setHeroRandom: () => { },
    setHeroName: () => { },
    //
    facebook: { service: false, widget: false },
    setFacebookService: () => { },
    setFacebookWidget: () => { },
    //
    microsoft: { service: false, calendar: false, contacts: false, drive: false, graph: false, outlook: false },
    setMicrosoftService: () => { },
    setMicrosoftCalendar: () => { },
    setMicrosoftContacts: () => { },
    setMicrosoftDrive: () => { },
    setMicrosoftGraph: () => { },
    setMicrosoftOutlook: () => { },
    //
    iss: { service: false, location: false, person: false },
    setIssService: () => { },
    setIssLocation: () => { },
    setIssPerson: () => { },
    //
    starwars: { service: false, people: false, planet: false },
    setStarwarsService: () => { },
    setStarwarsPeople: () => { },
    setStarwarsPlanet: () => { },
});

class WidgetProvider extends Component {
    state = {
        ip: "10.10.253.77:8080",
        isLogged: true,
        setIsLogged: (value) => { this.setState({ isLogged: value }) },
        token: 6,
        setToken: (value) => { this.setState({ token: value }) },

        potter: { service: false, spell: true, character: true, },
        setPotterService: (value) => {
            this.setState(prevState => ({
                potter: { ...prevState.potter, service: value, }
            }))
        },
        setPotterSpell: (value) => {
            this.setState(prevState => ({
                potter: { ...prevState.potter, spell: value, }
            }))
        },
        setPotterCharacter: (value) => {
            this.setState(prevState => ({
                potter: { ...prevState.potter, character: value, }
            }))
        },

        weather: { service: false, widget: true, },
        setWeatherService: (value) => {
            this.setState(prevState => ({
                weather: { ...prevState.weather, service: value, }
            }))
        },
        setWeatherWidget: (value) => {
            this.setState(prevState => ({
                weather: { ...prevState.weather, widget: value, }
            }))
        },

        chuck: { service: false, widget: true, },
        setChuckService: (value) => {
            this.setState(prevState => ({
                chuck: { ...prevState.chuck, service: value, }
            }))
        },
        setChuckWidget: (value) => {
            this.setState(prevState => ({
                chuck: { ...prevState.chuck, widget: value, }
            }))
        },

        movie: { service: false, widget: true, },
        setMovieService: (value) => {
            this.setState(prevState => ({
                movie: { ...prevState.movie, service: value, }
            }))
        },
        setMovieWidget: (value) => {
            this.setState(prevState => ({
                movie: { ...prevState.movie, widget: value, }
            }))
        },

        jikan: { service: false, anime: true, character: true, topAnime: true, topManga: true },
        setJikanService: (value) => {
            this.setState(prevState => ({
                jikan: { ...prevState.jikan, service: value, }
            }))
        },
        setJikanAnime: (value) => {
            this.setState(prevState => ({
                jikan: { ...prevState.jikan, anime: value, }
            }))
        },
        setJikanCharacter: (value) => {
            this.setState(prevState => ({
                jikan: { ...prevState.jikan, character: value, }
            }))
        },
        setJikanTopAnime: (value) => {
            this.setState(prevState => ({
                jikan: { ...prevState.jikan, topAnime: value, }
            }))
        },
        setJikanTopManga: (value) => {
            this.setState(prevState => ({
                jikan: { ...prevState.jikan, topManga: value, }
            }))
        },

        google: { service: false, ip: true, distance: true, place: true },
        setGoogleService: (value) => {
            this.setState(prevState => ({
                google: { ...prevState.google, service: value, }
            }))
        },
        setGoogleIp: (value) => {
            this.setState(prevState => ({
                google: { ...prevState.google, ip: value, }
            }))
        },
        setGoogleDistance: (value) => {
            this.setState(prevState => ({
                google: { ...prevState.google, distance: value, }
            }))
        },
        setGooglePlace: (value) => {
            this.setState(prevState => ({
                google: { ...prevState.google, place: value, }
            }))
        },

        joke: { service: false, widget: true },
        setJokeService: (value) => {
            this.setState(prevState => ({
                joke: { ...prevState.joke, service: value, }
            }))
        },
        setJokeWidget: (value) => {
            this.setState(prevState => ({
                joke: { ...prevState.joke, widget: value, }
            }))
        },

        pokemon: { service: false, detail: true, moves: true },
        setPokemonService: (value) => {
            this.setState(prevState => ({
                pokemon: { ...prevState.pokemon, service: value, }
            }))
        },
        setPokemonDetail: (value) => {
            this.setState(prevState => ({
                pokemon: { ...prevState.pokemon, detail: value, }
            }))
        },
        setPokemonMoves: (value) => {
            this.setState(prevState => ({
                pokemon: { ...prevState.pokemon, moves: value, }
            }))
        },

        picture: { service: false, widget: true },
        setPictureService: (value) => {
            this.setState(prevState => ({
                picture: { ...prevState.picture, service: value, }
            }))
        },
        setPictureWidget: (value) => {
            this.setState(prevState => ({
                picture: { ...prevState.picture, widget: value, }
            }))
        },

        news: { service: false, banana: true, theme: true },
        setNewsService: (value) => {
            this.setState(prevState => ({
                news: { ...prevState.news, service: value, }
            }))
        },
        setNewsBanana: (value) => {
            this.setState(prevState => ({
                news: { ...prevState.news, banana: value, }
            }))
        },
        setNewsTheme: (value) => {
            this.setState(prevState => ({
                news: { ...prevState.news, theme: value, }
            }))
        },

        hero: { service: false, random: true, name: true },
        setHeroService: (value) => {
            this.setState(prevState => ({
                hero: { ...prevState.hero, service: value, }
            }))
        },
        setHeroRandom: (value) => {
            this.setState(prevState => ({
                hero: { ...prevState.hero, random: value, }
            }))
        },
        setHeroName: (value) => {
            this.setState(prevState => ({
                hero: { ...prevState.hero, name: value, }
            }))
        },

        facebook: { service: false, widget: true },
        setFacebookService: (value) => {
            this.setState(prevState => ({
                facebook: { ...prevState.facebook, service: value, }
            }))
        },
        setFacebookWidget: (value) => {
            this.setState(prevState => ({
                facebook: { ...prevState.facebook, widget: value, }
            }))
        },

        microsoft: { service: false, calendar: true, contacts: true, drive: true, graph: true, outlook: true },
        setMicrosoftService: (value) => {
            this.setState(prevState => ({
                microsoft: { ...prevState.microsoft, service: value, }
            }))
        },
        setMicrosoftCalendar: (value) => {
            this.setState(prevState => ({
                microsoft: { ...prevState.microsoft, calendar: value, }
            }))
        },
        setMicrosoftContacts: (value) => {
            this.setState(prevState => ({
                microsoft: { ...prevState.microsoft, contacts: value, }
            }))
        },
        setMicrosoftDrive: (value) => {
            this.setState(prevState => ({
                microsoft: { ...prevState.microsoft, drive: value, }
            }))
        },
        setMicrosoftGraph: (value) => {
            this.setState(prevState => ({
                microsoft: { ...prevState.microsoft, graph: value, }
            }))
        },
        setMicrosoftOutlook: (value) => {
            this.setState(prevState => ({
                microsoft: { ...prevState.microsoft, outlook: value, }
            }))
        },

        iss: { service: true, location: true, person: true },
        setIssService: (value) => {
            this.setState(prevState => ({
                iss: { ...prevState.iss, service: value, }
            }))
        },
        setIssLocation: (value) => {
            this.setState(prevState => ({
                iss: { ...prevState.iss, location: value, }
            }))
        },
        setIssPerson: (value) => {
            this.setState(prevState => ({
                iss: { ...prevState.iss, person: value, }
            }))
        },

        starwars: { service: false, people: true, planet: true },
        setStarwarsService: (value) => {
            this.setState(prevState => ({
                starwars: { ...prevState.starwars, service: value, }
            }))
        },
        setStarwarsPeople: (value) => {
            this.setState(prevState => ({
                starwars: { ...prevState.starwars, people: value, }
            }))
        },
        setStarwarsPlanet: (value) => {
            this.setState(prevState => ({
                starwars: { ...prevState.starwars, planet: value, }
            }))
        },

    };

    render() {
        return (
            <WidgetContext.Provider value={this.state}>
                {this.props.children}
            </WidgetContext.Provider>
        );
    }
}

export const withWidget = Component => props => (
    <WidgetContext.Consumer>
        {store => <Component {...props} {...store} />}
    </WidgetContext.Consumer>
);

export default WidgetProvider;