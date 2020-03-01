import React, { useState } from "react";
import { View, Image } from 'react-native';
import axios from 'axios';
import Text from '../../components/Text'
import TextInput from '../../components/TextInput';

export default function JikanAnimeWidget(props) {
    const [character, setCharacter] = useState('');
    const [name, setName] = useState('Aelita Schaeffer');
    const [imageUrl, setImageUrl] = useState('https://fr.gravatar.com/userimage/153874692/c25f3db16ba5560cd9dbb58d53af938e?size=512');

    const handleChange = () => {
        axios.get(`http://${props.ip}/api/jikan/character/${character}`)
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
            <View style={{ paddingTop: 10 }}>
                <View style={{ paddingBottom: 5 }}>
                    <Text swag={{ fontSize: 17 }}> {name} </Text>
                </View>
                {name === 'Aelita Schaeffer' ? <Image
                    style={{ width: 200, height: 200, borderRadius: 15 }} source={{ uri: imageUrl }} /> :
                    <Image
                        style={{ width: 187, height: 290, borderRadius: 15 }} source={{ uri: imageUrl }} />}
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