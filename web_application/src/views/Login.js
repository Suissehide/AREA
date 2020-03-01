import React from 'react';
import {Redirect} from 'react-router-dom';

import UserAuth from "../services/UserAuth";

class Login extends React.Component {
    state = {
        redirectToReferrer: false,
        loading: true,
        error: null,

        toggleMode: true,

        loginEmail: '',
        loginPassword: '',

        registerUsername: '',
        registerEmail: '',
        registerPassword: '',
        registerConfirmPassword: '',
    };

    handleLogin = (e) => {
        e.preventDefault();

        // this._auth();
        this._login();
    };

    _login = () => {
        UserAuth.authenticate(() => {
            this.setState(() => ({
                redirectToReferrer: true
            }))
        });

        this.props.history.push('/home');
    };

    _auth = async () => {
        const {loginEmail, loginPassword} = this.state;
        const url = `http://127.0.0.1:8080/database/login/${loginEmail}/${loginPassword}`;

        await fetch(url, {
            method: "GET",
            headers: {},
        })
            .then(response => response.json())
            .then(responseJson => {
                this.setState({error: null});
                if (responseJson === true) this._login();
                else this.setState({error: 'Email or password invalid.'});
            })
            .catch(error => {
                console.error('Error: ', error);
        })
    };

    handleRegister = (e) => {
        e.preventDefault();

        this._register();
    };

    _register = async () => {
        const {registerEmail, registerPassword, registerUsername} = this.state;
        const url = `http://127.0.0.1:8080/database/signup/${registerEmail}/${registerPassword}/${registerUsername}`;

        await fetch(url, {
            method: "GET",
            headers: {},
        })
            .then(response => response.json())
            .then(responseJson => {
                this.setState({error: null});
                if (responseJson === true) this._login();
                else this.setState({error: 'Email already taken.'});
            })
            .catch(error => {
                console.error('Error: ', error);
            })
    };

    _handleChange = (e) => {
        this.setState({[e.target.name]: e.target.value});
    };

    _handleToggleMode = () => {
        this.setState({toggleMode: !this.state.toggleMode});
    };

    render() {
        const {from} = this.props.location.state || {from: {pathname: '/'}};
        const {redirectToReferrer} = this.state;

        if (redirectToReferrer === true) {
            return <Redirect to={from}/>
        }

        return (
            <div className="container__login">
                <div className={"cont " + (this.state.toggleMode ? '' : 's--signup')}>
                    <div className="form sign-in">
                        <h2>Welcome back,</h2>
                        <label>
                            <span>Email</span>
                            <input value={this.state.loginEmail} onChange={this._handleChange} name="loginEmail"
                                   type="email" autoComplete="username"/>
                        </label>
                        <label>
                            <span>Password</span>
                            <input value={this.state.loginPassword} onChange={this._handleChange} name="loginPassword"
                                   type="password" autoComplete="current-password"/>
                        </label>
                        <p className="forgot-pass">Forgot password?</p>
                        <p className="error-msg">{this.state.error}</p>
                        <button type="button" className="submit" onClick={this.handleLogin}>Sign In</button>
                        <button type="button" className="fb-btn">Connect with <span>microsoft</span></button>
                    </div>
                    <div className="sub-cont">
                        <div className="img">
                            <div className="img__text m--up">
                                <h2>New here?</h2>
                                <p>Sign up and discover great amount of new opportunities!</p>
                            </div>
                            <div className="img__text m--in">
                                <h2>One of us?</h2>
                                <p>If you already has an account, just sign in. We've missed you!</p>
                            </div>
                            <div className="img__btn" onClick={this._handleToggleMode}>
                                <span className="m--up">Sign Up</span>
                                <span className="m--in">Sign In</span>
                            </div>
                        </div>
                        <div className="form sign-up">
                            <h2>Time to feel like home,</h2>
                            <label>
                                <span>Name</span>
                                <input value={this.state.registerUsername} onChange={this._handleChange} name="registerUsername"
                                       type="text"/>
                            </label>
                            <label>
                                <span>Email</span>
                                <input value={this.state.registerEmail} onChange={this._handleChange} name="registerEmail"
                                       type="email"/>
                            </label>
                            <label>
                                <span>Password</span>
                                <input value={this.state.registerPassword} onChange={this._handleChange} name="registerPassword"
                                       type="password"/>
                            </label>
                            <label>
                                <span>Repeat password</span>
                                <input value={this.state.registerConfirmPassword} onChange={this._handleChange} name="registerConfirmPassword"
                                       type="password"/>
                            </label>
                            <p className="error-msg">{this.state.error}</p>
                            <button type="button" className="submit" onClick={this.handleRegister}>Sign Up</button>
                            <button type="button" className="fb-btn">Join with <span>microsoft</span></button>
                        </div>
                    </div>
                </div>
            </div>
        )
    }
}

export default Login;
