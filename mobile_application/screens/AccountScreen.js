import React, { Fragment, useState } from "react";
import { StyleSheet, View } from 'react-native';
import { ScrollView } from 'react-native-gesture-handler';
import { theme } from '../core/theme';
import { withWidget } from "../core/Context";
import MyCard from '../widgets/CardTemplate';
import Text from '../components/Text';
import Button from '../components/Button';
import axios from 'axios';
import { Card } from 'react-native-elements';

function AccountInfo(props) {
    const [name, setName] = useState('');
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [microsoftToken, setMicrosoftToken] = useState(null);
    const [facebookToken, setFacebookToken] = useState(null);
    const [googleToken, setGoogleToken] = useState(null);

    const handlechange = () => {
        axios.get(`http://${props.ip}:8080/database/users/${props.token}`)
            .then(response => {
                console.log(response);
                setName(response.data.users[0].name);
                setEmail(response.data.users[0].email);
                setPassword(response.data.users[0].pwd);
                setMicrosoftToken(response.data.users[0].microsoftToken);
                setFacebookToken(response.data.users[0].facebookToken);
                setGoogleToken(response.data.users[0].googleToken);
            })
            .catch(function (error) {
                console.log(error);
            });
    }
    return (
        <Card containerStyle={styles.card}>
            <Text swag={styles.title}>Account Settings</Text>
            <Text> Your Name : {name} </Text>
            <Text>Your E-mail : {email} </Text>
            <Text>Your Password : {password} </Text>
            {microsoftToken === null && facebookToken === null && googleToken === null ? <Text> You are not authenticated with any social services yet.</Text> : <Text>Your are authenticated with : </Text>}
            {microsoftToken !== null ? <Text>Microsoft</Text> : null}
            {facebookToken !== null ? <Text>facebook</Text> : null}
            {googleToken !== null ? <Text>google</Text> : null}
            <Text>Please visit our web browser to authenticate with more social services ! </Text>
            <Button onPress={handlechange} >REST</Button>
        </Card>
    );
}

export default withWidget(({ setIsLogged, ip, token }) => (
    <Fragment >
        <ScrollView contentContainerStyle={styles.contentContainer}>
            <AccountInfo ip={ip} token={token} />
            <View style={{ alignItems: 'center' }}>
                <Button style={styles.button} onPress={() => setIsLogged(false)}> <Text swag={styles.text} >Log Out </Text></Button>
            </View>
        </ScrollView>
    </Fragment>
));

const styles = StyleSheet.create({
    contentContainer: {
        paddingTop: 15,
    },
    button: {
        width: '50%',
        marginVertical: 10,
        backgroundColor: "#3D2314",
    },
    container: {
        flexDirection: 'row',
    },
    title: {
        fontSize: 20,
        alignSelf: "center",
    },
    card: {
        backgroundColor: theme.colors.primary,
        borderWidth: 0,
        borderRadius: 20
    },
    text: {
        color: "#FCCD2D"
    },
});
