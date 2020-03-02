import React from 'react';
import GoogleMapReact from 'google-map-react';

class IpMapWidget extends React.Component {

    state = {
        data: null,
    };

    componentDidMount() {
        this._fetch();
    }

    _fetch = () => {
        const url = `http://127.0.0.1:8080/api/ip`;

        fetch(url, {
            method: "GET",
            headers: {},
        })
            .then(response => response.json())
            .then(responseJson => {
                this.setState({data: responseJson});
            })
            .catch(error => {
                console.error('Error: ', error);
            })
    };

    render() {
        if (this.state.data) {
            return (
                <>
                    <div>
                        <div>
                            <p>Your IP is {this.state.data.query}.</p>
                            <p>You are situated
                                in {this.state.data.city} {this.state.data.zip}, {this.state.data.country}.</p>
                            <p>Your organisation is {this.state.data.isp}.</p>
                        </div>
                        <div className="map">
                            <GoogleMapReact
                                bootstrapURLKeys={{
                                    key: "AIzaSyDd8Vt3lX66W7uN9mpU2OmYHDPOiHGOrco",
                                    language: 'fr'
                                }}
                                defaultCenter={{lat: this.state.data.lat, lng: this.state.data.lon}}
                                center={{lat: this.state.data.lat, lng: this.state.data.lon}}
                                defaultZoom={12}
                                onChildMouseEnter={this.onChildMouseEnter}
                                onChildMouseLeave={this.onChildMouseLeave}
                            />
                        </div>
                    </div>
                </>
            );
        } else {
            return (
                <div/>
            );
        }
    }
}

export default IpMapWidget
