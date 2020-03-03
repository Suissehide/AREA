import axios from 'axios';
import React, { useEffect, useState } from "react";
import config from '../../services/Config';

export default function FacebookWidget(props) {
    const [like, setLike] = useState("");
    const [number, setNumber] = useState(0);
    const [atoken, setaToken] = useState(0);

    useEffect(() => {
        const token = localStorage.getItem('email') === null ? '' : localStorage.getItem('email');
        axios.get(`${config.serverIp}/database/users/${token}`)
            .then(response => {
                setaToken(response.data.users[0].microsoftToken)
            })
            .catch(function (error) {
                console.log(error);
            });
    }, []);

    useEffect(() => {
        console.log(atoken)
        if (atoken !== 0)
            axios.get(`${config.serverIp}/api/facebook/${atoken}`)
                .then(response => {
                    console.log(response.data)
                    setLike(response.data.likes)
                })
                .catch(function (error) {
                    console.log(error);
                });
    }, [atoken]);

    return (
        <div  >
            {like === null ? <div>You don't have any like.</div> : null}
        </div>
    );
}