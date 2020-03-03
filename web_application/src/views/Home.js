import React from 'react';
import '../css/Home.css';
import Card from "../components/Card";
import SideMenu from "../components/SideMenu";
import Sidebar from "../components/Navbar";
import Footer from "../components/Footer";
import Tabs from "../components/Tabs";
import config from '../services/Config';

class Home extends React.Component {
    state = {
        json: `{
            "id": 0,
            "email": "i@i.i",
            "preferences": {
                "ChuckService": {
                    "service": true,
                    "widgets": {
                        "ChuckWidget": true
                    }
                },
                "JokeService": {
                    "service": true,
                    "widgets": {
                        "JokeWidget": true
                    }
                },
                "PotterService": {
                    "service": true,
                    "widgets": {
                        "SpellWidget": true,
                        "CharacterWidget": true
                    }
                },
                "WeatherService": {
                    "service": true,
                    "widgets": {
                        "WeatherWidget": true
                    }
                },
                "MovieService": {
                    "service": true,
                    "widgets": {
                        "MovieWidget": true
                    }
                },
                "PokemonService": {
                    "service": true,
                    "widgets": {
                        "DetailWidget": true,
                        "MovesWidget": true
                    }
                },
                "MicrosoftService": {
                    "service": true,
                    "widgets": {
                        "OutlookWidget": true,
                        "CalendarWidget": true,
                        "ContactsWidget": true,
                        "GraphWidget": true,
                        "DriveWidget": true
                    }
                },
                "GoogleService": {
                    "service": true,
                    "widgets": {
                        "IpMapWidget": true,
                        "DistanceMatrixWidget": true
                    }
                },
                "FacebookService": {
                    "service": true,
                    "widgets": {
                        "FacebookWidget": true
                    }
                },
                "NewsService": {
                    "service": true,
                    "widgets": {
                        "BananaWidget": true,
                        "NewsWidget": true
                    }
                },
                "PhotoService": {
                    "service": true,
                    "widgets": {
                        "PhotoWidget": true
                    }
                },
                "HeroService": {
                    "service": true,
                    "widgets": {
                        "IdWidget": true,
                        "NameWidget": true
                    }
                },
                "JikanService": {
                    "service": true,
                    "widgets": {
                        "AnimeWidget": true,
                        "JikanWidget": true,
                        "TopAnimeWidget": true,
                        "TopMangaWidget": true
                    }
                }
            }
        }`,
        obj: null,
    };

    componentDidMount() {
        localStorage.setItem('email', 'idoia.reinares@epitech.eu');
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

    resetProfile = () => {
        this.setState({ profile: false });
    };

    _generateService = (services) => {
        if (services) {
            return (
                Object.keys(services).map((service, i) => {
                    if (services[service]["state"]) {
                        return (
                            <Tabs ref={i + 1} key={i + 1}
                                title={service}
                                tabs={services[service]["widgets"]}
                            />
                        )
                    } else {
                        return null
                    }
                })
            )
        }
    };

    render() {
        return (

            <div className="wrapper">
                <SideMenu active={1} />

                <div className="main">
                    <Sidebar title={"Dashboard"} />

                    <div className="content" onClick={this.resetProfile}>
                        <div className="container-fluid">
                            <div className="row">
                                <div className="col col-4">
                                    <Card type={'card-header-info'} headerIcon={'fab fa-twitter'} category={'Followers'} title={'+245'}
                                        footerIcon={'fas fa-history'} footerText={' Just Updated'} />
                                </div>
                                <div className="col col-4">
                                    <Card type={'card-header-danger'} headerIcon={'fas fa-info-circle'} category={'Fixed Issues'} title={'75'}
                                        footerIcon={'fas fa-tag'} footerText={' Tracked from Github'} />
                                </div>
                            </div>
                            <div className="row row-2">
                                {this._generateService(this.state.obj)}
                            </div>
                        </div>
                    </div>

                    <Footer />
                </div>
            </div>
        );
    }
}

export default Home;
