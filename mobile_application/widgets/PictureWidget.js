import axios from 'axios';
import React, { useState } from "react";
import { Image, View } from 'react-native';
import TextInput from '../components/TextInput';

export default function PictureWidget(props) {
    const [picture, setPicture] = useState("https://images.unsplash.com/photo-1548681528-6a5c45b66b42?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEwMDc2NX0");
    const [theme, setTheme] = useState("");
    const [description, setDescription] = useState("Cute Kitty");
    const [random, setRandom] = useState(0);

    const handleChange = () => {
        axios.get(`http://${props.ip}/api/photo/${theme}`)
            .then(response => {
                setRandom(Math.floor(Math.random() * response.data.results.length));
                setPicture(response.data.results[random].urls.raw);
                setDescription(response.data.results[random].description);
            })
            .catch(function (error) {
                console.log(error);
            });
    }

    return (
        <View style={{ alignItems: 'center', paddingTop: 20 }}>
            <Image style={{ width: 250, height: 250, borderRadius: 15 }} source={{ uri: picture }} />
            <TextInput
                id="picture"
                label="Theme of the Picture"
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