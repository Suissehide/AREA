import React from 'react';
import MicrosoftLogin from "react-microsoft-login";
import ButtonTheme from "./ButtonTheme.sj";

export default function MicrosoftAuth(props) {
    const clientId = '0a445f3f-e6cb-4890-90c8-2521b2797226';
    const typeAuth = ["user.read", "mail.read", "sites.readwrite.all", "people.read", "calendars.readwrite"];
    const redirectUri = 'http://localhost:3000';
    
    return (
        <MicrosoftLogin clientId={clientId}
                        authCallback={props.callback}
                        redirectUri={redirectUri}
                        children={<ButtonTheme />}
                        graphScopes={typeAuth}
        />
    );
}
