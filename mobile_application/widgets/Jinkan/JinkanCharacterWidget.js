import React, { useState } from "react";
import { View, Image } from 'react-native';
import axios from 'axios';
import Text from '../../components/Text'
import TextInput from '../../components/TextInput';

export default function JinkanAnimeWidget(props) {
    const [character, setCharacter] = useState('');
    const [name, setName] = useState('Aelita Schaeffer');
    const [imageUrl, setImageUrl] = useState('https://fr.gravatar.com/userimage/153874692/c25f3db16ba5560cd9dbb58d53af938e?size=512');

    const handleChange = () => {
        axios.get(`http://${props.ip}:8080/api/jinkan/character/${character}`)
            .then(response => {
                setName(response.data.characterInfo[0].name);
                setImageUrl(response.data.characterInfo[0].imageUrl);
            })
            .catch(function (error) {
                console.log(error);
            });
    }
    return (
        <View style={{ alignItems: 'center' }}>
            <View style={{ paddingTop: 10, paddingBottom: 20 }}>
                <View style={{ paddingBottom: 5 }}>
                    <Text swag={{ fontSize: 17 }}> {name} </Text>
                </View>
                <Image style={{ width: 200, height: 200 }} source={{ uri: imageUrl }} />
            </View>
            <TextInput
                id="outlined-name"
                label="Character Name"
                value={character}
                onChangeText={event => {
                    setCharacter(event);
                }}
                onSubmitEditing={handleChange}
                margin="normal"
                variant="outlined"
            />
        </View>
    );
}