import React, { useState } from "react";
import { StyleSheet, View, FormData } from 'react-native';
import Button from '../components/Button'
import axios from 'axios';
import Text from '../components/Text'
import { TextInput } from "react-native-paper";

export default function ChuckWidget(props) {
    const [chuck1, setChuck1] = useState("");
    const [chuck2, setChuck2] = useState("");
    const [chuck3, setChuck3] = useState("");
    const [theme, setTheme] = useState("beer");

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

    return (
        <View style={{ alignItems: 'center' }}>
            <View style={{ paddingTop: 10, paddingBottom: 20 }}>
                <Text>{chuck1}</Text>
                <Text>{chuck2}</Text>
                <Text>{chuck3}</Text>
            </View>
            <TextInput
                id="outlined-name"
                label="Theme of the Joke"
                value={theme}
                onChange={event => {
                    setTheme(event.target.value);
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