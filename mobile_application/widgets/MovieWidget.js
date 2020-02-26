import React, { useState } from "react";
import { View } from 'react-native';
import axios from 'axios';
import Text from '../components/Text'
import { TextInput } from "react-native-paper";

export default function MovieWidget(props) {
    const [movie, setMovie] = useState('Harry Potter');
    const [title, setTitle] = useState('');
    const [overview, setOverview] = useState('');

    axios.get(`http://${props.ip}:8080/api/TmdbApi/movie/${movie}`)
        .then(response => {
            setTitle(response.data[0].title);
            setOverview(response.data[0].overview);
        })
        .catch(function (error) {
            console.log(error);
        });

    return (
        <View style={{ alignItems: 'center' }}>
            <View style={{ paddingTop: 10, paddingBottom: 20 }}>
                <View style={{ paddingBottom: 5 }}>
                    <Text swag={{ fontSize: '17px' }}> {title} </Text>
                </View>
                <Text>{overview}</Text>
            </View>
            <TextInput
                id="outlined-name"
                label="Movie Title"
                value={movie}
                onChange={event => {
                    setMovie(event.target.value);
                }}
                margin="normal"
                variant="outlined"
            />
        </View>
    );
}