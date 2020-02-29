import React from "react";
import { StyleSheet, View, Switch } from 'react-native';
import { Text } from 'react-native-elements';

export default function PotterService(props) {
    return (
        <View style={styles.container}>
            {props.potter.service === true ?
                <View >
                    <View style={styles.contained}>
                        <Text style={styles.title}>Display a random spell</Text>
                        <Switch
                            style={{ marginTop: 3 }}
                            onValueChange={event => props.setSpell(event)}
                            value={props.potter.spell} />
                    </View>
                    <View style={styles.contained}>

                        <Text style={styles.title}>Display a random character</Text>
                        <Switch
                            style={{ marginTop: 3 }}
                            onValueChange={event => props.setCharacter(event)}
                            value={props.potter.character} />
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
