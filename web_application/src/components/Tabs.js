import React from 'react';
import '../css/Card.css';

import ChuckWidget from "./widgets/ChuckWidget";
import JokeWidget from "./widgets/JokeWidget";
import SpellWidget from "./widgets/Potter/SpellWidget";
import CharacterWidget from "./widgets/Potter/CharacterWidget";
import WeatherWidget from "./widgets/WeatherWidget";
import MovieWidget from "./widgets/MovieWidget";

class Tabs extends React.Component {

    state = {
        active: 0,
    };

    _getComponent = (type) => {
        switch (type) {
            //CHUCK NORRIS FACTS
            case 'ChuckWidget':
                return <ChuckWidget />;

            //JOKE
            case 'JokeWidget':
                return <JokeWidget />;

            //POTTER
            case 'SpellWidget':
                return <SpellWidget />;
            case 'CharacterWidget':
                return <CharacterWidget />;

            //WEATHER
            case 'WeatherWidget':
                return <WeatherWidget />;

            //MOVIE
            case 'MovieWidget':
                return <MovieWidget />;

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
                Object.keys(tabs).map((tab, i) => {
                    if (tabs[tab]) {
                        return (
                            <li className="nav-item" ref={i + 1} key={i + 1}>
                                <button onClick={this._handleActive.bind(null, i)} className={"nav-link " + (this.state.active === i ? 'active' : '')} data-id={i}
                                        data-toggle="tab">
                                    {tab}
                                </button>
                            </li>
                        )
                    } else {
                        return null
                    }
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
