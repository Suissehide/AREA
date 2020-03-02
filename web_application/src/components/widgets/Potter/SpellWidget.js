import React from 'react';

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
        const url = `http://127.0.0.1:8080/api/potter/spell`;

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

    render() {
        if (this.state.data) {
            return (
                <>
                    <div>
                        <h1>{this.state.data.spell}</h1>
                        <em>{this.state.data.type}</em>
                        <p>{this.state.data.effect}</p>
                    </div>
                    <button type="button" className="submit refresh" onClick={this._handleRefresh}><i className="fa fa-sync"/></button>
                </>
            );
        } else {
            return (
                <>
                    <button type="button" className="submit refresh" onClick={this._handleRefresh}><i className="fa fa-sync"/></button>
                </>
            )
        }
    }
}

export default SpellWidget
