import React, { createContext, Component } from "react";

export const WidgetContext = createContext({
    ip: "localhost",
    //
    potterS: false,
    setPotterS: () => { },
    potterSpell: true,
    setPotterSpell: () => { },
    potterCharacter: true,
    setPotterCharacter: () => { },
    //
    weatherS: false,
    setWeatherS: () => { },
    weatherW: false,
    setWeatherW: () => { },
    //
    chuckS: true,
    setChuckS: () => { },
    chuckW: true,
    setChuckW: () => { },
    //
    movieS: true,
    setMovieS: () => { },
    movieW: true,
    setMovieW: () => { },
    //
    jinkanS: true,
    setJinkanS: () => { },
    jinkanAnime: true,
    setJinkanAnime: () => { },
    jinkanCharacter: true,
    setJinkanCharacter: () => { },
    //
});

class WidgetProvider extends Component {
    state = {
        ip: "192.168.1.88",
        //
        potterS: false,
        setPotterS: value => { this.setState({ potterS: value }) },
        potterSpell: true,
        setPotterSpell: value => { this.setState({ potterSpell: value }) },
        potterCharacter: true,
        setPotterCharacter: value => { this.setState({ potterCharacter: value }) },
        //
        weatherS: false,
        setWeatherS: (value) => { this.setState({ weatherS: value }) },
        weatherW: true,
        setWeatherW: (value) => { this.setState({ weatherW: value }) },
        //
        chuckS: false,
        setChuckS: (value) => { this.setState({ chuckS: value }) },
        chuckW: true,
        setChuckW: (value) => { this.setState({ chuckW: value }) },
        //
        movieS: false,
        setMovieS: (value) => { this.setState({ movieS: value }) },
        movieW: true,
        setMovieW: (value) => { this.setState({ movieW: value }) },
        //
        jinkanS: true,
        setJinkanS: (value) => { this.setState({ jinkanS: value }) },
        jinkanAnime: true,
        setJinkanAnime: (value) => { this.setState({ jinkanAnime: value }) },
        jinkanCharacter: true,
        setJinkanCharacter: (value) => { this.setState({ jinkanCharacter: value }) },
        //
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