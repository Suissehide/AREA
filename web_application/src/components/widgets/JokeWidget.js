import React from 'react';
import config from '../../services/Config';

class JokeWidget extends React.Component {

    state = {
        theme: 'fun',
        data: [],
    };

    _handleChange = (e) => {
        this.setState({ [e.target.name]: e.target.value });
    };

    _handleSubmit = () => {
        this._fetch();
    };

    _fetch = () => {
        const { theme } = this.state;
        const url = `${config.serverIp}/api/joke/${theme}`;

        fetch(url, {
            method: "GET",
            headers: {},
        })
            .then(response => response.json())
            .then(responseJson => {
                this.setState({ data: responseJson.results });
            })
            .catch(error => {
                console.error('Error: ', error);
            })
    };

    render() {
        return (
            <>
                <ul>
                    {Object.keys(this.state.data).map((s, i) => (
                        <li key={i} className={i > 0 ? 'separator' : ''}>{this.state.data[s].joke}</li>
                    ))}
                </ul>
                <div className="flex">
                    <input onChange={this._handleChange} name="theme"
                        type="text" placeholder="Theme of the Joke" />
                    <button type="button" className="submit" onClick={this._handleSubmit}>Submit</button>
                </div>
            </>
        );
    }
}

export default JokeWidget
