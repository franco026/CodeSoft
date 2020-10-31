import React from 'react';
import { Route } from "react-router-dom";
// Components
import Home from './container/Home';
import SideMenu from './components/Layout/SideMenu';
import Reports from './components/Reports'
import Chat from './components/Chat';
import LoginUser from './container/Login';

const BaseRouter = () => (
  <div>
    <Route exact path='/' component={Home} />
    <Route exact path='/profile' component={SideMenu} />{" "}
    <Route exact path='/reports' component={Reports} />
    <Route exact path='/Login' component={LoginUser} />
    <Route exact path='/chat' component={Chat} />
  </div>
);

export default BaseRouter;
