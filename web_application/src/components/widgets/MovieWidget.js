import React from 'react';

class MovieWidget extends React.Component {

    state = {
        movie: 'Interstellar',
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
        const { movie } = this.state;
        const url = `http://127.0.0.1:8080/api/movie-database/movie/${movie}`;

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
        if (this.state.data && this.state.data[0]) {
            return (
                <>
                    <div className="flex flex-align-items">
                        <div className="movie">
                            <h1>{this.state.data[0].title}</h1>
                            <em>{this.state.data[0].release}</em>
                            <p>{this.state.data[0].overview}</p>
                        </div>
                        <div className="popularity">
                            {this.state.data[0].popularity}
                        </div>
                    </div>
                    <div className="flex">
                        <input onChange={this._handleChange} name="movie"
                            type="text" placeholder="Movie's title" />
                        <button type="button" className="submit" onClick={this._handleSubmit}>Submit</button>
                    </div>
                </>
            );
        } else {
            return (
                <>
                    <div className="flex">
                        <input onChange={this._handleChange} name="movie"
                            type="text" placeholder="Movie's title" />
                        <button type="button" className="submit" onClick={this._handleSubmit}>Submit</button>
                    </div>
                </>
            )
        }
    }
}

export default MovieWidget
