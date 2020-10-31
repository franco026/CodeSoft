import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import * as s from './sidebar.styles';




const Sidebar = props => {
    const {
        backgroundImage = '',
        SidebarHeader = '',
        menuItems = [],
        fonts = {
            header: '',
            menu: ''
        },
    } = props;

    //state
    const [selected, setSelectedMenuItem] = useState(menuItems[0].name);
    const [isSidebarOpen, setSidebarState] = useState(true);


    const handleMenuItemClick = name => {
        setSelectedMenuItem(name)
    }

    //update sidebar state
    useEffect(() => {
        const updateWindowWidth = () => {
            if (window.innerWidth < 1280 && isSidebarOpen) setSidebarState(false);
            else setSidebarState(true)
        }

        window.addEventListener('resize', updateWindowWidth);

        return () => window.removeEventListener('resize', updateWindowWidth);
    }, [isSidebarOpen]);

    const menuItemsJSX = menuItems.map((item, index) => {
        const isItemSelected = selected === item.name;

        return (
            <Link to={item.to} style={{textDecoration:'none'}}>
            <s.MenuItem
                key={index}
                font={fonts.menu}
                selected={isItemSelected}
                onClick={() => handleMenuItemClick(item.name)}
                isSidebarOpen={isSidebarOpen}
            >
                <s.Icon isSidebarOpen={isSidebarOpen} src={item.icon}></s.Icon>
                <s.Text isSidebarOpen={isSidebarOpen}>{item.name}</s.Text>
            </s.MenuItem>
            </Link>
        )
    })

    return (
        <s.SidebarContainer backgroundImage={backgroundImage} isSidebarOpen={isSidebarOpen}>
            <s.SidebarHeader font={fonts.header}>{<img src={process.env.PUBLIC_URL + SidebarHeader} alt="igma" width="80%" height="80%"></img>}</s.SidebarHeader>
            <s.MenuItemContainer>{menuItemsJSX}</s.MenuItemContainer>
            <s.TogglerContainer onClick={() => setSidebarState(!isSidebarOpen)}>
                <s.Toggler />
            </s.TogglerContainer>
        </s.SidebarContainer>
    )
}

export default Sidebar