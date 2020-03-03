import React, {useState} from 'react';

export default function AuthHandler(props) {
    // const classes = useStyle();
    const [username, setUsername] = useState(0);

    const authHandler = (err, data) => {
        console.log(err, data);
        setUsername(data.authResponseWithAccessToken.account.name);
        props.changeAccessToken(data.authResponseWithAccessToken.accessToken);
    }
}
