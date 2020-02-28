import React from "react";
import { StyleSheet, View, Switch } from 'react-native';
import { Text } from 'react-native-elements';

export default function PotterService(props) {
    return (
        <View style={styles.container}>
            {props.potterS === true ?
                <View >
                    <View style={styles.contained}>
                        <Text style={styles.title}>Harry Potter's Random Spell</Text>
                        <Switch
                            style={{ marginTop: 10 }}
                            onValueChange={event => props.setSpell(event)}
                            value={props.spell} />
                    </View>
                    <View style={styles.contained}>

                        <Text style={styles.title}>Random Character from Harry Potter</Text>
                        <Switch
                            style={{ marginTop: 10 }}
                            onValueChange={event => props.setCharacter(event)}
                            value={props.character} />
                    </View>

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
