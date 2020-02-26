import React, { useState } from "react";
import { StyleSheet, View } from 'react-native';
import { Text } from 'react-native-elements';
import { theme } from '../../core/theme';
import Button from '../../components/Button'
import axios from 'axios';

export default function PotterSpell() {
    const [id, setId] = useState("");
    const [spell, setSpell] = useState("");
    const [type, setType] = useState("");
    const [effect, setEffect] = useState("");

    const handleChange = () => {
        axios.get(`http://localhost:8080/api/PotterApi/randomSpells`)
            .then(response => {
                setId(response.data.id);
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
    container: {
        flex: 1,
        backgroundColor: '#fafafa',
    },
    button: {
        width: '80%',
        marginVertical: 10,
        backgroundColor: "#3D2314",
    },
    contentContainer: {
        paddingTop: 15,
    },
    title: {
        fontSize: 20,
        alignSelf: "center",
    },
    card: {
        backgroundColor: theme.colors.primary,
        borderWidth: 0,
        borderRadius: 20
    },
    text: {
        color: "#FCCD2D"
    },
});
