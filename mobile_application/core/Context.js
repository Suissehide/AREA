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
    google: { service: false, ip: false, distance: false },
    setGoogleService: () => { },
    setGoogleIp: () => { },
    setGoogleDistance: () => { },
    //
    joke: { service: false, widget: false },
    setJokeService: () => { },
    setJokeWidget: () => { },
    //
    pokemon: { service: false, widget: false },
    setPokemonService: () => { },
    setPokemonWidget: () => { },
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
});

class WidgetProvider extends Component {
    state = {
        ip: "172.20.10.5:8080",
        isLogged: true,
        setIsLogged: (value) => { this.setState({ isLogged: value }) },
        token: 6,
        setToken: (value) => { this.setState({ token: value }) },

        potter: { service: false, spell: false, character: false, },
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

        weather: { service: false, widget: false, },
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

        chuck: { service: false, widget: false, },
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

        movie: { service: false, widget: false, },
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

        jikan: { service: false, anime: false, character: false, topAnime: false, topManga: false },
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

        google: { service: false, ip: false, distance: false },
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

        joke: { service: false, widget: false },
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

        pokemon: { service: false, widget: false },
        setPokemonService: (value) => {
            this.setState(prevState => ({
                pokemon: { ...prevState.pokemon, service: value, }
            }))
        },
        setPokemonWidget: (value) => {
            this.setState(prevState => ({
                pokemon: { ...prevState.pokemon, widget: value, }
            }))
        },

        picture: { service: false, widget: false },
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

        news: { service: false, banana: false, theme: false },
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

        hero: { service: true, random: true, name: true },
        setHeroService: (value) => {
            this.setState(prevState => ({
                hero: { ...prevState.news, service: value, }
            }))
        },
        setHeroRandom: (value) => {
            this.setState(prevState => ({
                hero: { ...prevState.news, random: value, }
            }))
        },
        setHeroName: (value) => {
            this.setState(prevState => ({
                hero: { ...prevState.news, name: value, }
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