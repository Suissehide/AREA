import React from 'react';
import '../css/Card.css';

import ChuckWidget from "./widgets/ChuckWidget";
import JokeWidget from "./widgets/JokeWidget";
import SpellWidget from "./widgets/Potter/SpellWidget";
import CharacterWidget from "./widgets/Potter/CharacterWidget";
import WeatherWidget from "./widgets/WeatherWidget";
import MovieWidget from "./widgets/MovieWidget";
import MovesWidget from "./widgets/Pokemon/MovesWidget";
import DetailWidget from "./widgets/Pokemon/DetailWidget";
import PhotoWidget from "./widgets/PhotoWidget";
import IdWidget from "./widgets/Hero/IdWidget";
import NameWidget from "./widgets/Hero/NameWidget";
import TopMangaWidget from "./widgets/Jikan/TopMangaWidget";
import TopAnimeWidget from "./widgets/Jikan/TopAnimeWidget";
import JikanWidget from "./widgets/Jikan/JikanWidget";
import AnimeWidget from "./widgets/Jikan/AnimeWidget";
import NewsWidget from "./widgets/News/NewsWidget";
import BananeWidget from "./widgets/News/BananaWidget";
import IpMapWidget from "./widgets/Google/IpMapWidget";
import DistanceMatrixWidget from './widgets/Google/DistanceMatrixWidget';

class Tabs extends React.Component {

    state = {
        active: 0,
    };

    _getComponent = (type) => {
        switch (type) {
            //CHUCK NORRIS FACTS
            case 'Themed Chuck Norris Jokes':
                return <ChuckWidget />;

            //JOKE
            case 'Themed Joke':
                return <JokeWidget />;

            //POTTER
            case 'Random Spell':
                return <SpellWidget />;
            case 'Random Character':
                return <CharacterWidget />;

            //WEATHER
            case 'City Weather':
                return <WeatherWidget />;

            //MOVIE
            case 'Movie Information':
                return <MovieWidget />;

            //POKEMON
            case 'Pokemon Information':
                return <DetailWidget />;
            case 'Pokemon Abilities':
                return <MovesWidget />;

            //PICTURE
            case 'Themed Picture':
                return <PhotoWidget />;

            //HERO
            case 'Random Superhero':
                return <IdWidget />;
            case 'Your Superhero':
                return <NameWidget />;

            //JIKAN
            case 'Highest Scored Mangas':
                return <TopMangaWidget />;
            case 'Highest Scored Animes':
                return <TopAnimeWidget />;
            case 'Character Information':
                return <JikanWidget />;
            case 'Anime Information':
                return <AnimeWidget />;

            //NEWS
            case 'Themed News':
                return <NewsWidget />;
            case 'Bananews':
                return <BananeWidget />;

            //GOOGLE
            case 'Your IP Location':
                return <IpMapWidget />;
            case 'Distance and Time between 2 Spots':
                return <DistanceMatrixWidget />;
            case 'Place Information':
                return;

            //ISS
            case 'ISS Location':
                return;
            case 'People in Space':
                return;

            default:
                return <div>error</div>;
        }
    };

    _handleActive = (i) => {
        this.setState({
            active: i
        })
    };

    _generateTabs = (tabs) => {
        if (tabs) {
            return (
                Object.keys(tabs)
                    .filter(tab => tabs[tab])
                    .map((tab, i) => {
                        return (
                            <li className="nav-item" ref={i + 1} key={i + 1}>
                                <button onClick={this._handleActive.bind(null, i)} className={"nav-link " + (this.state.active === i ? 'active' : '')} data-id={i}
                                    data-toggle="tab">
                                    {tab}
                                </button>
                            </li>
                        )
                    })
            )
        }
    };

    _generateContents = (tabs) => {
        if (tabs) {
            return (
                Object.keys(tabs).map((tab, i) => {
                    if (tabs[tab]) {
                        return (
                            <div className={"tab-pane " + (this.state.active === i ? 'active' : '')} ref={i + 1} key={i + 1}>
                                {this._getComponent(tab)}
                            </div>
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
            <div className="card card-large">
                <div className="card-header card-header-tabs card-header-primary">
                    <div className="nav-tabs-navigation">
                        <div className="nav-tabs-wrapper">
                            <span className="nav-tabs-title">{this.props.title}</span>
                            <ul className="nav nav-tabs" data-tabs="tabs">
                                {this._generateTabs(this.props.tabs)}
                            </ul>
                        </div>
                    </div>
                </div>
                <div className="card-body">
                    <div className="tab-content">
                        {this._generateContents(this.props.tabs)}
                    </div>
                </div>
            </div>
        );
    }
}

export default Tabs
