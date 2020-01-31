import React from 'react';
import background from '../assets/img/jungle_background.jpg';
import '../css/Home.css';
import Card from "../components/Card";
import SideMenu from "../components/SideMenu";

class Home extends React.Component {
    state = {
        profile: false,
    };

    triggerProfile = () => {
        this.setState({profile: !this.state.profile});
    };

    resetProfile = () => {
        this.setState({profile: false});
    };

    render() {
        return (

            <div className="wrapper">
                <SideMenu active={1}/>

                <div className="main">

                    <nav className="navbar navbar-expand-lg navbar-transparent navbar-absolute fixed-top">
                        <div className="container-fluid">
                            <div className="navbar-wrapper">
                                <a className="navbar-brand" href="#home">Dashboard</a>
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
                                            <span className="notification">5</span>
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
                                            <a className="dropdown-item" href="#0">Log out</a>
                                        </div>
                                    </li>
                                </ul>
                            </div>
                        </div>
                    </nav>

                    <div className="content" onClick={this.resetProfile}>
                        <div className="container-fluid">
                            <div className="row">
                                <div className="col col-4">
                                    <Card type={'card-header-info'} headerIcon={'fab fa-twitter'} category={'Followers'} title={'+245'}
                                          footerIcon={'fas fa-history'} footerText={' Just Updated'}/>
                                </div>
                                <div className="col col-4">
                                    <Card type={'card-header-danger'} headerIcon={'fas fa-info-circle'} category={'Fixed Issues'} title={'75'}
                                          footerIcon={'fas fa-tag'} footerText={' Tracked from Github'}/>
                                </div>
                            </div>
                        </div>
                    </div>

                    <footer className="footer">
                        <div className="container-fluid footer__flex">
                            <nav>
                                <ul>
                                    <li><a href="#0">About us</a></li>
                                    <li><a href="#0">Blog</a></li>
                                    <li><a href="#0">Licenses</a></li>
                                </ul>
                            </nav>
                            <div className="copyright">
                                @2020, made with <i className="fas fa-heart"/> by <a href="#0" target="_blank">Léo
                                Couffinhal</a>
                            </div>
                        </div>
                    </footer>
                </div>
            </div>
        );
    }
}

export default Home;
