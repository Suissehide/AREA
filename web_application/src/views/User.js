import React from 'react';
import {withRouter} from 'react-router-dom'
import '../css/SideMenu.css';
import SideMenu from "../components/SideMenu";
import Sidebar from "../components/Navbar";
import Footer from "../components/Footer";
import UserAuth from "../services/UserAuth";

import config from '../services/Config';

import MicrosoftAuth from "../services/Microsoft/Microsoft";
import FacebookAuth from "../services/Facebook/Facebook";

const AuthButton = withRouter(({history}) => (
    <button className="submit warning-btn" onClick={() => {
        UserAuth.signout(() => history.push('/'));
        localStorage.clear();
    }}>
        Log out
    </button>
));

class User extends React.Component {
    state = {
        profile: false,
        error: '',

        username: '',
        email: '',
        password: '',
        id: '',

        tokenFacebook: '',
        usernameFacebook: '',

        tokenMicrosoft: '',
    };

    componentDidMount() {
        this._refresh();
    }

    _handleChange = (e) => {
        this.setState({[e.target.name]: e.target.value});
    };

    _refresh = async () => {
        const {email} = this.state;
        const url = `http://127.0.0.1:8080/database/users/${email}`;

        await fetch(url, {
            method: "GET",
            headers: {},
        })
            .then(response => response.json())
            .then(responseJson => {
                this.setState({
                    email: responseJson.users[0].email,
                    id: responseJson.users[0].email,
                    username: responseJson.users[0].username,
                    password: responseJson.users[0].password,
                });
                localStorage.setItem('email', responseJson.users[0].email);
            })
            .catch(error => {
                console.error('Error: ', error);
            })
    };

    _deleteAccount = () => {
        const {email} = this.state;
        const url = `http://127.0.0.1:8080/database/delete/${email}`;

        fetch(url, {
            method: "GET",
            headers: {},
        })
            .then(response => response.json())
            .then(responseJson => {
                if (responseJson === true) {
                    UserAuth.authenticate(() => {
                        this.setState(() => ({
                            redirectToReferrer: true
                        }))
                    });
                    this.props.history.push('/');
                    localStorage.clear();
                }
            })
            .catch(error => {
                console.error('Error: ', error);
            })
    };

    _save = async () => {
        const {email, username, password, id} = this.state;
        const url = `${config.serverIp}/database/editaccount/${username}/${password}/${email}/${id}`;

        await fetch(url, {
            method: "GET",
            headers: {},
        })
            .then(response => response.json())
            .then(responseJson => {
                this.setState({error: null});
                if (responseJson === true) {
                    this.setState({
                        id: this.state.email,
                    });
                    localStorage.setItem('email', responseJson.users[0].email);
                } else {
                    this.setState({error: 'Email already taken.'});
                }
            })
            .catch(error => {
                console.error('Error: ', error);
            })
    };

    responseMicrosoft = (err, data) => {
        console.log(data);
        this.setState({tokenMicrosoft: data.authResponseWithAccessToken.accessToken} );
        const {email} = this.state;
        const url = `${config.serverIp}/database/editmicrosofttoken/${email}/` + data.authResponseWithAccessToken.accessToken;

        fetch(url, { method: "GET", headers: {}, })
            .then(response => response.json())
            .then(responseJson => { console.log(responseJson) })
            .catch(error => {
                console.error('Error: ', error);
            })
    };

    responseFacebook = (response) => {
        this.setState({tokenFacebook: response.accessToken, usernameFacebook: response.name} );
        const {email} = this.state;
        const url = `${config.serverIp}/database/editmicrosofttoken/${email}/` + response.accessToken;

        fetch(url, { method: "GET", headers: {}, })
            .then(response => response.json())
            .then(responseJson => { console.log(responseJson) })
            .catch(error => {
                console.error('Error: ', error);
            })
    };

    _facebookButton = () => {
        if (this.state.tokenFacebook === '')
            return (
                <FacebookAuth callback={this.responseFacebook}/>
            );
        else
            return (
                <button className="submit facebook-btn">Hello {this.state.usernameFacebook}</button>
            );
    };

    render() {
        return (
            <div className="wrapper">
                <SideMenu active={2}/>

                <div className="main">
                    <Sidebar title={"User profile"}/>

                    <div className="content center">
                        <form className="card user-form">
                            <label>
                                <span>Name</span>
                                <input value={this.state.username} onChange={this._handleChange} name="registerUsername"
                                       type="text" autoComplete={"username"}/>
                            </label>
                            <label>
                                <span>Email</span>
                                <input value={this.state.email} onChange={this._handleChange} name="registerEmail"
                                       type="email" autoComplete={"email"}/>
                            </label>
                            <label>
                                <span>Password</span>
                                <input value={this.state.password} onChange={this._handleChange} name="registerPassword"
                                       type="password" autoComplete={"current-password"}/>
                            </label>
                            <p className="error-msg">{this.state.error}</p>
                            <MicrosoftAuth callback={this.responseMicrosoft}/>
                            {this._facebookButton()}
                            <button type="button" className="submit success-btn" onClick={this._save}>Save changes</button>
                            <AuthButton />
                            <button type="button" className="submit danger-btn" onClick={this._deleteAccount}>Delete account</button>
                        </form>
                    </div>

                    <Footer/>
                </div>

            </div>
        )
    }
}

export default User;
