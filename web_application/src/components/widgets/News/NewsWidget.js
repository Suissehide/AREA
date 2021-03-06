import React from 'react';
import config from '../../../services/Config';

class NewsWidget extends React.Component {

    state = {
        theme: 'fart',
        data: null,
    };

    componentDidMount() {
        this._fetch();
    }

    _fetch = () => {
        const { theme } = this.state;
        const url = `${config.serverIp}/api/news/${theme}`;

        fetch(url, {
            method: "GET",
            headers: {},
        })
            .then(response => response.json())
            .then(responseJson => {
                this.setState({ data: responseJson.articles });
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
                                <h3>{this.state.data[i].title}</h3>
                                <p>{this.state.data[i].description}</p>
                                <em>{this.state.data[i].source.name} | {this.state.data[i].publishedAt}</em>
                                <div className="article-link"><a className="submit refresh" href={this.state.data[i].url}><i className="fas fa-arrow-right" /></a></div>
                            </li>
                        ))}
                    </ul>
                    <div className="flex">
                        <input onChange={this._handleChange} name="theme"
                            type="text" placeholder="Anime's title" />
                        <button type="button" className="submit" onClick={this._handleSubmit}>Submit</button>
                    </div>
                </>
            );
        } else {
            return (
                <>
                    <div className="flex">
                        <input onChange={this._handleChange} name="theme"
                            type="text" placeholder="Anime's title" />
                        <button type="button" className="submit" onClick={this._handleSubmit}>Submit</button>
                    </div>
                </>
            )
        }
    }
}

export default NewsWidget
