import axios from 'axios';
import React, {useEffect, useState}  from 'react';
import { useParams } from 'react-router';

const Verify = () => {
    const {token} = useParams();
    console.log(token);
    const [loading, setloading] = useState(1)
    useEffect(() => {
        axios.get(`http://localhost:8000/api/auth/register/verifing/?token=${token}`).then(res => {
            console.log(res);
            setloading(3)
        }).catch(err => {
            console.log(err);
            setloading(2)
        })
    }, [])
    if (loading === 1) {
        return <div> loading </div>
    } else if (loading === 2) {
        return <div> 404 Not Found </div>
    }
    return (
        <>
            <h2>Your account is successfully verified ... you can log in now</h2>
        </>
    );
};

export default Verify;