import React, { useState } from "react";
import { View } from 'react-native';
import axios from 'axios';
import Text from '../components/Text'
import TextInput from '../components/TextInput';

export default function MovieWidget(props) {
    const [movie, setMovie] = useState('');
    const [title, setTitle] = useState('');
    const [overview, setOverview] = useState('');
    const [voteAverage, setVoteAverage] = useState(null);

    const handleChange = () => {
        axios.get(`http://${props.ip}/api/movie-database/movie/${movie}`)
            .then(response => {
                setTitle(response.data[0].title);
                setOverview(response.data[0].overview);
                setVoteAverage(response.data[0].voteAverage);
            })
            .catch(function (error) {
                console.log(error);
            });
    }

    return (
        <View style={{ alignItems: 'center' }}>
            <View style={{ paddingTop: 10, paddingBottom: 20 }}>
                <View style={{ paddingBottom: 5 }}>
                    <Text swag={{ fontSize: 17 }}> {title} </Text>
                </View>
                {voteAverage !== null ? <Text>{voteAverage}/10</Text> : null}
                <Text>{overview}</Text>
            </View>
            <TextInput
                id="movie"
                label="Movie Title"
                value={movie}
                onChangeText={event => {
                    setMovie(event);
                }}
                onSubmitEditing={handleChange}
                margin="normal"
                variant="outlined"
            />
        </View>
    );
}