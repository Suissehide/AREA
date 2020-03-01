import React from "react";
import { StyleSheet, Switch, View } from 'react-native';
import { Text, Card } from 'react-native-elements';
import { theme } from '../core/theme';
import ServiceTemplate from './ServiceTemplate';

export default function CardService(props) {
    return (
        <Card containerStyle={styles.card}>
            <View style={styles.container}>
                <Text style={styles.title}>{props.title}</Text>
                <Switch
                    style={{ marginTop: 3 }}
                    onValueChange={event => props.setService(event)}
                    value={props.service.service} />
            </View>
            <ServiceTemplate service={props.service}
                setWidget={props.setWidget} title={props.widgetTitle} widget={props.widget}
                w2={props.w2} setW2={props.setW2} t2={props.t2}
                w3={props.w3} setW3={props.setW3} t3={props.t3}
                w4={props.w4} setW4={props.setW4} t4={props.t4}
                w5={props.w5} setW5={props.setW5} t5={props.t5}
            />
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
        borderRadius: 20,
        width: '100%'
    }
});
