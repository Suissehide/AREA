import axios from 'axios';
import React, { useState } from "react";
import { Image, View } from 'react-native';
import Text from '../../components/Text';
import TextInput from '../../components/TextInput';

export default function PokemonMovesWidget(props) {
    const [pokemon, setPokemon] = useState('');
    const [name, setName] = useState('');
    const [moves, setMoves] = useState(null);


    const handleChange = () => {
        axios.get(`http://${props.ip}/api/pokemon/${pokemon}/moves`)
            .then(response => {
                setName(response.data.name);
                console.log(response.data.moves);
                setMoves(response.data.moves);
            })
            .catch(function (error) {
                console.log(error);
            });
    }

    return (
        <View style={{ alignItems: 'center' }}>
            <View style={{ paddingTop: 10 }}>
                {moves === null ? null :
                    <View style={{ paddingBottom: 5 }}>
                        <Text swag={{ fontSize: 17 }}> <Text swag={{ fontWeight: 'bold' }} >{name}</Text>'s 5 random abilities : </Text>
                        <Text swag={{ fontSize: 17 }}> {moves[Math.floor(Math.random() * moves.length)].moveMove.name} </Text>
                        <Text swag={{ fontSize: 17 }}> {moves[Math.floor(Math.random() * moves.length)].moveMove.name} </Text>
                        <Text swag={{ fontSize: 17 }}> {moves[Math.floor(Math.random() * moves.length)].moveMove.name} </Text>
                        <Text swag={{ fontSize: 17 }}> {moves[Math.floor(Math.random() * moves.length)].moveMove.name} </Text>
                        <Text swag={{ fontSize: 17 }}> {moves[Math.floor(Math.random() * moves.length)].moveMove.name} </Text>
                    </View>
                }
            </View>
            <TextInput
                id="pokemonmoves"
                label="Pokemon Name or Pokedex Number"
                value={pokemon}
                onChangeText={event => { setPokemon(event); }}
                onSubmitEditing={handleChange}
                margin="normal"
                variant="outlined" autoCapitalize="none"
            />
        </View>
    );
}