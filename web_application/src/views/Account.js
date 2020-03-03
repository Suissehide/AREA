import React from 'react';
import '../css/SideMenu.css';
import SideMenu from "../components/SideMenu";
import Sidebar from "../components/Navbar";
import Footer from "../components/Footer";
import Select from "../components/Select";
import config from '../services/Config';

class Account extends React.Component {
    state = {
        profile: false,
        json: `{
            "id": 0,
            "email": "i@i.i",
            "preferences": {
                "Chuck_Norris_Service": {
                    "state": false,
                    "widgets": {
                        "Themed Chuck Norris Jokes": true
                    }
                },
                "Joke_Service": {
                    "state": true,
                    "widgets": {
                        "Themed Joke": true
                    }
                },
                "Harry_Potter_Service": {
                    "state": true,
                    "widgets": {
                        "Random Spell": true,
                        "Random Character": true
                    }
                },
                "Weather_Service": {
                    "state": true,
                    "widgets": {
                        "City Weather": true
                    }
                },
                "The_Movie_Database_Service": {
                    "state": true,
                    "widgets": {
                        "Movie Information": true
                    }
                },
                "Pokemon_Service": {
                    "state": true,
                    "widgets": {
                        "Pokemon Information": true,
                        "Pokemon Abilities": true
                    }
                },
                "Microsoft_Service": {
                    "state": true,
                    "widgets": {
                        "OutlookWidget": true,
                        "CalendarWidget": true,
                        "ContactsWidget": true,
                        "GraphWidget": true,
                        "DriveWidget": true
                    }
                },
                "Google_Service": {
                    "state": true,
                    "widgets": {
                        "IpMapWidget": true,
                        "DistanceMatrixWidget": true
                    }
                },
                "Facebook_Service": {
                    "state": true,
                    "widgets": {
                        "FacebookWidget": true
                    }
                },
                "News_Service": {
                    "state": true,
                    "widgets": {
                        "BananaWidget": true,
                        "NewsWidget": true
                    }
                },
                "Photo_Service": {
                    "state": true,
                    "widgets": {
                        "PhotoWidget": true
                    }
                },
                "Hero_Service": {
                    "state": true,
                    "widgets": {
                        "IdWidget": true,
                        "NameWidget": true
                    }
                },
                "Jikan_Service": {
                    "state": true,
                    "widgets": {
                        "AnimeWidget": true,
                        "CharacterWidget": true,
                        "TopAnimeWidget": true,
                        "TopMangaWidget": true
                    }
                },
                "Iss _Service":{
                    "state": true,
                    "widgets" :{
                        "ISS Location": true,
                        "People in Space": true
                    }
                }
            }
        }`,
        obj: null,
    };

    componentDidMount() {
        const token = localStorage.getItem('email') === null ? '' : localStorage.getItem('email');
        const url = `${config.serverIp}/database/preferences/${token}`;

        fetch(url, {
            method: "GET",
            headers: {},
        })
            .then(response => response.json())
            .then(responseJson => {
                this.setState({ obj: responseJson.services });
            })
            .catch(error => {
                console.error('Error: ', error);
            })
    }

    _generateService = (services) => {
        if (services) {
            return (
                Object.keys(services).map((service, i) => {
                    return (
                        <div ref={i + 1} key={i + 1}>
                            <Select
                                title={service}
                                status={services[service]["state"]}
                                tabs={services[service]["widgets"]}
                            />
                        </div>
                    )
                })
            )
        }
    };


    render() {
        return (
            <div className="wrapper">
                <SideMenu active={4} />

                <div className="main">
                    <Sidebar title={"Manage your account"} />

                    <div className="content flex flex-wrap flex-grid">

                        {this._generateService(this.state.obj)}

                        <div><div className="card fit-content">
                            <div className="card-header card-header-info card-flex">
                                <div className="card-logo">
                                    <i className="fab fa-facebook" />
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
                                            type="text" />
                                    </label>
                                    <label>
                                        <span>Password</span>
                                        <input value={this.state.registerPassword} onChange={this._handleChange}
                                            name="registerPassword"
                                            type="password" />
                                    </label>
                                    <button type="button" className="submit" onClick={this.handleRegister}>Sign Up
                                    </button>
                                </form>
                            </div>
                        </div></div>

                    </div>

                    <Footer />
                </div>

            </div>
        )
    }
}

export default Account;

