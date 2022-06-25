import React, { useContext } from 'react';
import { useHistory } from 'react-router-dom';
import { Menu, Layout } from 'antd';
import { UserOutlined, UserAddOutlined, HomeOutlined, UserSwitchOutlined } from '@ant-design/icons';

const { Header } = Layout;

const AppHeader = () => {
    const history = useHistory();
    const jumpToPage = (path) => {
        history.push(path);
    };
    const logout = () => {
        localStorage.removeItem('token');
        localStorage.removeItem('email');
        jumpToPage('/');
    }

    return (
        <Layout>
            <Header className="header" style={{ opacity: '0.8' }}>
                <div className="logo">Faze Clan Movie System</div>
                <Menu theme="dark" mode="horizontal" style={{ justifyContent: 'end' }} >
                    <Menu.Item key="1" > <UserOutlined />  Login</Menu.Item>
                    <Menu.Item key="2" > <UserAddOutlined />  Register</Menu.Item>
                    <Menu.Item key="3" > <HomeOutlined />  Home</Menu.Item>
                </Menu>
            </Header>
        </Layout>
    )
};

export default AppHeader;
