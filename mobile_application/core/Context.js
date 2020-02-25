import React, { createContext, Component } from "react";

export const UserContext = createContext({
    name: "",
    setName: () => { },
    activated: false,
    setActivated: () => { },
});

class UserProvider extends Component {
    state = {
        name: "Random",
        setName: name => this.setState({ name: name }),
        activated: false,
        setActivated: activated => this.setState({ activated: activated }),
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
