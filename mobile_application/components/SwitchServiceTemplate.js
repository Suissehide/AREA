import React from "react";
import { StyleSheet, Switch, View } from 'react-native';
import { Text } from 'react-native-elements';

function NewWidget(props) {
    return (
        <View>
            {props.t != null ?
                <View style={styles.contained}>
                    <Text style={styles.title}>{props.t}</Text>
                    <Switch
                        style={{ marginTop: 3 }}
                        onValueChange={event => props.setW2(event)}
                        value={props.w2} />
                </View>
                : null}
        </View>
    );
}

export default function ServiceTemplate(props) {

    return (
        <View style={styles.container}>
            {props.service.service === true ?
                <View>
                    <View style={styles.contained}>
                        <Text style={styles.title}>{props.title}</Text>
                        {props.t2 != null ?
                            <Switch
                                style={{ marginTop: 3 }}
                                onValueChange={event => props.setWidget(event)}
                                value={props.widget} />
                            :
                            <Switch
                                style={{ marginTop: 3 }}
                                onValueChange={event => props.setWidget(event)}
                                value={props.service.widget} />}
                    </View>
                    <NewWidget t={props.t2} setW2={props.setW2} w2={props.w2} />
                    <NewWidget t={props.t3} setW2={props.setW3} w2={props.w3} />
                    <NewWidget t={props.t4} setW2={props.setW4} w2={props.w4} />
                    <NewWidget t={props.t5} setW2={props.setW5} w2={props.w5} />
                </View>
                : null
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
