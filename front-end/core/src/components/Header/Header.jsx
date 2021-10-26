import React from 'react';
import { NavLink } from 'react-router-dom';
import '../../asserts/css/header.css'
import { useState, useEffect } from 'react';
import axios from 'axios';
import axiosInstance from '../../axios';



const Header = () => {
    
    const [cats, setCats] = useState([]);
    const [inCart, setinCart] = useState('0');
    const token = localStorage.getItem('access');
    useEffect(() => {
        axiosInstance.get('products/categories/').then(res => {
            setCats(res.data)
        }).catch(err => {
            console.log(err);
        })
    },[]);

    useEffect(() => {
        axiosInstance.get('products/cart/').then(res => {

            let qts = res.data.map(item => item.quantity);
            let in_cart = qts.reduce((total, current) => {
                return total += current
            });
            
            setinCart(in_cart.toString());
           
        }).catch(err => {
            console.log(err);
        });
    }, []);
    return (
        <>
            <nav>
                <div className="header-containter">
                    <div className="logo">
                        <NavLink to="/"><h3>ECOMMERCE FULLSTACK</h3></NavLink>
                    </div>
                    <div className="links">
                        <ul>
                            <li>
                                <NavLink to='/' >Home</NavLink>
                            </li>
                            {cats.map(cat => (
                                <li>
                                <NavLink to={`/category/${cat.name}`} >{cat.name}</NavLink>
                            </li>
                            ))}
                            {
                            token ? 
                            <>
                                <li>
                                    <NavLink to='/Logout' className="login">Logout</NavLink>
                                </li>
                                <li>
                                    <NavLink to='/login' className="login">Account</NavLink>
                                </li>
                            </>
                            :
                            <>
                                <li>
                                <NavLink to='/register' className="register">register</NavLink>
                                </li>
                                <li>
                                <NavLink to='/login' className="login">login</NavLink>
                                </li>
                            </>
                            }
                            
                             <li>
                                
                                <NavLink to='/cart' className="cart" incart={inCart} ><i class="fa fa-shopping-cart" aria-hidden="true"></i>
</NavLink>
                            </li>
                            
                            
                        </ul>
                    </div>
                </div>
            </nav>
        </>
    );
};



export default Header;