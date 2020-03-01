import React, { useState } from "react";
import { View } from 'react-native';
import { StyleSheet } from 'react-native';
import axios from 'axios';
import Text from '../../components/Text'
import TextInput from '../../components/TextInput';
import Button from '../../components/Button';

export default function GoogleDistanceWidget(props) {
    const [origin, setOrigin] = useState('');
    const [destination, setDestination] = useState('');
    const [destinationAddresses, setDestinationAddresses] = useState('');
    const [originAddresses, setOriginAddresses] = useState('');
    const [distance, setDistance] = useState('');
    const [duration, setDuration] = useState('');
    const [status, setStatus] = useState('');
    var key = "AIzaSyCQCPjXryFKgZ9wN9B5E6b05XgYH8yU8j0";

    const handleChange = () => {
        axios.get(`http://${props.ip}/api/google/maps/distance/origin=${origin}&destination=${destination}&key=${key}`)
            .then(response => {
                setStatus(response.data.rows[0].elements[0].status);
                setDestinationAddresses(response.data.destinationAddresses[0]);
                setOriginAddresses(response.data.originAddresses[0]);
                setDistance(response.data.rows[0].elements[0].distance);
                setDuration(response.data.rows[0].elements[0].duration);
            })
            .catch(function (error) {
                console.log(error);
            });
    }

    return (
        <View style={{ alignItems: 'center' }}>
            <TextInput id="origin" label="From"
                value={origin} onChangeText={event => { setOrigin(event); }}
                margin="normal" variant="outlined"
            />
            <TextInput id="destination" label="To"
                value={destination}
                onChangeText={event => { setDestination(event); }}
                onSubmitEditing={handleChange}
                margin="normal" variant="outlined"
            />

            {status === "NOT_FOUND" || status === "ZERO_RESULTS" ? <Text>No results found.</Text> : status === "OK" ?
                <Text swag={{ fontSize: 20 }} >
                    The distance between <Text swag={{ fontWeight: 'bold' }} >{originAddresses}</Text> and <Text swag={{ fontWeight: 'bold' }} >
                        {destinationAddresses}</Text> is <Text swag={{ fontWeight: 'bold' }} >{distance.text}</Text>.
                    {"\n"}It takes <Text swag={{ fontWeight: 'bold' }} >{duration.text}</Text> by car.
                </Text> : null
            }
            <Button style={styles.button} onPress={handleChange}><Text swag={styles.text}>Calculate Distance</Text></Button>
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
});
