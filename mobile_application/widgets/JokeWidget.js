import React, { useState } from "react";
import { View } from 'react-native';
import axios from 'axios';
import Text from '../components/Text'
import TextInput from '../components/TextInput';

export default function JokeWidget(props) {
    const [joke, setJoke] = useState("");
    const [theme, setTheme] = useState("");

    const handleChange = () => {
        axios.get(`http://${props.ip}/api/joke/${theme}`)
            .then(response => {
                setJoke(response.data.results[Math.floor(Math.random() * response.data.total_jokes)].joke);
            })
            .catch(function (error) {
                console.log(error);
            });
    }

    return (
        <View style={{ alignItems: 'center' }}>
            <Text swag={{ paddingBottom: 10, paddingTop: 15 }}>{joke}</Text>
            <TextInput
                id="joke"
                label="Theme of the Joke"
                value={theme}
                onChangeText={event => {
                    setTheme(event);
                }}
                onSubmitEditing={handleChange}
                margin="normal"
                variant="outlined"
            />
        </View>
    );
}