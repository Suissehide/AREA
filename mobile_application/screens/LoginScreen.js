import React, { useState } from 'react';
import { TouchableOpacity, StyleSheet, Text, View } from 'react-native';
import Background from '../components/Background';
import Logo from '../components/Logo';
import Header from '../components/Header';
import Button from '../components/Button';
import TextInput from '../components/TextInput';
import { theme } from '../core/theme';
import { emailValidator, passwordValidator } from '../core/utils';
import ForgotPasswordScreen from "./ForgotPasswordScreen";
import RegisterScreen from "./RegisterScreen"

export default function LoginScreen(props) {
    const [email, setEmail] = useState({ value: '', error: '' });
    const [password, setPassword] = useState({ value: '', error: '' });
    const [view, setView] = useState('normal');
    const _onLoginPressed = () => {
        const emailError = emailValidator(email.value);
        const passwordError = passwordValidator(password.value);

        if (emailError || passwordError) {
            setEmail({ ...email, error: emailError });
            setPassword({ ...password, error: passwordError });
            return;
        }
        props.setIsLoginOk(true);
    };

    switch (view) {
        case 'normal':
            return (
                <Background>
                    <Logo />
                    <Header>Welcome on Bananews !</Header>

                    <TextInput
                        label="Email"
                        returnKeyType="next"
                        value={email.value}
                        onChangeText={text => setEmail({ value: text, error: '' })}
                        error={!!email.error}
                        errorText={email.error}
                        autoCapitalize="none"
                        autoCompleteType="email"
                        textContentType="emailAddress"
                        keyboardType="email-address"
                    />

                    <TextInput
                        label="Password"
                        returnKeyType="done"
                        value={password.value}
                        onChangeText={text => setPassword({ value: text, error: '' })}
                        error={!!password.error}
                        errorText={password.error}
                        secureTextEntry
                    />

                    <View style={styles.forgotPassword}>
                        <TouchableOpacity
                            onPress={() => setView('password')}
                        >
                            <Text style={styles.label}>Forgot your password?</Text>
                        </TouchableOpacity>
                    </View>

                    <Button mode="contained" onPress={_onLoginPressed}>
                        Login
                    </Button>

                    <View style={styles.row}>
                        <Text style={styles.label}>Don’t have an account? </Text>
                        <TouchableOpacity
                            onPress={() => setView('newUser')}
                        >
                            <Text style={styles.link}>Sign up</Text>
                        </TouchableOpacity>
                    </View>
                </Background>
            );
        case 'password':
            return (<ForgotPasswordScreen setView={setView} />);
        case 'newUser':
            return (<RegisterScreen setView={setView} setIsLoginOk={props.setIsLoginOk} />);
    }
};

const styles = StyleSheet.create({
    forgotPassword: {
        width: '100%',
        alignItems: 'flex-end',
        marginBottom: 24,
    },
    row: {
        flexDirection: 'row',
        marginTop: 4,
    },
    label: {
        color: theme.colors.secondary,
    },
    link: {
        fontWeight: 'bold',
        color: theme.colors.primary,
    },
});