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
});

class WidgetProvider extends Component {
    state = {
        ip: "localhost",
        //
        potterS: false,
        setPotterS: value => { this.setState({ potterS: value }) },
        potterSpell: false,
        setPotterSpell: value => { this.setState({ potterSpell: value }) },
        potterCharacter: false,
        setPotterCharacter: value => { this.setState({ potterCharacter: value }) },
        //
        weatherS: true,
        setWeatherS: (value) => { this.setState({ weatherS: value }) },
        weatherW: true,
        setWeatherW: (value) => { this.setState({ weatherW: value }) },
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