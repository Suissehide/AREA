import React, { createContext, Component } from "react";

export const WidgetContext = createContext({
    ip: "localhost",
    isLogged: false,
    setIsLogged: () => { },
    token: 1,
    setToken: () => { },
    //
    potter: { service: false, spell: true, character: true, },
    setPotterService: () => { },
    setPotterSpell: () => { },
    setPotterCharacter: () => { },
    //
    weather: { service: false, widget: false, },
    setWeatherService: () => { },
    setWeatherWidget: () => { },
    //
    chuck: { service: true, widget: true, },
    setChuckService: () => { },
    setChuckWidget: () => { },
    //
    movie: { service: true, widget: true, },
    setMovieService: () => { },
    setMovieWidget: () => { },
    //
    jikan: { service: true, anime: true, character: true, },
    setJikanService: () => { },
    setJikanAnime: () => { },
    setJikanCharacter: () => { },
    //
    google: { service: true, ip: false, distance: false },
    setGoogleService: () => { },
    setGoogleIp: () => { },
    setGoogleDistance: () => { },
});

class WidgetProvider extends Component {
    state = {
        ip: "172.20.10.5:8080",
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

        jikan: { service: false, anime: false, character: true, },
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

        google: { service: true, ip: true, distance: false },
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