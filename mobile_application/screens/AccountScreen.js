import React, { Fragment, useState } from "react";
import { StyleSheet, View } from 'react-native';
import { theme } from '../core/theme';
import { withWidget } from "../core/Context";
import Text from '../components/Text';
import Button from '../components/Button';
import axios from 'axios';
import TextInput from '../components/TextInput';
import Background from '../components/Background';
import {
    emailValidator,
    passwordValidator,
    nameValidator,
} from '../core/utils';
import { ScrollView } from 'react-native-gesture-handler';

function AccountInfo(props) {
    const [name, setName] = useState({ value: '', error: '' });
    const [email, setEmail] = useState({ value: '', error: '' });
    const [password, setPassword] = useState({ value: '', error: '' });
    const [socialToken, setSocialToken] = useState({ microsoft: null, facebook: null, google: null });

    const nameError = nameValidator(name.value);
    const emailError = emailValidator(email.value);
    const passwordError = passwordValidator(password.value);
    const CancelToken = axios.CancelToken;
    const source = CancelToken.source();

    const getData = () => {
        axios.get(`http://${props.ip}:8080/database/users/${props.token}`)
            .then(response => {
                console.log(response);
                setName({ ...name, value: response.data.users[0].name });
                setEmail({ ...email, value: response.data.users[0].email });
                setPassword({ ...password, value: response.data.users[0].pwd });
                setSocialToken({
                    ...socialToken, microsoft: response.data.users[0].microsoftToken,
                    facebook: response.data.users[0].facebookToken, google: response.data.users[0].googleToken
                });
            })
            .catch(function (error) {
                console.log(error);
            });
    }

    const log = () => {
        if (emailError || passwordError || nameError) {
            setName({ ...name, error: nameError });
            setEmail({ ...email, error: emailError });
            setPassword({ ...password, error: passwordError });
            return;
        }
        props.setToken(email.value);
        let loadData = () => {
            try {
                axios.get(`http://${props.ip}:8080/database/editaccount/${name.value}/${password.value}/${email.value}/${props.token}`)
                    .then(response => {
                        console.log(response.data);
                        response.data === true ? props.setToken(email.value) : setEmail({ ...email, error: "Email already taken." });
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
    }

    const deleteAccount = () => {
        let loadData = () => {
            try {
                axios.get(`http://${props.ip}:8080/database/delete/${email.value}`)
                    .then(response => {
                        console.log(response.data);
                        response.data === true ? props.setIsLogged(false) : null;
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
    }

    function Social() {
        var value = '';
        for (value in socialToken) {
            if (value !== null) {
                return (
                    <View>
                        {socialToken.microsoft === true ? <Text>Microsoft</Text> : null}
                        {socialToken.facebook === true ? <Text>facebbook</Text> : null}
                        {socialToken.google === true ? <Text>google</Text> : null}
                    </View>
                );
            }
        }
        return (
            <Text>You are not authenticated with any social service. Please visit Bananews.com on a web browser for more informations.</Text>
        );
    }

    return (
        <Background>
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
            <Social />
            <Button style={styles.saveButton} onPress={getData} > <Text swag={styles.text} >Get Info</Text></Button>
            <Button style={styles.saveButton} onPress={log} > <Text swag={styles.text} >Save Changes</Text></Button>
            <Button style={styles.button} onPress={() => props.setIsLogged(false)}> <Text swag={styles.text} >Log Out </Text></Button>
            <Button style={styles.delButton} onPress={deleteAccount} > <Text swag={styles.text}> Delete Account </Text> </Button>
        </Background>
    );
};


export default withWidget(({ setIsLogged, ip, token, setToken }) => (
    <Fragment>
        <ScrollView style={{ width: '100%' }} >
            <AccountInfo ip={ip} token={token} setToken={setToken} setIsLogged={setIsLogged} />
        </ScrollView>
    </Fragment >
));

const styles = StyleSheet.create({
    button: {
        width: '100%',
        marginVertical: 10,
        backgroundColor: "#FCCD2D",
    },
    saveButton: {
        width: '100%',
        marginVertical: 10,
        backgroundColor: "#99CC33",
    },
    delButton: {
        width: '100%',
        marginVertical: 10,
        backgroundColor: "#D70000",
    },
    text: {
        color: "#3D2314"
    },
    label: {
        color: theme.colors.secondary,
    },
});
