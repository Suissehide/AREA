import axios from 'axios';
import React, { Fragment, useEffect, useState } from "react";
import { Image, StyleSheet, View } from 'react-native';
import { KeyboardAwareScrollView } from 'react-native-keyboard-aware-scroll-view';
import Background from '../components/Background';
import Button from '../components/Button';
import Text from '../components/Text';
import TextInput from '../components/TextInput';
import { withWidget } from "../core/Context";
import { theme } from '../core/theme';
import { emailValidator, nameValidator, passwordValidator } from '../core/utils';

function AccountInfo(props) {
    const [name, setName] = useState({ value: '', error: '' });
    const [email, setEmail] = useState({ value: '', error: '' });
    const [password, setPassword] = useState({ value: '', error: '' });
    const [socialToken, setSocialToken] = useState({ microsoft: "", facebook: "", google: "" });

    const nameError = nameValidator(name.value);
    const emailError = emailValidator(email.value);
    const passwordError = passwordValidator(password.value);
    const CancelToken = axios.CancelToken;
    const source = CancelToken.source();

    useEffect(() => {
        axios.get(`http://${props.ip}/database/users/${props.token}`)
            .then(response => {
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
    }, []);

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
                axios.get(`http://${props.ip}/database/editaccount/${name.value}/${password.value}/${email.value}/${props.token}`)
                    .then(response => {
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
                axios.get(`http://${props.ip}/database/delete/${email.value}`)
                    .then(response => {
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
        return (
            <View style={{ flexDirection: 'row', justifyContent: 'space-around' }} >
                {socialToken.microsoft !== "" ? <Image source={require('../assets/images/social/microsoftV.png')} style={styles.image} /> :
                    <Image source={require('../assets/images/social/microsoftX.png')} style={styles.image} />}
                {socialToken.facebook !== "" ? <Image source={require('../assets/images/social/facebookV.png')} style={styles.image} /> :
                    <Image source={require('../assets/images/social/facebookX.png')} style={styles.image} />}
                {socialToken.google !== "" ? <Image source={require('../assets/images/social/googleV.png')} style={styles.image} /> :
                    <Image source={require('../assets/images/social/googleX.png')} style={styles.image} />}
            </View>
        );
    }

    return (
        <View style={{ width: '80%', alignSelf: 'center' }} >
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
            <Text swag={{ paddingTop: 20 }} >If you want to remove / add more social services, please go to Bananews.com.</Text>
            <Button style={styles.saveButton} onPress={log} > <Text swag={styles.text} >Save Changes</Text></Button>
            <Button style={styles.button} onPress={() => props.setIsLogged(false)}> <Text swag={styles.text} >Log Out </Text></Button>
            <Button style={styles.delButton} onPress={deleteAccount} > <Text swag={styles.text}> Delete Account </Text> </Button>
        </View>
    );
};


export default withWidget(({ setIsLogged, ip, token, setToken }) => (
    <Background style={{ width: '100%' }}  >
        <KeyboardAwareScrollView style={{ width: '100%', marginTop: -8 }} >
            <Fragment>
                <AccountInfo ip={ip} token={token} setToken={setToken} setIsLogged={setIsLogged} />
            </Fragment >
        </KeyboardAwareScrollView>
    </Background>
));

const styles = StyleSheet.create({
    button: {
        width: '100%',
        marginVertical: 10,
        backgroundColor: theme.colors.primary,
    },
    saveButton: {
        width: '100%',
        marginVertical: 10,
        backgroundColor: theme.colors.green,
    },
    delButton: {
        width: '100%',
        marginVertical: 10,
        backgroundColor: theme.colors.red,
    },
    text: {
        color: theme.colors.brown
    },
    label: {
        color: theme.colors.secondary,
    },
    image: {
        width: 50,
        height: 50,
        marginRight: 15,
        marginLeft: 15,
    },
});
