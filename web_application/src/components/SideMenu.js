import React from 'react';
import '../css/SideMenu.css';
import background from "../assets/img/jungle_background.jpg";

class SideMenu extends React.Component {
    render() {
        return (
            <div className="sidebar">
                <div className="sidebar__logo">
                    <a href="#0" className="logo-normal simple-text ">BanaNews</a>
                </div>
                <div className="sidebar__wrapper">
                    <ul className="nav">
                        <li className={"nav-item " + (this.props.active === 1 ? 'active' : '')}><a className="nav-link" href="/home">
                            <i className="fas fa-list"/>
                            <p>Dashboard</p>
                        </a></li>
                        <li className={"nav-item " + (this.props.active === 2 ? 'active' : '')}><a className="nav-link" href="#0">
                            <i className="fas fa-user"/>
                            <p>User profile</p>
                        </a></li>
                        <li className={"nav-item " + (this.props.active === 3 ? 'active' : '')}><a className="nav-link" href="/notifications">
                            <i className="fas fa-bell"/>
                            <p>Notifications</p>
                        </a></li>
                        <li className={"nav-item " + (this.props.active === 4 ? 'active' : '')}><a className="nav-link" href="/account">
                            <i className="fas fa-cookie"/>
                            <p>Account</p>
                        </a></li>
                    </ul>
                </div>
                <div className="sidebar__background" style={{backgroundImage: `url(${background})`}}/>
            </div>
        )
    }
}

export default SideMenu
