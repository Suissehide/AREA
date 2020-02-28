import React, { useState } from "react";
import { StyleSheet, View } from 'react-native';
import Button from '../../components/Button'
import Text from '../../components/Text'
import axios from 'axios';

export default function PotterCharacter(props) {
    const [name, setName] = useState("");
    const [role, setRole] = useState("");
    const [house, setHouse] = useState("");
    const [school, setSchool] = useState("");
    const [ministryOfMagic, setministryOfMagic] = useState(false);
    const [orderOfThePhoenix, setorderOfThePhoenix] = useState(false);
    const [dumbledoresArmy, setdumbledoresArmy] = useState(false);
    const [deathEater, setdeathEater] = useState(false);
    const [bloodStatus, setbloodStatus] = useState("");
    const [species, setspecies] = useState("");

    const handleChange = () => {
        axios.get(`http://${props.ip}:8080/api/potter/random-character`)
            .then(response => {
                setName(response.data.name);
                setRole(response.data.role);
                setHouse(response.data.house);
                setSchool(response.data.school);
                setministryOfMagic(response.data.ministryOfMagic);
                setorderOfThePhoenix(response.data.orderOfThePhoenix);
                setdumbledoresArmy(response.data.dumbledoresArmy);
                setdeathEater(response.data.deathEater);
                setbloodStatus(response.data.bloodStatus);
                setspecies(response.data.species);
            })
            .catch(function (error) {
                console.log(error);
            });
    }
    return (
        <View style={{ alignItems: 'center' }}>
            <Button style={styles.button} onPress={handleChange}><Text swag={styles.text}>Random character</Text></Button>
            <Text> {name} </Text>
            {role !== null ? <Text>{role}</Text> : null}
            <Text>This Character is a {species} and its blood status is {bloodStatus}.</Text>
            {school !== null ? <Text> {name} went to {school}</Text> : null}
            {house !== null ? <Text>and more precisely in {house} house.</Text> : house}
            {ministryOfMagic === false && orderOfThePhoenix === false && dumbledoresArmy === false && deathEater === false ? <Text>{name} doesn{"'"}t have any affiliation.</Text> : <Text>{name} {"'"}s affiliations are :</Text>}
            {ministryOfMagic !== false ? <Text>{'['}Ministry of Magic{']'}</Text> : null}
            {orderOfThePhoenix !== false ? <Text>{'['}Order Of The Phoenix{']'}</Text> : null}
            {dumbledoresArmy !== false ? <Text>{'['}Dumbledore{"'"}s Army{']'}</Text> : null}
            {deathEater !== false ? <Text>{'['}Death Eater{']'}</Text> : null}
        </View>
    );
}

const styles = StyleSheet.create({
    button: {
        width: '80%',
        marginVertical: 10,
        backgroundColor: "#3D2314",
    },
    text: {
        color: "#FCCD2D"
    },
});
