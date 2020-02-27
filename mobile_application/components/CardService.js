import React from "react";
import { StyleSheet, Switch, View } from 'react-native';
import { Text, Card } from 'react-native-elements';
import { theme } from '../core/theme';

export default function CardService(props) {
    return (
        <Card containerStyle={styles.card}>
            <View style={styles.container}>
                <Text style={styles.title}>{props.title}</Text>
                <Switch
                    style={{ marginTop: 10 }}
                    onValueChange={event => props.setValue(event)}
                    value={props.value} />
            </View>
            {props.widget}
        </Card>
    );
}

const styles = StyleSheet.create({
    container: {
        flexDirection: 'row',
        justifyContent: 'space-between',
    },
    title: {
        fontSize: 20,
        alignSelf: "center",
    },
    card: {
        backgroundColor: theme.colors.primary,
        borderWidth: 0,
        borderRadius: 20
    }
});
