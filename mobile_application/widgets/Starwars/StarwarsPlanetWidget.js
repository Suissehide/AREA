import axios from 'axios';
import React, { useState } from "react";
import { StyleSheet, View } from 'react-native';
import Button from '../../components/Button';
import Text from '../../components/Text';
import { theme } from '../../core/theme';

export default function StarwarsPlanetWidget(props) {
    const [name, setName] = useState("Socorro");
    const [rotationPeriod, setRotationPeriod] = useState("20");
    const [orbitalPeriod, setOrbitalPeriod] = useState("326");
    const [diameter, setDiameter] = useState("0");
    const [climate, setClimate] = useState("arid");
    const [gravity, setGravity] = useState("1 standard");
    const [terrain, setTerrain] = useState("deserts, mountains");
    const [population, setPopulation] = useState("300000000000");

    const handleChange = () => {
        axios.get(`http://${props.ip}/api/starwars/planet/random`)
            .then(response => {
                setName(response.data.name);
                setRotationPeriod(response.data.rotationPeriod);
                setOrbitalPeriod(response.data.orbitalPeriod);
                setDiameter(response.data.diameter);
                setClimate(response.data.climate);
                setGravity(response.data.gravity);
                setTerrain(response.data.terrain);
                setPopulation(response.data.population);
            })
            .catch(function (error) {
                console.log(error);
            });
    }
    return (
        <View style={{ alignItems: 'center' }}>
            <Button style={styles.button} onPress={handleChange}><Text swag={styles.text}>Random Planet</Text></Button>
            <Text> {name} </Text>
            <Text>This planet has a rotation period of {rotationPeriod} days and an orbital period of {orbitalPeriod} days. </Text>
            <Text> {name} has a diameter of {diameter}km and its gravity is {gravity}G.</Text>
            <Text> Its climate is {climate} and its terrain is composed of {terrain}.</Text>
            <Text>There is {population} people living here. </Text>
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
