import axios from 'axios';
import React, { useEffect, useState } from "react";
import { FlatList, View } from 'react-native';
import Text from '../../components/Text';

export default function IssPersonWidget(props) {
    const [name, setName] = useState(null);
    const [craft, setCraft] = useState(null);
    const [number, setNumber] = useState(null);
    const [people, setPeople] = useState(null);

    useEffect(() => {
        axios.get(`http://${props.ip}/api/location/person`)
            .then(response => {
                setPeople(response.data.people);
                setNumber(response.data.number);
            })
            .catch(function (error) {
                console.log(error);
            });
    }, []);

    const renderItem = ({ item }) => {
        return (
            <View style={{ flex: 1, flexDirection: 'column' }}>
                <Text>{item.name}, on {item.craft}</Text>
            </View>
        );
    };

    return (
        <View style={{ alignItems: 'center', paddingTop: 20 }}>
            <Text swag={{ paddingBottom: 10 }} > There is currently {number} persons in space : </Text>
            <FlatList
                data={people}
                keyExtractor={(item, index) => index.toString()}
                renderItem={renderItem}
            />
        </View>
    );
}
