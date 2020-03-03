import React from 'react';

class JikanWidget extends React.Component {

    state = {
        name: 'Naruto',
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
        const url = `${config.serverIp}/api/jikan/character/${name}`;

        fetch(url, {
            method: "GET",
            headers: {},
        })
            .then(response => response.json())
            .then(responseJson => {
                if (responseJson.status)
                    return;
                this.setState({ data: responseJson.characterInfo });
            })
            .catch(error => {
                console.error('Error: ', error);
            })
    };

    render() {
        if (typeof (this.state.data) !== 'undefined' && this.state.data) {
            return (
                <>
                    <ul className="flex">
                        {Object.keys(this.state.data).map((s, i) => (
                            <li key={i} className="flex flex-column">
                                <img className={'picture'} src={this.state.data[i].imageUrl} alt="" />
                                <em>{this.state.data[i].name}</em>
                            </li>
                        ))}
                    </ul>
                    <div className="flex">
                        <input onChange={this._handleChange} name="name"
                            type="text" placeholder="Character's Name" />
                        <button type="button" className="submit" onClick={this._handleSubmit}>Submit</button>
                    </div>
                </>
            );
        } else {
            return (
                <>
                    <div className="flex">
                        <input onChange={this._handleChange} name="name"
                            type="text" placeholder="Character's Name" />
                        <button type="button" className="submit" onClick={this._handleSubmit}>Submit</button>
                    </div>
                </>
            )
        }
    }
}

export default JikanWidget
