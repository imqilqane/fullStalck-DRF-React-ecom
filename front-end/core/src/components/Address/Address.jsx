import React from 'react';
import axios from 'axios';
import { useState, useEffect } from 'react';
import { useHistory } from 'react-router-dom';
import axiosInstance from '../../axios';
import '../../asserts/css/add_address.css'

const Address = () => {
    const history = useHistory();
    const my_address = Object.freeze({
        "street":'',
        "zip":'',
        "city":'',
        "country":'',
        'is_default':false,
        'use_default':false,
    })
    let [address, setAddress] = useState(my_address);

    const getData = (e) => {
        if (e.target.id === "is_default") {
            if (address['is_default'] === 'on') {
                setAddress({...address, [e.target.name.trim()] : false,})
            } else {
                setAddress({...address, [e.target.name.trim()] : "on",})
            }

        } else if (e.target.id === "use_default") {
            if (address['use_default'] === 'on') {
                setAddress({...address, [e.target.name.trim()] : false,})
            } else {
                setAddress({...address, [e.target.name.trim()] : "on",})
            }
            
        } else {
            setAddress({...address, [e.target.name.trim()] : e.target.value.trim(),})
        }
    }

    const postData = (e) => {
        e.preventDefault();
        axiosInstance.post('checkout/add/', address).then(res => {
            console.log(res);
            history.push('/checkout/payment');

        }).catch(err => {
            console.log(err);
        });

    }

    return (
        <>
            <div className="container">
                <h3>Add Address</h3>
                <form method='POST' onSubmit={postData}>
                    <input type="text" name="street" placeholder="street" onChange={getData}/>
                    <input type="text" name="zip_code" placeholder="zip code" onChange={getData}/>
                    <input type="text" name="city" placeholder="city" onChange={getData}/>
                    <input type="text" name="country" placeholder="country" onChange={getData}/>
                    <div className="check">
                        <input type="checkbox" name="is_default" id="is_default" onChange={getData}/>
                        <label for="is_default">add as default</label>

                    </div>
                    <div className="check">
                        <input type="checkbox" name="use_default" id="use_default" onChange={getData}/>
                        <label for="use_default">use default</label>

                    </div>
                    
                    <button className="btn btn-success">Add Address</button>
                </form>
            </div>
        </>
    );
};

export default Address;