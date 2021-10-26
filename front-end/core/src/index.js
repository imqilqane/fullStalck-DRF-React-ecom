import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import Header from './components/Header/Header';
import Footer from './components/Footer/Footer';
import Products from './components/Products/Products';
import Category from './components/Category/Category';
import Cart from './components/Cart/Cart';
import Address from './components/Address/Address';
import Payment from './components/Payment/Payment'
import Register from './components/Register/Register';
import Login from './components/Login/Login';
import Logout from './components/Logout/Logout';
import StripeContainer from './components/Payment/StripeContainer';
import Verify from './components/Register/Verify';
import {Route, BrowserRouter, Switch} from 'react-router-dom'

ReactDOM.render(
  <React.StrictMode>
    <BrowserRouter>
      <Header />
      <Switch>
          <Route exact path='/' component={Products} ></Route>
          <Route path='/category/:category' component={Category} ></Route>
          <Route path='/cart' component={Cart} ></Route>
          <Route exact path='/checkout' component={Address} ></Route>
          <Route path='/checkout/payment' component={StripeContainer} ></Route>
          <Route exact path='/register' component={Register} ></Route>
          <Route path='/api/auth/register/verifing/:token' component={Verify} ></Route>
          <Route path='/login' component={Login} ></Route>
          <Route path='/logout' component={Logout} ></Route>
      </ Switch>
      <Footer />
    </BrowserRouter>

  </React.StrictMode>,
  document.getElementById('root')
);

