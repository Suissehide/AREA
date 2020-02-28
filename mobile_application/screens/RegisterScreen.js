import React, { memo, useState, useEffect } from 'react';
import { View, Text, StyleSheet, TouchableOpacity } from 'react-native';
import Background from '../components/Background';
import Logo from '../components/Logo';
import Header from '../components/Header';
import Button from '../components/Button';
import TextInput from '../components/TextInput';
import BackButton from '../components/BackButton';
import { theme } from '../core/theme';
import axios from 'axios';
import {
    emailValidator,
    passwordValidator,
    nameValidator,
} from '../core/utils';

export default function RegisterScreen(props) {
    const [name, setName] = useState({ value: '', error: '' });
    const [email, setEmail] = useState({ value: '', error: '' });
    const [password, setPassword] = useState({ value: '', error: '' });
    const nameError = nameValidator(name.value);
    const emailError = emailValidator(email.value);
    const passwordError = passwordValidator(password.value);
    const CancelToken = axios.CancelToken;
    const source = CancelToken.source();

    const log = () => {
        if (emailError || passwordError || nameError) {
            setName({ ...name, error: nameError });
            setEmail({ ...email, error: emailError });
            setPassword({ ...password, error: passwordError });
            return;
        }
        props.setToken(email.value);
        const loadData = () => {
            try {
                axios.get(`http://${props.ip}:8080/database/signup/${name.value}/${password.value}/${email.value}`)
                    .then(response => {
                        console.log(response.data);
                        props.setToken(response.data);
                        console.log(props.token);
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
        props.setIsLoginOk(true);
        return () => { source.cancel(); };
    }

    return (
        <Background>
            <BackButton goBack={() => props.setView('normal')} />
            <Logo />
            <Header>Create Account</Header>
            <TextInput
                label="Name" returnKeyType="next" value={name.value}
                onChangeText={text => setName({ value: text, error: '' })}
                error={!!name.error} errorText={name.error}
            />

            <TextInput
                label="Email" returnKeyType="next" value={email.value}
                onChangeText={text => setEmail({ value: text, error: '' })}
                error={!!email.error} errorText={email.error}
                autoCapitalize="none" autoCompleteType="email"
                textContentType="emailAddress" keyboardType="email-address"
            />

            <TextInput
                label="Password" returnKeyType="done" value={password.value}
                onChangeText={text => setPassword({ value: text, error: '' })}
                error={!!password.error} errorText={password.error}
                secureTextEntry
            />

            <Button mode="contained" onPress={log} style={styles.button}>
                Sign Up
            </Button>

            <View style={styles.row}>
                <Text style={styles.label}>Already have an account? </Text>
                <TouchableOpacity onPress={() => props.setView('normal')}>
                    <Text style={styles.link}>Login</Text>
                </TouchableOpacity>
            </View>
        </Background>
    );
};

const styles = StyleSheet.create({
    label: {
        color: theme.colors.secondary,
    },
    button: {
        marginTop: 24,
    },
    row: {
        flexDirection: 'row',
        marginTop: 4,
    },
    link: {
        fontWeight: 'bold',
        color: theme.colors.primary,
    },
});
