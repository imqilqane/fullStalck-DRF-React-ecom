import React from 'react';
import axios from 'axios';
import axiosInstance from '../../axios';
import {useHistory} from 'react-router-dom';
const Logout = () => {
    const history = useHistory()
    const token = localStorage.getItem('refresh');
    (token||history.push('/'));
    const data = {refresh_token : token};
    axiosInstance.post('auth/logout/',data).then(res => {
        localStorage.clear();
        history.push('/login');
    }).catch(err => {
        console.log(err);
    })
    return (
        <>
            
        </>
    );
};

export default Logout;