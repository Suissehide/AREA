import React from 'react';
import '../css/SideMenu.css';
import {withRouter} from "react-router-dom";
import UserAuth from "../services/UserAuth";

const AuthButton = withRouter(({history}) => (
    <button className="dropdown-item" onClick={() => {
        UserAuth.signout(() => history.push('/'));
        localStorage.clear();
    }}>
        Log out
    </button>
));

class Sidebar extends React.Component {
    state = {
        profile: false,
    };

    triggerProfile = () => {
        this.setState({profile: !this.state.profile});
    };

    render() {
        return (
            <nav className="navbar navbar-expand-lg navbar-transparent navbar-absolute fixed-top">
                <div className="container-fluid">
                    <div className="navbar-wrapper">
                        <a className="navbar-brand" href="#home">{this.props.title}</a>
                    </div>

                    <div className="collapse navbar-collapse justify-content-end">
                        <form className="navbar-form">
                                <span className="bmd-form-group">
                                    <div className="input-group no-border">
                                        <input type="text" className="form-control" placeholder="Search..."/>
                                        <button type="submit" className="btn btn-white btn-round btn-just-icon">
                                          <i className="fas fa-search"/>
                                          <div className="ripple-container"/>
                                        </button>
                                    </div>
                                </span>
                        </form>
                        <ul className="navbar-nav">
                            <li className="nav-item">
                                <a className="nav-link" href="#0">
                                    <i className="fas fa-th-list"/>
                                </a>
                            </li>
                            <li className="nav-item dropdown">
                                <a className="nav-link" href="#0" id="navbarDropdownMenuLink"
                                   data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                                    <i className="fas fa-bell"/>
                                    <span className="pastille">5</span>
                                </a>
                            </li>
                            <li className="nav-item dropdown">
                                <a className="nav-link" href="#0" id="navbarDropdownProfile"
                                   onClick={this.triggerProfile}
                                   data-toggle="dropdown"
                                   aria-haspopup="true" aria-expanded="false">
                                    <i className="fas fa-user"/>
                                </a>
                                <div
                                    className={"dropdown-menu dropdown-menu-right " + (this.state.profile ? 'show' : '')}
                                    aria-labelledby="navbarDropdownProfile">
                                    <a className="dropdown-item" href="#0">Profile</a>
                                    <a className="dropdown-item" href="#0">Settings</a>
                                    <div className="dropdown-divider"/>
                                    <AuthButton />
                                    {/*<a className="dropdown-item" href="#0">Log out</a>*/}
                                </div>
                            </li>
                        </ul>
                    </div>
                </div>
            </nav>
        )
    }
}

export default Sidebar;
