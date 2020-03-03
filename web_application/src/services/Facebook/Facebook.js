import React from 'react';
import FacebookLogin from 'react-facebook-login';

export default function FacebookAuth(props) {
    const appId = 1247960065390755;

    return (
        <FacebookLogin
            appId={appId}
            autoLoad={false}
            fields="name,email,picture"
            callback={props.callback}
            icon="fa-facebook"
            size="small"
            cssClass="submit facebook-btn"
        />
    )
}
