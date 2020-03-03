import React from 'react';
import config from '../../../services/Config';

class SpellWidget extends React.Component {

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
        const url = `${config.serverIp}/api/potter/spell`;

        fetch(url, {
            method: "GET",
            headers: {},
        })
            .then(response => response.json())
            .then(responseJson => {
                this.setState({ data: responseJson });
            })
            .catch(error => {
                console.error('Error: ', error);
            })
    };

    render() {
        if (this.state.data) {
            return (
                <>
                    <div>
                        <h1>{this.state.data.spell}</h1>
                        <em>{this.state.data.type}</em>
                        <p>{this.state.data.effect}</p>
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

export default SpellWidget
