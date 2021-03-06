import axios from 'axios';
import React, { useState } from 'react';
import { KeyboardAvoidingView, StyleSheet, Text, TouchableOpacity, View } from 'react-native';
import Background from '../components/Background';
import Button from '../components/Button';
import Header from '../components/Header';
import Logo from '../components/Logo';
import TextInput from '../components/TextInput';
import { withWidget } from "../core/Context";
import { theme } from '../core/theme';
import { emailValidator, passwordValidator } from '../core/utils';
import ForgotPasswordScreen from "./ForgotPasswordScreen";
import RegisterScreen from "./RegisterScreen";

function Login(props) {
    const [email, setEmail] = useState({ value: '', error: '' });
    const [password, setPassword] = useState({ value: '', error: '' });
    const [view, setView] = useState('normal');
    const CancelToken = axios.CancelToken;
    const source = CancelToken.source();

    const _onLoginPressed = () => {
        const emailError = emailValidator(email.value);
        const passwordError = passwordValidator(password.value);

        if (emailError || passwordError) {
            setEmail({ ...email, error: emailError });
            setPassword({ ...password, error: passwordError });
            return;
        }

        const loadData = () => {
            try {
                axios.get(`http://${props.ip}/database/login/${email.value}/${password.value}`)
                    .then(response => {
                        response.data === true ? props.setToken(email.value) : setEmail({ ...email, error: "Email or password invalid." });
                        response.data === true ? props.setIsLoginOk(true) : setPassword({ ...password, error: "Email or password invalid." });
                    });
            } catch (error) {
                if (axios.isCancel(error)) {
                    console.log("cancelled");
                } else {
                    throw error;
                }
            }
        };
        loadData();
        return () => { source.cancel(); };
    };

    switch (view) {
        case 'normal':
            return (
                <Background>
                    <KeyboardAvoidingView style={styles.container} behavior="padding">
                        <Logo />
                        <Header>Welcome on Bananews !</Header>

                        <TextInput label="Email" returnKeyType="next" value={email.value}
                            onChangeText={text => setEmail({ value: text, error: '' })}
                            error={!!email.error} errorText={email.error}
                            autoCapitalize="none" autoCompleteType="email"
                            textContentType="emailAddress" keyboardType="email-address" />

                        <TextInput label="Password" returnKeyType="done" value={password.value}
                            onChangeText={text => setPassword({ value: text, error: '' })}
                            error={!!password.error} errorText={password.error} secureTextEntry />

                        <View style={styles.forgotPassword}>
                            {/* onPress={() => setView('password')} */}
                            <TouchableOpacity >
                                <Text style={styles.label}>Forgot your password?</Text>
                            </TouchableOpacity>
                        </View>

                        <Button mode="contained" onPress={_onLoginPressed}> Login </Button>

                        <View style={styles.row}>
                            <Text style={styles.label}>Don’t have an account? </Text>
                            <TouchableOpacity onPress={() => setView('newUser')} >
                                <Text style={styles.link}>Sign up</Text>
                            </TouchableOpacity>
                        </View>
                    </KeyboardAvoidingView>
                </Background >
            );
        case 'password':
            return (<ForgotPasswordScreen setView={setView} />);
        case 'newUser':
            return (<RegisterScreen setView={setView} setIsLoginOk={props.setIsLoginOk} ip={props.ip} setToken={props.setToken} token={props.token} />);
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
        fontSize: 17,
    },
    link: {
        fontSize: 17,
        fontWeight: 'bold',
        color: theme.colors.primary,
    },
    container: {
        flex: 1,
        padding: 20,
        width: '100%',
        maxWidth: 340,
        alignSelf: 'center',
        alignItems: 'center',
        justifyContent: 'center',
    },
});

export default withWidget(({ token, setToken, setIsLogged, ip }) => (
    <Login token={token} setToken={setToken} setIsLoginOk={setIsLogged} ip={ip} />
));