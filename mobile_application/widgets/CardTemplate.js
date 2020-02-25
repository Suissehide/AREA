import React, { Fragment } from "react";
import { StyleSheet, View } from 'react-native';
import { Text, Card, Divider } from 'react-native-elements';
import { theme } from '../core/theme';
import { withUser } from "../core/Context";
import TextInput from '../components/TextInput';

export default withUser((props, { name, setName, activated }) => (
    <Fragment>
        <Card containerStyle={styles.card}>
            <Text style={styles.title}>{props.title}</Text>
            {props.widget}
        </Card>
    </Fragment>
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
        fontSize: 20,
        alignSelf: "center",
    },
    card: {
        backgroundColor: theme.colors.primary,
        borderWidth: 0,
        borderRadius: 20
    }
});
