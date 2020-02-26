import React, { useState } from "react";
import { View } from 'react-native';
import axios from 'axios';
import Text from '../components/Text'
import { Divider } from "react-native-paper";
import TextInput from '../components/TextInput';

export default function ChuckWidget(props) {
    const [chuck1, setChuck1] = useState("");
    const [chuck2, setChuck2] = useState("");
    const [chuck3, setChuck3] = useState("");
    const [theme, setTheme] = useState("beer");

    const handleChange = () => {
        axios.get(`http://${props.ip}:8080/api/Chuck/${theme}`)
            .then(response => {
                if (response.data.total)
                    setChuck1(response.data.result[Math.floor(Math.random() * response.data.total)].value);
                setChuck2(response.data.result[Math.floor(Math.random() * response.data.total)].value);
                setChuck3(response.data.result[Math.floor(Math.random() * response.data.total)].value);
            })
            .catch(function (error) {
                console.log(error);
            });
    }

    return (
        <View style={{ alignItems: 'center' }}>
            <View style={{ paddingTop: 10, paddingBottom: 20 }}>
                <Text>{chuck1}</Text>
                <View style={{ paddingBottom: 10, paddingTop: 10 }}>
                    <Divider />
                </View>
                <Text>{chuck2}</Text>
                <View style={{ paddingBottom: 10, paddingTop: 10 }}>
                    <Divider />
                </View>
                <Text>{chuck3}</Text>
            </View>
            <TextInput
                id="outlined-name"
                label="Theme of the Joke"
                value={theme}
                onChangeText={event => {
                    setTheme(event);
                }}
                onSubmitEditing={handleChange}
                margin="normal"
                variant="outlined"
            />
        </View>
    );
}