import React, { Fragment } from "react";
import { StyleSheet } from 'react-native';
import { Card } from 'react-native-elements';
import { theme } from '../core/theme';
import { withWidget } from "../core/Context";
import Text from './Text'

export default withWidget((props) => (
    <Fragment>
        <Card containerStyle={styles.card}>
            <Text swag={styles.title}>{props.title}</Text>
            {props.widget}
        </Card>
    </Fragment>
));

const styles = StyleSheet.create({
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
