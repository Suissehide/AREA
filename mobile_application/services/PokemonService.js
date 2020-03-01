import React from "react";
import { StyleSheet, View, Switch } from 'react-native';
import { Text } from 'react-native-elements';

export default function PokemonService(props) {
    return (
        <View style={styles.container}>
            {props.pokemon.service === true ?
                <View style={styles.contained}>
                    <Text style={styles.title}>Get informations on a Pokemon</Text>
                    <Switch
                        style={{ marginTop: 3 }}
                        onValueChange={event => props.setPokemonWidget(event)}
                        value={props.pokemon.widget} />
                </View> : null
            }
        </View>
    );
}

const styles = StyleSheet.create({
    contained: {
        flexDirection: 'row',
        justifyContent: "space-between",
    },
    title: {
        fontSize: 15,
        alignSelf: "center",
    },
});
