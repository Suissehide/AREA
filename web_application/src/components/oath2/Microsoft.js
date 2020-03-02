import React, { Component }  from 'react';
import qs from 'query-string';
import { BrowserRouter as Router, Route } from 'react-router-dom';
import { Container } from 'reactstrap';
import NavBar from './NavBar';
import ErrorMessage from './ErrorMessage';
import Welcome from './Welcome';

// import 'bootstrap/dist/css/bootstrap.css';

import config from './Config';
import { UserAgentApplication } from 'msal';
import { getUserDetails } from './GraphService';

class Microsoft extends React.Component {
    constructor(props) {
        super(props);

        this.userAgentApplication = new UserAgentApplication({
            auth: {
                clientId: config.appId,
                redirectUri: config.redirectUri
            },
            cache: {
                cacheLocation: "localStorage",
                storeAuthStateInCookie: true
            }
        });

        var user = this.userAgentApplication.getAccount();

        this.state = {
            isAuthenticated: (user !== null),
            user: {},
            error: null
        };

        if (user) {
            // Enhance user object with data from Graph
            this.getUserProfile();
        }
    }

    componentDidMount() {
        // const token = qs.parse(this.props.location.hash, { ignoreQueryPrefix: true }).access_token;
        // this._getJeton(token);
    }

    async login() {
        try {
            await this.userAgentApplication.loginPopup(
                {
                    scopes: config.scopes,
                    prompt: "select_account"
                });
            await this.getUserProfile();
        }
        catch(err) {
            var error = {};

            if (typeof(err) === 'string') {
                var errParts = err.split('|');
                error = errParts.length > 1 ?
                    { message: errParts[1], debug: errParts[0] } :
                    { message: err };
            } else {
                error = {
                    message: err.message,
                    debug: JSON.stringify(err)
                };
            }

            this.setState({
                isAuthenticated: false,
                user: {},
                error: error
            });
        }
    }

    logout() {
        this.userAgentApplication.logout();
    }

    async getUserProfile() {
        try {
            // Get the access token silently
            // If the cache contains a non-expired token, this function
            // will just return the cached token. Otherwise, it will
            // make a request to the Azure OAuth endpoint to get a token

            var accessToken = await this.userAgentApplication.acquireTokenSilent({
                scopes: config.scopes
            });

            if (accessToken) {
                // Get the user's profile from Graph
                var user = await getUserDetails(accessToken);
                this.setState({
                    isAuthenticated: true,
                    user: {
                        displayName: user.displayName,
                        email: user.mail || user.userPrincipalName
                    },
                    error: null
                });
            }
        }
        catch(err) {
            var error = {};
            if (typeof(err) === 'string') {
                var errParts = err.split('|');
                error = errParts.length > 1 ?
                    { message: errParts[1], debug: errParts[0] } :
                    { message: err };
            } else {
                error = {
                    message: err.message,
                    debug: JSON.stringify(err)
                };
            }

            this.setState({
                isAuthenticated: false,
                user: {},
                error: error
            });
        }
    }

    // _getJeton = async (token) => {
    //     if (!token)
    //         return;
    //
    //     const url = `https://login.microsoftonline.com/901cb4ca-b862-4029-9306-e5cd0f6d9f86/oauth2/v2.0/token`;
    //
    //     console.log(token);
    //
    //     await fetch(url, {
    //         method: "POST",
    //         headers: {
    //             // 'Access-Control-Allow-Origin': '*',
    //             // 'Access-Control-Allow-Headers': 'Origin, Content-Type, Accept, X-Auth-Token',
    //             // 'Access-Control-Allow-Credentials': 'true',
    //             // 'Access-Control-Request-Headers': 'Origin, X-Custom-Header, X-Requested-With, Authorization, Content-Type, Accept',
    //             // 'Access-Control-Expose-Headers': 'Content-Length, X-Kuma-Revision',
    //             // 'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, PATCH, OPTIONS',
    //             'Content-Type': 'application/x-www-form-urlencoded',
    //         },
    //         body: {
    //             'client_id': '04bd8816-75eb-4996-b663-fdce462165d1',
    //             'client_secret': '=h]2z.el1a79OYfarQD/aodAmmRkk=5T',
    //             'redirect_uri': 'http://localhost:3000/microsoft',
    //             'grant_type': 'authorization_code',
    //             'code': token,
    //             'scope': 'openid+Mail.Read',
    //         },
    //     })
    //         .then(response => {
    //             console.log(response)
    //         })
    //         .then(responseJson => {
    //             console.log(responseJson);
    //         })
    //         .catch(error => {
    //             this.setState({error, loading: false});
    //             console.error('Error: ', error);
    //         })
    // };

    render() {
        let error = null;
        if (this.state.error) {
            error = <ErrorMessage message={this.state.error.message} debug={this.state.error.debug} />;
        }

        return (
            <Router>
                <div>
                    <NavBar
                        isAuthenticated={this.state.isAuthenticated}
                        authButtonMethod={null}
                        user={this.state.user}/>
                    <Container>
                        {error}
                        <Route exact path="/"
                               render={(props) =>
                                   <Welcome {...props}
                                            isAuthenticated={this.state.isAuthenticated}
                                            user={this.state.user}
                                            authButtonMethod={null} />
                               } />
                    </Container>
                </div>
            </Router>
        );
    }

    setErrorMessage(message, debug) {
        this.setState({
            error: {message: message, debug: debug}
        });
    }
}

export default Microsoft
