import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Home from './pages/Home';
import AppHeader from './component/Header';

function AppRouter() {
  return (
    <Router>
      <AppHeader/>
      <Switch>
        <Route exact path="/" component={Home}/>
      </Switch>
    </Router>
  );
}

export default AppRouter;
