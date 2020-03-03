import axios from 'axios';
import React, { useState } from "react";
import { Image, StyleSheet, View } from 'react-native';
import Text from '../../components/Text';
import TextInput from '../../components/TextInput';

export default function HeroRandomWidget(props) {
    const [name, setName] = useState("Scarlet Witch");
    const [powerstats, setPowerstats] = useState("");
    const [url, setUrl] = useState('https://www.superherodb.com/pictures2/portraits/10/100/444.jpg');
    const [text, setText] = useState("");

    const handleChange = () => {
        axios.get(`http://${props.ip}/api/hero/name/${text}`)
            .then(response => {

                setName(response.data.results[0].name);
                setPowerstats(response.data.results[0].powerstats);
                setUrl(response.data.results[0].image.url);
            })
            .catch(function (error) {
                console.log(error);
            });
    };

    return (
        <View style={{ paddingTop: 15, alignItems: 'center' }}>
            <Text swag={{ fontSize: 17 }}> {name} </Text>
            <Image style={{ width: 200, height: 310, borderRadius: 15 }} source={{ uri: url }} />
            <TextInput
                id="namehero"
                label="Superhero's Name"
                value={text}
                onChangeText={event => {
                    setText(event);
                }}
                onSubmitEditing={handleChange}
                margin="normal"
                variant="outlined"
            />
        </View >
    );
}

const styles = StyleSheet.create({

});