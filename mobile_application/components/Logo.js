import React, { memo } from 'react';
import { Image, StyleSheet } from 'react-native';

const Logo = () => (
    <Image source={require('../assets/bananews.png')} style={styles.image} />
);

const styles = StyleSheet.create({
    image: {
        width: 177,
        height: 166,
    },
});

export default memo(Logo);
