import axios from 'axios';
import React, { useState } from "react";
import { Image, View } from 'react-native';
import Text from '../components/Text';
import TextInput from '../components/TextInput';

export default function JikanAnimeWidget(props) {
    const [pokemon, setPokemon] = useState('');
    const [name, setName] = useState('');
    const [id, setId] = useState('');
    const [type1, setType1] = useState('');
    const [type2, setType2] = useState('');
    const [height, setHeight] = useState('');
    const [weigth, setWeight] = useState('');
    const [sprite, setSprite] = useState('');
    const [shiny, setShiny] = useState('');

    const handleChange = () => {
        axios.get(`http://${props.ip}/api/pokemon/${pokemon}`)
            .then(response => {
                setId(response.data.id);
                setName(response.data.name);
                setHeight(response.data.height);
                setWeight(response.data.weight);
                setType1(response.data.types[0].type.name);
                response.data.types.length > 1 ?
                    setType2(response.data.types[1].type.name) : setType2('');
                setSprite(response.data.sprites.frontDefault);
                setShiny(response.data.sprites.frontShiny);
            })
            .catch(function (error) {
                console.log(error);
            });
    }
    return (
        <View style={{ alignItems: 'center' }}>
            <View style={{ paddingTop: 10 }}>
                {name === '' ? null :
                    <View style={{ paddingBottom: 5 }}>
                        <Text swag={{ fontSize: 17 }}> #{id} {name} </Text>
                        <Text>Height: {height / 10}m | Weigth: {weigth / 10}kg {"\n"}
                            Type: {type1} {type2}
                        </Text>
                        <View style={{ flexDirection: 'row' }} >
                            <Image
                                style={{ width: 100, height: 100 }} source={{ uri: sprite }} />
                            <Image
                                style={{ width: 100, height: 100 }} source={{ uri: shiny }}
                            />
                        </View>
                    </View>
                }
            </View>
            <TextInput
                id="pokemon"
                label="Pokemon Name or Pokedex Number"
                value={pokemon}
                onChangeText={event => { setPokemon(event); }}
                onSubmitEditing={handleChange}
                margin="normal"
                variant="outlined"
            />
        </View>
    );
}