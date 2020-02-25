import React, { Fragment } from "react";
import { Image, Platform, StyleSheet, Text, TouchableOpacity, View, Switch } from 'react-native';
import { ScrollView } from 'react-native-gesture-handler';
import Button from '../components/Button';
import { withWidget } from "../core/Context";
import MyCard from '../components/CardService';
import PotterService from '../services/PotterService'

export default withWidget(({ potterS, setPotterS }) => (
    <View style={styles.container} >
        <Fragment>
            <ScrollView style={styles.container} contentContainerStyle={styles.contentContainer}>
                <MyCard title="Potter Service" value={potterS} setValue={setPotterS} widget={<PotterService potterS={potterS} />} />
            </ScrollView>
        </Fragment>
    </View >
));

const styles = StyleSheet.create({
    container: {
        flex: 1,
        backgroundColor: '#fff',
    },
    contentContainer: {
        paddingTop: 30,
    },
    getStartedContainer: {
        alignItems: 'center',
        marginHorizontal: 50,
    },
});
