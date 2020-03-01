import { LinearGradient } from 'expo-linear-gradient';
import React from "react";
import { StyleSheet, Switch, View } from 'react-native';
import { Text } from 'react-native-elements';
import { theme } from '../core/theme';
import ServiceTemplate from './SwitchServiceTemplate';

export default function CardService(props) {
    return (
        <LinearGradient
            colors={[theme.colors.green, theme.colors.primary]}
            style={styles.card}
            start={[0, 1]}
            end={[1, 0]}
        >
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
        </LinearGradient>
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
        color: theme.colors.brown,
    },
    card: {
        width: '100%',
        backgroundColor: theme.colors.primary,
        borderRadius: 10,
        borderColor: theme.colors.brown,
        borderStyle: 'solid',
        borderWidth: 2,
        padding: 10,
        marginTop: 10,
        marginHorizontal: 15,
    }
});
