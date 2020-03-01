import { Ionicons } from '@expo/vector-icons';
import axios from 'axios';
import React, { useEffect, useState } from "react";
import { TouchableOpacity, View } from 'react-native';
import Text from '../../components/Text';

export default function MicrosoftDriveWidget(props) {
    const [displayNameCreated, setDisplayNameCreated] = useState("");
    const [displayNameEdited, setDisplayNameEdited] = useState("");
    const [name, setName] = useState("");
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
        axios.get(`http://${props.ip}/api/microsoft/drive?authorization=${token}`)
            .then(response => {
                setSaveLen(response.data.value.length);
                setDisplayNameCreated(response.data.value[number].createdBy.user.displayName);
                setDisplayNameEdited(response.data.value[number].lastModifiedBy.user.displayName);
                setName(response.data.value[number].name);
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
        axios.get(`http://${props.ip}/api/microsoft/drive?authorization=${token}`)
            .then(response => {
                setDisplayNameCreated(response.data.value[number].createdBy.user.displayName);
                setDisplayNameEdited(response.data.value[number].lastModifiedBy.user.displayName);
                setName(response.data.value[number].name);
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
                    <Text swag={{ fontSize: 15 }} >{name} </Text>
                    <Text swag={{ fontSize: 15 }} >Created By {displayNameCreated} </Text>
                    <Text swag={{ fontSize: 15 }} >Last Modified By {displayNameEdited} </Text>
                </View>
                <TouchableOpacity onPress={() => handleChange(1)}>
                    <MyIcon name="ios-arrow-forward" />
                </TouchableOpacity>
            </View>
        </View>
    );
}