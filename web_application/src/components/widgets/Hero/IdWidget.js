import React from 'react';
import config from '../../../services/Config';

class IdWidget extends React.Component {

    state = {
        data: null,
    };

    componentDidMount() {
        this._fetch();
    }

    _handleRefresh = () => {
        this._fetch();
    };

    _fetch = () => {
        const url = `${config.serverIp}/api/hero/random`;

        fetch(url, {
            method: "GET",
            headers: {},
        })
            .then(response => response.json())
            .then(responseJson => {
                if (responseJson.status)
                    return;
                this.setState({ data: responseJson });
            })
            .catch(error => {
                console.error('Error: ', error);
            })
    };

    render() {
        if (typeof (this.state.data) !== 'undefined' && this.state.data) {
            return (
                <>
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
                    <button type="button" className="submit refresh" onClick={this._handleRefresh}><i className="fa fa-sync" /></button>
                </>
            );
        } else {
            return (
                <>
                    <button type="button" className="submit refresh" onClick={this._handleRefresh}><i className="fa fa-sync" /></button>
                </>
            )
        }
    }
}

export default IdWidget
