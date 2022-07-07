import React, { useReducer } from 'react';
import { reducer, UserContext } from './utils/reducer';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Home from './pages/Home';
import AppHeader from './component/Header';
import SearchResult from './pages/SearchResult';
import Login from './pages/Login';
import Userinfo from './pages/UserInfo';
import Register from './pages/Register';
import MovieInfo from './pages/MovieInfo';

const initValue = {
  userID: localStorage.getItem('userID')
}

function AppRouter() {
  const [state, dispatch] = useReducer(reducer, initValue);
  return (
    <UserContext.Provider value={{ state, dispatch }}>
      <Router>
        <AppHeader />
        <Switch>
          <Route exact path="/" component={Home} />
          <Route exact path="/search/:searchResult?" component={SearchResult} />
          <Route exact path="/movie/:movieId?" component={MovieInfo} />
          <Route exact path="/login/" component={Login} />
          <Route exact path="/register/" component={Register} />
          <Route exact path="/userinfo/" component={Userinfo} />
        </Switch>
      </Router>
    </UserContext.Provider>
  );
}

export default AppRouter;
