import { LinearGradient } from 'expo-linear-gradient';
import React, { Fragment } from "react";
import { StyleSheet } from 'react-native';
import { withWidget } from "../core/Context";
import { theme } from '../core/theme';
import Text from './Text';

export default withWidget((props) => (
    <Fragment>
        <LinearGradient
            colors={[theme.colors.green, theme.colors.primary]}
            style={styles.card}
            start={[0, 1]}
            end={[1, 0]}
        >
            <Text swag={styles.title}>{props.title}</Text>
            {props.widget}
        </LinearGradient>
    </Fragment>
));

const styles = StyleSheet.create({
    title: {
        fontSize: 22,
        alignSelf: "center",
        fontWeight: 'bold',
    },
    card: {
        width: '90%',
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
