import React from 'react';
import '../css/Home.css';
import Card from "../components/Card";
import SideMenu from "../components/SideMenu";
import Sidebar from "../components/Navbar";
import Footer from "../components/Footer";

class Home extends React.Component {
    state = {

    };

    resetProfile = () => {
        this.setState({profile: false});
    };

    render() {
        return (

            <div className="wrapper">
                <SideMenu active={1}/>

                <div className="main">
                    <Sidebar title={"Dashboard"}/>

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

                    <Footer/>
                </div>
            </div>
        );
    }
}

export default Home;
