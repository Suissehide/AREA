import React from 'react';
import '../css/SideMenu.css';
import SideMenu from "../components/SideMenu";
import Sidebar from "../components/Navbar";
import Footer from "../components/Footer";
import Account from "./Account";

class User extends React.Component {
    state = {
        profile: false,
    };

    render() {
        return (
            <div className="wrapper">
                <SideMenu active={2}/>

                <div className="main">
                    <Sidebar title={"User profile"}/>

                    <div className="content">
                    </div>

                    <Footer/>
                </div>

            </div>
        )
    }
}

export default User;
