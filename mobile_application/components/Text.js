import React, { memo } from 'react';
import { StyleSheet } from 'react-native';
import { Text } from 'react-native-elements';
import { theme } from '../core/theme';

const MyText = ({ mode, style, children, ...props }) => (
    <Text
        style={[
            styles.text,
        ]}
        mode={mode}
        {...props}
    >
        {children}
    </Text>
);

const styles = StyleSheet.create({
    text: {
        textAlign: 'center',
    },
});

export default memo(MyText);
