import React from "react";
import { StyleSheet, View, Switch } from 'react-native';
import { Text } from 'react-native-elements';

export default function JinkanService(props) {
    return (
        <View style={styles.container}>
            {props.jinkanS === true ?
                <View >
                    <View style={styles.contained}>
                        <Text style={styles.title}>Information on an Anime</Text>
                        <Switch
                            style={{ marginTop: 10 }}
                            onValueChange={event => props.setJinkanAnime(event)}
                            value={props.jinkanAnime} />
                    </View>
                    <View style={styles.contained}>
                        <Text style={styles.title}>Information on an Anime Character</Text>
                        <Switch
                            style={{ marginTop: 10 }}
                            onValueChange={event => props.setJinkanCharacter(event)}
                            value={props.jinkanCharacter} />
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
