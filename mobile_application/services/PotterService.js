import React from "react";
import { StyleSheet, View } from 'react-native';
import { Text } from 'react-native-elements';

export default function PotterService(props) {
    return (
        <View>
            {props.potterS === true ?
                <Text style={styles.title}>PotterSpell</Text> : null
            }
        </View>
    );
}

const styles = StyleSheet.create({
    title: {
        fontSize: 15,
        alignSelf: "center",
    },
});
