import React, { useState } from "react";
import { View } from 'react-native';
import axios from 'axios';
import Text from '../components/Text'
import TextInput from '../components/TextInput';

export default function WeatherWidget(props) {
    const [city, setCity] = useState('');
    const [name, setName] = useState('Bordeaux');
    const [description, setdescription] = useState('Sunny');
    const [temp, setTemp] = useState(26);
    const [feelsLike, setFeelsLike] = useState(30);
    const [tempMin, setTempMin] = useState(26);
    const [tempMax, setTempMax] = useState(26);
    const [humidity, setHumidity] = useState(0);
    const [visibility, setVisibility] = useState(0);
    const [wind, setWind] = useState(0);
    const [clouds, setclouds] = useState(0);

    const handleChange = () => {
        setName(city)
        axios.get(`http://${props.ip}:8080/api/weather/${name}`)
            .then(response => {
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
    }

    return (
        <View style={{ alignItems: 'center' }}>
            <View style={{ paddingTop: 10, paddingBottom: 20 }}>
                <Text swag={{ fontSize: 17 }}>In {name} : {description}. </Text>
                <Text>Temperature is {temp.toFixed(2)}C but feels like {feelsLike.toFixed(2)}C.</Text>
                <Text>Min : {tempMin.toFixed(2)}C | Max : {tempMax.toFixed(2)}C</Text>
            </View>
            <TextInput
                id="weather"
                label="City"
                value={city}
                onChangeText={event => {
                    setCity(event);
                }}
                onSubmitEditing={handleChange}
                margin="normal"
                variant="outlined"
            />
        </View>
    );
}