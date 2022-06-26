import React from 'react';
import { Menu, Layout } from 'antd';
import { UserOutlined, UserAddOutlined, HomeOutlined } from '@ant-design/icons';
import styled from 'styled-components'
import { useHistory } from 'react-router-dom';

const { Header } = Layout;

const AppHeader = () => {
  const history = useHistory();
  const jumpToPage = (path) => {
    history.push(path);
  }

  return (
    <HeaderContainer>
      <Header className="header" style={{ opacity: '0.8' }}>
        <Logo>Faze Clan Movie System</Logo>
        <MenusContainer theme="dark" mode="horizontal" style={{ justifyContent: 'end' }} >
          <Menu.Item key="1" > <UserOutlined />  Login</Menu.Item>
          <Menu.Item key="2" > <UserAddOutlined />  Register</Menu.Item>
          <Menu.Item key="3" onClick={() => jumpToPage('/')} > <HomeOutlined />  Home</Menu.Item>
        </MenusContainer>
      </Header>
    </HeaderContainer>
  )
};

export default AppHeader;

const HeaderContainer = styled(Layout)`
  display: flex;
  flex-direction: column;
`

const Logo = styled.div`
  display: inline-block;
  text-align: center;
  width: 300px;
  height: 50px;
  margin-left: 40px;
  font-family: 'Gill Sans', 'Gill Sans MT', Calibri, 'Trebuchet MS', sans-serif ;
  font-size: 28px;
  color: #fff;
`
const MenusContainer = styled(Menu)`
  width: 301px;
  display: inline-block;
  float: right;
  height: 50px;
`
