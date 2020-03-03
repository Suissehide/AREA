import React from 'react';
import MicrosoftLogin from "react-microsoft-login";
import ButtonTheme from "./ButtonTheme.sj";

export default function MicrosoftAuth(props) {
    const clientId = '04bd8816-75eb-4996-b663-fdce462165d1';
    const typeAuth = ["user.read", "mail.read", "sites.readwrite.all", "people.read", "calendars.readwrite"];
    const redirectUri = 'http://localhost:3000/user';

    return (
        <MicrosoftLogin clientId={clientId}
            authCallback={props.callback}
            redirectUri={redirectUri}
            children={<ButtonTheme />}
            graphScopes={typeAuth}
        />
    );
}
