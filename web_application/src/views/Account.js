import React from 'react';
import '../css/SideMenu.css';
import SideMenu from "../components/SideMenu";
import Sidebar from "../components/Navbar";
import Footer from "../components/Footer";

class Account extends React.Component {
    state = {
        profile: false,
    };

    render() {
        return (
            <div className="wrapper">
                <SideMenu active={4}/>

                <div className="main">
                    <Sidebar title={"Manage your account"}/>

                    <div className="content">
                        <div className="card fit-content">
                            <div className="card-header card-header-info card-flex">
                                <div className="card-logo">
                                    <i className="fab fa-facebook"/>
                                </div>
                                <div>
                                    <h4 className="card-title">Facebook</h4>
                                    <p className="card-category">Social media</p>
                                </div>
                            </div>
                            <div className="card-body">
                                <form className="account-form">
                                    <label>
                                        <span>Username</span>
                                        <input value={this.state.registerUsername} onChange={this._handleChange}
                                               name="registerUsername"
                                               type="text"/>
                                    </label>
                                    <label>
                                        <span>Password</span>
                                        <input value={this.state.registerPassword} onChange={this._handleChange}
                                               name="registerPassword"
                                               type="password"/>
                                    </label>
                                    <button type="button" className="submit" onClick={this.handleRegister}>Sign Up
                                    </button>
                                </form>
                            </div>
                        </div>

                        <div className="card fit-content">
                            <div className="card-header card-header-info card-flex">
                                <div className="card-logo">
                                    <i className="fab fa-twitter"/>
                                </div>
                                <div>
                                    <h4 className="card-title">Twitter</h4>
                                    <p className="card-category">Social media</p>
                                </div>
                            </div>
                            <div className="card-body">
                                <form className="account-form">
                                    <label>
                                        <span>Username</span>
                                        <input value={this.state.registerUsername} onChange={this._handleChange}
                                               name="registerUsername"
                                               type="text"/>
                                    </label>
                                    <label>
                                        <span>Password</span>
                                        <input value={this.state.registerPassword} onChange={this._handleChange}
                                               name="registerPassword"
                                               type="password"/>
                                    </label>
                                    <button type="button" className="submit" onClick={this.handleRegister}>Sign Up
                                    </button>
                                </form>
                            </div>
                        </div>
                    </div>

                    <Footer/>
                </div>

            </div>
        )
    }
}

export default Account;

