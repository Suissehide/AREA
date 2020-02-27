import React, { useState } from "react";
import { View } from 'react-native';
import axios from 'axios';
import Text from '../../components/Text'
import TextInput from '../../components/TextInput';

export default function JinkanAnimeWidget(props) {
    const [anime, setAnime] = useState('');
    const [title, setTitle] = useState('Bishoujo Senshi Sailor Moon');
    const [synopsis, setSynopsis] = useState('');
    const [type, setType] = useState('TV');
    const [episodes, setEpisodes] = useState('152');

    const handleChange = () => {
        axios.get(`http://${props.ip}:8080/api/jinkan/anime/${anime}`)
            .then(response => {
                setTitle(response.data.result[0].title);
                setSynopsis(response.data.result[0].synopsis);
                setType(response.data.result[0].type);
                setEpisodes(response.data.result[0].episodes);
            })
            .catch(function (error) {
                console.log(error);
            });
    }

    return (
        <View style={{ alignItems: 'center' }}>
            <View style={{ paddingTop: 10, paddingBottom: 20 }}>
                <View style={{ paddingBottom: 5 }}>
                    <Text swag={{ fontSize: 17 }}> {title} | {type} | {episodes} episodes </Text>
                </View>
                <Text>{synopsis}</Text>
            </View>
            <TextInput
                id="outlined-name"
                label="Anime Title"
                value={anime}
                onChangeText={event => {
                    setAnime(event);
                }}
                onSubmitEditing={handleChange}
                margin="normal"
                variant="outlined"
            />
        </View>
    );
}