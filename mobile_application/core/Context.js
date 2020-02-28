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
    jinkan: { service: true, anime: true, character: true, },
    setJinkanService: () => { },
    setJinkanAnime: () => { },
    setJinkanCharacter: () => { },
    //
});

class WidgetProvider extends Component {
    state = {
        ip: "172.20.10.2",
        isLogged: false,
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

        jinkan: { service: true, anime: false, character: true, },
        setJinkanService: (value) => {
            this.setState(prevState => ({
                jinkan: { ...prevState.jinkan, service: value, }
            }))
        },
        setJinkanAnime: (value) => {
            this.setState(prevState => ({
                jinkan: { ...prevState.jinkan, anime: value, }
            }))
        },
        setJinkanCharacter: (value) => {
            this.setState(prevState => ({
                jinkan: { ...prevState.jinkan, character: value, }
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