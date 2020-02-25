import React, { createContext, Component } from "react";

export const WidgetContext = createContext({
    potterS: false,
    setPotterS: () => { },
    potterSpell: true,
    setPotterSpell: () => { },
    potterCharacters: true,
    setPotterCharacter: () => { },
    //
    weatherS: false,
    setWeatherS: () => { },
});

class WidgetProvider extends Component {
    state = {
        potterS: true,
        setPotterS: value => { this.setState({ potterS: value }) },
        potterSpell: false,
        setPotterSpell: value => { this.setState({ potterSpell: value }) },
        potterCharacters: false,
        setPotterCharacter: value => { this.setState({ potterCharacters: value }) },
        //
        weatherS: false,
        setWeatherS: (value) => { this.setState({ weatherS: value }) },

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