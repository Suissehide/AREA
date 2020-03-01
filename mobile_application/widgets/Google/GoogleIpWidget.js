import axios from 'axios';
import React, { useEffect, useState } from "react";
import { StyleSheet, View } from 'react-native';
import MapView, { Marker } from 'react-native-maps';
import Text from '../../components/Text';

export default function GoogleIpWidget(props) {
    const [country, setCountry] = useState('');
    const [city, setCity] = useState('');
    const [zip, setZip] = useState('');
    const [org, setOrg] = useState('');
    const [lat, setLat] = useState(0);
    const [lon, setLon] = useState(0);
    const [query, setQuery] = useState();

    useEffect(() => {
        axios.get(`http://${props.ip}/api/ip`)
            .then(response => {
                setQuery(response.data.query);
                setCountry(response.data.country);
                setCountry(response.data.country);
                setCity(response.data.city);
                setZip(response.data.zip);
                setOrg(response.data.org);
                setLat(response.data.lat);
                setLon(response.data.lon);
            })
            .catch(function (error) {
                console.log(error);
            });
    }, []);

    return (
        <View style={{ paddingTop: 10, alignItems: 'center' }}>
            <Text swag={{ fontSize: 17, paddingBottom: 5 }}>
                Your IP is {query}. {"\n"}You are situated in {city} {zip}, {country}. {"\n"}
                Your organisation is {org}.
            </Text>
            {lat !== 0 ?
                <View style={{ height: 300, width: 250, marginTop: 10 }}>
                    <MapView style={styles.map}
                        initialRegion={{
                            latitude: lat,
                            longitude: lon,
                            latitudeDelta: 0.0922,
                            longitudeDelta: 0.0421,
                        }}
                        scrollEnabled={false} provider={"google"} >
                        <Marker coordinate={{ latitude: lat, longitude: lon }} />
                    </MapView>
                </View> : null}
        </View>
    );
}

const styles = StyleSheet.create({
    map: {
        ...StyleSheet.absoluteFillObject,
    },
});
