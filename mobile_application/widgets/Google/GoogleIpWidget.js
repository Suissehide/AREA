import React, { useState } from "react";
import { StyleSheet, View } from 'react-native';
import axios from 'axios';
// import MapView, { Marker } from 'react-native-maps';
import Text from '../../components/Text';
import Button from '../../components/Button';

export default function GoogleIpWidget(props) {
    const [country, setCountry] = useState('');
    const [region, setRegion] = useState('');
    const [regionName, setRegionName] = useState('');
    const [city, setCity] = useState('');
    const [zip, setZip] = useState('');
    const [org, setOrg] = useState('');
    const [lat, setLat] = useState(0);
    const [lon, setLon] = useState(0);
    const [query, setQuery] = useState();

    const handleChange = () => {
        axios.get(`http://${props.ip}/api/ip`)
            .then(response => {
                setQuery(response.data.query);
                setCountry(response.data.country);
                setRegion(response.data.region);
                setCountry(response.data.country);
                setRegionName(response.data.regionName);
                setCity(response.data.city);
                setZip(response.data.zip);
                setOrg(response.data.org);
                setLat(response.data.lat);
                setLon(response.data.lon);
            })
            .catch(function (error) {
                console.log(error);
            });
    }

    return (
        <View style={{ alignItems: 'center' }}>
            {lat === 0 ?
                <Button style={styles.button} onPress={handleChange}><Text swag={styles.text}>See</Text></Button>
                :
                <View>
                    <View style={{ paddingTop: 10, paddingBottom: 20 }}>
                        <View style={{ paddingBottom: 5 }}>
                            <Text swag={{ fontSize: 17 }}>
                                Your IP is {query}. {"\n"}You are situated in {city} {zip}, {country}. {"\n"}
                                Your organisation is {org}.
                        </Text>
                        </View>
                    </View>
                    <View style={{ height: 300, width: 250, marginTop: -10 }}>
                        <MapView
                            style={styles.map}
                            initialRegion={{
                                latitude: lat,
                                longitude: lon,
                                latitudeDelta: 0.0922,
                                longitudeDelta: 0.0421,
                            }}
                            marker={{}}
                            scrollEnabled={false}
                            provider={"google"}
                        >
                            <Marker coordinate={{ latitude: lat, longitude: lon }} />
                        </MapView>
                    </View>
                </View>
            }
        </View>
    );
}

const styles = StyleSheet.create({
    button: {
        width: '80%',
        marginVertical: 10,
        backgroundColor: "#3D2314",
    },
    text: {
        color: "#FCCD2D"
    },
    map: {
        ...StyleSheet.absoluteFillObject,
    },
});
