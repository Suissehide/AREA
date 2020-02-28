import React from "react";
import { StyleSheet, View, Switch } from 'react-native';
import { Text } from 'react-native-elements';

export default function ChuckService(props) {
    return (
        <View style={styles.container}>
            {props.chuckS === true ?
                <View style={styles.contained}>
                    <Text style={styles.title}>Chuck Norris Jokes</Text>
                    <Switch
                        style={{ marginTop: 10 }}
                        onValueChange={event => props.setChuckW(event)}
                        value={props.chuckW} />
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
