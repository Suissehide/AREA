import React from "react";
import { StyleSheet, View, Switch } from 'react-native';
import { Text } from 'react-native-elements';

export default function JikanService(props) {
    return (
        <View style={styles.container}>
            {props.jikan.service === true ?
                <View >
                    <View style={styles.contained}>
                        <Text style={styles.title}>Get informations on an anime</Text>
                        <Switch
                            style={{ marginTop: 3 }}
                            onValueChange={event => props.setJikanAnime(event)}
                            value={props.jikan.anime} />
                    </View>
                    <View style={styles.contained}>
                        <Text style={styles.title}>Get informations on a character</Text>
                        <Switch
                            style={{ marginTop: 3 }}
                            onValueChange={event => props.setJikanCharacter(event)}
                            value={props.jikan.character} />
                    </View>
                    <View style={styles.contained}>
                        <Text style={styles.title}>Display the highest scored animes</Text>
                        <Switch
                            style={{ marginTop: 3 }}
                            onValueChange={event => props.setJikanTopAnime(event)}
                            value={props.jikan.topAnime} />
                    </View>
                    <View style={styles.contained}>
                        <Text style={styles.title}>Display the highest scored animes</Text>
                        <Switch
                            style={{ marginTop: 3 }}
                            onValueChange={event => props.setJikanTopManga(event)}
                            value={props.jikan.topManga} />
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
