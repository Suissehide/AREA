import React from 'react';

class PhotoWidget extends React.Component {

    state = {
        theme: 'cat',
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
        const { theme } = this.state;
        const url = `${config.serverIp}/api/photo/${theme}`;

        fetch(url, {
            method: "GET",
            headers: {},
        })
            .then(response => response.json())
            .then(responseJson => {
                if (responseJson.status)
                    return;
                this.setState({ data: responseJson.results });
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
                            <img key={i} className={'picture'} src={this.state.data[s].urls.small} alt="" />
                        ))}
                    </ul>
                    <div className="flex">
                        <input onChange={this._handleChange} name="theme"
                            type="text" placeholder="Theme of the picture" />
                        <button type="button" className="submit" onClick={this._handleSubmit}>Submit</button>
                    </div>
                </>
            );
        } else {
            return (
                <>
                    <div className="flex">
                        <input onChange={this._handleChange} name="theme"
                            type="text" placeholder="Theme of the picture" />
                        <button type="button" className="submit" onClick={this._handleSubmit}>Submit</button>
                    </div>
                </>
            )
        }
    }
}

export default PhotoWidget
