import axios from 'axios';
import React, { useEffect, useState } from "react";
import { Image, View, StyleSheet } from 'react-native';
import Button from '../../components/Button';
import Text from '../../components/Text';

export default function HeroRandomWidget(props) {
    const [name, setName] = useState("");
    const [powerstats, setPowerstats] = useState("");
    const [url, setUrl] = useState('a');

    const handleChange = () => {
        axios.get(`http://${props.ip}/api/hero/random/`)
            .then(response => {
                console.log(response)
                setName(response.data.name);
                setPowerstats(response.data.powerstats);
                setUrl(response.data.image.url);
            })
            .catch(function (error) {
                console.log(error);
            });
    };

    return (
        <View style={{ paddingTop: 15, alignItems: 'center' }}>

            <Button style={styles.button} onPress={handleChange}><Text swag={styles.text}>Random character</Text></Button>

            <Text swag={{ fontSize: 17 }}> {name} </Text>
            <Image style={{ width: 200, height: 310, borderRadius: 15 }} source={{ uri: url }} />
        </View >
    );
}

const styles = StyleSheet.create({
    button: {
        width: '80%',
        marginVertical: 10,
        backgroundColor: "#3D2314",
    },
    text: {
        color: "#FCCD2D"
    },
});