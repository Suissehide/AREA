import React from 'react';

class MovesWidget extends React.Component {

    state = {
        pokemon: 'pikachu',
        data: null,
    };

    componentDidMount() {
        this._fetch();
    }

    _handleChange = (e) => {
        this.setState({[e.target.name]: e.target.value});
    };

    _handleSubmit = () => {
        this._fetch();
    };

    _fetch = () => {
        const {pokemon} = this.state;
        const url = `http://127.0.0.1:8080/api/pokemon/${pokemon}/moves`;

        fetch(url, {
            method: "GET",
            headers: {},
        })
            .then(response => response.json())
            .then(responseJson => {
                if (responseJson.status)
                    return;
                this.setState({data: responseJson.moves});
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
                            <li key={i} className={i > 0 ? 'separator' : ''}>{this.state.data[i].moveMove.name}</li>
                        ))}
                    </ul>
                    <div className="flex">
                        <input onChange={this._handleChange} name="pokemon"
                               type="text" placeholder="Pokemon Name or Pokedex Number"/>
                        <button type="button" className="submit" onClick={this._handleSubmit}>Submit</button>
                    </div>
                </>
            );
        } else {
            return (
                <>
                    <div className="flex">
                        <input onChange={this._handleChange} name="pokemon"
                               type="text" placeholder="Pokemon Name or Pokedex Number"/>
                        <button type="button" className="submit" onClick={this._handleSubmit}>Submit</button>
                    </div>
                </>
            )
        }
    }
}

export default MovesWidget
