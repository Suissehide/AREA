import { Ionicons } from '@expo/vector-icons';
import axios from 'axios';
import React, { useEffect, useState } from "react";
import { TouchableOpacity, View } from 'react-native';
import Text from '../../components/Text';

export default function MicrosoftDriveWidget(props) {
    const [displayName, setDisplayName] = useState(null);
    const [givenName, setGivenName] = useState(null);
    const [jobTitle, setJobTitle] = useState(null);
    const [mail, setMail] = useState(null);
    const [surname, setSurname] = useState(null);
    const [mobilePhone, setMobilePhone] = useState(null);
    const [officeLocation, setOfficeLocation] = useState(null);
    const [preferedLanguage, setPrefferedLanguage] = useState(null);
    var token = "a";

    useEffect(() => {
        axios.get(`http://${props.ip}/api/microsoft/graph?authorization=${token}`)
            .then(response => {
                setDisplayName(response.data.displayName);
                setGivenName(response.data.givenName);
                setJobTitle(response.data.jobTitle);
                setMail(response.data.mail);
                setSurname(response.data.surname);
                setMobilePhone(response.data.mobilePhone);
                setOfficeLocation(response.data.officeLocation);
                setPreferedLanguage(response.data.preferedLanguage);
            })
            .catch(function (error) {
                console.log(error);
            });
    }, []);

    return (
        <View style={{ alignItems: 'center', paddingTop: 20 }}>
            <View style={{ width: '80%' }} >
                {displayName === null ? <Text>You didn't enter a Display Name yet</Text> : <Text>Your Display Name is <Text swag={{ fontWeight: 'bold' }} >{displayName}</Text></Text>}
                {givenName === null ? <Text>You didn't enter a Given Name yet</Text> : <Text>Your Given Name is <Text swag={{ fontWeight: 'bold' }} >{givenName}</Text></Text>}
                {surname === null ? <Text>You didn't enter a Surname yet</Text> : <Text>Your Surname is <Text swag={{ fontWeight: 'bold' }} >{surname}</Text></Text>}
                {mail === null ? <Text>You didn't enter a Mail Address yet</Text> : <Text>Your Mail Address is <Text swag={{ fontWeight: 'bold' }} >{mail}</Text></Text>}
                {mobilePhone === null ? <Text>You didn't enter a Mobile Phone Number yet</Text> : <Text>Your Mobile Phone Number is <Text swag={{ fontWeight: 'bold' }} >{mobilePhone}</Text></Text>}
                {jobTitle === null ? <Text>You didn't enter a Job Title yet</Text> : <Text>Your Job Title is <Text swag={{ fontWeight: 'bold' }} >{jobTitle}</Text></Text>}
                {officeLocation === null ? <Text>You didn't enter an Office Location yet</Text> : <Text>Your Office Location is <Text swag={{ fontWeight: 'bold' }} >{officeLocation}</Text></Text>}
                {preferedLanguage === null ? <Text>You didn't enter a Preffered Language yet</Text> : <Text>Your Preffered Language is <Text swag={{ fontWeight: 'bold' }} >{preferedLanguage}</Text></Text>}
            </View>
        </View>
    );
}

<Text swag={{ fontWeight: 'bold' }} ></Text>