import React from 'react';

class WeatherWidget extends React.Component {

    state = {
        city: 'Bordeaux',
        data: null,
    };

    componentDidMount() {
        this._fetch();
    }

    _handleChange = (e) => {
        this.setState({[e.target.name]: e.target.value});
    };

    _handleSubmit = () => {
        this._fetch();
    };

    _fetch = () => {
        const {city} = this.state;
        const url = `http://127.0.0.1:8080/api/weather/${city}`;

        fetch(url, {
            method: "GET",
            headers: {},
        })
            .then(response => response.json())
            .then(responseJson => {
                this.setState({data: responseJson});
            })
            .catch(error => {
                console.error('Error: ', error);
            })
    };

    _getIcon(type) {
        switch (type) {
            case 'Clear':
                return <i className="fas fa-sun"/>;
            case 'Clouds':
                return <i className="fas fa-cloud"/>;
            case 'Smog':
                return <i className="fas fa-smog"/>;
            case 'Wind':
                return <i className="fas fa-wing"/>;
            case 'Rain':
                return <i className="fas fa-cloud-rain"/>;
            default:
                return <i className="fas fa-sun"/>;
        }
    }

    _calcTemp = (temp) => {
        return Math.round((Number(temp) - 273));
    };

    render() {
        if (this.state.data) {
            return (
                <>
                    <div className="flex flex-align-items">
                        <div className="weather">
                            {this._getIcon(this.state.data.weather[0].main)}
                            <p><i className="fas fa-map-marker-alt"/><em>{this.state.data.name}</em> | {this.state.data.weather[0].description}</p>
                        </div>
                        <div>
                            <div className="temp">{this._calcTemp(this.state.data.main.temp)}°</div>
                            <div>{this._calcTemp(this.state.data.main.tempMin)}° / {this._calcTemp(this.state.data.main.tempMax)}°</div>
                        </div>
                    </div>
                    <div className="flex">
                        <input onChange={this._handleChange} name="city"
                               type="text" placeholder="City"/>
                        <button type="button" className="submit" onClick={this._handleSubmit}>Submit</button>
                    </div>
                </>
            );
        } else {
            return (
                <>
                    <div className="flex">
                        <input onChange={this._handleChange} name="city"
                               type="text" placeholder="City"/>
                        <button type="button" className="submit" onClick={this._handleSubmit}>Submit</button>
                    </div>
                </>
            )
        }
    }
}

export default WeatherWidget
