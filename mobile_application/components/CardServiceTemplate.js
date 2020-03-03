import { LinearGradient } from 'expo-linear-gradient';
import React, { useEffect } from "react";
import { StyleSheet, Switch, View } from 'react-native';
import { Text } from 'react-native-elements';
import { theme } from '../core/theme';
import ServiceTemplate from './SwitchServiceTemplate';
import { withWidget } from "../core/Context";
import axios from 'axios';


function CardService(props) {

    useEffect(() => {
        axios.get(`http://${props.props.ip}/database/editservice/${props.props.token}/${props.props.title.replace(/ |\n/g, "_")}/${props.props.service.service}/`)
            .then(response => {

            })
            .catch(function (error) {
                console.log(error);
            });
    }, [props.props.service.service]);

    if (props.props.widget === undefined) {
        useEffect(() => {
            axios.get(`http://${props.props.ip}/database/editwidget/${props.props.token}/${props.props.title.replace(/ |\n/g, "_")}/${props.props.widgetTitle}/${props.props.service.widget}/`)
                .then(response => {
                })
                .catch(function (error) {
                    console.log(error);
                });
        }, [props.props.service.widget]);
    }
    else {
        useEffect(() => {
            axios.get(`http://${props.props.ip}/database/editwidget/${props.props.token}/${props.props.title.replace(/ |\n/g, "_")}/${props.props.widgetTitle}/${props.props.widget}/`)
                .then(response => {
                })
                .catch(function (error) {
                    console.log(error);
                });
        }, [props.props.widget]);
    }


    if (props.props.w2 !== undefined) {
        useEffect(() => {
            axios.get(`http://${props.props.ip}/database/editwidget/${props.props.token}/${props.props.title.replace(/ |\n/g, "_")}/${props.props.t2}/${props.props.w2}/`)
                .then(response => {

                })
                .catch(function (error) {
                    console.log(error);
                });
        }, [props.props.w2]);
    }

    if (props.props.w3 !== undefined) {
        useEffect(() => {
            axios.get(`http://${props.props.ip}/database/editwidget/${props.props.token}/${props.props.title.replace(/ |\n/g, "_")}/${props.props.t3}/${props.props.w3}/`)
                .then(response => {

                })
                .catch(function (error) {
                    console.log(error);
                });
        }, [props.props.w3]);
    }

    if (props.props.w4 !== undefined) {
        useEffect(() => {
            axios.get(`http://${props.props.ip}/database/editwidget/${props.props.token}/${props.props.title.replace(/ |\n/g, "_")}/${props.props.t4}/${props.props.w4}/`)
                .then(response => {

                })
                .catch(function (error) {
                    console.log(error);
                });
        }, [props.props.w4]);
    }

    if (props.props.w5 !== undefined) {
        useEffect(() => {
            axios.get(`http://${props.props.ip}/database/editwidget/${props.props.token}/${props.props.title.replace(/ |\n/g, "_")}/${props.props.t5}/${props.props.w5}/`)
                .then(response => {

                })
                .catch(function (error) {
                    console.log(error);
                });
        }, [props.props.w5]);
    }

    return (
        <LinearGradient
            colors={[theme.colors.green, theme.colors.primary]}
            style={styles.card}
            start={[0, 1]}
            end={[1, 0]}
        >
            <View style={styles.container}>

                <Text style={styles.title}>{props.props.title}</Text>
                <Switch
                    style={{ marginTop: 3 }}
                    onValueChange={event => props.props.setService(event)}
                    value={props.props.service.service} />
            </View>
            <ServiceTemplate service={props.props.service}
                setWidget={props.props.setWidget} title={props.props.widgetTitle} widget={props.props.widget}
                w2={props.props.w2} setW2={props.props.setW2} t2={props.props.t2}
                w3={props.props.w3} setW3={props.props.setW3} t3={props.props.t3}
                w4={props.props.w4} setW4={props.props.setW4} t4={props.props.t4}
                w5={props.props.w5} setW5={props.props.setW5} t5={props.props.t5}
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

export default withWidget((props) => (
    <CardService props={props} />
));