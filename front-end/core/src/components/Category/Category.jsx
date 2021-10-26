import React from 'react';
import axios from 'axios';
import { useState, useEffect } from 'react';
import {useParams,} from 'react-router-dom'
import axiosInstance from '../../axios';

const Category = () => {
    const category = useParams();
    const [products, setProducts] = useState([]);
    console.log(category);
    useEffect(()=>{
        axiosInstance.get(`products/category/${category.category}`).then( res => { 
            setProducts(res.data) 
            console.log(res.data);
        }).catch(err => {
            console.log(err);
        });
    })
    return (
        <>
        <main>
            <div className="products-container">
                {products.map(item => (
                    <div className="product">
                    <div className="img">
                        <img src={`http://localhost:8000${item.main_image}`} alt="image" />
                    </div>
                    <h5 className='price'>{item.price}$</h5>

                    <div className="info">
                        <div className="title">
                            <h5>{item.title.substring(0,50)} ...</h5>
                        </div>
                        {console.log()}
                    </div>
                </div>
                ))}
                
            </div>
        </main>
    </>
    );
};

export default Category;