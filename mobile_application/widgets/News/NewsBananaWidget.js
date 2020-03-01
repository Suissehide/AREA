import { Ionicons } from '@expo/vector-icons';
import axios from 'axios';
import React, { useEffect, useState } from "react";
import { Linking, TouchableOpacity, View } from 'react-native';
import Text from '../../components/Text';

export default function NewsBananaWidget(props) {
    const [description, setDescription] = useState("Cute Kitty");
    const [number, setNumber] = useState(0);
    const [title, setTitle] = useState("");
    const [url, setUrl] = useState("a");
    const [source, setSource] = useState("");
    const [publishedAt, setPublishedAt] = useState("");

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
        axios.get(`http://${props.ip}/api/news/banana`)
            .then(response => {
                setTitle(response.data.articles[number].title);
                setDescription(response.data.articles[number].description);
                setUrl(response.data.articles[number].url);
                setSource(response.data.articles[number].source.name);
                setPublishedAt(response.data.articles[number].publishedAt);
            })
            .catch(function (error) {
                console.log(error);
            });
    });

    return (
        <View style={{ alignItems: 'center', paddingTop: 20 }}>
            <View style={{ flexDirection: 'row', width: '100%', alignItems: 'center', justifyContent: 'space-around', paddingTop: 15 }} >
                <TouchableOpacity onPress={() => setNumber(Math.abs(number - 1))}>
                    <MyIcon name="ios-arrow-back" />
                </TouchableOpacity>
                <View style={{ width: '80%', alignItems: 'center' }} >
                    <Text swag={{ fontSize: 20, fontWeight: 'bold' }} >{title}</Text>
                    <Text >Source : <Text swag={{ fontWeight: 'bold' }} > {source} </Text></Text>
                    <Text swag={{ paddingTop: 10, paddingBottom: 10 }} > {description} </Text>
                    <Text swag={{ color: 'blue' }}
                        onPress={() => Linking.openURL(url)}>
                        Read the article on {source}
                    </Text>
                </View>
                <TouchableOpacity onPress={() => setNumber(number + 1)}>
                    <MyIcon name="ios-arrow-forward" />
                </TouchableOpacity>
            </View>
        </View>
    );
}