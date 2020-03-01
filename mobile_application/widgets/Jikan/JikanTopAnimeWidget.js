import { Ionicons } from '@expo/vector-icons';
import axios from 'axios';
import React, { useEffect, useState } from "react";
import { Image, TouchableOpacity, View } from 'react-native';
import Text from '../../components/Text';

export default function JikanTopAnimeWidget(props) {
    const [number, setNumber] = useState(0);
    const [rank, setRank] = useState(1);
    const [title, setTitle] = useState('');
    const [imageUrl, setImageUrl] = useState('a');
    const [type, setType] = useState("");
    const [episodes, setEpisodes] = useState('');
    const [startDate, setStartDate] = useState('');
    const [endDate, setEndDate] = useState('');
    const [score, setScore] = useState('');

    function MyIcon(props) {
        return (
            <Ionicons
                name={props.name}
                size={30}
                style={{ marginBottom: -3 }}
            />
        );
    }

    useEffect(() => {
        axios.get(`http://${props.ip}/api/jikan/top_anime/`)
            .then(response => {
                setRank(response.data.top[number].rank);
                setTitle(response.data.top[number].title);
                setImageUrl(response.data.top[number].imageUrl);
                setType(response.data.top[number].type);
                setEpisodes(response.data.top[number].episodes);
                setScore(response.data.top[number].score);
                setStartDate(response.data.top[number].startDate);
                setEndDate(response.data.top[number].endDate);
            })
            .catch(function (error) {
                console.log(error);
            });
    });

    return (
        <View style={{ paddingTop: 15 }}>
            <Text swag={{ fontSize: 17 }}> #{rank} {title} </Text>
            {type === "Movie" ? <Text swag={{ fontSize: 17 }}>{type} </Text> : <Text swag={{ fontSize: 17 }}> {episodes} episodes </Text>}
            <Text swag={{ fontSize: 17 }}> Scored {score}/10 {"\n"} Started: {startDate} | Ended: {endDate} </Text>
            <View style={{ flexDirection: 'row', width: '100%', alignItems: 'center', justifyContent: 'space-around', paddingTop: 15 }} >
                <TouchableOpacity onPress={() => setNumber(Math.abs(number - 1))}>
                    <MyIcon name="ios-arrow-back" />
                </TouchableOpacity>
                <Image style={{ width: 200, height: 310, borderRadius: 15 }} source={{ uri: imageUrl }} />
                <TouchableOpacity onPress={() => setNumber(number + 1)}>
                    <MyIcon name="ios-arrow-forward" />
                </TouchableOpacity>
            </View>
        </View >
    );
}