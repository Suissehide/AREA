import axios from 'axios';
import React, { useState } from "react";
import { StyleSheet, View } from 'react-native';
import Button from '../../components/Button';
import Text from '../../components/Text';
import { theme } from '../../core/theme';

export default function PotterSpell(props) {
    const [spell, setSpell] = useState("Oblivates");
    const [type, setType] = useState("Charm");
    const [effect, setEffect] = useState("Erases Memories");

    const handleChange = () => {
        axios.get(`http://${props.ip}/api/potter/spell`)
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
            <Button style={styles.button} onPress={handleChange}><Text swag={styles.text}>Random Spell</Text></Button>
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
        backgroundColor: theme.colors.brown,
    },
    text: {
        color: theme.colors.primary
    },
});
