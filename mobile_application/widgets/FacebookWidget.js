import { Ionicons } from '@expo/vector-icons';
import axios from 'axios';
import React, { useEffect, useState } from "react";
import { TouchableOpacity, View, Linking } from 'react-native';
import Text from '../components/Text';

export default function FacebookWidget(props) {
    const [like, setLike] = useState("");
    const [number, setNumber] = useState(0);
    var token = 'oui';

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
        axios.get(`http://${props.ip}/api/facebook/${token}`)
            .then(response => {
                setLike(response.data.likes.data[number].name)
            })
            .catch(function (error) {
                console.log(error);
            });
    });

    return (
        <View style={{ alignItems: 'center', paddingTop: 20 }}>
            <View style={{ flexDirection: 'row', width: '100%', alignItems: 'center', justifyContent: 'space-around', paddingTop: 15 }} >
                <TouchableOpacity onPress={() => setNumber(Math.abs(number - 1))}>
                    <MyIcon name="ios-arrow-back" />
                </TouchableOpacity>
                <View style={{ width: '80%', alignItems: 'center' }} >
                    <Text swag={{ fontSize: 20, fontWeight: 'bold' }} >{like}</Text>
                </View>
                <TouchableOpacity onPress={() => setNumber(number + 1)}>
                    <MyIcon name="ios-arrow-forward" />
                </TouchableOpacity>
            </View>
        </View>
    );
}