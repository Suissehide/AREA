import { Ionicons } from '@expo/vector-icons';
import axios from 'axios';
import React, { useEffect, useState } from "react";
import { TouchableOpacity, View } from 'react-native';
import Text from '../../components/Text';

export default function MicrosoftContactWidget(props) {
    const [displayName, setDisplayName] = useState("");
    const [address, setAddress] = useState("");
    const [number, setNumber] = useState(0);
    const [saveLen, setSaveLen] = useState(2);
    var token = "a";

    function MyIcon(props) {
        return (
            <Ionicons
                name={props.name}
                size={30}
                style={{ marginBottom: -3 }}
            />
        );
    }

    useEffect(() => {
        axios.get(`http://${props.ip}/api/microsoft/contacts?authorization=${token}`)
            .then(response => {
                setSaveLen(response.data.value.length);
                setDisplayName(response.data.value[number].displayName);
                setAddress(response.data.value[number].scoredEmailAddresses.address);
            })
            .catch(function (error) {
                console.log(error);
            });
    }, []);

    const handleChange = (value) => {
        if (value === -1 && number !== 0)
            setNumber(number + value)
        else if (value === 1 && number < saveLen)
            setNumber(number + value)
    }
    useEffect(() => {
        axios.get(`http://${props.ip}/api/microsoft/contacts?authorization=${token}`)
            .then(response => {
                setDisplayName(response.data.value[number].displayName);
                setAddress(response.data.value[number].scoredEmailAddresses[0].address);
            })
            .catch(function (error) {
                console.log(error);
            });
    }, [number]);

    return (
        <View style={{ alignItems: 'center', paddingTop: 20 }}>
            <View style={{ flexDirection: 'row', width: '100%', alignItems: 'center', justifyContent: 'space-around', paddingTop: 15 }} >
                <TouchableOpacity onPress={() => handleChange(-1)}>
                    <MyIcon name="ios-arrow-back" />
                </TouchableOpacity>
                <View style={{ width: '80%', alignItems: 'center' }} >
                    <Text swag={{ fontSize: 15 }} >{displayName} {"["}{address}{"]"}</Text>
                </View>
                <TouchableOpacity onPress={() => handleChange(1)}>
                    <MyIcon name="ios-arrow-forward" />
                </TouchableOpacity>
            </View>
        </View>
    );
}