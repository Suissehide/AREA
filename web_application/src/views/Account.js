import React from 'react';
import '../css/SideMenu.css';
import SideMenu from "../components/SideMenu";
import Sidebar from "../components/Navbar";
import Footer from "../components/Footer";
import Select from "../components/Select";

class Account extends React.Component {
    state = {
        profile: false,
        json: `{
            "id": 0,
            "email": "i@i.i",
            "preferences": {
                "Chuck_Norris_Service": {
                    "service": false,
                    "widgets": {
                        "ChuckWidget": true
                    }
                },
                "Joke_Service": {
                    "service": true,
                    "widgets": {
                        "JokeWidget": true
                    }
                },
                "Potter_Service": {
                    "service": true,
                    "widgets": {
                        "SpellWidget": true,
                        "CharacterWidget": true
                    }
                },
                "Weather_Service": {
                    "service": true,
                    "widgets": {
                        "WeatherWidget": true
                    }
                },
                "Movie_Service": {
                    "service": true,
                    "widgets": {
                        "MovieWidget": true
                    }
                },
                "Pokemon_Service": {
                    "service": true,
                    "widgets": {
                        "MovesWidget": true,
                        "DetailWidget": true
                    }
                },
                "Microsoft_Service": {
                    "service": true,
                    "widgets": {
                        "OutlookWidget": true,
                        "CalendarWidget": true,
                        "ContactsWidget": true,
                        "GraphWidget": true,
                        "DriveWidget": true
                    }
                },
                "Google_Service": {
                    "service": true,
                    "widgets": {
                        "IpMapWidget": true,
                        "DistanceMatrixWidget": true
                    }
                },
                "Facebook_Service": {
                    "service": true,
                    "widgets": {
                        "FacebookWidget": true
                    }
                },
                "News_Service": {
                    "service": true,
                    "widgets": {
                        "BananaWidget": true,
                        "NewsWidget": true
                    }
                },
                "Photo_Service": {
                    "service": true,
                    "widgets": {
                        "PhotoWidget": true
                    }
                },
                "Hero_Service": {
                    "service": true,
                    "widgets": {
                        "IdWidget": true,
                        "NameWidget": true
                    }
                },
                "Jikan_Service": {
                    "service": true,
                    "widgets": {
                        "AnimeWidget": true,
                        "CharacterWidget": true,
                        "TopAnimeWidget": true,
                        "TopMangaWidget": true
                    }
                },
                "Iss _Service":{
                    "service": true,
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
        this.setState({
            obj: JSON.parse(this.state.json).preferences,
        });
    }

    _generate_Service = (services) => {
        if (services) {
            return (
                Object.keys(services).map((service, i) => {
                    return (
                        <div ref={i + 1} key={i + 1}>
                            <Select
                                title={service}
                                status={services[service]["service"]}
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

                        {this._generate_Service(this.state.obj)}

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

