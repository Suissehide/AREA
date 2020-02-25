import React, { Fragment } from "react";
import { StyleSheet, View } from 'react-native';
import { Text, Card, Divider } from 'react-native-elements';
import { theme } from '../core/theme';
import { withUser } from "../core/Context";

export default withUser((props, { potterS, potterSpell, setPotterSpell }) => (
    < Fragment >
        {console.log(props.potterS)}
        {props.potterS === true ?
            <Text style={styles.title}>PotterSpell</Text> : null}
    </Fragment >
));

const styles = StyleSheet.create({
    container: {
        flex: 1,
        backgroundColor: '#fafafa',
    },
    contentContainer: {
        paddingTop: 15,
    },
    title: {
        fontSize: 15,
        alignSelf: "center",
    },
    card: {
        backgroundColor: theme.colors.primary,
        borderWidth: 0,
        borderRadius: 20
    }
});
