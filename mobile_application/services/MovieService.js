import React from "react";
import { StyleSheet, View, Switch } from 'react-native';
import { Text } from 'react-native-elements';

export default function MovieService(props) {
    return (
        <View style={styles.container}>
            {props.movie.service === true ?
                <View style={styles.contained}>
                    <Text style={styles.title}>Get information on a movie</Text>
                    <Switch
                        style={{ marginTop: 3 }}
                        onValueChange={event => props.setMovieW(event)}
                        value={props.movie.widget} />
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
