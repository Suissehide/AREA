import React from 'react';
import ReactDOM from 'react-dom';
import {Route, BrowserRouter as Router, Switch, Redirect} from 'react-router-dom'

import './css/index.css';

import UserAuth from "./services/UserAuth";
import Home from './views/Home'
import Login from "./views/Login";
import Notfound from "./views/NotFound";
import Notifications from "./views/Notifications";

import * as serviceWorker from './serviceWorker';

const PrivateRoute = ({ component: Component, ...rest }) => (
    <Route {...rest} render={(props) => (
        UserAuth.isAuthenticated === 'true'
            ? <Component {...props} />
            : <Redirect to={{
                pathname: '/login',
                state: { from: props.location }
            }} />
    )} />
);

class Index extends React.Component {

    render () {
        return (
            <Router>
                <div className={"container"}>
                    <Switch>
                        <PrivateRoute exact activeClassName="active" path="/" component={Login}/>
                        <PrivateRoute activeClassName="active" path="/home" component={Home}/>
                        <PrivateRoute activeClassName="active" path="/notifications" component={Notifications}/>
                        <Route activeClassName="active" path="/login" component={Login}/>
                        <Route activeClassName="active" component={Notfound}/>
                    </Switch>
                </div>
            </Router>
        );
    }
}

ReactDOM.render(<Index />, document.getElementById('root'));

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();
