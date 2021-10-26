import React from 'react';
import { Link, NavLink, Router } from 'react-router-dom';
import '../../asserts/css/footer.css'

const Footer = () => {
    return (
        <>
            <footer>
                <div className="footer-containter">
                    <div className="f-row">
                        <div className="row-title">
                            <h4>Title</h4>
                        </div>
                        <div className="footer-links">
                            <ul>
                               
                                <li>
                                    <NavLink to='/' >Category 1</NavLink>
                                </li>
                                <li>
                                    <NavLink to='/' >Category 2</NavLink>
                                </li>
                                <li>
                                    <NavLink to='/' >Category 3</NavLink>
                                </li>
                            </ul>
                        </div>
                    </div>

                    <div className="f-row">
                        <div className="row-title">
                            <h4>Title</h4>
                        </div>
                        <div className="footer-links">
                            <ul>
                               
                                <li>
                                    <NavLink to='/' >Category 1</NavLink>
                                </li>
                                <li>
                                    <NavLink to='/' >Category 2</NavLink>
                                </li>
                                <li>
                                    <NavLink to='/' >Category 3</NavLink>
                                </li>
                            </ul>
                        </div>
                    </div>

                    <div className="f-row">
                        <div className="row-title">
                            <h4>Title</h4>
                        </div>
                        <div className="footer-links">
                            <ul>
                              
                                <li>
                                    <NavLink to='/' >Category 1</NavLink>
                                </li>
                                <li>
                                    <NavLink to='/' >Category 2</NavLink>
                                </li>
                                <li>
                                    <NavLink to='/' >Category 3</NavLink>
                                </li>
                            </ul>
                        </div>
                    </div>
                   
                </div>
            </footer>
        </>
    );
};

export default Footer;