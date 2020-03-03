import React from 'react';

class NameWidget extends React.Component {

    state = {
        name: 'Léo',
        data: null,
    };

    componentDidMount() {
        this._fetch();
    }

    _handleChange = (e) => {
        this.setState({ [e.target.name]: e.target.value });
    };

    _handleSubmit = () => {
        this._fetch();
    };

    _fetch = () => {
        const { name } = this.state;
        const url = `${config.serverIp}/api/hero/name/${name}`;

        fetch(url, {
            method: "GET",
            headers: {},
        })
            .then(response => response.json())
            .then(responseJson => {
                if (responseJson.status)
                    return;
                this.setState({ data: responseJson.results[0] });
            })
            .catch(error => {
                console.error('Error: ', error);
            })
    };

    render() {
        if (typeof (this.state.data) !== 'undefined' && this.state.data) {
            return (
                <>
                    <div>
                        <div className="flex">
                            <div className="flex flex-column flex-align-items hero">
                                <img className="picture" src={this.state.data.image.url} alt="" />
                                <em>{this.state.data.name}</em>
                            </div>
                            <ul>
                                <li>Intelligence: {this.state.data.powerstats.intelligence}</li>
                                <li>Strength: {this.state.data.powerstats.strength}</li>
                                <li>Speed: {this.state.data.powerstats.speed}</li>
                                <li>Durability: {this.state.data.powerstats.durability}</li>
                                <li>Power: {this.state.data.powerstats.power}</li>
                                <li>Combat: {this.state.data.powerstats.combat}</li>
                            </ul>
                        </div>
                    </div>
                    <div className="flex">
                        <input onChange={this._handleChange} name="name"
                            type="text" placeholder="Superhero's name" />
                        <button type="button" className="submit" onClick={this._handleSubmit}>Submit</button>
                    </div>
                </>
            );
        } else {
            return (
                <>
                    <div className="flex">
                        <input onChange={this._handleChange} name="name"
                            type="text" placeholder="Superhero's name" />
                        <button type="button" className="submit" onClick={this._handleSubmit}>Submit</button>
                    </div>
                </>
            )
        }
    }
}

export default NameWidget
