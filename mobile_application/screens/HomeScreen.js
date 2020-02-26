import React, { Fragment } from "react";
import { Image, Platform, StyleSheet, Text, TouchableOpacity, View, Switch } from 'react-native';
import { ScrollView } from 'react-native-gesture-handler';
import Button from '../components/Button';
import { withWidget } from "../core/Context";
import MyCard from '../components/CardService';
import PotterService from '../services/PotterService'

export default withWidget(({ potterS, setPotterS, potterSpell, setPotterSpell, potterCharacter, setPotterCharacter }) => (
    <View style={styles.container} >
        <Fragment>
            <ScrollView style={styles.container} contentContainerStyle={styles.contentContainer}>
                <MyCard title="Harry Potter Service" value={potterS} setValue={setPotterS}
                    widget={<PotterService potterS={potterS} spell={potterSpell} setSpell={setPotterSpell} character={potterCharacter} setCharacter={setPotterCharacter} />}
                />
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
