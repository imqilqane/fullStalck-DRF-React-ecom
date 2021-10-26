import React from 'react';
import axios from 'axios'
import { useState, useEffect } from 'react';
import axiosInstance from '../../axios';
import '../../asserts/css/products.css'
import { Link } from 'react-router-dom';

const Products = () => {
    const [IsLoading, setIsLoading] = useState(true);
    const [products, setProducts] = useState([]);
    const [cats, setCats] = useState([]);

    useEffect(() => {
        axios.all([
            axiosInstance.get('products/categories/'),
            axiosInstance.get('products/')
        ]).then(axios.spread((res1, res2)=> {
            setCats(res1.data)
            setProducts(res2.data)
            setIsLoading(false)

        })).catch(err => {
            console.log(err);
        })
    }, [])

    const addToCart = (item_id) => {
        axiosInstance.get(`products/add-to-cart/${item_id}`).then(res => {
            console.log(res);
            window.location.reload()
        }).catch(err => {
            console.log(err);
        })
    }

    if (IsLoading) {
        return <h3>loading ...</h3>
    }

    return (
        <>
            <main>
                <div className="products-container">
                    {products.map(item => (
                        <div className="product">
                        <div className="img">
                            <img src={`${item.main_image}`} alt="image" />
                        </div>
                        <h5 className='price'>{item.price}$</h5>

                        <div className="info">
                            <div className="title">
                                <h5>{item.title.substring(0,50)} ...</h5>
                            </div>
                            <h5>{cats.find(cat => cat.id == item.category).name}</h5>
                            <button className='addToCart' onClick={() => {addToCart(item.id)}}>Add TO Cart</button>
                        </div>
                    </div>
                    ))}
                    
                </div>
            </main>
        </>
    );
};

export default Products;