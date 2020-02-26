import React, { useState } from "react";
import { StyleSheet, View, Switch } from 'react-native';
import { Text } from 'react-native-elements';

export default function PotterService(props) {
    const [value, setValue] = useState(true);
    return (
        <View style={styles.container}>
            {props.potterS === true ?
                <View >
                    <View style={styles.contained}>
                        <Text style={styles.title}>PotterSpell</Text>
                        <Switch
                            style={{ marginTop: 10 }}
                            onValueChange={event => setValue(event)}
                            value={value} />
                    </View>
                    <View style={styles.contained}>

                        <Text style={styles.title}>PotterCharacter</Text>
                        <Switch
                            style={{ marginTop: 10 }}
                            onValueChange={event => setValue(event)}
                            value={value} />
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
