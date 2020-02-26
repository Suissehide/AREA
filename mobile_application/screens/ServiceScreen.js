import React, { Fragment } from "react";
import { StyleSheet, View } from 'react-native';
import { ScrollView } from 'react-native-gesture-handler';
import { withWidget } from "../core/Context";
import MyCard from '../components/CardService';
import PotterService from '../services/PotterService';
import WeatherService from '../services/WeatherService';

export default withWidget(({ potterS, setPotterS, potterSpell, setPotterSpell, potterCharacter, setPotterCharacter,
    weatherS, setWeatherS, weatherW, setWeatherW }) => (
        <View style={styles.container} >
            <Fragment>
                <ScrollView style={styles.container} contentContainerStyle={styles.contentContainer}>
                    <MyCard title="Harry Potter Service" value={potterS} setValue={setPotterS}
                        widget={<PotterService potterS={potterS} spell={potterSpell} setSpell={setPotterSpell} character={potterCharacter} setCharacter={setPotterCharacter} />}
                    />
                    <MyCard title="Weather Service" value={weatherS} setValue={setWeatherS}
                        widget={<WeatherService weatherS={weatherS} weatherW={weatherW} setWeatherW={setWeatherW} />}
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
