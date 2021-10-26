import React, {useState} from 'react';
import axios from 'axios'
import {useHistory} from 'react-router-dom'

const Register = () => {
    const history = useHistory();
    const token = localStorage.getItem('access');
    const user_info = Object.freeze({
        username : "",
        email : "",
        first_name : "",
        last_name : "",
        password : "",
    });
    const [user, setUser] = useState(user_info);
    (!token|| history.push('/'));
    const getData = (e) => {
        setUser({...user , [e.target.name.trim()] : e.target.value.trim()});
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        axios.post('http://localhost:8000/api/auth/register/', user).then(res => {
            console.log(res.data);
            history.push('/')
        }).catch(err => {
            console.log(err);
        })
    }
    return (
        <>
            <form method="post" onSubmit={handleSubmit}>
                <input type="text" name="username" id="username" placeholder="username" onChange={getData} />
                <input type="email" name="email" id="email" placeholder="email" onChange={getData} />
                <input type="text" name="first_name" id="first_name" placeholder="First name" onChange={getData} />
                <input type="text" name="last_name" id="last_name" placeholder="Last name" onChange={getData} />
                <input type="password" name="password" id="password" placeholder="password" onChange={getData} />
                <label>profile picture</label>
                <input type="file" onChange={getData} />

                <button>Register</button>
            </form>
        </>
    );
};

export default Register;