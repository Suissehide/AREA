import React, { useState } from "react";
import { StyleSheet, View } from 'react-native';
import { Text } from 'react-native-elements';
import { theme } from '../../core/theme';
import Button from '../../components/Button'
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
        axios.get(`http://${props.ip}:8080/api/PotterApi/randomCharacter`)
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
            <Button style={styles.button} onPress={handleChange}><Text style={styles.text}>Get a random character</Text></Button>
            <Text> {name} {role !== null ? <Text>| {role}</Text> : null}. This Character is a {species} and his blood status is {bloodStatus}.</Text>
            {school !== null ? <Text> She/He went to {school}</Text> : null}
            {house !== null ? <Text>and more precisely in {house} house.</Text> : house}
            {ministryOfMagic === false && orderOfThePhoenix === false && dumbledoresArmy === false && deathEater === false ? <Text>He/She doesn't have any affiliation.</Text> : <Text>Her/His affiliation is/are :</Text>}
            {ministryOfMagic !== false ? <Text>{'['}Ministry of Magic{']'}</Text> : null}
            {orderOfThePhoenix !== false ? <Text>{'['}Order Of The Phoenix{']'}</Text> : null}
            {dumbledoresArmy !== false ? <Text>{'['}Dumbledore{"'"}s Army{']'}</Text> : null}
            {deathEater !== false ? <Text>{'['}Death Eater{']'}</Text> : null}
        </View>
    );
}

const styles = StyleSheet.create({
    container: {
        flex: 1,
        backgroundColor: '#fafafa',
    },
    button: {
        width: '80%',
        marginVertical: 10,
        backgroundColor: "#3D2314",
    },
    contentContainer: {
        paddingTop: 15,
    },
    title: {
        fontSize: 20,
        alignSelf: "center",
    },
    card: {
        backgroundColor: theme.colors.primary,
        borderWidth: 0,
        borderRadius: 20
    },
    text: {
        color: "#FCCD2D"
    },
});
