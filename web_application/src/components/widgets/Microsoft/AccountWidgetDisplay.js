import React, { useState } from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Button from '@material-ui/core/Button';

const useStyles = makeStyles(theme => ({
    button: {
        margin: theme.spacing(1),
    }
}));

export default function Display(props) {
    const classes = useStyles();
    const [showFullName, setShowFullName] = useState(false);
    const [showId, setShowId] = useState(false);
    const [showMail, setShowMail] = useState(false);
    const [showJobTitle, setShowJobTitle] = useState(false);
    const [showBusinessPhones, setShowBusinessPhones] = useState(false);

    return (
        <div>
            <Button variant="contained" className={classes.button} onClick={() => showFullName === false ? setShowFullName(true) : setShowFullName(false)}>
                {showFullName === false ? <div>Show Full Name</div> : <div>  {props.fullName} </div>}
            </Button>
            <Button variant="contained" color="secondary" className={classes.button} onClick={() => showMail === false ? setShowMail(true) : setShowMail(false)}>
                {showMail === false ? <div>Show Mail</div> : <div> {props.mail} </div>}
            </Button>
            <Button variant="contained" className={classes.button} onClick={() => showBusinessPhones === false ? setShowBusinessPhones(true) : setShowBusinessPhones(false)}>
                {showBusinessPhones === false ? <div>Show Business Phone</div> : <div>  {props.businessPhones} </div>}
            </Button>
            <Button variant="contained" color="secondary" className={classes.button} onClick={() => showJobTitle === false ? setShowJobTitle(true) : setShowJobTitle(false)}>
                {showJobTitle === false ? <div>Show Job Title</div> : <div> {props.jobTitle} </div>}
            </Button>
        </div>
    );
};