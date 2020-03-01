import React from "react";
import { StyleSheet, View, Switch } from 'react-native';
import { Text } from 'react-native-elements';

export default function WeatherService(props) {
    return (
        <View style={styles.container}>
            {props.weather.service === true ?
                <View style={styles.contained}>
                    <Text style={styles.title}>Get the weather of a city</Text>
                    <Switch
                        style={{ marginTop: 3 }}
                        onValueChange={event => props.setWeatherW(event)}
                        value={props.weather.widget} />
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
