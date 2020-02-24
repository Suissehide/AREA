import React from 'react';
import background from '../assets/img/jungle_background.jpg';
import '../css/Home.css';
import Card from "../components/Card";
import SideMenu from "../components/SideMenu";
import Sidebar from "../components/Navbar";

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

                    <Sidebar/>

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
