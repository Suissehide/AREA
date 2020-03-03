import React from 'react';
import '../css/Switch.css';
import config from "../services/Config";

const Switch = ({ isOn, handleToggle, id, service, isService }) => {

    const changeSetting = () => {
        const email = localStorage.getItem('email') === null ? '' : localStorage.getItem('email');
        var url = '';
        if (isService)
            url = `${config.serverIp}/database/editservice/${email}/${service}/${!isOn}`;
        else
            url = `${config.serverIp}/database/editwidget/${email}/${service}/${id}/${!isOn}`;


        fetch(url, {
            method: "GET",
            headers: {},
        })
            .then(response => response.json())
            .then(responseJson => {

            })
            .catch(error => {
                console.error('Error: ', error);
            })
    };

    return (
        <>
            <input onClick={changeSetting}
                checked={isOn}
                onChange={handleToggle}
                className="react-switch-checkbox"
                id={id}
                type="checkbox"
            />
            <label
                style={{ background: isOn && '#3D2314' }}
                className="react-switch-label"
                htmlFor={id}
            >
                <span className={`react-switch-button`} />
            </label>
        </>
    );
};

export default Switch;
