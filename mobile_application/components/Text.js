import React, { memo } from 'react';
import { StyleSheet } from 'react-native';
import { Text } from 'react-native-elements';

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
    },
});

export default memo(MyText);
