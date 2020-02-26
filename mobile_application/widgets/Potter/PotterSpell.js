import React, { useState } from "react";
import { StyleSheet, View } from 'react-native';
import { Text } from 'react-native-elements';
import Button from '../../components/Button'
import axios from 'axios';

export default function PotterSpell(props) {
    const [spell, setSpell] = useState("");
    const [type, setType] = useState("");
    const [effect, setEffect] = useState("");

    const handleChange = () => {
        axios.get(`http://${props.ip}:8080/api/PotterApi/randomSpells`)
            .then(response => {
                setSpell(response.data.spell);
                setType(response.data.type);
                setEffect(response.data.effect);
            })
            .catch(function (error) {
                console.log(error);
            });
    }
    return (
        <View style={{ alignItems: 'center' }}>
            <Button style={styles.button} onPress={handleChange}><Text style={styles.text}>Get a random spell</Text></Button>
            <Text> Spell Name : {spell}</Text>
            <Text> Spell Type : {type}</Text>
            <Text> Spell Effect : {effect}</Text>
        </View>
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
