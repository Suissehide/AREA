import axios from 'axios';
import React, { useState } from "react";
import { StyleSheet, View } from 'react-native';
import Button from '../../components/Button';
import Text from '../../components/Text';
import { theme } from '../../core/theme';

export default function PotterCharacter(props) {
    const [name, setName] = useState("Harry Potter");
    const [role, setRole] = useState("Student");
    const [house, setHouse] = useState("Gryffondor");
    const [school, setSchool] = useState("Hogwards");
    const [ministryOfMagic, setministryOfMagic] = useState(false);
    const [orderOfThePhoenix, setorderOfThePhoenix] = useState(true);
    const [dumbledoresArmy, setdumbledoresArmy] = useState(true);
    const [deathEater, setdeathEater] = useState(false);
    const [bloodStatus, setbloodStatus] = useState("half-blood");
    const [species, setspecies] = useState("human");

    const handleChange = () => {
        axios.get(`http://${props.ip}/api/potter/character`)
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
        backgroundColor: theme.colors.brown,
    },
    text: {
        color: theme.colors.primary
    },
});
