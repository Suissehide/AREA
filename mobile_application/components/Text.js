import React, { memo } from 'react';
import { StyleSheet } from 'react-native';
import { Text } from 'react-native-elements';
import { theme } from '../core/theme';

const MyText = ({ mode, style, children, ...props }) => (
    <Text
        style={[
            styles.onText,
            props.swag,
        ]}
        mode={mode}
        {...props}
    >
        {children}
    </Text>
);

const styles = StyleSheet.create({
    onText: {
        textAlign: 'center',
        color: theme.colors.brown
    },
});

export default memo(MyText);
