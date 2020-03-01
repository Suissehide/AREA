import axios from 'axios';
import React, { useState } from "react";
import { Image, StyleSheet, View } from 'react-native';
import Button from '../../components/Button';
import Text from '../../components/Text';
import { theme } from '../../core/theme';

export default function HeroRandomWidget(props) {
    const [name, setName] = useState("Iron Man");
    const [powerstats, setPowerstats] = useState("");
    const [url, setUrl] = useState('https://www.superherodb.com/pictures2/portraits/10/100/85.jpg');

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
            <Text swag={{ fontSize: 17 }}> {name} </Text>
            <Image style={{ width: 200, height: 310, borderRadius: 15 }} source={{ uri: url }} />
            <Button style={styles.button} onPress={handleChange}><Text swag={styles.text}>Random character</Text></Button>
        </View >
    );
}

const styles = StyleSheet.create({
    button: {
        width: '80%',
        marginVertical: 10,
        backgroundColor: theme.colors.brown,
    },
    text: {
        color: theme.colors.primary
    },
});