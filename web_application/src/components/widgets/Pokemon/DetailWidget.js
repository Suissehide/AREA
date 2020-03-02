import React from 'react';

class DetailWidget extends React.Component {

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
        const url = `http://127.0.0.1:8080/api/pokemon/${pokemon}/detail`;

        fetch(url, {
            method: "GET",
            headers: {},
        })
            .then(response => response.json())
            .then(responseJson => {
                if (responseJson.status)
                    return;
                this.setState({data: responseJson});
            })
            .catch(error => {
                console.error('Error: ', error);
            })
    };

    render() {
        if (typeof(this.state.data) !== 'undefined' && this.state.data) {
            return (
                <>
                    <div>
                        <div className="flex flex-space-between flex-align-items">
                            <div>N°{this.state.data.id}</div>
                            <h1>{this.state.data.name}</h1>
                        </div>
                        <div>
                            {Object.keys(this.state.data.sprites).map((s, i) => (
                                <img key={i} className={'pokemon-sprite'} src={this.state.data.sprites[s]} alt="" />
                            ))}
                        </div>
                        <div>
                            <p>Weight: {Number(this.state.data.weight)/10}kg | Height: {Number(this.state.data.height)/10}m</p>
                        </div>
                    </div>
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

export default DetailWidget
