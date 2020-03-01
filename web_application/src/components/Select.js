import React from 'react';
import '../css/Card.css';

import Switch from "./Switch";

class Select extends React.Component {

    state = {
        active: [],
    };

    componentDidMount() {
        this._initActive();
    }

    _initActive = () => {
        const arr = [this.props.status];
        Object.keys(this.props.tabs).map((tab, i) => {
            return arr[i + 1] = this.props.tabs[tab];
        });
        this.setState({active: arr});
    };

    _getService = (title) => {
        switch (title) {
            //CHUCK NORRIS FACTS
            case 'ChuckService':
                return [<i className="fa fa-smile-wink"/>, 'ChuckService', 'Joke'];

            //JOKE
            case 'JokeService':
                return [<i className="fa fa-smile-wink"/>, 'JokeService', 'Joke'];

            //POTTER
            case 'PotterService':
                return [<i className="fa fa-magic"/>, 'PotterService', 'Fantasy'];

            //WEATHER
            case 'WeatherService':
                return [<i className="fa fa-cloud-sun-rain"/>, 'WeatherService', 'Weather'];

            //JIKAN
            case 'JikanService':
                return [<i className="fa fa-film"/>, 'JikanService', 'Movie'];

            //MOVIE DATABASE
            case 'MovieService':
                return [<i className="fa fa-film"/>, 'MovieService', 'Movie'];

            //POKEMON
            case 'PokemonService':
                return [<i className="fa fa-gamepad"/>, 'PokemonService', 'Game'];

            //MICROSOFT
            case 'MicrosoftService':
                return [<i className="fab fa-microsoft"/>, 'MicrosoftService', 'Work'];

            //PHOTO
            case 'PhotoService':
                return [<i className="fa fa-image"/>, 'PhotoService', 'Photo'];

            //GOOGLE
            case 'GoogleService':
                return [<i className="fa fa-map-marked-alt"/>, 'GoogleService', 'Localisation'];

            //IPMAP
            case 'IpMapService':
                return [<i className="fa fa-map-marked-alt"/>, 'IpMapService', 'Localisation'];

            //NEWS
            case 'NewsService':
                return [<i className="fa fa-newspaper"/>, 'NewsService', 'News'];

            //FACEBOOK
            case 'FacebookService':
                return [<i className="fab fa-facebook"/>, 'FacebookService', 'Social media'];

            //HERO
            case 'HeroService':
                return [<i className="fa fa-gamepad"/>, 'HeroService', 'Game'];


            default:
                return [<i className="fa fa-question"/>, 'title', 'category'];
        }
    };

    _generateContents = (tabs) => {
        if (tabs) {
            return (
                Object.keys(tabs).map((tab, i) => {
                    return (
                        <div className={"flex flex-space-between " +  (i > 0 ? 'separator' : '')} ref={i + 1} key={i + 1}>
                            <div className="flex-center">{tab}</div>
                            <Switch
                                id={tab}
                                isOn={this.state.active[i + 1] || false}
                                handleToggle={() => this.setState({active: this.state.active.map((el, k) => (k === i + 1 ? !this.state.active[i + 1] : el))})} />
                        </div>
                    )
                })
            )
        }
    };

    render() {
        return (
            <div className="card fit-content">
                <div className="card-header card-header-success card-flex flex-space-between">
                    <div className="flex">
                        <div className="card-logo">
                            {this._getService(this.props.title)[0]}
                        </div>
                        <div>
                            <h4 className="card-title">{this._getService(this.props.title)[1]}</h4>
                            <p className="card-category">{this._getService(this.props.title)[2]}</p>
                        </div>
                    </div>
                    <div className="flex-center">
                        <Switch
                            id={this.props.title}
                            isOn={this.state.active[0] || false}
                            handleToggle={() => this.setState({active: this.state.active.map((el, k) => (k === 0 ? !this.state.active[0] : el))})} />
                    </div>
                </div>
                <div className="card-body">
                    {this._generateContents(this.props.tabs)}
                </div>
            </div>
        );
    }
}

export default Select
