import React, {useState} from 'react';
import axios from 'axios';
import {useHistory} from 'react-router-dom';

const Login = () => {
    const token = localStorage.getItem('access');
    const history = useHistory();
    const data = Object.freeze({
        email :"",
        password :""
    })
    const [user, setUser] = useState(data);
    (!token|| history.push('/'));
    const getData = (e) =>{
        setUser({...user, [e.target.name.trim()]:e.target.value.trim(),});
    };
    const handleSubmit = (e) => {
        e.preventDefault();
        axios.post('http://localhost:8000/api/auth/login/',user).then(res => {
            console.log(res.data);
            localStorage.setItem('refresh',res.data.token['refresh']);
            localStorage.setItem('access',res.data.token['access']);
            history.push('/');
        }).catch(err => {
            console.log(err);
        });
    };
    return (
        <>
        <form method="post" onSubmit={handleSubmit}>
            <input type="email" name="email" id="email" placeholder="email" onChange={getData} />
            <input type="password" name="password" id="password" placeholder="password" onChange={getData} />

            <button>Login</button>
        </form>
    </>
    );
};

export default Login;