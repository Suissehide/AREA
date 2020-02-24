import React from 'react';
import SideMenu from "../components/SideMenu";

import '../css/Notification.css';

class Notifications extends React.Component {
    state = {
        profile: false,
    };

    render() {
        return (
            <div className="wrapper">
                <SideMenu active={3}/>

                <div className="main notification__wrapper">
                    <div className="notification green">
                        <div className="info">
                            <h1>This is a <a href="https://goo.gl/GykQEn">notification</a></h1>
                            <p>You have been notified</p>
                        </div>
                        <div className="icon">
                            <i className="fas fa-asterisk"/>
                        </div>
                    </div>

                    <div className="notification red">
                        <div className="info">
                            <h1><a href="https://goo.gl/IiwBDn">ruandre</a> followed you</h1>
                            <p>You have a new follower! Feel the fame flow through your vains!</p>
                        </div>
                        <div className="icon">
                            <i className="fas fa-heart"/>
                        </div>
                    </div>

                    <div className="notification blue">
                        <div className="info">
                            <h1><a href="https://goo.gl/I8lNLu">Windows 10</a> preview is here</h1>
                            <p>Windows 10 represents the first step of a whole new generation of Windows. Windows 10
                                unlocks new experiences for customers to work, play and connect.</p>
                            <a href="https://goo.gl/Z83wbD" className="button">Full story</a><a href="#"
                                                                                                className="button gray">Dismiss</a>
                        </div>
                        <div className="icon">
                            <i className="fas fa-newspaper"/>
                        </div>
                    </div>

                    <div className="notification purple">
                        <div className="info">
                            <h1><a>8 min</a> to home with a bicycle</h1>
                            <p>Bicycle 2.4 km, 8 min. Use caution - may involve errors or sections not suited for
                                bicycling</p>
                            <a href="https://goo.gl/YbvshI" className="button">Navigate</a><a href="#"
                                                                                              className="button gray">Dismiss</a>
                        </div>
                        <div className="icon">
                            <i className="fa fa-bicycle"/>
                        </div>
                    </div>

                    <div className="notification blue">
                        <div className="info">
                            <h1><a href="https://goo.gl/C1PuL7">@munkkeli</a> followed you!</h1>
                            <p>You have a new follower! Feel the fame flow through your vains!</p>
                        </div>
                        <div className="icon">
                            <i className="fab fa-twitter"/>
                        </div>
                    </div>
                </div>
            </div>
        );
    }
}

export default Notifications
