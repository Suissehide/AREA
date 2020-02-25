import React, { useState } from "react";
import { StyleSheet, View, Switch } from 'react-native';
import { Text } from 'react-native-elements';

export default function PotterService(props) {
    const [value, setValue] = useState(true);
    return (
        <View>
            {props.potterS === true ?
                <View>
                    <Text style={styles.title}>PotterSpell</Text>
                    <Switch
                        style={{ marginTop: 30 }}
                        onValueChange={event => setValue(event)}
                        value={value} />
                    <Text style={styles.title}>PotterCharacter</Text>
                    <Switch
                        style={{ marginTop: 30 }}
                        onValueChange={event => setValue(event)}
                        value={value} />
                </View> : null
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
