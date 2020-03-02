import { Ionicons } from '@expo/vector-icons';
import axios from 'axios';
import React, { useEffect, useState } from "react";
import { StyleSheet, View } from 'react-native';
import Text from '../../components/Text';
import TextInput from '../../components/TextInput';
import { theme } from '../../core/theme';
// import MapView, { Marker } from 'react-native-maps';

export default function GooglePlaceWidget(props) {
    const [query, setQuery] = useState('');
    const [id, setId] = useState('');
    const [name, setName] = useState('');
    const [status, setStatus] = useState(null);
    const [formattedAddress, setFormattedAddress] = useState(null);
    const [rating, setRating] = useState(null);
    const [location, setLocation] = useState(null);
    var key = "AIzaSyCQCPjXryFKgZ9wN9B5E6b05XgYH8yU8j0";

    function MyIcon(props) {
        return (
            <Ionicons
                name={props.name}
                size={25}
                style={{ color: theme.colors.primary }}
            />
        );
    }

    const handleChange = () => {
        axios.get(`http://${props.ip}/api/google/maps/place/search/query=${query}&key=${key}`)
            .then(response => {
                setId(response.data.results[0].placeId);
                setLocation(response.data.results[0].geometry.location);
                setFormattedAddress(response.data.results[0].formattedAddress);
            })
            .catch(function (error) {
                console.log(error);
            })
    }

    useEffect(() => {
        axios.get(`http://${props.ip}/api/google/maps/place/detail/id=${id}&key=${key}`)
            .then(response => {
                setStatus(response.data.status);
                setName(response.data.result.name);
                setRating(response.data.result.rating);
            })
            .catch(function (error) {
                console.log(error);
            })
    }, [id]);

    return (
        <View style={{ alignItems: 'center' }}>
            <TextInput id="place" label="Place Name"
                value={query} onChangeText={event => { setQuery(event) }}
                margin="normal" variant="outlined"
                onSubmitEditing={() => handleChange()}
            />
            {status === "OK" ? <View>
                <Text swag={{ fontSize: 17, fontWeight: 'bold' }} > {name} </Text>
                <Text> Rated: {rating}/5 </Text>
                <Text> Address: {formattedAddress} </Text>
                <View style={{ height: 300, width: 250, marginVertical: 10 }}>
                    <MapView style={styles.map}
                        region={{
                            latitude: location.lat,
                            longitude: location.lng,
                            latitudeDelta: 0.01,
                            longitudeDelta: 0.0421,
                        }}
                        scrollEnabled={false} provider={"google"} >
                        <Marker coordinate={{
                            latitude: location.lat,
                            longitude: location.lng,
                        }} />
                    </MapView>
                </View>
            </View>
                : status === null ? null : <Text> No results found. </Text>
            }
        </View >
    );
}

const styles = StyleSheet.create({
    button: {
        width: '100%',
        marginVertical: 10,
        backgroundColor: theme.colors.brown,
    },
    text: {
        color: theme.colors.primary
    },
    map: {
        ...StyleSheet.absoluteFillObject,
    },
});
