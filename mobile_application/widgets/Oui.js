import React, { Fragment } from "react";
import { StyleSheet, View } from 'react-native';
import { Ionicons } from '@expo/vector-icons';
import * as WebBrowser from 'expo-web-browser';
import { RectButton, ScrollView } from 'react-native-gesture-handler';
import { Text, Card, Divider } from 'react-native-elements';
import { theme } from '../core/theme';
import { withUser } from "../core/Context";
import TextInput from '../components/TextInput';
import MyCard from './CardTemplate';

export default withUser(({ name, setName, activated }) => (
    <Text>Oui</Text>
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
