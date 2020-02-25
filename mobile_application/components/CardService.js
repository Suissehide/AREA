import React from "react";
import { StyleSheet } from 'react-native';
import { Text, Card } from 'react-native-elements';
import { theme } from '../core/theme';
import Button from '../components/Button';

export default function CardService(props) {
    return (
        <Card containerStyle={styles.card}>
            <Text style={styles.title}>{props.title}</Text>
            <Button color={styles.container.backgroundColor} onPress={() => props.value === true ? props.setValue(false) : props.setValue(true)}>
                {props.value === true ? <Text>Désactiver</Text> : <Text>Activer</Text>}
            </Button>
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
