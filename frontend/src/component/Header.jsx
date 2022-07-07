import React, { useContext } from 'react';
import { Menu, Layout } from 'antd';
import { UserOutlined, UserAddOutlined, HomeOutlined } from '@ant-design/icons';
import styled from 'styled-components'
import { useHistory } from 'react-router-dom';
import { UserContext } from '../utils/reducer';


const AppHeader = () => {
  const { state, dispatch } = useContext(UserContext);
  const { Header } = Layout;
  const history = useHistory();
  const jumpToPage = (path) => {
    history.push(path);
  }
  const logout = () => {
    localStorage.removeItem('userID');
    dispatch({ type: 'userID', userID: ''});
    jumpToPage('/')
  }
  return (
    <HeaderContainer>
      <Header className="header" style={{ opacity: '0.8' }}>
        <Logo onClick={() => jumpToPage('/')} >Faze Clan Movie System</Logo>
        <MenusContainer theme="dark" mode="horizontal" style={{ justifyContent: 'end' }} >
          <Menu.Item key="1" onClick={() => jumpToPage('/')} > <HomeOutlined /> Home</Menu.Item>
          {!state.userID && <>
            <Menu.Item key="2" onClick={() => jumpToPage('/login')}> <UserOutlined /> Login</Menu.Item>
            <Menu.Item key="3" onClick={() => jumpToPage('/register')}> <UserAddOutlined /> Register</Menu.Item>
          </>}
          {state.userID && <>
            <Menu.Item key="4" onClick={() => jumpToPage('/userinfo')}> <UserOutlined /> User Profile</Menu.Item>
            <Menu.Item key="5" onClick={logout}> <UserOutlined /> Logout</Menu.Item>
          </>}
        </MenusContainer>
      </Header>
    </HeaderContainer>
  )
};

export default AppHeader;

const HeaderContainer = styled(Layout)`
`

const Logo = styled.div`
  cursor: pointer;
  text-align: center;
  width: 300px;
  height: 50px;
  margin-left: 40px;
  font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif ;
  font-size: 28px;
  color: #fff;
  float: left;
`
const MenusContainer = styled(Menu)`
`
