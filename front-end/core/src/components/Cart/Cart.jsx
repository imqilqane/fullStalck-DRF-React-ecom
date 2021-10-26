import React from 'react';
import axios from 'axios';
import { useState, useEffect } from 'react';
import { useParams } from 'react-router';
import '../../asserts/css/cart.css'
import { Link } from 'react-router-dom';
import axiosInstance from '../../axios';
const Cart = () => {
    const [products, setProducts] = useState([]);
    const [IsLoading, setIsLoading] = useState(true);
    const [cart, setCart] = useState([]);
    var total = 0;
    useEffect(()=>{
        axios.all([
            axiosInstance.get('products/cart/'),
            axiosInstance.get('products/')
        ]).then(axios.spread((res1, res2) =>{
            setCart(res1.data);
            setProducts(res2.data);
            setIsLoading(false)
        }))
    },[]);

    function getTotal (){
        cart.map(item=>{
            const product = products.find(curent => curent.id === item.product)
            total += (product.price * item.quantity)
        }) 
    };

    if (IsLoading) {
        return <h3>Is loading ...</h3>
    }
    getTotal()

    return (
        <>
        <div className="container">
        <h3>Cart</h3>
        <table class="table">
                <thead class="thead-dark">
                    <tr>
                    <th scope="col">#</th>
                    <th scope="col" className='table-title'>Title</th>
                    <th scope="col">Qte</th>
                    <th scope="col" className='table-price'>Price</th>
                    </tr>
                </thead>
                <tbody>
                    {cart.map((item , index) =>  {
                        let product = products.filter( product => item.product === product.id );
                        
                        return (<tr>
                        <th scope="row">{index + 1}</th>
                        <td>{product[0].title}</td>
                        <td>{item.quantity}</td>
                        <td>$ {product[0].price * item.quantity}</td>
                        </tr>
                        )
                    
                    })}
                </tbody>
                <tbody>
                    <th>Total Price</th>
                    <td></td>
                    <td></td>
                    <td>$ {total.toFixed(2)}</td>
                </tbody>
        </table>
        <Link to='/' className='btn btn-danger'>Continue Shopping</Link>

        <Link to='/checkout' className='btn btn-success'>Continue To CheckOut</Link>
        </div>
           

                
        </>
    );
};

export default Cart;