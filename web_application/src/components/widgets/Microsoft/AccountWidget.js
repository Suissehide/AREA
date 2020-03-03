import React, { useState, useEffect } from 'react';
import axios from 'axios';
import Display from './AccountWidgetDisplay';
import config from '../../../services/Config';

export default function AccountWidget(props) {
    const [fullName, setFullName] = useState(0);
    const [id, setId] = useState(0);
    const [mail, setMail] = useState(0);
    const [jobTitle, setJobTitle] = useState(0);
    const [businessPhones, setBusinessPhones] = useState(0);
    const [acessToken, setAcessToken] = useState(0);

    useEffect(() => {
        const token = localStorage.getItem('email') === null ? '' : localStorage.getItem('email');
        axios.get(`${config.serverIp}/database/users/${token}`)
            .then(response => {
                setAcessToken(response.data.users[0].microsoftToken)
            })
            .catch(function (error) {
                console.log(error);
            });

    }, [])

    axios.get(`${config.serverIp}/api/microsoft/graph?authorization=${props.acessToken}`)
        .then(response => {
            setFullName(response.data.displayName);
            setJobTitle(response.data.jobTitle);
            setMail(response.data.mail);
        })
        .catch(function (error) {
            console.log(error);
        });

    return (
        <div>
            <h2>Microsoft Account Informations</h2>
            {
                <Display fullName={fullName} mail={mail} businessPhones={businessPhones} jobTitle={jobTitle} />
            }
        </div>
    );
}