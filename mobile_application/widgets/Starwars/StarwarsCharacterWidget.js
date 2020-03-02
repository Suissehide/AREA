import axios from 'axios';
import React, { useState } from "react";
import { StyleSheet, View } from 'react-native';
import Button from '../../components/Button';
import Text from '../../components/Text';
import { theme } from '../../core/theme';

export default function StarwarsCharacterWidget(props) {
    const [name, setName] = useState("Mace Windu");
    const [height, setHeight] = useState("188");
    const [mass, setMass] = useState("84");
    const [birthYear, setBirthDay] = useState("72BBY");
    const [gender, setGender] = useState("male");

    const handleChange = () => {
        axios.get(`http://${props.ip}/api/starwars/people/random`)
            .then(response => {
                setName(response.data.name);
                setHeight(response.data.height);
                setMass(response.data.mass);
                setBirthDay(response.data.birthYear);
                setGender(response.data.gender);
            })
            .catch(function (error) {
                console.log(error);
            });
    }
    return (
        <View style={{ alignItems: 'center' }}>
            <Button style={styles.button} onPress={handleChange}><Text swag={styles.text}>Random character</Text></Button>
            <Text> {name} </Text>
            <Text>This Character is {height / 100}m and {mass}kg. </Text>
            <Text> {name} is born in {birthYear} and is a {gender}.</Text>
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
