import React, { useState } from "react";
import { StyleSheet, View, FormData } from 'react-native';
import Button from '../components/Button'
import axios from 'axios';
import Text from '../components/Text'
import { TextInput } from "react-native-paper";

export default function WeatherWidget(props) {
    const [name, setName] = useState('Bordeaux');
    const [main, setMain] = useState('Sunny');
    const [description, setdescription] = useState('Sunny');
    const [temp, setTemp] = useState(26);
    const [feelsLike, setFeelsLike] = useState(30);
    const [tempMin, setTempMin] = useState(26);
    const [tempMax, setTempMax] = useState(26);
    const [humidity, setHumidity] = useState(0);
    const [visibility, setVisibility] = useState(0);
    const [wind, setWind] = useState(0);
    const [clouds, setclouds] = useState(0);

    axios.get(`http://${props.ip}:8080/api/weather/${name}`)
        .then(response => {
            setMain(response.data.weather[0].main);
            setdescription(response.data.weather[0].description);
            setTemp(response.data.main.temp - 273);
            setFeelsLike(response.data.main.feelsLike - 273);
            setTempMin(response.data.main.tempMin - 273);
            setTempMax(response.data.main.tempMax - 273);
            setHumidity(response.data.main.humidity);
            setVisibility(response.data.visibility);
        })
        .catch(function (error) {
            console.log(error);
        });

    return (
        <View style={{ alignItems: 'center' }}>
            <View style={{ paddingTop: 10, paddingBottom: 20 }}>
                <Text style={styles.font}>In {name} : {description}. </Text>
                <Text>Temperature is {temp.toFixed(2)}C but feels like {feelsLike.toFixed(2)}C.</Text>
                <Text>Min : {tempMin.toFixed(2)}C | Max : {tempMax.toFixed(2)}C</Text>
            </View>
            <TextInput
                id="outlined-name"
                label="City"
                value={name}
                onChange={event => {
                    setName(event.target.value);
                }}
                margin="normal"
                variant="outlined"
            />
        </View>
    );
}

const styles = StyleSheet.create({
    button: {
        width: '80%',
        marginVertical: 5,
        backgroundColor: "#3D2314",
    },
    text: {
        color: "#FCCD2D"
    },
    font: {
        fontSize: 25,
    }
});