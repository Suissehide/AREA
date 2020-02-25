import React from "react";
import { StyleSheet, Switch } from 'react-native';
import { Text, Card } from 'react-native-elements';
import { theme } from '../core/theme';
import Button from '../components/Button';

export default function CardService(props) {
    return (
        <Card containerStyle={styles.card}>
            <Text style={styles.title}>{props.title}</Text>
            <Switch
                style={{ marginTop: 30 }}
                onValueChange={event => props.setValue(event)}
                value={props.value} />
            {props.widget}
        </Card>
    );
}

const styles = StyleSheet.create({
    container: {
        flex: 1,
        backgroundColor: '#fafafa',
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
