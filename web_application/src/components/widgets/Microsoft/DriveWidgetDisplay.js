import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import List from '@material-ui/core/List';
import ListItem from '@material-ui/core/ListItem';
import Divider from '@material-ui/core/Divider';
import ListItemText from '@material-ui/core/ListItemText';

const useStyles = makeStyles(theme => ({
    root: {
        width: '100%',
        maxWidth: 360,
        backgroundColor: theme.palette.background.paper,
    }
}));

function Test(props) {
    return (
        <ListItemText
            primary={props.info.name}
            secondary={
                <React.Fragment>
                    Created By : {props.info.createdBy.user.displayName} <br /> Last Modified By : {props.info.lastModifiedBy.user.displayName}
                </React.Fragment>
            }
        />
    );
};

export default function Display(props) {
    const classes = useStyles();
    return (
        <div>
            <List className={classes.root}>
                <ListItem alignItems="flex-start">
                    <div>
                        {props.mark >= 1 ? <div><Test info={props.info[0]} /> <Divider /> </div> : null}
                        {props.mark >= 2 ? <div><Test info={props.info[1]} /> <Divider /> </div> : null}
                        {props.mark >= 3 ? <div><Test info={props.info[2]} /> <Divider /> </div> : null}
                        {props.mark >= 4 ? <div><Test info={props.info[3]} /> <Divider /> </div> : null}
                        {props.mark >= 5 ? <div><Test info={props.info[4]} /> <Divider /> </div> : null}
                        {props.mark >= 6 ? <div><Test info={props.info[5]} /> <Divider /> </div> : null}
                        {props.mark >= 7 ? <div><Test info={props.info[6]} /> <Divider /> </div> : null}
                        {props.mark >= 8 ? <div><Test info={props.info[7]} /> <Divider /> </div> : null}
                        {props.mark >= 9 ? <div><Test info={props.info[8]} /> <Divider /> </div> : null}
                        {props.mark >= 10 ? <div><Test info={props.info[9]} /> <Divider /> </div> : null}
                        {props.mark >= 11 ? <div><Test info={props.info[10]} /> <Divider /> </div> : null}
                        {props.mark >= 12 ? <div><Test info={props.info[11]} /> <Divider /> </div> : null}
                        {props.mark >= 13 ? <div><Test info={props.info[12]} /> <Divider /> </div> : null}
                        {props.mark >= 14 ? <div><Test info={props.info[13]} /> <Divider /> </div> : null}
                        {props.mark >= 15 ? <div><Test info={props.info[14]} /> <Divider /> </div> : null}
                    </div>
                </ListItem>
            </List>
        </div >
    );
}