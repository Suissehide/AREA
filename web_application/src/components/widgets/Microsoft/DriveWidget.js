import React, { useState } from 'react';
import axios from 'axios';
import LockIcon from '@material-ui/icons/Lock';
import Slider from '@material-ui/core/Slider';
import Display from './DriveWidgetDisplay';

export default function DriveWidget(props) {
    const [info, setInfo] = useState(0);
    const [mark, setMark] = useState(0);
    var acessToken = props.acessToken;

    function valuetext(value) {
        setMark(value);
        return `${value}°C`;
    }

    const Change = () => {
        axios.get(`http://localhost:8080/drive?authorization=${acessToken}`)
            .then(response => {
                console.log(response)
                setInfo(response.data.value);
            })
            .catch(function (error) {
                console.log(error);
            });
    };

    return (
        <div>
            <h2>Microsoft OneDrive</h2>
            {acessToken === "yolo" ? <div> <LockIcon />  Please sign in with Microsoft first</div> : null}
            {
                acessToken !== "yolo" ?
                    <div>
                        <Slider
                            defaultValue={0}
                            getAriaValueText={valuetext}
                            aria-labelledby="discrete-slider"
                            valueLabelDisplay="auto"
                            onChange={Change}
                            step={1}
                            min={0}
                            max={15}
                        />
                        {info !== 0 ? <Display info={info} mark={mark} /> : null}
                    </div>
                    : null
            }
        </div>
    );
}