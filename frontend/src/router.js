import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Home from './pages/Home';
import AppHeader from './component/Header';
import SearchResult from './pages/SearchResult';

function AppRouter() {
  return (
    <Router>
      <AppHeader/>
      <Switch>
        <Route exact path="/" component={Home}/>
        <Route exact path="/search/:searchResult?" component={SearchResult} />
      </Switch>
    </Router>
  );
}

export default AppRouter;
