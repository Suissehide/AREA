import React from "react";
import { StyleSheet, View, Switch } from 'react-native';
import { Text } from 'react-native-elements';

export default function JikanService(props) {
    return (
        <View style={styles.container}>
            {props.jikan.service === true ?
                <View >
                    <View style={styles.contained}>
                        <Text style={styles.title}>Information on an Anime</Text>
                        <Switch
                            style={{ marginTop: 10 }}
                            onValueChange={event => props.setJikanAnime(event)}
                            value={props.jikan.anime} />
                    </View>
                    <View style={styles.contained}>
                        <Text style={styles.title}>Information on an Anime Character</Text>
                        <Switch
                            style={{ marginTop: 10 }}
                            onValueChange={event => props.setJikanCharacter(event)}
                            value={props.jikan.character} />
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
