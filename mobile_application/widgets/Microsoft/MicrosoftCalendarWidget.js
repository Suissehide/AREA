import { Ionicons } from '@expo/vector-icons';
import axios from 'axios';
import React, { useEffect, useState } from "react";
import { TouchableOpacity, View } from 'react-native';
import Text from '../../components/Text';

export default function MicrosoftCalendarWidget(props) {
    const [subject, setSubject] = useState("");
    const [dateTime, setDateTime] = useState(0);
    const [number, setNumber] = useState(0);
    const [saveLen, setSaveLen] = useState(2);
    var token =
        "eyJ0eXAiOiJKV1QiLCJub25jZSI6InU5WXZxa3pkYmdmSmdocXA0ZnhnNEZvb1pLVGNVWncxbkZXb0NZQmVZajQiLCJhbGciOiJSUzI1NiIsIng1dCI6IkhsQzBSMTJza3hOWjFXUXdtak9GXzZ0X3RERSIsImtpZCI6IkhsQzBSMTJza3hOWjFXUXdtak9GXzZ0X3RERSJ9.eyJhdWQiOiIwMDAwMDAwMy0wMDAwLTAwMDAtYzAwMC0wMDAwMDAwMDAwMDAiLCJpc3MiOiJodHRwczovL3N0cy53aW5kb3dzLm5ldC85MDFjYjRjYS1iODYyLTQwMjktOTMwNi1lNWNkMGY2ZDlmODYvIiwiaWF0IjoxNTgzMDYxMjI5LCJuYmYiOjE1ODMwNjEyMjksImV4cCI6MTU4MzA2NTEyOSwiYWNjdCI6MCwiYWNyIjoiMSIsImFpbyI6IkFTUUEyLzhPQUFBQWNOclhmanlFQ3RVWjEwbWZoYVdwTDJPd2xka2QxWFlHVHVRWDFKVWlzdEU9IiwiYW1yIjpbInB3ZCJdLCJhcHBfZGlzcGxheW5hbWUiOiJkYXNoYm9hcmQiLCJhcHBpZCI6IjM3YWNkMTY4LTNiMGMtNGY5OC05N2Q1LTgzMmYzNzcxYmE3ZSIsImFwcGlkYWNyIjoiMCIsImZhbWlseV9uYW1lIjoiUmVpbmFyZXMiLCJnaXZlbl9uYW1lIjoiSWRvaWEiLCJpcGFkZHIiOiI3Ny4yMDUuMTUyLjI1NCIsIm5hbWUiOiJJZG9pYSBSZWluYXJlcyIsIm9pZCI6IjIyZmM0YjNiLTRkZmEtNDE0Yy1iYTJhLWQ1NGYyMzFmNWY0NCIsIm9ucHJlbV9zaWQiOiJTLTEtNS0yMS0xNTUyNDM1Mjc3LTE1OTY0OTU3OTUtMzA4OTYxMzczMS0zMDMzMyIsInBsYXRmIjoiMyIsInB1aWQiOiIxMDAzQkZGREEzRTQ1QUUyIiwic2NwIjoiQ2FsZW5kYXJzLlJlYWRXcml0ZSBNYWlsLlJlYWQgb3BlbmlkIFBlb3BsZS5SZWFkIHByb2ZpbGUgU2l0ZXMuUmVhZFdyaXRlLkFsbCBVc2VyLlJlYWQgZW1haWwiLCJzaWduaW5fc3RhdGUiOlsia21zaSJdLCJzdWIiOiJSeWRlOUxUUFZ2cV9jc3o1ZnNYeUdIYXNuWWlIQWhKWDBpeDJrRmpCSnZJIiwidGlkIjoiOTAxY2I0Y2EtYjg2Mi00MDI5LTkzMDYtZTVjZDBmNmQ5Zjg2IiwidW5pcXVlX25hbWUiOiJpZG9pYS5yZWluYXJlc0BlcGl0ZWNoLmV1IiwidXBuIjoiaWRvaWEucmVpbmFyZXNAZXBpdGVjaC5ldSIsInV0aSI6ImVGX0p3RG4xSUVXUzJxZzZFWkZ2QUEiLCJ2ZXIiOiIxLjAiLCJ4bXNfc3QiOnsic3ViIjoiUzcxcVdSTWtxenhUdThIR1dJb1BZTV9fSGU5TFg2ZmMxQUZrS1lyWk14YyJ9LCJ4bXNfdGNkdCI6MTQxNzgwNDg4N30.VtdGOiN0ILr901qSrdA9e2Ij91pILb8_1PD7stGWgILByw0gO_pfA0YrxKHtW_hBi4Qtvi-uvHA-2Co1ayPtC9jH94rWu7Xp7RS8H9Bggj9RW8zH20aoHmaB9Bm0GvLYOyYXofyC-sWToyKrxEKGRz3lBGvFRrXElLxqY_qESic-DrxlXtK_K_T5FC3HRvDCwTVkZDTTKyf1XNOs72yTCLoipDJaIViFncr_KlrwFFvfQZ2l1rrzU_8vUWRGqwIQ1PiaB7IaA5FtlYsPr_K336Y2CD7f73noBBp-uULoFIqxCXNhb50boYt-PIimnt8s5PvQICwHt0NANWKXe2ionw"

    function MyIcon(props) {
        return (
            <Ionicons
                name={props.name}
                size={30}
                style={{ marginBottom: -3 }}
            />
        );
    }

    useEffect(() => {
        axios.get(`http://${props.ip}/api/microsoft/calendar?authorization=${token}`)
            .then(response => {
                setSaveLen(response.data.value.length);
                setSubject(response.data.value[number].subject);
                setDateTime(response.data.value[number].start.dateTime);
                setDateTime(String(new Date(dateTime)));
            })
            .catch(function (error) {
                console.log(error);
            });
    }, []);

    const handleChange = (value) => {
        if (value === -1 && number !== 0)
            setNumber(number + value)
        else if (value === 1 && number < saveLen)
            setNumber(number + value)
    }

    useEffect(() => {
        axios.get(`http://${props.ip}/api/microsoft/calendar?authorization=${token}`)
            .then(response => {
                setSubject(response.data.value[number].subject);
                setDateTime(response.data.value[number].start.dateTime);
                setDateTime(String(new Date(dateTime)));
            })
            .catch(function (error) {
                console.log(error);
            });
    }, [number]);

    return (
        <View style={{ alignItems: 'center', paddingTop: 20 }}>
            <View style={{ flexDirection: 'row', width: '100%', alignItems: 'center', justifyContent: 'space-around', paddingTop: 15 }} >
                <TouchableOpacity onPress={() => handleChange(-1)}>
                    <MyIcon name="ios-arrow-back" />
                </TouchableOpacity>
                <View style={{ width: '80%', alignItems: 'center' }} >
                    <Text swag={{ fontSize: 15 }} >{subject} on {String(dateTime)} </Text>
                </View>
                <TouchableOpacity onPress={() => handleChange(1)}>
                    <MyIcon name="ios-arrow-forward" />
                </TouchableOpacity>
            </View>
        </View>
    );
}