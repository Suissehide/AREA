import React, { createContext, Component } from "react";

export const UserContext = createContext({
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

class UserProvider extends Component {
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
            <UserContext.Provider value={this.state}>
                {this.props.children}
            </UserContext.Provider>
        );
    }
}

export const withUser = Component => props => (
    <UserContext.Consumer>
        {store => <Component {...props} {...store} />}
    </UserContext.Consumer>
);

export default UserProvider;