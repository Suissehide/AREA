import React from 'react';

class DistanceMatrixWidget extends React.Component {

    state = {
        data: null,
        origin: 'Paris',
        destination: 'Bordeaux',
        mode: 'driving',
        key: "AIzaSyCQCPjXryFKgZ9wN9B5E6b05XgYH8yU8j0",
    };

    componentDidMount() {
        this._fetch();
    }

    _handleSubmit = () => {
        this._fetch();
    };

    _handleChange = (e) => {
        this.setState({ [e.target.name]: e.target.value });
    };

    _fetch = () => {
        const url = `http://127.0.0.1:8080/api/google/maps/distance/mode/origin=${this.state.origin}&destination=${this.state.destination}&mode=${this.state.mode}&key=${this.state.key}`;

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
        if (this.state.data) {
            const d = this.state.data;
            return (
                <>
                    <div>
                        <h3> From {d.originAddresses[0]} to {d.destinationAddresses[0]} there is {d.rows[0].elements[0].distance.text} and
                        it takes {d.rows[0].elements[0].duration.text} by {this.state.mode} </h3>
                        <div className="flex">
                            <input onChange={this._handleChange} name="orgin"
                                type="text" placeholder="From" />
                            <input onChange={this._handleChange} name="destination"
                                type="text" placeholder="To" />
                            <button type="button" className="submit" onClick={this._handleSubmit}>Submit</button>
                        </div>
                    </div>
                </>
            );
        } else {
            return (
                <div />
            );
        }
    }
}

export default DistanceMatrixWidget
