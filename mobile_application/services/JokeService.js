import React from "react";
import { StyleSheet, View, Switch } from 'react-native';
import { Text } from 'react-native-elements';

export default function JokeService(props) {
    return (
        <View style={styles.container}>
            {props.joke.service === true ?
                <View style={styles.contained}>
                    <Text style={styles.title}>Get a random themed joke</Text>
                    <Switch
                        style={{ marginTop: 3 }}
                        onValueChange={event => props.setJokeWidget(event)}
                        value={props.joke.widget} />
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
