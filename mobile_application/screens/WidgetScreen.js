import React, { Fragment } from "react";
import { StyleSheet, View } from 'react-native';
import { RectButton, ScrollView } from 'react-native-gesture-handler';
import { Text, Card, Divider } from 'react-native-elements';
import { theme } from '../core/theme';
import { withWidget } from "../core/Context";
import MyCard from '../widgets/CardTemplate';
import Oui from '../widgets/Oui';
import PotterSpell from '../widgets/Potter/PotterSpell'

export default withWidget(({ potterS, potterSpell, potterCharacter, ip }) => (
    <ScrollView style={styles.container} contentContainerStyle={styles.contentContainer}>
        <Fragment>
            {potterS === true && potterSpell === true ?
                <MyCard title="Harry Potter's Random Spell" widget={<PotterSpell ip={ip} />} /> : null}
            {potterS === true && potterCharacter === true ?
                <MyCard title="Random Character from Harry Potter" widget={<Oui />} /> : null}
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
