import React from 'react';

class BananeWidget extends React.Component {

    state = {
        data: null,
    };

    componentDidMount() {
        this._fetch();
    }

    _fetch = () => {
        const url = `http://127.0.0.1:8080/api/news/banana`;

        fetch(url, {
            method: "GET",
            headers: {},
        })
            .then(response => response.json())
            .then(responseJson => {
                this.setState({data: responseJson.articles});
            })
            .catch(error => {
                console.error('Error: ', error);
            })
    };

    render() {
        if (typeof(this.state.data) !== 'undefined' && this.state.data) {
            return (
                <>
                    <ul>
                        {Object.keys(this.state.data).map((s, i) => (
                            <li key={i} className={i > 0 ? 'separator' : ''}>
                                <h3>{this.state.data[i].title}</h3>
                                <p>{this.state.data[i].description}</p>
                                <em>{this.state.data[i].source.name} | {this.state.data[i].publishedAt}</em>
                                <div className="article-link"><a className="submit refresh" href={this.state.data[i].url}><i className="fas fa-arrow-right"/></a></div>
                            </li>
                        ))}
                    </ul>
                </>
            );
        } else {
            return (
                <></>
            )
        }
    }
}

export default BananeWidget
