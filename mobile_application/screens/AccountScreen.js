import React, { Fragment, useState } from "react";
import { StyleSheet } from 'react-native';
import { ScrollView } from 'react-native-gesture-handler';
import { theme } from '../core/theme';
import { withWidget } from "../core/Context";
import MyCard from '../widgets/CardTemplate';
import Text from '../components/Text';
import Button from '../components/Button';
import LoginScreen from './LoginScreen';

export default withWidget(({ email, logOut, setLogOut, logIn, setLogIn }) => (
    <ScrollView style={styles.container} contentContainerStyle={styles.contentContainer}>
        <Fragment>
        </Fragment>
    </ScrollView>
));

const styles = StyleSheet.create({
    container: {
        flex: 1,
        backgroundColor: '#fafafa',
    },
    contentContainer: {
        paddingTop: 15,
    },
});
