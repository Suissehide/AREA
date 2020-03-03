import React from 'react';

class AnimeWidget extends React.Component {

    state = {
        anime: 'cat',
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
        const { anime } = this.state;
        const url = `${config.serverIp}/api/jikan/anime/${anime}`;

        fetch(url, {
            method: "GET",
            headers: {},
        })
            .then(response => response.json())
            .then(responseJson => {
                if (responseJson.status)
                    return;
                this.setState({ data: responseJson.result });
            })
            .catch(error => {
                console.error('Error: ', error);
            })
    };

    render() {
        if (typeof (this.state.data) !== 'undefined' && this.state.data) {
            return (
                <>
                    <ul>
                        {Object.keys(this.state.data).map((s, i) => (
                            <li key={i} className={i > 0 ? 'separator' : ''}>
                                <div className="manga-title">{this.state.data[i].title}</div>
                                <p>{this.state.data[i].synopsis}</p>
                                <a className="submit refresh" href={this.state.data[i].url}><i className="fas fa-arrow-right" /></a>
                            </li>
                        ))}
                    </ul>
                    <div className="flex">
                        <input onChange={this._handleChange} name="anime"
                            type="text" placeholder="Anime's title" />
                        <button type="button" className="submit" onClick={this._handleSubmit}>Submit</button>
                    </div>
                </>
            );
        } else {
            return (
                <>
                    <div className="flex">
                        <input onChange={this._handleChange} name="anime"
                            type="text" placeholder="Anime's title" />
                        <button type="button" className="submit" onClick={this._handleSubmit}>Submit</button>
                    </div>
                </>
            )
        }
    }
}

export default AnimeWidget
