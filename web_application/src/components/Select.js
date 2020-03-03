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
        this.setState({ active: arr });
    };

    _getService = (title) => {
        switch (title) {
            //CHUCK NORRIS FACTS
            case 'Chuck_Norris_Service':
                return [<i className="fa fa-smile-wink" />, 'Chuck Norris Service', 'Joke'];

            //JOKE
            case 'Joke_Service':
                return [<i className="fa fa-smile-wink" />, 'Joke Service', 'Joke'];

            //POTTER
            case 'Harry_Potter_Service':
                return [<i className="fa fa-magic" />, 'Harry Potter Service', 'Fantasy'];

            //WEATHER
            case 'Weather_Service':
                return [<i className="fa fa-cloud-sun-rain" />, 'Weather Service', 'Weather'];

            //JIKAN
            case 'Jikan_Service':
                return [<i className="fa fa-film" />, 'Jikan Service', 'Movie'];

            //MOVIE DATABASE
            case 'The_Movie_Database_Service':
                return [<i className="fa fa-film" />, 'The_Movie_Databse_Service', 'Movie'];

            //POKEMON
            case 'Pokemon_Service':
                return [<i className="fa fa-gamepad" />, 'PokemonService', 'Game'];

            //MICROSOFT
            case 'Microsoft_Service':
                return [<i className="fab fa-microsoft" />, 'Microsoft_Service', 'Work'];

            //PHOTO
            case 'Photo_Database_Service':
                return [<i className="fa fa-image" />, 'Photo_Database_Service', 'Photo'];

            //GOOGLE
            case 'Google_Service':
                return [<i className="fa fa-map-marked-alt" />, 'Google Service', 'Localisation'];

            //NEWS
            case 'News_Service':
                return [<i className="fa fa-newspaper" />, 'News Service', 'News'];

            //FACEBOOK
            case 'Facebook_Service':
                return [<i className="fab fa-facebook" />, 'Facebook Service', 'Social media'];

            //HERO
            case 'Superhero_Service':
                return [<i className="fa fa-gamepad" />, 'Superhero Service', 'Game'];

            //ISS
            case 'ISS_Service':
                return [<i clasName="fa fa-space-shuttle" />, 'ISS Service', 'Location'];

            //StarWars
            case 'Star_Wars_Service':
                return [<i className="fa fa-jedi-order" />, "Star Wars Service", 'Movie'];

            default:
                return [<i className="fa fa-question" />, 'title', 'category'];
        }
    };

    _generateContents = (tabs) => {
        if (tabs) {
            return (
                Object.keys(tabs).map((tab, i) => {
                    return (
                        <div className={"flex flex-space-between " + (i > 0 ? 'separator' : '')} ref={i + 1} key={i + 1}>
                            <div className="flex-center">{tab}</div>
                            <Switch
                                id={tab}
                                isOn={this.state.active[i + 1] || false}
                                handleToggle={() => this.setState({ active: this.state.active.map((el, k) => (k === i + 1 ? !this.state.active[i + 1] : el)) })} />
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
                            handleToggle={() => this.setState({ active: this.state.active.map((el, k) => (k === 0 ? !this.state.active[0] : el)) })} />
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
