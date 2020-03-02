import axios from 'axios';
import React, { useEffect, useRef, useState } from "react";
import { View, StyleSheet } from 'react-native';
import Text from '../../components/Text';
// import MapView, { Marker } from 'react-native-maps';

export default function IssLocationWidget(props) {
    const [latitude, setLatitude] = useState(0);
    const [longitude, setLongitude] = useState(0);
    const savedCallback = useRef();

    function callback() {
        axios.get(`http://${props.ip}/api/location/station_location`)
            .then(response => {
                setLatitude(response.data.issPosition.latitude);
                setLongitude(response.data.issPosition.longitude);
            })
            .catch(function (error) {
                console.log(error);
            });
    }

    useEffect(() => {
        savedCallback.current = callback;
    });

    useEffect(() => {
        function tick() {
            savedCallback.current();
        }

        let id = setInterval(tick, 5000);
        return () => clearInterval(id);
    }, []);

    return (
        <View style={{ alignItems: 'center', paddingTop: 20 }}>
            <Text> The ISS is currently at {"\n"}<Text swag={{ fontWeight: 'bold' }} >
                {latitude} </Text>lat, <Text swag={{ fontWeight: 'bold' }} >
                    {longitude} </Text>lon. </Text>
            <View style={{ height: 300, width: 250, marginVertical: 10 }}>
                <MapView style={styles.map}
                    region={{
                        latitude: parseFloat(latitude),
                        longitude: parseFloat(longitude),
                        latitudeDelta: 50,
                        longitudeDelta: 0.0421,
                    }}
                    scrollEnabled={false} provider={"google"} >
                    <Marker coordinate={{
                        latitude: parseFloat(latitude),
                        longitude: parseFloat(longitude),
                    }} title="ISS" />
                </MapView>
            </View>
            <Text>Actualised every 5 secondes.</Text>
        </View>
    );
}

const styles = StyleSheet.create({
    map: {
        ...StyleSheet.absoluteFillObject,
    },
});