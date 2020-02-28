import React from "react";
import { StyleSheet, View, Switch } from 'react-native';
import { Text } from 'react-native-elements';

export default function WeatherService(props) {
    return (
        <View style={styles.container}>
            {props.weatherS === true ?
                <View style={styles.contained}>
                    <Text style={styles.title}>Weather by City</Text>
                    <Switch
                        style={{ marginTop: 10 }}
                        onValueChange={event => props.setWeatherW(event)}
                        value={props.weatherW} />
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