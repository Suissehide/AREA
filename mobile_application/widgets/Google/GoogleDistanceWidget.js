import { Ionicons } from '@expo/vector-icons';
import axios from 'axios';
import React, { useState, useEffect } from "react";
import { StyleSheet, View } from 'react-native';
import Button from '../../components/Button';
import Text from '../../components/Text';
import TextInput from '../../components/TextInput';
import { theme } from '../../core/theme';

export default function GoogleDistanceWidget(props) {
    const [origin, setOrigin] = useState('');
    const [destination, setDestination] = useState('');
    const [destinationAddresses, setDestinationAddresses] = useState('');
    const [originAddresses, setOriginAddresses] = useState('');
    const [distance, setDistance] = useState('');
    const [duration, setDuration] = useState('');
    const [status, setStatus] = useState('');
    const [mode, setMode] = useState('');
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

    useEffect(() => {
        axios.get(`http://${props.ip}/api/google/maps/distance/origin=${origin}&destination=${destination}&mode=${mode}&key=${key}`)
            .then(response => {
                console.log(response.data)
                setStatus(response.data.rows[0].elements[0].status);
                setDestinationAddresses(response.data.destinationAddresses[0]);
                setOriginAddresses(response.data.originAddresses[0]);
                setDistance(response.data.rows[0].elements[0].distance);
                setDuration(response.data.rows[0].elements[0].duration);
            })
            .catch(function (error) {
                console.log(error);
            });
    }, [mode]);

    return (
        <View style={{ alignItems: 'center' }}>
            <TextInput id="origin" label="From"
                value={origin} onChangeText={event => { setOrigin(event); }}
                margin="normal" variant="outlined"
            />
            <TextInput id="destination" label="To"
                value={destination}
                onChangeText={event => { setDestination(event); }}
                margin="normal" variant="outlined"
            />
            {status === "NOT_FOUND" || status === "ZERO_RESULTS" ? <Text>No results found.</Text> : status === "OK" ?
                <Text swag={{ fontSize: 20 }} >
                    The distance between <Text swag={{ fontWeight: 'bold' }} >{originAddresses}</Text> and <Text swag={{ fontWeight: 'bold' }} >
                        {destinationAddresses}</Text> is <Text swag={{ fontWeight: 'bold' }} >{distance.text}</Text>.
                    {"\n"}It takes <Text swag={{ fontWeight: 'bold' }} >{duration.text}</Text> by {mode}.
                </Text> : null
            }
            <View style={{ flexDirection: 'row', marginHorizontal: 10 }} >
                <Button style={styles.button} onPress={() => setMode('driving')}><MyIcon name="md-car" /> </Button>
                <Button style={styles.button} onPress={() => setMode('walking')}><MyIcon name="md-walk" /></Button>
                <Button style={styles.button} onPress={() => setMode('bicycling')}><MyIcon name="md-bicycle" /></Button>
                <Button style={styles.button} onPress={() => setMode('transit')}><MyIcon name="md-train" /></Button>
            </View>
        </View >
    );
}

const styles = StyleSheet.create({
    button: {
        width: '0%',
        marginVertical: 10,
        backgroundColor: theme.colors.brown,
        marginHorizontal: 3
    },
    text: {
        color: theme.colors.primary
    },
});
