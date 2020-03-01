import { Ionicons } from '@expo/vector-icons';
import axios from 'axios';
import React, { useEffect, useState } from "react";
import { TouchableOpacity, View } from 'react-native';
import Text from '../../components/Text';

export default function MicrosoftOutlookWidget(props) {
    const [subject, setSubject] = useState(null);
    const [address, setAddress] = useState(null);
    const [name, setName] = useState(null);
    const [number, setNumber] = useState(0);
    const [saveLen, setSaveLen] = useState(2);
    var token = "";

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
        axios.get(`http://${props.ip}/api/microsoft/outlook?authorization=${token}`)
            .then(response => {
                setSaveLen(response.data.value.length);
                setSubject(response.data.value[number].subject);
                setName(response.data.value[number].sender.emailAddress.name);
                setAddress(response.data.value[number].sender.emailAddress.address);
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
        axios.get(`http://${props.ip}/api/microsoft/outlook?authorization=${token}`)
            .then(response => {
                setSubject(response.data.value[number].subject);
                setName(response.data.value[number].sender.emailAddress.name);
                setAddress(response.data.value[number].sender.emailAddress.address);
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
                    <Text swag={{ fontWeight: 'bold', fontSize: 17 }} > {subject}  </Text>
                    <Text> {name} | {address} </Text>
                </View>
                <TouchableOpacity onPress={() => handleChange(1)}>
                    <MyIcon name="ios-arrow-forward" />
                </TouchableOpacity>
            </View>
        </View>
    );
}