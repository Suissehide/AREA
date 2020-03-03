import React from 'react';
import GoogleMapReact from 'google-map-react';
import config from '../../../services/Config';

class IssLocationWidget extends React.Component {

    state = {
        data: null,
    };

    componentDidMount() {
        this._fetch();
        this.timerID = setInterval(
            () => this._fetch(),
            5000
        );
    }

    componentWillUnmount() {
        clearInterval(this.timerID);
    }

    _fetch = () => {
        const url = `${config.serverIp}/api/location/station_location`;

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
            return (
                <>
                    <p>The location of the ISS is {this.state.data.issPosition.latitude} LAT and {this.state.data.issPosition.longitude} LON.</p>
                    <div className="map">
                        <GoogleMapReact
                            bootstrapURLKeys={{
                                key: "AIzaSyDd8Vt3lX66W7uN9mpU2OmYHDPOiHGOrco",
                                language: 'fr'
                            }}
                            defaultCenter={{ lat: parseFloat(this.state.data.issPosition.latitude), lng: parseFloat(this.state.data.issPosition.longitude) }}
                            center={{ lat: parseFloat(this.state.data.issPosition.latitude), lng: parseFloat(this.state.data.issPosition.longitude) }}
                            defaultZoom={7}
                            onChildMouseEnter={this.onChildMouseEnter}
                            onChildMouseLeave={this.onChildMouseLeave}
                        />
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

export default IssLocationWidget;
