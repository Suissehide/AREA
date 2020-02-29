import React from "react";
import { StyleSheet, View, Switch } from 'react-native';
import { Text } from 'react-native-elements';

export default function GoogleService(props) {
    return (
        <View style={styles.container}>
            {props.google.service === true ?
                <View >
                    <View style={styles.contained}>
                        <Text style={styles.title}>Display your localisation depending{"\n"}on your IP</Text>
                        <Switch
                            style={{ marginTop: 3 }}
                            onValueChange={event => props.setGoogleIp(event)}
                            value={props.google.ip} />
                    </View>
                    <View style={styles.contained}>
                        <Text style={styles.title}>Get the distance and time between {"\n"} two points</Text>
                        <Switch
                            style={{ marginTop: 3 }}
                            onValueChange={event => props.setGoogleDistance(event)}
                            value={props.google.distance} />
                    </View>
                </View> : null
            }
        </View >
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
