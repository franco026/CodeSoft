import React from 'react';
import { Route } from "react-router-dom";
// Components
import Home from './container/Home';
import SideMenu from './components/Layout/SideMenu';
import Reports from './components/Reports'
import Chat from './components/Chat';
import LoginUser from './container/Login';
import Register from './container/Register';
import RegisterPatientr from './container/RegisterPatient';

const BaseRouter = () => (
  <div>
    <Route exact path='/' component={Home} />
    <Route exact path='/profile' component={SideMenu} />{" "}
    <Route exact path='/reports' component={Reports} />
    <Route exact path='/Login' component={LoginUser} />
    <Route exact path='/chat' component={Chat} />
    <Route exact path='/SingUp' component={Register} />
    <Route exact path='/SingUpPatient' component={RegisterPatientr} />
  </div>
);

export default BaseRouter;
